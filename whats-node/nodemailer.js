require('dotenv').config('/.env');

const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL,
    pass: process.env.PASS
  },
});


transporter.sendMail({
  from: 'Virginia Sacudato virginia@relojeslenox.com.ar', // sender address
  to: "virginiasacudato@gmail.com", // list of receivers
  subject: "Medium @edigleyssonsilva ✔", // Subject line
  text: "There is a new article. It's about sending emails, check it out!", // plain text body
  html: "<b>There is a new article. It's about sending emails, check it out!</b>", // html body
}).then(info => {
  console.log({info});
}).catch(console.error);