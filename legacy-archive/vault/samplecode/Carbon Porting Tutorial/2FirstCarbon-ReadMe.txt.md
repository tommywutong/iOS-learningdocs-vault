---
title: Carbon Porting Tutorial
apple_id: DTS10003904
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-07-25'
source_url: https://developer.apple.com/library/archive/samplecode/CarbonPorting/Listings/2_First_Carbon_ReadMe_txt.html
archived_at: '2026-07-18T03:02:59.689179Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Carbon Porting Tutorial](Carbon%20Porting%20Tutorial.md)


[Next](3CarbonEvents-CarbonPrefix.h.md)[Previous](2FirstCarbon-PrefsWindow.r.md)

# 2_First_Carbon/ReadMe.txt

```
ExamplePrefs 2.0

Step 2 in your Carbonizing project is the final Classic version of the program.  The TARGET_API_MAC_XXX constants are manually defined in the prefix file in order to switch on which headers to include.  OPAQUE_TOOLBOX_STRUCTS and  ACCESSOR_CALLS_ARE_FUNCTIONS are defined true in the prefix as well.  This means that Toolbox accessor functions are now used instead of directly accessing the various Toolbox structures and the Classic target links against CarbonAccessors.o.  The exception is the IconListDef project.  CarbonAccessors.o is 84K and the IconListDef resource file is 4K, so rather than increase the size of the resource by a factor of 20, the six accessor functions it uses are defined in its source.  The upshot of using accessor functions everywhere is that far less of the code has to be conditionalized for Classic/Carbon.  The window/list method continues to be more work than the dialog/list box control method, this time it's 624 (+58 from 1.0) lines to 323 (+44 from 1.0) lines.
```

[Next](3CarbonEvents-CarbonPrefix.h.md)[Previous](2FirstCarbon-PrefsWindow.r.md)

