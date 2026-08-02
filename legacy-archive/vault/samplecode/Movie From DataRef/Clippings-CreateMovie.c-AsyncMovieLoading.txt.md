---
title: Movie From DataRef
apple_id: DTS10001039
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Movie_From_DataRef/Listings/Clippings_CreateMovie_c_AsyncMovieLoading_txt.html
archived_at: '2026-07-18T03:16:21.589739Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Movie From DataRef](Movie%20From%20DataRef.md)


[Next](Clippings-CreateMovie.c-CreateDataRef.txt.md)[Previous](Application%20Files-MacApplication.r.md)

# Clippings/CreateMovie.c/AsyncMovieLoading.txt

```
        // Handle asynchronous movie loading here. We use the new
        // GetMovieLoadState function to determine the load state
        // of the movie.
        do
        {
            long newLoadState;

            // Get new load state to see if there was a change in
            // state.
            newLoadState = GetMovieLoadState(theMovie);
            if (newLoadState != loadState)
            {
                loadState = newLoadState;
                if (loadState < 0)
                {
                    // failed to load the movie - this will cause
                    // us to drop out of this loop and report an
                    // error
                }

                if (loadState < kMovieLoadStatePlayable)
                {
                    // we need to keep tasking the movie so it gets
                    // time to load

                    MoviesTask(theMovie, 0);
                }

                if (loadState < kMovieLoadStateComplete)
                {
                    // we just became playable
                }

                if (loadState >= kMovieLoadStateComplete)
                {
                    // now we know all media data is available
                    // this will drop us out of this loop so we
                    // can display the movie
                }
            }
        } 
        while ((loadState > kMovieLoadStateError) && (loadState < kMovieLoadStateComplete));

        CheckError(err, "NewMovieFromDataRef error");

        // dispose of our data reference handle since it is no longer needed
        DisposeHandle(dataRef);

        result = GetMovieStatus (theMovie, &firstProblemTrack);

        // if GetMovieLoadState from above returned kMovieLoadStateError, and
        // GetMovieStatus returns nil for the firstProblemTrack parameter we
        // know an error occurred
        if ((loadState == kMovieLoadStateError) && (firstProblemTrack == nil))
        {
            CheckError(-1, "NewMovieFromDataRef error");
        }
```

[Next](Clippings-CreateMovie.c-CreateDataRef.txt.md)[Previous](Application%20Files-MacApplication.r.md)

