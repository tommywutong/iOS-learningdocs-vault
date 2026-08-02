---
title: Avoiding Pauses When Looping Audio files with QuickTime
apple_id: DTS10003389
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2004-09-08'
source_url: https://developer.apple.com/library/archive/qa/qa1371/_index.html
archived_at: '2026-07-18T02:30:27.293979Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1371

# Avoiding Pauses When Looping Audio files with QuickTime

## Q:  In my program I open an audio file as a QuickTime movie, set the movie's looping state attribute, then start it playing. This all works, and my audio movie properly loops (it automatically starts over again when it finishes), but I experience a very short pause when the movie finishes and starts over. Is there any way to fix this pause?

A: This is a known issue in QuickTime (r. 3792717). For short audio loops you may experience this problem.

The workaround is to create a temporary movie, and add multiple references to your audio source in this temporary movie (QuickTime allows you to reference the same audio data inside a movie multiple times). Then, when you play the temporary movie you are simply playing references to the same audio file over and over again, which QuickTime can do quite smoothly, without pausing.

Adding multiple references (even hundreds) to your source audio file in this manner does not result in a large movie file since each reference contains only a pointer to the actual data, rather than a copy of the data.

You will of course hear the pause when the movie finishes, but if your movie contains hundreds of references to the same audio file the pause will only occur once after the audio has repeated hundreds of times.

The code snippet below shows how to create a temporary movie with multiple references to the original audio file.

__Listing 1__  Creating a temporary movie with multiple references to an audio file.

```
// specifies the number of references to the original audio file
// we will add to our temporary movie

#define kRefCount   30

//
// createAudioRefMovie
//
// This code creates a temporary movie
// with multiple references to the
// the specified audio file
//
// Inputs
//
//     srcAudioFilePath
// - a full path to any audio file that
//         QT understands (an MP3 file for example)
//
// Outputs
//
// - function returns a new movie which
//         contains multiple references to the
//         audio file specified in the
//         srcAudioFilePath parameter

Movie createAudioRefMovie(CFStringRef srcAudioFilePath)
{
    Movie       tempMovie, srcMovie;
    TimeValue   srcMovDuration;
    OSErr       err = noErr;
    Handle      audioFileDataRef;
    OSType      audioFileDataRefType;
    short       i, resID = 0;

    assert(srcAudioFilePath != nil);

        // create a QuickTime data reference
        // for our audio source file
    err = QTNewDataReferenceFromFullPathCFString (
                           srcAudioFilePath,
                           kQTNativeDefaultPathStyle,
                           0,
                           &audioFileDataRef,
                           &audioFileDataRefType );
    assert(err == noErr);

        // create a QuickTime movie for the audio file
        // using the audio file's data reference
    err = NewMovieFromDataRef (
                         &srcMovie,
                         newMovieActive,
                         &resID,
                         audioFileDataRef,
                         audioFileDataRefType );
    assert(err == noErr);

        // initialize our movie
    tempMovie = nil;

        // create a temporary movie -- we'll add
        // references to the audio file to this movie
    tempMovie = NewMovie(newMovieActive);
    assert(tempMovie != nil);

    srcMovDuration = GetMovieDuration(srcMovie);

        // add multiple references to our audio file

        // Note:
        // by not calling BeginMediaEdits/EndMediaEdits
        // we are telling QuickTime to *not* copy the
        // actual data - this will give us only references
        // to the data which are small
    for (i = 0; i < kRefCount; ++i)
    {
           // add a reference to the source audio file to
           // our temporary movie
        err =  InsertMovieSegment (
                                 srcMovie,   // our audio file
                                 tempMovie,  // temporary movie
                                 0,
                                 srcMovDuration,
                                 GetMovieDuration(tempMovie) );
        assert(err == noErr);
    }

       // for completeness we'll copy the movie settings
       // from the source file
    err = CopyMovieSettings(srcMovie, tempMovie);
    assert(err == noErr);

    return tempMovie;
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-09-08 | New document that demonstrates how to avoid pauses when looping audio files with QuickTime |

