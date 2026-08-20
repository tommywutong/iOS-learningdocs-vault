---
title: Movie From DataRef
apple_id: DTS10001039
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Movie_From_DataRef/Listings/Clippings_CreateMovie_c_CreateMovieFromDataRef_txt.html
archived_at: '2026-07-18T03:16:21.700699Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Movie From DataRef](Movie%20From%20DataRef.md)


[Next](Common%20Files-ComFramework.c.md)[Previous](Clippings-CreateMovie.c-CreateDataRefVars.txt.md)

# Clippings/CreateMovie.c/CreateMovieFromDataRef.txt

```
        // Create the movie file using a URL data reference. This
        // URL is added to the movie as a streaming movie track.
        // We make sure and pass the newMovieAsyncOK flag to enable
        // us to query the state of the movie as it loads via the
        // GetMovieLoadState function.

        err = NewMovieFromDataRef(&theMovie,                        /* the movie */
                                newMovieActive | newMovieAsyncOK,   /* flags */
                                nil,                                /* don't return resource id of movie resource */
                                dataRef,                            /* the data reference */
                                URLDataHandlerSubType);             /* the type of data reference */
```

[Next](Common%20Files-ComFramework.c.md)[Previous](Clippings-CreateMovie.c-CreateDataRefVars.txt.md)

