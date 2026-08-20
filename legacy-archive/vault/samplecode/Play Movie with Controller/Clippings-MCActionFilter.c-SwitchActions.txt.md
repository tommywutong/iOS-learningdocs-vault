---
title: Play Movie with Controller
apple_id: DTS10001041
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Play_Movie_with_Controller/Listings/Clippings_MCActionFilter_c_SwitchActions_txt.html
archived_at: '2026-07-18T03:19:10.313559Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Play Movie with Controller](Play%20Movie%20with%20Controller.md)


[Next](Clippings-OpenMovieInWindow.c-Dispose.txt.md)[Previous](Clippings-Events.c-MCIsPlayerEvent.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html](https://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html)

# Clippings/MCActionFilter.c/SwitchActions.txt

```
        // handle window resizing
        case mcActionControllerSizeChanged:
            if (MCIsControllerAttached(theMC) == 1)
                QTFrame_SizeWindowToMovie(myWindowObject);
            break;

        // handle idle events
        case mcActionIdle:
            QTApp_Idle((**myWindowObject).fWindow);
            break;
```

[Next](Clippings-OpenMovieInWindow.c-Dispose.txt.md)[Previous](Clippings-Events.c-MCIsPlayerEvent.txt.md)

