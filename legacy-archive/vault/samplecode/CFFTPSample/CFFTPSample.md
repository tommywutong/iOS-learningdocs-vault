---
title: CFFTPSample
apple_id: DTS10003223
resource_type: Sample Code
platform: macOS
topic: Networking, Internet, & Web
technology: CoreFoundation
published: '2006-10-13'
source_url: https://developer.apple.com/library/archive/samplecode/CFFTPSample/Introduction/Intro.html
archived_at: '2026-07-18T03:02:25.448077Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CFFTPSample.c.md)

# CFFTPSample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2006-10-13 Fixed a crash when CFFTPCreateParsedResourceListing returned a positive value but a NULL dictionary (r. 4533718). Follow CFNetwork best practice by only reading only one chunk of data per callback (r. 4515194). Terminate FTP upload in recommended fashion (by closing the stream rather than writing zero bytes). General tidy up. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmrsgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 2.4 or later |
| __Runtime Requirements:__ | Mac OS X 10.3.9 or later |

CFFTPSample demonstrates how to use CFNetwork to download and upload files using FTP, as well as how to parse FTP directory listings.

[Next](CFFTPSample.c.md)

