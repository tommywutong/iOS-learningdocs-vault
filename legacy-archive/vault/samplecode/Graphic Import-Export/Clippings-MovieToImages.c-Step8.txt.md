---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_MovieToImages_c_Step8_txt.html
archived_at: '2026-07-18T03:10:58.792589Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-MultipleImages.clp-GetImageCount.txt.md)[Previous](Clippings-MovieToImages.c-OpenADefaultComponent2.txt.md)

# Clippings/MovieToImages.c/Step8.txt

```
    // open the movie
    err = OpenMovieFile( &theFSSpec, &refNum, fsRdWrPerm );
    resID = movieInDataForkResID;

    // add the movie resource to the file
    err = AddMovieResource( movie, refNum, &resID, NULL );
    err = CloseMovieFile( refNum );
```

[Next](Clippings-MultipleImages.clp-GetImageCount.txt.md)[Previous](Clippings-MovieToImages.c-OpenADefaultComponent2.txt.md)

