---
title: ColorMatching
apple_id: DTS10003160
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2003-12-18'
source_url: https://developer.apple.com/library/archive/samplecode/ColorMatching/Introduction/Intro.html
archived_at: '2026-07-18T03:03:56.795316Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# ColorMatching

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-12-18 Performs simple color matching of images using ColorSync or the QuickTime 6.4 Graphics Importers. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Mac OS X Mac OS 10.3 "Panther" |

ColorMatching is an example Cocoa application that shows how to perform simple color matching of images using ColorSync or the QuickTime 6.4 Graphics Importers. Image files are read from disk using the QuickTime Graphics Importers, or may be acquired from any connected digital camera using Apple Image Capture. More specifically, the sample allows the user to build a ColorSync color world for color matching based on custom selections for source, abstract, proof and destination profiles. This color world is then used to color-match the image. The resulting color matched image is displayed in a Cocoa window. Alternately, on Panther systems the user may select the built-in ColorSync color matching support provided by the QuickTime Graphics Importer components, rather than use ColorSync directly. The QuickTime Graphics Importers will honor any embedded profile in the image. Requirements: Mac OS 10.3 "Panther" Keywords: ColorSync color match QuickTime graphics importer

[Next](main.m.md)

