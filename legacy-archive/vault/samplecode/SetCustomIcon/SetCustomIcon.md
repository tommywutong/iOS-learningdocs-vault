---
title: SetCustomIcon
apple_id: DTS10003477
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-08-01'
source_url: https://developer.apple.com/library/archive/samplecode/SetCustomIcon/Introduction/Intro.html
archived_at: '2026-07-18T03:23:41.104775Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# SetCustomIcon

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2006-08-01 Added Mac OS X 10.4 support to set disk icons. Updated to produce a universal binary. No code changes were required. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbxg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode |
| __Runtime Requirements:__ | Mac OS X |

SetCustomIcon demonstrates how to programmatically set a custom icon of either a file or folder. A typical example may be to create an icon representation of a photo or picture. This example uses QuickTime's Graphics Importers in two areas. The Graphics Importer is used to draw the source image to the screen from the user panes kEventControlDraw event handler routine. It is also used during the process of converting the image to a PicHandle which is then used in the creation of an IconFamilyHandle. The utility routine SaveCustomIcon() is responsible for saving the IconFamilyHandle data as a resource in the appropriate format and location.

[Next](main.c.md)

