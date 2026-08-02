---
title: Apple URL Scheme Reference
apple_id: TP40007899
resource_type: Guide
platform: watchOS|Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/SMSLinks/SMSLinks.html
archived_at: '2026-07-18T02:29:23.436476Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md) · [Apple URL Scheme Reference](About%20Apple%20URL%20Schemes.md)


[Next](Map%20Links.md)[Previous](FaceTime%20Links.md)

# SMS Links

The `sms` scheme is used to launch the Messages app. The format for URLs of this type is “`sms:`_<phone>_”, where _<phone>_ is an optional parameter that specifies the target phone number of the SMS message. This parameter can contain the digits 0 through 9 and the plus (`+`), hyphen (`-`), and period (`.`) characters. The URL string must not include any message text or other information.

The following examples show strings formatted for Safari and for native apps.

- HTML links:

```
<a href="sms:">Launch Messages App</a>
<a href="sms:1-408-555-1212">New SMS Message</a>
```
- Native app URL strings:

```
sms:
sms:1-408-555-1212
```

[Next](Map%20Links.md)[Previous](FaceTime%20Links.md)

