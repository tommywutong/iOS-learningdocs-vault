---
title: CustomMedia
apple_id: DTS10000938
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-05-11'
source_url: https://developer.apple.com/library/archive/samplecode/CustomMedia/Introduction/Intro.html
archived_at: '2026-07-18T03:05:35.565425Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](src-com-vr-VRMedia.java.md)

# CustomMedia

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2006-05-11 Support for XCode 2. Modified project layout for platform independent distribution and compilation. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydaojthawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | XCode 2.2, or Java 2 SDK for Windows, and QuickTime 7 |
| __Runtime Requirements:__ | Java 1.5 and QuickTime 7, or later, recommended |

The user is prompted to select a QTVR Panoramic movie file. The media object and SampleDescription of all of the tracks that are found in the opened movie are printed. Factory methods are used to create Media subclasses based on the media type. If a match is not found, for QuickTime's default media types, a search is performed to see if the application has registered knowledge of custom or application specific media types. If a match is still not found the factory will return a GenericMedia object.
Standard Media calls can still be performed on a GenericMedia class - it is only if the application requires specific functionality and support for specific media or media handlers that custom media classes have to be written. This mechanism can be used to integrate those custom classes within the existing framework.

[Next](src-com-vr-VRMedia.java.md)

