---
title: Restore Screen Cluts
apple_id: DTS10000159
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-12'
source_url: https://developer.apple.com/library/archive/samplecode/Restore_Screen_Cluts/Introduction/Intro.html
archived_at: '2026-07-18T03:22:10.263089Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ColorReset.c.md)

# Restore Screen Cluts

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-03-12 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon System 7.0 or later |

This snippet shows how to restore all the screen's color tables back to what they normally are using two different methods. To demonstrate this, set your main screen to eight bits per pixel and run the program and open the Flowers PICT file. A window that displays the contents of the PICT file appears on the main screen, and its color table should change to the one in the PICT file. The is controlled by a palette full of tolerant colors. Now close the window, and you'll see that the screen's color table does not get set back to the default color table. But if you go to the Display menu and choose either of the commands there, all the screen's color tables should be restored back to what they normally are. Requirements: System 7.0 or later Keywords: RestoreDeviceClut, GetDeviceList, NewPalette, SetPalette, TestDeviceAttribute, GetCTable, CTab2Palette, GetNextDevice

[Next](ColorReset.c.md)

