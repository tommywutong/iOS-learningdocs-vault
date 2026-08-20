---
title: Play Movie with Controller
apple_id: DTS10001041
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Play_Movie_with_Controller/Listings/Clippings_SetupController_c_NewMovieController_txt.html
archived_at: '2026-07-18T03:19:10.697092Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Play Movie with Controller](Play%20Movie%20with%20Controller.md)


[Next](Clippings-SetupController.c-Resize.txt.md)[Previous](Clippings-SetupController.c-MCSetActionFilter.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html](https://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html)

# Clippings/SetupController.c/NewMovieController.txt

```
    // create the movie controller
    myMC = NewMovieController(theMovie, &myRect, mcTopLeftMovie);
    if (myMC == NULL)
        return(NULL);

    // enable the default movie controller editing
    MCEnableEditing(myMC, true);

    // suppress movie badge
    MCDoAction(myMC, mcActionSetUseBadge, (void *)false);
```

[Next](Clippings-SetupController.c-Resize.txt.md)[Previous](Clippings-SetupController.c-MCSetActionFilter.txt.md)

