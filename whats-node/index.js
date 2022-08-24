const qrcode = require('qrcode-terminal');
const fs = require("fs")
const {Client} = require('whatsapp-web.js');

let sessionData;
if(fs.existsSync(SESSION_FILE_PATH)) {
    sessionData = require(SESSION_FILE_PATH);
}

const client = new Client({
    session: sessionData
});


client.initialize();
client.on("qr", qr => {
    qrcode.generate(qr, {small: true} );
})


// DATOS A ENVIAR

client.on('authenticated', (session) => {
    sessionData = session;
    fs.writeFile(SESSION_FILE_PATH, JSON.stringify(session), function (err) {
        if (err) {
            console.error(err);
        }
    });
});

client.on("auth_failure" , msg => {
    console.log("Ocurrió un error, mensaje:", msg)
})