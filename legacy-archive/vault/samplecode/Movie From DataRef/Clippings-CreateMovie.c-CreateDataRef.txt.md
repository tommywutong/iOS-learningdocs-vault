---
title: Movie From DataRef
apple_id: DTS10001039
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Movie_From_DataRef/Listings/Clippings_CreateMovie_c_CreateDataRef_txt.html
archived_at: '2026-07-18T03:16:21.669265Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Movie From DataRef](Movie%20From%20DataRef.md)


[Next](Clippings-CreateMovie.c-CreateDataRefVars.txt.md)[Previous](Clippings-CreateMovie.c-AsyncMovieLoading.txt.md)

# Clippings/CreateMovie.c/CreateDataRef.txt

```
        // Create a data reference which we will use to create our movie. In this case,
        // we'll construct a URL data reference. The URL data reference
        // is simply a handle whose data is a URL describing a movie.

        dataRef = NewHandleClear(StrLength(url) + 1);
        CheckError(MemError(), "NewHandleClear error");
        BlockMoveData(url, *dataRef, StrLength(url) + 1);
```

[Next](Clippings-CreateMovie.c-CreateDataRefVars.txt.md)[Previous](Clippings-CreateMovie.c-AsyncMovieLoading.txt.md)

