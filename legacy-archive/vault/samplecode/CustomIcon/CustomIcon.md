---
title: CustomIcon
apple_id: DTS10000183
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CustomIcon/Introduction/Intro.html
archived_at: '2026-07-18T03:05:35.411857Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CustIcon.c.md)

# CustomIcon

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

This snippet shows how to use custom document icons in an application. The correct procedure for doing this is to add the Icon family to the document and set bit 10 of the finder info. An elegant way of adding the icon family is to use one of the routines described in the Icon Utilities chapter of Inside Macintosh More Toolbox Essentials: ForEachIconDo(). You can define an action proc that is called each time for each icon an an icon suite. Keywords: custom, icons

[Next](CustIcon.c.md)

