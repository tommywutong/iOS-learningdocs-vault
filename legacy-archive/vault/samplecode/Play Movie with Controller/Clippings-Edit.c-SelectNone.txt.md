---
title: Play Movie with Controller
apple_id: DTS10001041
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Play_Movie_with_Controller/Listings/Clippings_Edit_c_SelectNone_txt.html
archived_at: '2026-07-18T03:19:10.148217Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Play Movie with Controller](Play%20Movie%20with%20Controller.md)


[Next](Clippings-Edit.c-SwitchEdit.txt.md)[Previous](Clippings-Edit.c-SelectAll.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html](https://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html)

# Clippings/Edit.c/SelectNone.txt

```
    myTimeRecord.value.hi = 0;
    myTimeRecord.value.lo = 0;  
    myTimeRecord.base = 0;
    myTimeRecord.scale = GetMovieTimeScale(myMovie);    
    myErr = MCDoAction(theMC, mcActionSetSelectionDuration, &myTimeRecord);
```

[Next](Clippings-Edit.c-SwitchEdit.txt.md)[Previous](Clippings-Edit.c-SelectAll.txt.md)

