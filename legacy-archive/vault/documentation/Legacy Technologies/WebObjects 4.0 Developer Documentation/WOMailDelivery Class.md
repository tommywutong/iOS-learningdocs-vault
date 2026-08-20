---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.038.html
archived_at: '2026-07-15T07:58:44.707819Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](New%20Methods.md)

# WOMailDelivery Class

WOMailDelivery uses the WOSendMail tool to construct an email from a file and send it using SMTP. It requires an SMTP server to be set (the default value for the SMTP hostname is "smtp"; you can change this value with __defaults write NSGlobalDomain WOSMTPHost__ _hostName_ or by supplying the hostname as a WOApplication command-line argument).
WOMailDelivery defines the following methods:

|  WOMailDelivery |  |
|  Method |  Description |
|  sharedInstance |  Returns the shared WOMailDelivery object to which you should send the __composeEmailFrom...__ and __sendEmail:__ messages. |
|  composeEmailFrom:to:cc:subject:plainText:send: |  Composes an email message with a textual body and optionally sends it. The content type is set to __Content-type: TEXT/PLAIN; CHARSET=US-ASCII__. |
|  composeEmailFrom:to:cc:subject:component:send: |  Composes an email message (and optionally sends it) where the body is the HTML that results when __generateResponse__ is sent to the specified component. Note that the HTML generated is different from what would be generated in a request-response loop: all URLs in the page are complete (from __http://__) so that the mail reader can follow the links on the mailed page. |
|  sendEmail: |  Sends an email message created with one of the WOMailDelivery __composeEmailFrom...__ methods. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](Cookie%20API.md)
