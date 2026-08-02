---
title: Play Movie with Controller
apple_id: DTS10001041
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Play_Movie_with_Controller/Listings/Clippings_SetupController_c_SetupController_txt.html
archived_at: '2026-07-18T03:19:10.797641Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Play Movie with Controller](Play%20Movie%20with%20Controller.md)


[Next](Common%20Files-ComFramework.c.md)[Previous](Clippings-SetupController.c-Resize.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html](https://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html)

# Clippings/SetupController.c/SetupController.txt

```
    // CLUT table use
    MCDoAction(theMC, mcActionGetFlags, &myControllerFlags);
    MCDoAction(theMC, mcActionSetFlags, (void *)(myControllerFlags | mcFlagsUseWindowPalette));

    // enable keyboard event handling
    MCDoAction(theMC, mcActionSetKeysEnabled, (void *)true);

    // disable drag support
    MCDoAction(theMC, mcActionSetDragEnabled, (void *)false);
```

[Next](Common%20Files-ComFramework.c.md)[Previous](Clippings-SetupController.c-Resize.txt.md)

