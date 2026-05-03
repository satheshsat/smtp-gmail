const nodemailer = require('nodemailer');

async function main() {
  let transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: 'satheshs.sat@gmail.com',
      pass: 'your-app-password' // Use an App Password, not main password
    }
  });

  let info = await transporter.sendMail({
    from: '"Sender Name" <satheshs.sat@gmail.com>',
    to: "satheshs.sat@gmail.com",
    subject: "Hello",
    text: "Hello world?",
  });
  console.log("Message sent: %s", info.messageId);
}
main().catch(console.error);