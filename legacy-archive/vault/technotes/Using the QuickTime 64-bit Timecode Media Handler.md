---
title: Using the QuickTime 64-bit Timecode Media Handler
apple_id: DTS10004455
resource_type: Technical Note
platform: macOS
topic: null
technology: QuickTime
published: '2007-09-18'
source_url: https://developer.apple.com/library/archive/technotes/tn2198/_index.html
archived_at: '2026-07-26T19:54:09.260616Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2198

# Using the QuickTime 64-bit Timecode Media Handler

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

With the release of Mac OS X 10.5 and QuickTime 7.3, a new Timecode Media Handler supporting 64-bit counter values has been added to QuickTime. This Technical note discusses APIs and capabilities available with this new Timecode Media Handler allowing developers to work with 64-bit counter values.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvke4vcbi4yq)[Background](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvbecq2li5je6vkoiq)[Compatibility](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvke4vcbi4za)[Data Structures and Sample Description](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvcecvcbl5jviusvinkfkusfknpuctsel5juctkqjrcv6rcfknbveskqkreu6tq)[TimeCode64MediaType](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvcecvcbl5jviusvinkfkusfknpuctsel5juctkqjrcv6rcfknbveskqkreu6trnkreu2rkdj5ceknrujvcuiskbkrmvari)[TimeCode64Counter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvcecvcbl5jviusvinkfkusfknpuctsel5juctkqjrcv6rcfknbveskqkreu6trnkreu2rkdj5ceknruinhvktsuivja)[SMPTETime](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvcecvcbl5jviusvinkfkusfknpuctsel5juctkqjrcv6rcfknbveskqkreu6trnkngvavcfkreu2ri)[TimeCodeDef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvcecvcbl5jviusvinkfkusfknpuctsel5juctkqjrcv6rcfknbveskqkreu6trnkreu2rkdj5cekrcfiy)[TimeCodeDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvcecvcbl5jviusvinkfkusfknpuctsel5juctkqjrcv6rcfknbveskqkreu6trnkreu2rkdj5cekrcfknbveskqkreu6tq)[Timecode APIs for TimeCode64MediaType](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvkestkfinhuirk7ifiesu27izhvex2ujfgukq2pirctmncnivcesqkulfiek)[TCGetCurrentFrameAndTimeCodeDef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvkestkfinhuirk7ifiesu27izhvex2ujfgukq2pirctmncnivcesqkulfieklkuindukvcdkvjferkokrdfeqknivau4rcujfgukq2pircuirkg)[TCGetFrameAndTimeCodeDefAtTime](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvkestkfinhuirk7ifiesu27izhvex2ujfgukq2pirctmncnivcesqkulfieklkuindukvcgkjau2rkbjzcfisknivbu6rcfircumqkukreu2ri)[TCTimeCodeTimeToFrameNumber](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvkestkfinhuirk7ifiesu27izhvex2ujfgukq2pirctmncnivcesqkulfieklkuinkestkfinhuirkujfgukvcpizjectkfjzku2qsfki)[TCTimeCodeCounterToFrameNumber](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvkestkfinhuirk7ifiesu27izhvex2ujfgukq2pirctmncnivcesqkulfieklkuinkestkfinhuirkdj5ku4vcfkjke6rssifguktsvjvbekuq)[TCFrameNumberToTimeCodeTime](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvkestkfinhuirk7ifiesu27izhvex2ujfgukq2pirctmncnivcesqkulfieklkuindfeqknivhfktkcivjfit2ujfgukq2pircviskniu)[TCFrameNumberToTimeCodeCounter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvkestkfinhuirk7ifiesu27izhvex2ujfgukq2pirctmncnivcesqkulfieklkuindfeqknivhfktkcivjfit2ujfgukq2pircugt2vjzkekuq)[TCTimeCodeTimeToString](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvkestkfinhuirk7ifiesu27izhvex2ujfgukq2pirctmncnivcesqkulfieklkuinkestkfinhuirkujfgukvcpknkfeskoi4)[TCTimeCodeCounterToString](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvkestkfinhuirk7ifiesu27izhvex2ujfgukq2pirctmncnivcesqkulfieklkuinkestkfinhuirkdj5ku4vcfkjke6u2ukjeu4ry)[Additional Timecode APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvke4vcbi4zq)[TCGetSourceRef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvke4vcbi4zs2vcdi5cviu2pkvjegrksivda)[TCSetSourceRef](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvke4vcbi4zs2vcdkncviu2pkvjegrksivda)[TCGetTimeCodeFlags](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvke4vcbi4zs2vcdi5cvivcjjvcugt2eivdeyqkhkm)[TCSetTimeCodeFlags](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvke4vcbi4zs2vcdkncvivcjjvcugt2eivdeyqkhkm)[TCGetDisplayOptions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvke4vcbi4zs2vcdi5cvircjknieyqkzj5ifiskpjzjq)[TCSetDisplayOptions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvke4vcbi4zs2vcdkncvircjknieyqkzj5ifiskpjzjq)[Timecode Track Sample Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvkestkfinhuirk7krjecq2ll5juctkqjrcv6q2pircq)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwugsbrfvjekrsfkjcu4q2fkm)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbvguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Timecode media allows QuickTime movies to store additional timing information that is not created by or for QuickTime. This additional timing information is typically derived from the original source material for example, SMPTE timecode or audio sample rate. In essence, you can think of a timecode media as providing a link between QuickTime-specific timing information and the original timing information from the source material.

QuickTime has supplied a Timecode Media Handler (`TimeCodeMediaType` or '`tmcd`') supporting a 32-bit counter since the release of QuickTime 2.0. With the release of Mac OS X 10.5 and QuickTime 7.3, a new Timecode Media Handler (`TimeCode64MediaType` or '`tc64`') has been added supporting 64-bit counter values.

[Back to Top](#)

## Background

The new timecode media type (`TimeCode64MediaType`) uses an `SInt64` to store timecode samples and can therefore be used in situations where the older `TimeCodeMediaType` would fail due to its 32-bit counter limit. For example, for audio sampled above 48kHz a 32-bit counter is insufficient to store all timecode values that are valid within a range of 24 hours.

[Back to Top](#)

## Compatibility

The 64-bit `TimeCode64MediaType` media handler is implemented as a separate media handler component. The advantage is that the behavior and APIs offered by the original `TimeCodeMediaType` timecode media handler remain unchanged.

Developers with the need for a 64-bit counter can opt-in to using the `TimeCode64MediaType` media handler and corresponding APIs. This allows QuickTime to provide both the original timecode media support and the newer 64-bit timecode media enhancement without requiring developers to change existing code to deal with 64-bit samples.

[Back to Top](#)

## Data Structures and Sample Description

No new data types or structures have been added to support `TimeCode64MediaType` media. Each media sample in the `TimeCode64MediaType` media is a 64-bit signed quantity; an `SInt64` as defined in `MacTypes.h`.

The new APIs use existing data structures; `TimeCodeDescription` and `TimeCodeDef` from `QuickTimeComponents.h`, `SMPTETime` from `CoreAudioTypes.h` and return `CFString`'s instead of pascal strings.

### TimeCode64MediaType

```
// Movies.h

/*  TimeCode64MediaType: 64-bit time code media */
enum {
    TimeCode64MediaType = 'tc64'
};
```

### TimeCode64Counter

```c
// QuickTimeComponents.h

/* 64-bit counter */
typedef SInt64 TimeCode64Counter;
```

### SMPTETime

```swift
// CoreAudioTypes.h

// SMPTETime
// A structure for holding a SMPTE time.
struct SMPTETime
{
    SInt16  mSubframes; /* The number of subframes in the full message */
    SInt16  mSubframeDivisor; /* The number of subframes per frame (typically 80) */
    UInt32  mCounter; /* The total number of messages received */
    UInt32  mType; /* The kind of SMPTE time using the SMPTE time type constants */
    UInt32  mFlags; /*  A set of flags that indicate the SMPTE state */
    SInt16  mHours; /* The number of hours in the full message */
    SInt16  mMinutes; /* The number of minutes in the full message */
    SInt16  mSeconds; /* The number of seconds in the full message */
    SInt16  mFrames; /* The number of frames in the full message */
};
```

### TimeCodeDef

```swift
// QuickTimeComponents.h

// TimeCodeDef
// The timecode media sample description
struct TimeCodeDef {
  long      flags; /* Flags that provide timecode format information, such as drop-frame, etc.*/
  TimeScale fTimeScale; /* Contains the time scale for interpreting the frameDuration field */
                        /* This field indicates the number of time units per second (eg. 2997) */
  TimeValue frameDuration; /* Specifies how long each frame lasts, in the units defined by the */
                           /* fTimeScale field (eg. 100) */
  UInt8     numFrames; /* Indicates the number of frames stored per second (eg. 30) OR In the case */
                       /* of timecodes that are interpreted as counters, this field indicates the */
                       /* number of frames stored per timer "tick" */
  UInt8     padding; /* unused padding */
};
```

### TimeCodeDescription

```swift
// QuickTimeComponents.h

// TimeCodeDescription
// The timecode media sample description
struct TimeCodeDescription {
  long  descSize; /* Specifies the size of the sample description, in bytes */
  long  dataFormat; /* Indicates the sample description type */
  long  resvd1; /* Set to 0 */
  short resvd2; /* Set to 0 */
  short dataRefIndex; /* Contains an index value indicating which of the media's data references */
                      /* contains the sample data for this sample description */
  long  flags; /* Reserved, set to 0 */
  TimeCodeDef timeCodeDef; /* Contains a timecode definition structure that defines timecode */
                           /* format information */
  long  srcRef[1]; /* Contains the timecode's source information. This is formatted as a user data */
                   /* item that is stored in the sample description. The media handler provides */
                   /* functions that allow you to get and set this data */
};
```

[Back to Top](#)

## Timecode APIs for TimeCode64MediaType

The following APIs work with the `TimeCode64MediaType` media handler component and should __only__ be used with `TimeCode64MediaType` media. They are not compatible with `TimeCodeMediaType` media and are not implemented in the older `TimeCodeMediaType` media handler.

### TCGetCurrentFrameAndTimeCodeDef

```
HandlerError TCGetCurrentFrameAndTimeCodeDef(MediaHandler mh,
                                             SInt64 *outFrameNum,
                                             TimeCodeDef *outTCDef)

Description:

Retrieves the frame number and time code format information for the current movie time.

Parameters:

mh - The time code media handler.
outFrameNum - Pointer to a field that receives the current frame number.
outTCDef - Pointer to field that receives the time code format information.
```

### TCGetFrameAndTimeCodeDefAtTime

```
HandlerError TCGetFrameAndTimeCodeDefAtTime(MediaHandler mh,
                                            const TimeValue64* mediaTime,
                                            SInt64 *outFrameNum,
                                            TimeCodeDef *outTCDef)

Description:

Retrieves the frame number and time code format information for a specific media time.

Parameters:

mh - The time code media handler.
mediaTime - A const pointer to the field containing the media time at which time code information is required.
outFrameNum - Pointer to a field that receives the frame number at time mediaTime.
outTCDef - Pointer to field that receives the time code format information.
```

### TCTimeCodeTimeToFrameNumber

```
HandlerError TCTimeCodeTimeToFrameNumber(MediaHandler mh,
                                         const TimeCodeDef *tCDef,
                                         const SMPTETime *tCTime,
                                         SInt64 *outFrameNum)

Description:

Converts a time value into its corresponding frame number.

Parameters:

mh - The time code media handler.
tCDef - A const pointer to a TimeCodeDef that contains time code format info for the conversion.
tCTime - A const pointer to a SMPTETime structure that contains the time value to convert.
outFrameNum - Pointer to a field that is to receive the frame number corresponding to the time
              value in tCTime.
```

### TCTimeCodeCounterToFrameNumber

```
HandlerError TCTimeCodeCounterToFrameNumber(MediaHandler mh,
                                            const TimeCodeDef *tCDef,
                                            const TimeCode64Counter *tCCounter,
                                            SInt64 *outFrameNum)

Description:

Converts a counter value into its corresponding frame number.

Parameters:

mh - The time code media handler.
tCDef - A const pointer to a TimeCodeDef that contains format info for the conversion.
tCCounter - A const pointer to a TimeCode64Counter that contains the counter value to convert.
outFrameNum - Pointer to a field that is to receive the frame number corresponding to the counter
              value in tCCounter.
```

### TCFrameNumberToTimeCodeTime

```
HandlerError TCFrameNumberToTimeCodeTime(MediaHandler mh,
                                         const SInt64* frameNumber,
                                         const TimeCodeDef *tCDef,
                                         SMPTETime *outTCTime)

Description:

Converts a frame number to its corresponding timecode time value.

Parameters:

mh - The time code media handler.
frameNumber - A const pointer to the field containing the frame number that is to be converted.
tCDef - A const pointer to a TimeCodeDef that contains format info for
        the conversion.
outTCTime - Pointer to a SMPTETime structure that is to receive the time value.
```

### TCFrameNumberToTimeCodeCounter

```
HandlerError TCFrameNumberToTimeCodeCounter(MediaHandler mh,
                                            const SInt64* frameNumber,
                                            const TimeCodeDef *tCDef,
                                            TimeCode64Counter *outTCCounter)

Description:

Converts a frame number to its corresponding counter value.

Parameters:

mh The time code media handler.
frameNumber A const pointer to the field containing the frame number that is to be converted.
tCDef A const pointer to a TimeCodeDef that contains format info for the conversion.
outTCCounter Pointer to a TimeCode64Counter that is to receive the counter value.
```

### TCTimeCodeTimeToString

```
HandlerError TCTimeCodeTimeToString(MediaHandler mh,
                                    const TimeCodeDef *tCDef,
                                    const SMPTETime *tCTime,
                                    CFStringRef* outTCStr)

Description:

Converts a time value into a text string in the (-) HH:MM:SS:FF format.

Parameters:

mh - The time code media handler.
tCDef - A const pointer to a TimeCodeDef that contains time code format info for the conversion.
tCTime - A const pointer to a SMPTETime structure that contains the time value to convert.
outTCStr - Pointer to a CFStringRef that is to receive the converted time value.
           The client is responsible for disposing the string.
```

### TCTimeCodeCounterToString

```
HandlerError TCTimeCodeCounterToString(MediaHandler mh,
                                       const TimeCodeDef *tCDef,
                                       const TimeCode64Counter *tCCounter,
                                       CFStringRef* outTCStr)

Description:

Converts a counter value into a text string.

Parameters:

mh - The time code media handler.
tCDef - A const pointer to a TimeCodeDef that contains time code format info for the conversion.
tCCounter - A const pointer to a TimeCode64Counter that contains the counter value to convert.
outTCStr - Pointer to a CFStringRef that is to receive the converted time value.
           The client is responsible for disposing the string.
```

[Back to Top](#)

## Additional Timecode APIs

These APIs may be called when using both the `TimeCode64MediaType` and the `TimeCodeMediaType` media handlers as they do not deal with media samples or strings.

### TCGetSourceRef

```
HandlerError TCGetSourceRef(MediaHandler mh,
                            TimeCodeDescriptionHandle tcdH,
                            UserData *srefH)

Description:

Retrieves the source information from the timecode media sample reference.

Parameters:

mh - A timecode media handler. You obtain this identifier by calling GetMediaHandler. May be either the 32-bit
     Timecode Media Handler or the 64-bit Timecode Media Handler.
tcdH - Specifies a handle to a TimeCodeDescription structure that defines the media sample reference for this
       operation.
srefH - Specifies a pointer to a handle that will receive the source information as a UserDataRecord
        structure. It is your responsibility to dispose of this structure when you are done with it.
```

### TCSetSourceRef

```
HandlerError TCSetSourceRef(MediaHandler mh,
                            TimeCodeDescriptionHandle tcdH,
                            UserData srefH)

Description:

Changes the source information in the timecode media sample reference.

Parameters:

mh - A timecode media handler. You obtain this identifier by calling GetMediaHandler. May be either the 32-bit
     Timecode Media Handler or the 64-bit Timecode Media Handler.
tcdH - Specifies a handle containing the timecode media sample reference that is to be updated.
srefH - Specifies a handle to the source information to be placed in the sample reference as a UserDataRecord
         structure. It is your responsibility to dispose of this structure when you are done with it.
```

### TCGetTimeCodeFlags

```
HandlerError TCGetTimeCodeFlags(MediaHandler mh,
                                long *flags)

Description:

Retrieves the timecode control flags.

Parameters:

mh - A timecode media handler. You obtain this identifier by calling GetMediaHandler. May be either the 32-bit
     Timecode Media Handler or the 64-bit Timecode Media Handler.
flags - A pointer to a field that is to receive a control flag: tcdfShowTimeCode.
```

### TCSetTimeCodeFlags

```
HandlerError TCSetTimeCodeFlags(MediaHandler mh,
                                long flags,
                                long flagsMask)

Description:

Changes the flag that affects how the toolbox handles timecode information.

Parameters:

mh - A timecode media handler. You obtain this identifier by calling GetMediaHandler. May be either the 32-bit
     Timecode Media Handler or the 64-bit Timecode Media Handler.
flags - The new flag value. Can contain the control flag tcdfShowTimeCode.
flagsMask - Specifies which of the flag values are to change. The media handler modifies only those flag
            values that correspond to bits that are set to 1 in this parameter. Use the flag values from the
            flags parameter. To turn off timecode display, set the tcdfShowTimeCode flag to 1 in the flagsMask
            parameter and to 0 in the flags parameter.
```

### TCGetDisplayOptions

```
HandlerError TCGetDisplayOptions(MediaHandler mh,
                                 TCTextOptionsPtr textOptions)

Description:

Retrieves the text characteristics that apply to timecode information displayed in a movie.

Parameters:

mh - A timecode media handler. You obtain this identifier by calling GetMediaHandler. May be either the 32-bit
     Timecode Media Handler or the 64-bit Timecode Media Handler.
textOptions - A pointer to a TCTextOptions structure. This structure will receive font and style information.
```

### TCSetDisplayOptions

```
HandlerError TCSetDisplayOptions(MediaHandler mh,
                                 TCTextOptionsPtr textOptions)

Description:

Sets the text characteristics that apply to timecode information displayed in a movie.

Parameters:

mh - A timecode media handler. You obtain this identifier by calling GetMediaHandler. May be either the 32-bit
     Timecode Media Handler or the 64-bit Timecode Media Handler.
textOptions - A pointer to a TCTextOptions structure. This structure contains font and style information.
```

[Back to Top](#)

## Timecode Track Sample Code

You can create a timecode track and `TimeCode64MediaType` media in the same manner that you create any other track. Call `NewMovieTrack` to create the timecode track, and use `NewTrackMedia` to create the track’s media. Be sure to specify a media type value of `TimeCode64MediaType` when you call `NewTrackMedia`.

__Listing 1__  Create the track and media.

```
 Track theTCTrack = 0;
    Media theTCMedia = 0;
    MediaHandler theTCMediaHandler;

...

    // create a new track and TimeCode64MediaType media
    theTCTrack = NewMovieTrack(theMovie, FloatToFixed(movieSize.width), kTimeCodeTrackMaxHeight, kNoVolume);
    theTCMedia = NewTrackMedia(theTCTrack, TimeCode64MediaType, movieDuration.timeScale, NULL, 0);

    // get the media handler for later use
    theTCMediaHandler = GetMediaHandler(theTCMedia);

...
```

The timecode media sample description contains the control information that allows QuickTime to interpret the samples. This includes the timecode format information. Each sample in the timecode track provides timecode information for a span of movie time and includes duration information.

The actual sample data contains a frame number that identifies one or more content frames that use this timecode. Stored as a `SInt64`, this value identifies the first frame in the group of frames that use this timecode.

__Listing 2__  Add the media sample.

```
...

    TimeCodeDescriptionHandle theTCSampleDescriptionH = NULL;
    TimeCodeDef theTCDef;

    // the timecode or counter value to display depending on gUseTimeCode
    SMPTETime theTCTime = { 0, 1, 0, kSMPTETimeType2997, kSMPTETimeValid, 1, 0, 0, 0 }; // 01:00:00:00
    TimeCode64Counter theTCCounter = 1000;

    // fill in a timecode definition structure which becomes part of the timecode sample description
    // the tcCounter flag is used to display the counter instead of SMPTE timecode
    if (YES == gUseTimeCode) {
        theTCDef.flags = tcDropFrame | tc24HourMax;
    } else {
        theTCDef.flags = tcCounter;
    }
    theTCDef.fTimeScale = 2997;
    theTCDef.frameDuration = 100;
    theTCDef.numFrames = 30;

    // adding samples so start a media edit session
    BeginMediaEdits(theTCMedia);

    // fill in the sample description
    theTCSampleDescriptionH = (TimeCodeDescriptionHandle)NewHandleClear(sizeof(TimeCodeDescription));

    (**theTCSampleDescriptionH).descSize = sizeof(TimeCodeDescription);
    (**theTCSampleDescriptionH).dataFormat = TimeCode64MediaType;
    (**theTCSampleDescriptionH).timeCodeDef = theTCDef;

    // you may store source identification information as UserData if you wish

...

    // add the media sample
    SInt64 theMediaSample = 0L;

    // convert the timecode or counter into a frame number - the sample data contains a single frame
    // number that identifies one or more content frames that use the timecode
    if (YES == gUseTimeCode) {
        TCTimeCodeTimeToFrameNumber(theTCMediaHandler, &theTCDef, &theTCTime, &theMediaSample);
    } else {
        TCTimeCodeCounterToFrameNumber(theTCMediaHandler, &theTCDef, &theTCCounter, &theMediaSample);
    }

    // the timecode media sample must be big-endian
    theMediaSample = EndianS64_NtoB(theMediaSample);

...

    // add the media sample using AddMediaSample2 (don't use older APIs)
    // if you created the track with the same timescale as the movie you don't need to convert the duration
    AddMediaSample2(theTCMedia, (UInt8 *)(&theMediaSample), sizeof(SInt64),
                    movieDuration.timeValue, 0, (SampleDescriptionHandle)theTCSampleDescriptionH, 1, 0, NULL);

    // end the media edit session
    EndMediaEdits(theTCMedia);

    // insert the media reference into the track at the start
    InsertMediaIntoTrack(theTCTrack, 0, 0, movieDuration.timeValue, fixed1);

...
```

__Listing 3__  GetATimecodeMediaHandler.

```
/* MediaHandler GetATimecodeMediaHandler(Movie inMovie, OSType inTimecodeMediaType)

Returns a media handler for the first track containing the specified timecode media type in a specified movie.

inMovie - a QuickTime Movie.
inTimecodeMediaType - timecode media type, can be TimeCodeMediaType or TimeCode64MediaType.

*/
MediaHandler GetATimecodeMediaHandler(Movie inMovie, OSType inTimecodeMediaType)
{
    Track        track = NULL;
    Media        media = NULL;
    MediaHandler mediaHandler = 0;

    if ((inTimecodeMediaType == TimeCode64MediaType) ||
        (inTimecodeMediaType == TimeCodeMediaType)) {

        // get the first timecode track of the specified type in the specified movie
        track = GetMovieIndTrackType(inMovie, 1, inTimecodeMediaType, movieTrackMediaType);
        if (track != NULL) {
            // get the timecode track's media and media handler
            media = GetTrackMedia(track);
            if (media != NULL)
              mediaHandler = GetMediaHandler(media);
        }
    }

    return mediaHandler;
}
```

__Listing 4__  DoesMovieHaveTimecodeTrack.

```
/* Boolean DoesMovieHaveTimeCodeTrack(Movie theMovie, OSType inTimecodeMediaType)

Returns YES if a specified QuickTime Movie has a track of the specified Timecode media type.

inMovie - a QuickTime Movie.
inTimecodeMediaType - timecode media type, can be TimeCodeMediaType or TimeCode64MediaType.

*/
Boolean DoesMovieHaveTimecodeTrack(Movie inMovie, OSType inTimecodeMediaType)
{
    Boolean hasTrack = NO;

    if ((inTimecodeMediaType == TimeCode64MediaType) ||
        (inTimecodeMediaType == TimeCodeMediaType)) {

        hasTrack = (GetMovieIndTrackType(inMovie, 1, inTimecodeMediaType, movieTrackMediaType) != NULL);
    }

    return hasTrack;
}
```

__Listing 5__  GetCurrentTimeCode64`CFString`.

```
/* MediaHandler CFStringRef GetCurrentTimeCode64CFString(Movie inMovie)

Returns the timecode string value for the current movie time.

inMovie - a QuickTime Movie.
*/
CFStringRef GetCurrentTimeCode64CFString(Movie inMovie)
{
    MediaHandler mediaHandler = 0;
    CFStringRef  tcString = NULL;
    HandlerError err = noErr;

    TimeCodeDef tcDef;
    SInt64      frameNumber;
    SMPTETime   tcTime;

    mediaHandler = GetATimecodeMediaHandler(inMovie, TimeCode64MediaType);
    if (0 != mediaHandler) {
        // get the frame number for the current movie time
        err = TCGetCurrentFrameAndTimeCodeDef(mediaHandler, &frameNumber, &tcDef);

        if (noErr == err) {
            // get the timecode time
            err = TCFrameNumberToTimeCodeTime(mediaHandler, &frameNumber, &tcDef, &tcTime);

            if (noErr == err) {
                // get the string value
                err = TCTimeCodeTimeToString(mediaHandler, &tcDef, &tcTime, &tcString);
            }
        }
    }

    return tcString;
}
```

[Back to Top](#)

## References

- [Original Timecode Media Handler Functions](https://developer.apple.com/DOCUMENTATION/QuickTime/RM/MovieBasics/MTEditing/I-Chapter/chapter_1000_section_1.html)
- [QuickTime Media Types Timecode Media Handlers](https://developer.apple.com/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/E-Chapter%20copy%205/chapter_1000_section_1.html)
- [Sample Code 'QTKitTimeCode'](https://developer.apple.com/samplecode/QTKitTimeCode/index.html)
- [MacTech - Using QuickTime's Timecode Media Handler](http://www.mactech.com/articles/mactech/Vol.16/16.12/Dec00QTToolkit/index.html)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-09-18 | New document that discusses 64-bit Timecode Media support added with Mac OS X 10.5 and QuickTime 7.3 |

