---
title: Apple URL Scheme Reference
apple_id: TP40007899
resource_type: Guide
platform: watchOS|Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/MailLinks/MailLinks.html
archived_at: '2026-07-18T02:29:23.244691Z'
---
> 导航：[总目录](../../README.md) · [featuredarticles](../../_indexes/featuredarticles.md) · [Apple URL Scheme Reference](About%20Apple%20URL%20Schemes.md)


[Next](Phone%20Links.md)[Previous](About%20Apple%20URL%20Schemes.md)

# Mail Links

The `mailto` scheme is used to launch the Mail app and open the email compose sheet. When specifying a `mailto` URL, you must provide the target email address. The following examples show strings formatted for Safari and for native apps.

- HTML link:

```
<a href="mailto:frank@wwdcdemo.example.com">John Frank</a>
```
- Native app URL string:

```
mailto:frank@wwdcdemo.example.com
```

You can also include a subject field, a message, and multiple recipients in the To, Cc, and Bcc fields. (In iOS, the `from` attribute is ignored.) The following example shows a `mailto` URL that includes several different attributes:

```
mailto:foo@example.com?cc=bar@example.com&subject=Greetings%20from%20Cupertino!&body=Wish%20you%20were%20here!
```

For detailed information on the format of the `mailto` scheme, see [RFC 2368](http://www.ietf.org/rfc/rfc2368.txt).

[Next](Phone%20Links.md)[Previous](About%20Apple%20URL%20Schemes.md)

