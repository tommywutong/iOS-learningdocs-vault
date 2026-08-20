---
title: OSXAdapter
apple_id: DTS10000685
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2007-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/OSXAdapter/Introduction/Intro.html
archived_at: '2026-07-18T03:17:09.915865Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.txt.md)

# OSXAdapter

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.0, 2007-06-01 Rewritten for compile-time as well as run-time portability. Requires Ant 1.7 or Xcode 3.0. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanryguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | J2SE 1.4 or later, Ant 1.7.0 or later. Xcode project requires Xcode 3.0 |
| __Runtime Requirements:__ | J2SE 1.4 or later |

This sample uses a reflection Proxy model to hook existing preferences, about, and quit functionality into handlers for the Mac OS X application menu. This functionality is easily adopted by implementing the com.apple.eawt.ApplicationListener interface, but this sample's dynamic implementation will only be triggered on platforms that actually support the Apple APIs (e.g. Java 1.4 or later on Mac OS X), avoiding any compatibility concerns.

This sample is for developers looking to support multiple platforms, including support for Mac OS X-specific features, with a single codebase. It is written for and should build and run on any J2SE 1.4 implementation without any stub or placeholder libraries.

[Next](README.txt.md)

