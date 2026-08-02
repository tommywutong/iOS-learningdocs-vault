---
title: MoofWarsOld
apple_id: DTS10000057
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoofWarsOld/Introduction/Intro.html
archived_at: '2026-07-18T03:15:01.667903Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](MoofEncoder-AppConditionals.h.md)

# MoofWarsOld

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-10-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon PowerPC, DrawSprocket |

MoofWars is a piece of sample code that demonstrates a few techniques to build efficient animation code on the PowerPC. This code takes advantage of DrawSprocket to provide access to page flipping when the video hardware supports it. This sample is written in C++. The main features in this application are the graphic and tile classes, which are used to draw the background and then composite sprites on top of it. The blitters within these classes are designed to move data as efficiently as possible on PowerPC -- that is, whenever possible every read and every write is done on an aligned boundary, and data is moved in as big a chunks as possible. This version runs only in 8-bit mode, although DrawSprocket should set this mode automatically. By default, debugging code is compiled into the project, so you should have MacsBug installed when you run this code. Requirements: PowerPC, DrawSprocket Keywords: game, sprockets, sprite, blit, blitter, DrawSprocket, MoofWars

[Next](MoofEncoder-AppConditionals.h.md)

