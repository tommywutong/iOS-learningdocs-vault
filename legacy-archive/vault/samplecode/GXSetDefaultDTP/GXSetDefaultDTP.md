---
title: GXSetDefaultDTP
apple_id: DTS10000291
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/GXSetDefaultDTP/Introduction/Intro.html
archived_at: '2026-07-18T03:10:37.770416Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](FSSetPrinter.c.md)

# GXSetDefaultDTP

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

This application demonstrates how to send an AppleEvent to the Finder that will cause a new default desktop printer to be selected. The user interface consists of a dialog that collects a string that is the name of a desktop printer. Upon hitting the default button, the application forms an AppleEvent and sends it off to the Finder. The AppleEvent is constructed by getting the address of the Finder, generating a core event to a Finder extension, and adding a direct object which specifies the GX printing extension, the set default printer command, and the desktop printer name. If the Printing Finder Extension (part of QuickDraw GX) is installed and a valid desktop printer was specified then that printer should become the default printer. Requires: Keywords: print, desktop, AppleEvent

[Next](FSSetPrinter.c.md)

