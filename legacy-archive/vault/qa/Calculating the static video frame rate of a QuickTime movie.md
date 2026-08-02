---
title: Calculating the static video frame rate of a QuickTime movie.
apple_id: DTS10002297
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2008-08-06'
source_url: https://developer.apple.com/library/archive/qa/qa1262/_index.html
archived_at: '2026-07-18T02:30:18.057629Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1262

# Calculating the static video frame rate of a QuickTime movie.

## Q:  How do I calculate the static video frame rate of a QuickTime movie? And are there any special considerations for other media types such as MPEG-1 and MPEG-2?

A: You can compute the static video frame rate using the following simple formula:

static frame rate = (media sample count \* media time scale) / media duration

You can get a count of the samples in your video track media using `GetMediaSampleCount` (or `GetMovieNextInterestingTime`). Similarly, `GetMediaTimeScale` will give you the media's time scale, and `GetMediaDisplayDuration` will give you the display duration of a media.

For MPEG-1/MPEG-2 media the easiest way to get this information is with the `MediaGetPublicInfo` function (see MediaHandlers.h). Simply pass the selector `kMHInfoEncodedFrameRate`.

Here is a code snippet which demonstrates this technique:

__Listing 1__  Calculating the static video frame rate of a movie.

```c
#include <Carbon/Carbon.h>
#include <QuickTime/QuickTime.h>

#define   kCharacteristicHasVideoFrameRate  FOUR_CHAR_CODE('vfrr')
#define   kCharacteristicIsAnMpegTrack     FOUR_CHAR_CODE('mpeg')

OSErr           IsMPEGMediaHandler(MediaHandler inMediaHandler, Boolean *outIsMPEG);
ComponentResult MPEGMediaGetStaticFrameRate(MediaHandler inMPEGMediaHandler, Fixed *outStaticFrameRate);
OSErr           MediaGetStaticFrameRate(Media inMovieMedia, double *outFPS);
void            MovieGetVideoMediaAndMediaHandler(Movie inMovie, Media *outMedia,
                            MediaHandler *outMediaHandler);
void            MovieGetStaticFrameRate(Movie inMovie, double *outStaticFrameRate);

/*

Calculate the static frame rate for a given movie.

*/
void MovieGetStaticFrameRate(Movie inMovie, double *outStaticFrameRate)
{
  assert(inMovie != NULL);
  assert(outStaticFrameRate != NULL);

  *outStaticFrameRate = 0;

  Media movieMedia;
  MediaHandler movieMediaHandler;
  /* get the media identifier for the media that contains the first
    video track's sample data, and also get the media handler for
    this media. */
  MovieGetVideoMediaAndMediaHandler(inMovie, &movieMedia, &movieMediaHandler);
  if (movieMedia && movieMediaHandler)
  {
    Boolean isMPEG = false;
    /* is this the MPEG-1/MPEG-2 media handler? */
    OSErr err = IsMPEGMediaHandler(movieMediaHandler, &isMPEG);
    if (err == noErr)
    {
      if (isMPEG) /* working with MPEG-1/MPEG-2 media */
      {
        Fixed staticFrameRate;
        ComponentResult err = MPEGMediaGetStaticFrameRate(movieMediaHandler, &staticFrameRate);
        if (err == noErr)
        {
          /* convert Fixed data result to type double */
          *outStaticFrameRate = Fix2X(staticFrameRate);
        }
      }
      else  /* working with non-MPEG-1/MPEG-2 media */
      {
        OSErr err = MediaGetStaticFrameRate(movieMedia, outStaticFrameRate);
        assert(err == noErr);
      }
    }
  }
}

/*

Get the media identifier for the media that contains the first
video track's sample data, and also get the media handler for
this media.

*/
void MovieGetVideoMediaAndMediaHandler(Movie inMovie, Media *outMedia, MediaHandler *outMediaHandler)
{
  assert(inMovie != NULL);
  assert(outMedia != NULL);
  assert(outMediaHandler != NULL);

  *outMedia = NULL;
  *outMediaHandler = NULL;

  /* get first video track */
  Track videoTrack = GetMovieIndTrackType(inMovie, 1, kCharacteristicHasVideoFrameRate,
              movieTrackCharacteristic | movieTrackEnabledOnly);
  if (videoTrack != NULL)
  {
    /* get media ref. for track's sample data */
    *outMedia = GetTrackMedia(videoTrack);
    if (*outMedia)
    {
      /* get a reference to the media handler component */
      *outMediaHandler = GetMediaHandler(*outMedia);
    }
  }
}

/*

Return true if media handler reference is from the MPEG-1/MPEG-2 media handler.
Return false otherwise.

*/
OSErr IsMPEGMediaHandler(MediaHandler inMediaHandler, Boolean *outIsMPEG)
{
  assert(inMediaHandler != NULL);
  assert(outIsMPEG != NULL);

  /* is this the MPEG-1/MPEG-2 media handler? */
  return(MediaHasCharacteristic(inMediaHandler,
                  kCharacteristicIsAnMpegTrack,
                  outIsMPEG));
}

/*

Given a reference to the media handler used for media in a MPEG-1/MPEG-2
track, return the static frame rate.

*/
ComponentResult MPEGMediaGetStaticFrameRate(MediaHandler inMPEGMediaHandler, Fixed *outStaticFrameRate)
{
  assert(inMPEGMediaHandler != NULL);
  assert(outStaticFrameRate != NULL);

  *outStaticFrameRate = 0;

  MHInfoEncodedFrameRateRecord encodedFrameRate;
  Size encodedFrameRateSize = sizeof(encodedFrameRate);

    /* get the static frame rate */
  ComponentResult err = MediaGetPublicInfo(inMPEGMediaHandler,
                       kMHInfoEncodedFrameRate,
                       &encodedFrameRate,
                       &encodedFrameRateSize);
  if (err == noErr)
  {
    /* return frame rate at which the track was encoded */
    *outStaticFrameRate = encodedFrameRate.encodedFrameRate;
  }

  return err;
}

/*

Given a reference to the media that contains the sample data for a track,
calculate the static frame rate.

*/
OSErr MediaGetStaticFrameRate(Media inMovieMedia, double *outFPS)
{
  assert(inMovieMedia != NULL);
  assert(outFPS != NULL);

  *outFPS = 0;

    /* get the number of samples in the media */
  long sampleCount = GetMediaSampleCount(inMovieMedia);
  OSErr err = GetMoviesError();

  if (sampleCount && err == noErr)
  {
      /* find the media duration */
    TimeValue64 duration = GetMediaDisplayDuration(inMovieMedia);
    err = GetMoviesError();
    if (err == noErr)
    {
        /* get the media time scale */
      TimeValue64 timeScale = GetMediaTimeScale(inMovieMedia);
      err = GetMoviesError();
      if (err == noErr)
      {
        /* calculate the frame rate:
          frame rate = (sample count * media time scale) / media duration
          */
        *outFPS = (double)sampleCount * (double)timeScale / (double)duration;
      }
    }
  }

  return err;
}
```

Alternately, you could count the MPEG-1 MPEG-2 video frames using `GetMovieNextInterestingTime` as described in [Technical Q&A QTMTB54, 'How do I count the frames in an MPEG movie?'](https://developer.apple.com/qa/qtmtb/qtmtb54.html), then use the media duration and time scale values to compute the frame rate.

Here is a code snippet that demonstrates this technique:

__Listing 2__  Calculating the MPEG-1/MPEG-2 frame rate using `GetMovieNextInterestingTime`.

```c
#include <QuickTime/QuickTime.h>

long GetMPEGFrameCount (Movie theMovie)
{
    assert(theMovie != NULL);

    long        frameCount = 0;
    TimeValue   curMovieTime;

    curMovieTime = 0;
    while( curMovieTime >= 0 )
    {
        GetMovieNextInterestingTime(
                                    theMovie,
                                    nextTimeStep,
                                    0, NULL,
                                    curMovieTime,
                                    fixed1,
                                    &curMovieTime,
                                    NULL );
        frameCount++;
    }

    frameCount--; // there's an extra time step at the end of the movie

    return(frameCount);
}

OSErr MPEGMovieGetFrameRate(Movie theMovie, float *fps)
{
    assert(theMovie != NULL);
    assert(fps != NULL);

        /* initialize fps value */
    *fps = 0;

        /* get movie duration */
    float duration = GetMovieDuration(theMovie);
    OSErr err = GetMoviesError();
    if (err == noErr)
    {
            /* get movie time scale */
        float timeScale = GetMovieTimeScale(theMovie);
        err = GetMoviesError();
        if (err == noErr)
        {
                /* calculate frame rate */
            *fps = ((float)GetMPEGFrameCount(theMovie) * timeScale) / duration;
        }
    }

    return(err) ;
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-08-06 | Miscellaneous code changes. |
| 2007-07-30 | Code updated for QuickTime 7. |
| 2003-06-02 | New document that calculating the static video frame rate of a QuickTime movie. |

