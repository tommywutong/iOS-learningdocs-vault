---
title: Concordia
apple_id: DTS10000181
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-08-28'
source_url: https://developer.apple.com/library/archive/samplecode/Concordia/Introduction/Intro.html
archived_at: '2026-07-18T03:04:12.451362Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ChooseTkl.c.md)

# Concordia

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-08-28 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

Concordia is a menu definition procedure (MDEF) that replaces the standard text MDEF (MDEF 0). It does everything that the standard MDEF does except color and displaying small icon resources (sicns). It will display the shrunken icons that MultiFinder uses. The main differences between my MDEF and the standard MDEF is that it has proportional menu scrolling, scrolling arrows that appear quite differently from the standard ones, more consistent spacing between menu items and the edges of the menu, and the arrow icons are stored as resources rather than being hard-coded into the MDEF. Proportional scrolling means that the farther you drag the mouse into the scroll arrow of the menu, the faster the menu scrolls. If you have the mouse only one pixel into the scroll arrow, the menu will only scroll one pixel at a time. You'll have to paste the sicn resources for the arrow icons into the System file for the sample MDEF to find them. You can use this as a basis for your own replacement to the standard MDEF in case you need just a bit more functionality than the standard MDEF provides. Keywords: MDEF, proportional, scrolling

[Next](ChooseTkl.c.md)

