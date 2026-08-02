---
title: Looping Audio Files with QuickTime for Windows
apple_id: DTS10004491
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2007-10-09'
source_url: https://developer.apple.com/library/archive/qa/qa1559/_index.html
archived_at: '2026-07-18T02:32:18.212040Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1559

# Looping Audio Files with QuickTime for Windows

## Q:  I'd like to continuously loop an audio file in my application using QuickTime for Windows. I've tried this with QuickTime Player, but the initial portion of the audio is always clipped when it loops. Please explain.

A: When QuickTime reaches a loop point in a movie, a SetTime action is generated internally to jump back to the loop point. The movie timebase runs continuously through this action, and the video display tends to be fairly smooth across this transition. However, the QuickTime audio queue is flushed and audio data starting at the new position is transmitted.

For reasons having to do with the robustness of the DirectSound audio data callbacks, QuickTime for Windows maintains a fairly deep safety buffer for queuing audio samples...nearly a half a second (as opposed to a small fraction of that in QuickTime on Macintosh). This means that in order to keep audio and video in sync, the first half-second of audio at the loop point is silent while the newly queued samples move through the safety buffer. This doesn't happen on the initial play, or when you jump to a new position in the file, because QuickTime will intentionally delay the start of video to line up with the playback of the first audio sample.

We hope to improve this behavior by queuing the audio around the loop point, but the behavior for now, on Windows platforms, is what you've observed. Application writers who would prefer to hear all the audio data, rather than preserve the forward motion of the timeline, can manage the looping manually by setting a timebase callback for the loop endpoint, and then issuing a Stop/SetTime/Start sequence to restart at the loop start. This technique is demonstrated in the code snippet in Listing 1 below. This code uses a movie callback event which triggers when the movie finishes playing. Then, the movie Stop/SetTime/Start sequence is re-issued to restart at the loop start.

__Listing 1__  Looping an audio file using QuickTime for Windows callback events.

```swift
// convenient callback event data structure
typedef struct MyAppData
{
    Movie         myMovie;
    Boolean       keepLooping;
    TimeRecord    movieStartTime;
    QTCallBack    myQTCallBack;
    QTCallBackUPP myCallBackUPP;
} MyAppData, *MyAppDataPtr;

// continuously loop an audio file
void loopAMovie(Movie inMovie)
{
    // save movie for easy reference in the callback
    gAppData.myMovie = inMovie;

    // setup timebase callback for when the movie stops
    setupMovieCallback(&gAppData);

    // we'll check this flag in the callback to decide whether
    // or not to continue movie looping
    gAppData.keepLooping = true;

    // get & save movie start time for reference later in the callback
    GoToBeginningOfMovie (gAppData.myMovie);
    GetMovieTime(gAppData.myMovie, &gAppData.movieStartTime);

    // start the movie looping!
    StartMovie(gAppData.myMovie);
}

// Setup a callback event to trigger using the callBackAtExtremes and
// triggerAtStop flags.
//
// This function will be called when the movie finishes playing (when the
// timebase has stopped).
//

OSErr setupMovieCallback(MyAppDataPtr inAppData)
{
    QTCallBack    theQTCallBack;
    QTCallBackUPP theCallBackUPP;

    OSErr err = paramErr;

    // Create a new callback event
    theQTCallBack = NewCallBack(GetMovieTimeBase(inAppData->myMovie),
                                callBackAtExtremes);
    if (theQTCallBack)
    {
        // Now schedule our callback event to trigger at movie stop
        theCallBackUPP = NewQTCallBackUPP(&myMovieCallback);
        err = CallMeWhen(theQTCallBack,
                        theCallBackUPP,
                        (long)inAppData,
                        triggerAtStop,
                        0,
                        0);
    }

    // Save these so we can use them in our callback.
    // We'll also need to dispose of them properly later
    inAppData->myQTCallBack = theQTCallBack;
    inAppData->myCallBackUPP = theCallBackUPP;

    return err;
}

// Our callback function, installed by CallMeWhen.
//
// This will get called when the movie finishes playing.
// We'll then make movie Stop/SetTime/Start calls to
// restart at the loop start.

pascal void myMovieCallback(QTCallBack cb, long refCon)
{
    if (NULL == refCon) return;

    MyAppDataPtr myData;
    myData = (MyAppDataPtr)refCon;

    // do we want to continue looping?
    if (myData->keepLooping)
    {
        // reschedule callback event to trigger at movie stop
        OSErr err = CallMeWhen(myData->myQTCallBack,
                    myData->myCallBackUPP,
                    (long)myData,
                    triggerAtStop,
                    0,
                    0);

        // You must issue a Stop/SetTime/Start sequence to restart
        // at the movie loop start
        StopMovie(myData->myMovie);
        SetMovieTime(myData->myMovie, &myData->movieStartTime);
        StartMovie(myData->myMovie);
    }

    return;
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-10-09 | New document that how to Continuously Loop Audio Files with QuickTime for Windows |

