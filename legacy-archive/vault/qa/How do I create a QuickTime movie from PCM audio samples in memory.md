---
title: How do I create a QuickTime movie from PCM audio samples in memory?
apple_id: DTS10004420
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2009-08-27'
source_url: https://developer.apple.com/library/archive/qa/qa1539/_index.html
archived_at: '2026-07-18T02:32:15.505556Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1539

# How do I create a QuickTime movie from PCM audio samples in memory?

## Q:  I'm trying to create a QuickTime movie from a memory buffer of PCM audio samples (Stereo, 22.050 kHz) but I'm not having any luck. When I play the resulting movie all I get is silence. Also, how do I properly fill out a `SoundDescription` structure to describe my audio?

A: There are a couple of different ways in which to take an in-memory buffer of audio samples and convert them into an audio track of a movie. One way is to create an empty movie, create a new movie track and track media as defined by a `SoundDescription` structure, and insert your audio samples into the track media using `AddMediaSample2`. The code snippet in Listing 1 shows this technique.

In order to create a `SoundDescription` correctly you should first construct an `AudioStreamBasicDescription` structure (the fundamental descriptive structure in Core Audio) with the fields set correctly for your encoding, and then use the `QTSoundDescriptionCreate` function to translate these settings into a proper `SoundDescription`.

__Listing 1__  Creating a movie from PCM audio data in memory.

```objc
#import <QuickTime/QuickTime.h>

// Constants for use when creating our movie track and media

static const TimeValue  kSoundSampleDuration    = 1;
static const TimeValue  kTrackStart             = 0;
static const TimeValue  kMediaStart             = 0;

// These are custom settings which describe our audio samples.
// You'll want to change these to properly describe your own audio.

static const UInt32                 kNumChannels            = 2;
static const Float64                kSampleRate             = 22050.;
static const AudioChannelLayoutTag  kMyAudioChannelLayout   = kAudioChannelLayoutTag_Stereo;
static const long                   kNumSamples             = 11025; // .5 seconds of 22050

/*

createSoundDescription

Creates a sound description structure of the requested kind
from an AudioStreamBasicDescription, optional audio channel
layout, and optional magic cookie.

outDescHndl - pointer to a handle (empty) in which to copy
the new sound description

*/

-(OSErr) createSoundDescription: (SoundDescriptionHandle *)outDescHndl
{
    assert(outDescHndl != NULL);

    AudioStreamBasicDescription asbd = {0}; //see CoreAudioTypes.h

    asbd.mSampleRate           = kSampleRate;
    asbd.mFormatID             = kAudioFormatLinearPCM;
    asbd.mFormatFlags          = kAudioFormatFlagsNativeFloatPacked;
    // if multi-channel, the data format must be interleaved (non-interleaved is not allowed),
    // and you should set up the asbd accordingly
    asbd.mChannelsPerFrame     = kNumChannels; // 2 (Stereo)
    // mBitsPerChannel = number of bits of sample data for each channel in a frame of data
    asbd.mBitsPerChannel       = sizeof (Float32) * 8; // 32-bit floating point PCM
    // mBytesPerFrame = number of bytes in a single sample frame of data
    // (bytes per channel) * (channels per frame) = 4 * 2 = 8
    asbd.mBytesPerFrame        = (asbd.mBitsPerChannel>>3) // number of *bytes* per channel
                                  * asbd.mChannelsPerFrame; // channels per frame
    asbd.mFramesPerPacket      = 1; // For PCM, frames per packet is always 1
    // mBytesPerPacket = (bytes per frame) * (frames per packet) = 8 * 1 = 8
    asbd.mBytesPerPacket       = asbd.mBytesPerFrame * asbd.mFramesPerPacket;

    // The AudioChannelLayout is used to specify channel layouts
    // (see CoreAudioTypes.h) and consists of the following:
    // - a tag that indicates the layout
    // - channel usage bitmap (used if a "named" tag can't be found
    //        to describe the layout)
    // - a variable length array of AudioChannelDescriptions
    //        that describe the layout/position of a speaker (but if the
    //        tag field is non-zero it refers to one of the standard
    //        "named" layout tags, so the individual channel descriptions
    //        are just there to be more descriptive.

    UInt32 layoutSize;
    layoutSize = offsetof(AudioChannelLayout, mChannelDescriptions[0]);

    AudioChannelLayout *layout = NULL;
    layout = calloc(layoutSize, 1); // make sure all fields start cleared
    OSErr err = -1;
    if (layout != NULL)
    {
        // You must specify a tag identifying a particular pre-defined
        // channel layout as there are many different layouts to choose.
        // In this case we are specifying the following:
        //    kAudioChannelLayoutTag_Stereo
        // - a standard stereo stream (L R) - implied playback
        layout->mChannelLayoutTag = kMyAudioChannelLayout;

        err = QTSoundDescriptionCreate(
                    &asbd,              // format description
                    layout, layoutSize, // channel layout
                    NULL, 0,            // magic cookie (compression parameters)
                    kQTSoundDescriptionKind_Movie_LowestPossibleVersion,
                    outDescHndl); // SoundDescriptionHandle returned here
        free(layout);
    }

    return err;
}


/*

createMovieFromAudioData

Create a movie with a sound track containing the specified
audio data.

inAudioData - pointer to your audio data
inAudioDataSize - size of your audio data
outMovie - pointer to the resulting movie file

*/

-(OSErr) createMovieFromAudioData:(const void *)inAudioData
                                  dataSize:(long)inAudioDataSize
                                  movie:(Movie *)outMovie
{
    assert(inAudioData != NULL);
    assert(inAudioDataSize != 0);
    assert(outMovie != nil);

    *outMovie = NULL;

    // create an empty movie to which we'll add out audio data
    // as a sound track
    *outMovie = NewMovie(0);
    if (*outMovie == NULL) goto bail;

    SoundDescriptionHandle hSoundDesc = NULL;
    // Create a sound description for our audio data
    OSErr err = [self createSoundDescription:&hSoundDesc];
    if (err != noErr) goto bail;

    Track track = NULL;
    // create a movie track to hold our sound media
    track = NewMovieTrack(*outMovie, 0, 0, kFullVolume);
    err = GetMoviesError();
    if (err != noErr) goto bail;

    // create a data reference for storage to hold our media
    // data, because when you create an "empty" movie with
    // NewMovie() there is no designated storage for the movie
    // media.
    Handle dataRef = nil;
    Handle hMovieData = NewHandle(0);
    err = PtrToHand( &hMovieData, &dataRef, sizeof(Handle));
    if (err != noErr) goto bail;

    // get the sample rate value for our data from the asbd so
    // we can use it when creating our track media
    AudioStreamBasicDescription asbd = {0};
    OSStatus status = QTSoundDescriptionGetProperty (
                hSoundDesc,
                kQTPropertyClass_SoundDescription,
                kQTSoundDescriptionPropertyID_AudioStreamBasicDescription,
                sizeof(asbd), &asbd, NULL);
    if (status != 0) goto bail;

    Media media = NULL;
    // create a media for our new track, well add our audio
    // samples to this media
    media = NewTrackMedia(track, SoundMediaType,
                asbd.mSampleRate, // media time scale
                dataRef, HandleDataHandlerSubType); // movie data reference
    err = GetMoviesError();
    if (err != noErr) goto bail;

    err = BeginMediaEdits(media);
    if (err != noErr) goto bail;

    // Add sample data and sample description for our audio data
    // to the track media.
    err = AddMediaSample2 (media,
                           inAudioData, // ptr to our audio data
                           inAudioDataSize, // audio data size
                           /*
                              decodeDurationPerSample
                              The duration of each sample to be added,
                              representing the amount of time (in the
                              media's time scale) that passes while
                              the sample data is being displayed. Since
                              we are adding sound that was sampled at
                              22 kHz to media that contains a sound track
                              with the same time scale we set
                              durationPerSample to 1.

                              In CoreAudio, sample = frame. A frame is
                              an individually accessible uncompressed
                              pcm sample of data. When dealing with PCM,
                              1 packet = 1 frame. But for compressed
                              formats, 1 packet often equals a lot of frames.
                              For instance, 1 AAC packet = 1024 frames.
                              */
                           kSoundSampleDuration, // duration per sample = 1
                           0,
                           (SampleDescriptionHandle)hSoundDesc,
                           kNumSamples,
                           0, // 0 = no flags
                           nil);

    EndMediaEdits(media);
    if (err != noErr) goto bail;

    // Insert a reference to the media segment into the track.
    err = InsertMediaIntoTrack(track,
                            kTrackStart,    // track start time
                            kMediaStart,    // media start time
                            GetMediaDuration(media),
                            fixed1);

bail:
    if (hSoundDesc != NULL)
    {
        DisposeHandle((Handle)hSoundDesc);
    }
    if (err != noErr)
    {
        if (*outMovie != NULL)
        {
            DisposeMovie(*outMovie);
        }
        if (hMovieData != NULL)
        {
            DisposeHandle(hMovieData);
        }
    }

    return err;
}
```


- [Core Audio: Audio Channel Layouts](https://developer.apple.com/documentation/MusicAudio/Reference/CoreAudio/core_audio_types/chapter_6_section_8.html)
- [Core Audio: Audio Stream Basic Description](https://developer.apple.com/documentation/MusicAudio/Reference/CoreAudio/core_audio_types/chapter_6_section_4.html)
- [QuickTime 7 API Reference](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7UpdateGuide/Chapter03/chapter_3_section_1.html)
- [QTExtractAndConvertToAIFF sample code](https://developer.apple.com/samplecode/QTExtractAndConvertToAIFF/index.html)
- [QTExtractAndConvertToMovieFile sample code](https://developer.apple.com/samplecode/QTExtractAndConvertToMovieFile/index.htmll)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-08-27 | Editorial |
| 2007-08-29 | New document that how to create a QuickTime movie from PCM audio samples in memory |

