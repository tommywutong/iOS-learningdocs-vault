---
title: CustomHTTPProtocol
apple_id: DTS40013653
resource_type: Sample Code
platform: iOS
topic: null
technology: Foundation
published: '2014-08-20'
source_url: https://developer.apple.com/library/archive/samplecode/CustomHTTPProtocol/Introduction/Intro.html
archived_at: '2026-07-18T03:05:33.705111Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CustomHTTPProtocol-AppDelegate.h.md)

# CustomHTTPProtocol

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2014-08-20 Changed the protocol to use NSURLSession for its recursive requests. This works around a deadlock issue (r. 17342579) and makes the code more future proof. There were also numerous other minor changes. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnrvgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 5.1.1, iOS 7.1 SDK |
| __Runtime Requirements:__ | iOS 7.0 or later |

CustomHTTPProtocol shows how to use an NSURLProtocol subclass to intercept the NSURLConnections made by a high-level subsystem that does not otherwise expose its network connections. In this specific case, it intercepts the HTTPS requests made by a web view and overrides server trust evaluation, allowing you to browse a site whose certificate is not trusted by default.

[Next](CustomHTTPProtocol-AppDelegate.h.md)

