const qrcode = require('qrcode-terminal');
const fs = require("fs")
const { Client, LegacySessionAuth } = require('whatsapp-web.js');

// Ejecución de Python script 
/*const {PythonShell} = require("python-shell");
let pyshell = new PythonShell("../sys.py");

pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
});*/


// Path donde la sesión va a estar guardada 
const SESSION_FILE_PATH = './session.json';

// Cargar la sesión en caso de que ya este guardada 
let sessionData;
if(fs.existsSync(SESSION_FILE_PATH)) {
    sessionData = require(SESSION_FILE_PATH);
}

// Usar valores guardados
const client = new Client({
    authStrategy: new LegacySessionAuth({
        session: sessionData
    })
});

// Save session values to the file upon successful auth
client.on('authenticated', (session) => {
    sessionData = session;
    fs.writeFile(SESSION_FILE_PATH, JSON.stringify(session), (err) => {
        if (err) {
            console.error(err);
        }
    });
});
 
/*const SESSION_FILE_PATH = './session.json';

let sessionData;
if(fs.existsSync(SESSION_FILE_PATH)) {
    sessionData = require(SESSION_FILE_PATH);
}

const client = new Client({
    session: sessionData
});*/


client.initialize();
client.on("qr", qr => {
    qrcode.generate(qr, {small: true} );
})


const send_message = [
    "54123456789",
    "54123456789"
]

client.on("ready", () => {
    console.log("Listo")

    send_message.map(value => {
        const chatId = value +"@c.us"
        message = "Prueba 1"
        client.sendMessage(chatId,message);
})})






