---
title: How do I count the frames in an MPEG movie?
apple_id: DTS10002024
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-19'
source_url: https://developer.apple.com/library/archive/qa/qtmtb54/_index.html
archived_at: '2026-07-18T02:38:49.945986Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QTMTB54

# How do I count the frames in an MPEG movie?

## Q:  I'm using the Movie Toolbox function `GetMovieNextInterestingTime` with QuickTime 6 to count the frames in an MPEG movie but it does not seem to work. The first call to this function just returns a sample time of zero and a duration which is equal to the duration of the movie. Do I have to write special code for MPEG movie tracks?

A: `GetMovieNextInterestingTime` works for all kinds of tracks. However, you should avoid using the `nextTimeMediaSample` flag when searching for frames, because some media types store many frames in a single media sample (for example, MPEG and Flash do this). If you are searching for distinct frame times, pass the `nextTimeStep` flag to `GetMovieNextInterestingTime`.

Also, for MPEG media there is a bug (r. 3236091) in QuickTime 6 which requires you to first task the movie before calling `GetMovieNextInterestingTime` to count the frames in this manner. Here's a code snippet showing how it's done:

__Listing 1__  Counting the frames of an MPEG movie.

```c
#include <QuickTime/QuickTime.h>

long GetFrameCount (Movie theMovie)
{
    long        frameCount = 0;
    TimeValue   curMovieTime;

    if (theMovie == NULL) goto bail;

    // due to a bug in QuickTime 6 we
    // must task the movie first
    MoviesTask( theMovie, 0 );

    curMovieTime = 0;
    while( curMovieTime &gt;= 0 )
    {
        GetMovieNextInterestingTime(theMovie,
                                    nextTimeStep,
                                    0, NULL,
                                    curMovieTime,
                                    fixed1,
                                    &amp;curMovieTime,
                                    NULL );
        frameCount++;
     }

    // there's an extra time step at the end
    // of the movie
    frameCount--;

bail:

    return(frameCount);
}
```

Be aware, also, that tweening can be used to describe transformations that occur smoothly across a continuum of time rather than at discrete moments. For example, a wipe effect between two video sources will produce a distinct output image at every moment between its start and end times. In such a situation, the question, "How many frames are there?" isn't very helpful, since the honest answer is: "As many as you'd like."

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-19 | Editorial |
| 2003-05-02 | New document that talks about using the QuickTime Movie Toolbox function GetMovieNextInterestingTime with MPEG media tracks. |

