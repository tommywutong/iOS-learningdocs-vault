---
title: Incoming requests for /.well-known/apple-app-site-association file
apple_id: DTS40016874
resource_type: QA
platform: iOS
topic: Networking, Internet, & Web
technology: null
published: '2016-03-31'
source_url: https://developer.apple.com/library/archive/qa/qa1919/_index.html
archived_at: '2026-07-18T02:36:50.307071Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1919

# Incoming requests for /.well-known/apple-app-site-association file

## Q:  Why is my web server receiving requests for `https://example.com/.well-known/apple-app-site-association`?

A: The recently released iOS 9.3 update implements [RFC 5785](http://www.ietf.org/rfc/rfc5785.txt). Because of this, devices running iOS 9.3 will first request `/.well-known/apple-app-site-association` for the `apple-app-site-association` file that is required to implement [Universal Links](https://developer.apple.com/library/ios/documentation/General/Conceptual/AppSearch/UniversalLinks.html#//apple_ref/doc/uid/TP40016308-CH12-SW1) and [Shared Web Credentials](https://developer.apple.com/library/ios/documentation/Security/Reference/SharedWebCredentialsRef/index.html#//apple_ref/doc/uid/TP40014989). If the file is not found in this location, then the device will request the file in the root of the web server, as with prior releases of iOS 9.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-03-31 | New document that explains the reasons for seeing these incoming requests. |

