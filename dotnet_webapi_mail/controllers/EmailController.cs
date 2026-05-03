
using dotnet_webapi_mail.service;
using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;

namespace dotnet_webapi_mail.controllers;

[ApiController]
[Route("api/[controller]")]
public class EmailController : ControllerBase
{
    private readonly EmailService _emailService;
    public EmailController(EmailService emailService) => _emailService = emailService;

    [HttpPost("send")]
    public async Task<IActionResult> SendEmail(string to, string subject, string body)
    {
        await _emailService.SendEmailAsync(to, subject, body);
        return Ok("Email sent successfully!");
    }
}
