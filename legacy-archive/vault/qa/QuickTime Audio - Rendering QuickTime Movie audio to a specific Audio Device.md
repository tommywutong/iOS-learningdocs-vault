---
title: QuickTime Audio - Rendering QuickTime Movie audio to a specific Audio Device
apple_id: DTS10004584
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2008-01-08'
source_url: https://developer.apple.com/library/archive/qa/qa1578/_index.html
archived_at: '2026-07-18T02:32:19.803632Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1578

# QuickTime Audio - Rendering QuickTime Movie audio to a specific Audio Device

## Q:  How can I render QuickTime Movie audio to a specific Audio Device once I have a Audio Device ID?

A: This task can be accomplished with two QuickTime APIs. First, a QuickTime Audio Context must be created for the chosen Audio Device using `QTAudioContextCreateForAudioDevice`. Once a valid `QTAudioContextRef` is returned simply call `SetMovieAudioContext` to have QuickTime assign the Audio Context to the Movie. Listing 1 demonstrates these steps.

__Listing 1__  Creating a QuickTime Audio Context and assigning it to a Movie.

```
// Pass in a fully initialized QTKit QTMovie object and an Audio Device UID CFStringRef
// NOTE: The Audio Device UID String is the persistent kAudioDevicePropertyDeviceUID property returned
//       using AudioDeviceGetProperty.
OSStatus SetMyMovieAudioContextForDevice(QTMovie inMovie, CFStringRef inAudioDeviceUID)
{
    Movie aMovie;
    QTAudioContextRef audioContext;
    OSStatus status = paramErr;

    // while inAudioDeviceUID may be NULL to specify a default audio device the inMovie may not
    if (NULL == inMovie) return status;

    aMovie = [inMovie quickTimeMovie];
    if (NULL == aMovie) return status;

    // create a QT Audio Context and set it on a Movie
    status = QTAudioContextCreateForAudioDevice(kCFAllocatorDefault, inAudioDeviceUID,
                                                NULL, &audioContext);
    if (status) fprintf(stderr, "QTAudioContextCreateForAudioDevice failed: %d\n", (int)status);

    if (NULL != audioContext && noErr == status) {
        status = SetMovieAudioContext(aMovie, audioContext);
        if (status) fprintf(stderr, "SetMovieAudioContext failed: %d\n", (int)status);

        // release the Audio Context since SetMovieAudioContext will retain it
        CFRelease(audioContext);
    }

    return status;
}
```



```
Creates a QTAudioContext object that encapsulates a connection to a CoreAudio output device.

OSStatus QTAudioContextCreateForAudioDevice (
   CFAllocatorRef allocator,
   CFStringRef coreAudioDeviceUID,
   CFDictionaryRef options,
   QTAudioContextRef *newAudioContextOut );

Parameters:

allocator - Allocator used to create the audio context.

coreAudioDeviceUID - CoreAudio device UID, a CFString that contains a persistent identifier for the
                    AudioDevice (kAudioDevicePropertyDeviceUID).
                    Use NULL to specify the default device.

options - Reserved. Pass NULL.

newAudioContextOut - Points to a variable to receive the new audio context.

Discussion

This routine creates a QTAudioContext object that encapsulates a connection to a CoreAudio output
device. This object is suitable for passing to SetMovieAudioContext or NewMovieFromProperties, which
targets the audio output of the movie to that device. A QTAudioContext object cannot be associated with
more than one movie. Each movie needs its own connection to the device. In order to play more than one
movie to a particular device, create a QTAudioContext object for each movie. You are responsible for
releasing the QTAudioContext object created by this routine. After calling SetMovieAudioContext or
NewMovieFromProperties, you can release the object since these APIs will retain it for their own use.

Introduced in QuickTime 7
```



```
Targets a movie to render into an audio context.

OSStatus SetMovieAudioContext (
   Movie movie,
   QTAudioContextRef audioContext;

Parameters:

movie - A QuickTime Movie.

audioContext - The audio context that the movie will render into.

Introduced in QuickTime 7
```


- [QuickTime 7 Audio Enhancements](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7Win_Update_Guide/Chapter02/chapter_2_section_6.html)
- [Setting an Audio Context](https://developer.apple.com/documentation/QuickTime/RM/MovieBasics/MTOpenPlayMovies/3openplaymovies_output/chapter_1000_section_6.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-01-08 | New document that describes how to render Movie audio to a specific audio device. |

