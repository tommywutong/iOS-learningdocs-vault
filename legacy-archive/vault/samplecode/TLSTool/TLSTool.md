---
title: TLSTool
apple_id: DTS40014927
resource_type: Sample Code
platform: macOS
topic: Security
technology: Foundation
published: '2016-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/sc1236/Introduction/Intro.html
archived_at: '2026-07-26T19:54:14.628814Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](TLSTool-main.m.md)

# TLSTool

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2016-05-23 The s_client code now marks the certificates included in the server handshake with a “+”, which makes it easier to debug misconfigured servers. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojsg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 7.3 |
| __Runtime Requirements:__ | OS X 10.9 or later |

TLSTool is a sample that shows how to implement Transport Layer Security (TLS), and its predecessor, Secure Sockets Layer (SSL), using the NSStream API. TLSTool demonstrates TLS in both client and server mode.
TLSTool can also be used to explore TLS interactively, much like OpenSSL's s_client and s_server subcommands. However, because TLSTool uses the OS's built-in TLS stack, it will behave more like other built-in apps that use TLS (Mail, Safari, and so on).

[Next](TLSTool-main.m.md)

