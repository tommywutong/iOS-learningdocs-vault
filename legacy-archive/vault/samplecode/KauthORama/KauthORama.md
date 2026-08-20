---
title: KauthORama
apple_id: DTS10003633
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2014-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/KauthORama/Introduction/Intro.html
archived_at: '2026-07-18T03:13:21.149387Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](KauthORama.c.md)

# KauthORama

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.4, 2014-03-26 Updated to support the latest tools and techniques (64-bit, Developer ID code signing, Xcode 5, and so on) (r. 16127581) (r. 9272790). Added support for the KAUTH_FILEOP_DELETE operation (r. 6511762). [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrtgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 5.1 |
| __Runtime Requirements:__ | OS X 10.9 Mavericks |

KauthORama demonstrates the use of the Kernel Authorization (Kauth) subsystem. KauthORama allows you to register a listener for any scope. The listener has no effect on authorization decisions, but it prints a record of each authorization request so that you can see how Kauth interacts with high-level operations, like listing directories or copying files.

[Next](KauthORama.c.md)

