---
title: HairLines
apple_id: DTS10000292
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/HairLines/Listings/About_HairLines_txt.html
archived_at: '2026-07-18T03:11:44.148930Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HairLines](HairLines.md)


[Next](Document%20Revision%20History.md)[Previous](HairLines.md)

# About HairLines.txt

```

Hey!  What the Hell is this?!

sample: HairLines
Language: MPW Pascal 3.2

HairLines is an MPW 3.2 Pascal sample that demonstrates different methods of creating hairlines on printers.  You select the method(s) you want to use from the Settings menu.

The SetLineWidth method is only supported by PostScript printers, although all printer drivers will support it in the future.

The PrGeneral method can be used with any printer, QuickDraw or PostScript, and is the method of choice to date.  It has the drawback that all of your graphics and text need to be scaled to the resolution you print at.

For the truly sadistic, the two methods can also be combined.

Using the PrGeneral method without scaling selected yields nasty results.  This option is provided in the sample to demonstrate one of the biggest traps of using PrGeneral.  Remember to scale your graphics when using SetRsl!!

If you print the test page without the PrGeneral or SetLineWidth methods checked, you can see what the test image like without hairlines.  Pretty messy, but good to compare against.

That's it.

- Dave ÒgdÓ Hersey
  MacDTS
  10/9/91
```

[Next](Document%20Revision%20History.md)[Previous](HairLines.md)

