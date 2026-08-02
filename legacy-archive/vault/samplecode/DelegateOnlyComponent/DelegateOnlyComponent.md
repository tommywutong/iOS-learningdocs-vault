---
title: DelegateOnlyComponent
apple_id: DTS10000814
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2005-10-18'
source_url: https://developer.apple.com/library/archive/samplecode/DelegateOnlyComponent/Introduction/Intro.html
archived_at: '2026-07-18T03:06:13.980259Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](DelegateOnlyImageCodec-DelegateOnlyCodec.c.md)

# DelegateOnlyComponent

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0.1, 2005-10-18 Updated to produce a universal binary. No code changes were required. |
| __Build Requirements:__ | Xcode 2.1 or greater. |
| __Runtime Requirements:__ | Mac OS X 10.4 or greater with QuickTime 7 or greater. |

DelegateOnlyComponent pretends to be an Image Codec. But all it does is delegate to a real Image Codec (in this case a '2vuy' decompressor).
This is a useful component sample to start with if you are writing a component to overide the functionality of another component, or just interested in seeing basic component functionality.
The project builds three targets:
1) A Test Application containing the DelegateOnly component linked into it that can be run as is.
2) A Test Application that requires the DelegateOnly component bundle to be installed in /Library/QuickTime/.
3) The DelegateOnly component bundle itself. This should be placed in /Library/QuickTime/.
This project builds universal binaries.

[Next](DelegateOnlyImageCodec-DelegateOnlyCodec.c.md)

