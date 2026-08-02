---
title: Sending an Email
apple_id: DTS10003445
resource_type: QA
platform: macOS
topic: Data Management
technology: null
published: '2004-11-05'
source_url: https://developer.apple.com/library/archive/qa/qa1084/_index.html
archived_at: '2026-07-18T02:29:55.681848Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1084

# Sending an Email

## Q:  I want to add a feature to my application that allows a user to easily email my technical support address. What's the easiest way to do this?

A: I want to add a feature to my application that allows a user to easily email my technical support address. What's the easiest way to do this?

The Message framework (`/System/Library/Frameworks/Message`) allows you to send an email directly from your application. However, for the situation you describe, it's best to just create the message in the user's preferred email application and let them send it. You can do this by opening a `mailto` URL. The extended `mailto` URL format (as documented in [RFC 2368](http://www.ietf.org/rfc/rfc2368.txt)) lets you specify the subject line and message body as part of the URL. Listing 1 shows a simple example of this in Cocoa; Listing 2 does the same thing in plain C.

__Listing 1__  Creating an email message in Cocoa

```objc
- (IBAction)sendMailCocoa:(id)sender     // Create a mail message in the user's preferred mail client      // by opening a mailto URL. The extended mailto URL format      // is documented by RFC 2368 and is supported by Mail.app      // and other modern mail clients.     //     // This routine's prototype makes it easy to connect it as      // the action of a user interface object in Interface Builder. {     NSURL *     url;      // Create the URL.      url = [NSURL URLWithString:@"mailto:dts@apple.com"         "?subject=Hello%20Cruel%20World!"         "&body=Share%20and%20Enjoy"     ];     assert(url != nil);      // Open the URL.      (void) [[NSWorkspace sharedWorkspace] openURL:url]; }
```


__Listing 2__  Creating an email message in plain C

```
static void SendMailCarbon(void)     // Create a mail message in the user's preferred mail client      // by opening a mailto URL. The extended mailto URL format      // is documented by RFC 2368 and is supported by Mail.app      // and other modern mail clients. {     OSStatus    err;     CFURLRef    url;     static const char kMailtoURL[] =          "mailto:dts@apple.com"         "?subject=Hello%20Cruel%20World!"         "&body=Share%20and%20Enjoy";      url = CFURLCreateWithBytes(         NULL,          (const UInt8 *) kMailtoURL,          sizeof(kMailtoURL),         kCFStringEncodingASCII,          NULL     );     assert(url != NULL);      err = LSOpenCFURLRef(url, NULL);     assert(err == noErr);      CFRelease(url); }
```

Things get more complex if you want to create a message with an attachment. The underlying technology for opening a URL is the `'GURL'` Apple event suite. While that suite's [specification](ftp://ftp.stairways.com/other/url-ae-standard-1-1-info.txt) describes an optional parameter for attaching files, this parameter is not widely supported (for example, it's not supported by the Mail application (r. 3855958)). Therefore, if you need to send an attachment, the best solution is to script Mail, as described in [Technical Q&A QA1018, 'Using AppleScript to send an email with an attachment'](https://developer.apple.com/qa/qa2001/qa1018.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-11-05 | New document that shows how to create an email in the user's prefered email application. |

