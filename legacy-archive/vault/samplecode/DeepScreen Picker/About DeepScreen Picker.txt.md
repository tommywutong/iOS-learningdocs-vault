---
title: DeepScreen Picker
apple_id: DTS10000081
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/DeepScreen_Picker/Listings/About_DeepScreen_Picker_txt.html
archived_at: '2026-07-18T03:06:09.099088Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeepScreen Picker](DeepScreen%20Picker.md)


[Next](DeepScreen%20Picker.r.md)[Previous](DeepScreen%20Picker.md)

# About DeepScreen Picker.txt

```

Hey!  What the Hell is this?!

sample: DeepScreen Picker
Language: MPW Pascal 3.2

This sample shows how to slam and center the Color Picker dialog onto the deepest device when 32 Bit QuickDraw is not available.  (If itÕs available, you can just pass the top left coordinates of
(-1,-1) and the dialog will be centered on the deepest device.)

Even if 32 BQD is available, this method has the benefit of allowing you to give preference to color or grayscale monitors of the same depth.  In contrast, if there is a tie for deepest monitor, the Color Picker code takes the first one it finds.

For example, suppose you need the user to select a color.  Also suppose that two monitors are connected with the same maximum depth; a grayscale and a color one.  In this case, youÕd rather have the Color Picker displayed on the color monitor so that the user can really see which color is being selected.  This code lets you specify things like that, whereas the 32 BQD Color Picker centering code does not.

- Dave ÒgdÓ Hersey
  MacDTS
  10/9/91
```

[Next](DeepScreen%20Picker.r.md)[Previous](DeepScreen%20Picker.md)

