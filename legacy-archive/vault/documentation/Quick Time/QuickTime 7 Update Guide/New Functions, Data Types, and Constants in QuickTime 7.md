---
title: QuickTime 7 Update Guide
apple_id: TP40001163
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2005-04-29'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/Conceptual/QT7UpdateGuide/Chapter03/03QT7_Update_Guide.html
archived_at: '2026-07-18T01:58:11.267233Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime 7 Update Guide](Introduction%20to%20QuickTime%207.md)


[Next](Document%20Revision%20History.md)[Previous](What%E2%80%99s%20New%20in%20QuickTime%207.md)

# New Functions, Data Types, and Constants in QuickTime 7

This chapter describes all the new QuickTime
functions, data structures, constants, and callbacks available in
this software release.

If you are a QuickTime API-level developer, content author,
multimedia producer or Webmaster who is currently working with QuickTime,
you should read this chapter and use it for reference, as needed,
in your application development.

The following functions, callbacks, structures, and constants
are new or changed with this release of QuickTime.

Functions that are new in QuickTime 7 are
described in this section; they are listed in alphabetical order.

Adds sample data and a description to a media.

```
OSErr AddMediaSample2 (
   Media                      theMedia,
   const UInt8                *dataIn,
   ByteCount                  size,
   TimeValue64                decodeDurationPerSample,
   TimeValue64                displayOffset,
   SampleDescriptionHandle    sampleDescriptionH,
   ItemCount                  numberOfSamples,
   MediaSampleFlags           sampleFlags,
   TimeValue64                *sampleDecodeTimeOut );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
dataIn
A handle to the sample data. The function
adds this data to the media specified by
theMedia
.
You specify the number of bytes of sample data with the
size
parameter.
size
The number of bytes of sample data to be added
to the media. This parameter indicates the total number of bytes
in the sample data to be added to the media, not the number of bytes
per sample. Use the
numberOfSamples
parameter
to indicate the number of samples that are contained in the sample
data.
decodeDurationPerSample
The duration of each sample to be added, representing
the amount of time that passes while the sample data is being displayed.
You must specify this parameter in the media’s time scale. For
example, if you are adding sound that was sampled at 22 kHz to a
media that contains a sound track with the same time scale, you
would set
durationPerSample
to 1.
Similarly, if you are adding video that was recorded at 10 frames
per second to a video media that has a time scale of 600, you would
set this parameter to 60. Note that this is the duration
per
sample
, regardless of the number of samples being added.
displayOffset
A 64-bit time value that specifies the offset
between the decode time (the start time of the track plus the duration
of all previous samples) and the display time. This value is normally
zero unless the sample is frame reordering compressed video.
sampleDescriptionH
A handle to a
SampleDescription
structure.
Some media structures may require sample descriptions. There are
different descriptions for different types of samples. For example,
a media that contains compressed video requires that you supply
an
ImageDescription
structure. A media that contains
sound requires that you supply a
SoundDescription
structure.
If the media does not require a
SampleDescription
structure,
set this parameter to NIL.
numberOfSamples
The number of samples contained in the sample
data to be added to the media. The Movie Toolbox considers the value
of this parameter as well as the value of the
size
parameter
when it determines the size of each sample that it adds to the media.
You should set the value of this parameter so that the resulting
sample size represents a reasonable compromise between total data
retrieval time and the overhead associated with input and output.
You should also consider the speed of the data storage device; CD-ROM
devices are much slower than hard disks, for example, and should
therefore have a smaller sample size. For a video media, set a sample
size that corresponds to the size of a frame. For a sound media,
choose a number of samples that corresponds to between 0.5 and 1.0
seconds of sound. In general, you should not create groups of sound
samples that are less than 2 KB in size or greater than 15 KB. Typically,
a sample size of about 8 KB is reasonable for most storage devices.
sampleFlags
Flags that control the add operation; set
unused flags to 0:
mediaSampleNotSync
Indicates that the sample to be added is not a sync
sample. Set this flag to 1 if the sample is not a sync sample; set
it to 0 if the sample is a sync sample.
sampleDecodeTimeOut
A pointer to a time value that represents
the sample decode time. After adding the sample data to the media,
the function returns in this parameter the time where the sample
was inserted. If you don’t want to receive this information, set
this parameter to
NIL
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. You can access Movie Toolbox error returns through `GetMoviesError` and `GetMoviesStickyError`,
as well as in the function result.

```
Discussion
Your application specifies the sample and the media for the
operation. This function updates the media so that it contains the
sample data. One call to this function can add several samples to
a media. This function replaces
AddMediaSample
;
it adds 64-bit support and support for frame reordering video compression
(display offset). This function can return these errors:
noErr
Success.
memFullErr
Could not allocate memory.
paramErr
Invalid parameter.
errMediaDoesNotSupportDisplayOffsets
The media does not support nonzero display offsets.
errDisplayTimeAlreadyInUse
There is already a sample with this display time.
errDisplayTimeTooEarly
A sample’s display time would be earlier than the
display time of an existing sample that does not have the
mediaSampleEarlierDisplayTimesAllowed
flag
set.
```

```
Version Notes
Introduced in QuickTime 7. This function extends and supersedes
AddMediaSample
. Whereas
AddMediaSample
takes
a
Handle
+
offset
+
size
,
AddMediaSample2
takes
a
Ptr
+
size
.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Adds sample data and description from an encoded frame
to a media.

```
OSErr AddMediaSampleFromEncodedFrame (
   Media theMedia,
   ICMEncodedFrameRef encodedFrame,
   TimeValue64 *sampleDecodeTimeOut );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
encodedFrame
An encoded frame token returned by an ICMCompressionSequence.
sampleDecodeTimeOut
A pointer to a time value. After adding the
sample data to the media, the function returns the decode time where
the first sample was inserted in the time value referred to by this
parameter. If you don’t want to receive this information, set
this parameter to
NULL
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. You can access Movie Toolbox error returns through `GetMoviesError` and `GetMoviesStickyError`,
as well as in the function result.

```
Discussion
This is a convenience API to make it easy to add frames emitted
by new ICM compression functions to media. It can return these errors:
noErr
Success.
memFullErr
Could not allocate memory.
paramErr
Invalid parameter.
errMediaDoesNotSupportDisplayOffsets
The media does not support nonzero display offsets.
errDisplayTimeAlreadyInUse
There is already a sample with this display time.
errDisplayTimeTooEarly
A sample’s display time would be earlier than the
display time of an existing sample that does not have the
mediaSampleEarlierDisplayTimesAllowed
flag
set.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Adds a sample table to a media.

```
OSErr AddSampleTableToMedia (
   Media               theMedia,
   QTSampleTableRef    sampleTable,
   SInt64              startSampleNum,
   SInt64              numberOfSamples,
   TimeValue64         *sampleDecodeTimeOut );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
sampleTable
A reference to an opaque sample table object
containing sample references to be added to the media.
startSampleNum
The sample number of the first sample reference
in the sample table to be added to the media. The first sample’s
number is 1.
numberOfSamples
The number of sample references from the sample
table to be added to the media.
sampleDecodeTimeOut
A pointer to a time value. After adding the
sample references to the media, the function returns the decode
time where the first sample was inserted in the time value referred
to by this parameter. If you don’t want to receive this information,
set this parameter to
NULL
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. You can access Movie Toolbox error returns through `GetMoviesError` and `GetMoviesStickyError`,
as well as in the function result.

```
Discussion
This function can return these errors:
noErr
Success.
memFullErr
Could not allocate memory.
paramErr
Invalid parameter.
errMediaDoesNotSupportDisplayOffsets
The media does not support nonzero display offsets.
errDisplayTimeAlreadyInUse
There is already a sample with this display time.
errDisplayTimeTooEarly
A sample’s display time would be earlier than the
display time of an existing sample that does not have the
mediaSampleEarlierDisplayTimesAllowed
flag
set.
If
errDisplayTimeAlreadyInUse
or
errDisplayTimeTooEarly
is
returned, no samples are added.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Obtains information about sample references in a media
in the form of a sample table.

```
OSErr CopyMediaMutableSampleTable (
   Media                      theMedia,
   TimeValue64                startDecodeTime,
   TimeValue64                *sampleStartDecodeTime,
   SInt64                     maxNumberOfSamples,
   TimeValue64                maxDecodeDuration,
   QTMutableSampleTableRef    *sampleTableOut );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
startDecodeTime
A 64-bit time value that represents the starting
decode time of the sample references to be retrieved. You must specify
this value in the media’s time scale.
sampleStartDecodeTime
A pointer to a time value. The function updates
this time value to indicate the actual decode time of the first
returned sample reference. If you are not interested in this information,
set this parameter to
NULL
.
The returned time may differ from the time you specified with the
startDecodeTime
parameter.
This will occur if the time you specified falls in the middle of
a sample.
maxNumberOfSamples
A 64-bit signed integer that contains the
maximum number of sample references to be returned. If you set this
parameter to 0, the Movie Toolbox uses a value that is appropriate
to the media.
maxDecodeDuration
A 64-bit time value that represents the maximum
decode duration to be returned. The function does not return samples
with greater decode duration than you specify with this parameter.
If you set this parameter to 0, the Movie Toolbox uses a value that
is appropriate for the media.
sampleTableOut
A reference to an opaque sample table object.
When you are done with the returned sample table, release it with
QTSampleTableRelease
.
```

##### Return Value

An error code. Returns `memFullErr` if
it could not allocate memory, `paramErr` if
there was an invalid parameter, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. You can access Movie Toolbox error returns through `GetMoviesError` and `GetMoviesStickyError`,
as well as in the function result.

```
Discussion
To find out how many samples were returned in the sample table,
call
QTSampleTableGetNumberOfSamples
.
```

```
Version Notes
Introduced in QuickTime 7. This function supersedes
GetMediaSampleReferences
and
GetMediaSampleReferences64
.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Disposes of a `MovieExportStageReachedCallbackUPP` pointer.

```
void DisposeMovieExportStageReachedCallbackUPP (
   MovieExportStageReachedCallbackUPP    userUPP );
```

```
Parameters
userUPP
A
MovieExportStageReachedCallbackUPP
pointer.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
QuickTimeComponents.h
```


Disposes a track property listener UPP.

```
void DisposeQTTrackPropertyListenerUPP (
   QTTrackPropertyListenerUPP userUPP );
```

```
Parameters
userUPP
A QTTrackPropertyListenerUPP pointer. See
Universal Procedure Pointers in the
QuickTime API Reference
for more information.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Prepares a media for the addition of a completely new
sequence of samples by ensuring that the media display end time
is not later than the media decode end time.

```
OSErr ExtendMediaDecodeDurationToDisplayEndTime (
   Media      theMedia,
   Boolean    *mediaChanged );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
mediaChanged
A pointer to a
Boolean
that
returns
TRUE
if any samples
in the media were adjusted,
FALSE
otherwise.
If you don’t want to receive this information, set this parameter
to
NULL
.
```

##### Return Value

An error code. Returns `memFullErr` if
it could not allocate memory, `paramErr` if
there was an invalid parameter, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. You can access Movie Toolbox error returns through `GetMoviesError` and `GetMoviesStickyError`,
as well as in the function result.

```
Discussion
After adding a complete, well-formed set of samples to a media,
the media’s display end time should be the same as the media’s
decode end time (also called the media decode duration). However,
this is not necessarily the case after individual sample-adding operations,
and hence it is possible for a media to be left with a display end
time later than its decode end time (if adding a sequence of frames
is aborted halfway, for example).
This may make it difficult to add a new group of samples,
because a well-formed group of samples’ earliest display time
should be the same as the first frame’s decode time. If such a
well-formed group is added to an incompletely finished media, frames
from the old and new groups frames might collide in display time.
This function prevents any such collision or overlap by extending
the last sample’s decode duration as necessary. It ensures that
the next added sample will have a decode time no earlier than the
media’s display end time. If this was already the case, it makes
no change to the media.
You can call this function before you begin adding samples
to a media if you’re not certain that the media was left in a
well-finished state. You do not need to call it before adding samples
to a newly created media, nor should you call it between sample
additions from the same compression session.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the display direction for a decompress sequence.

```
OSErr GetDSequenceNonScheduledDisplayDirection (
   ImageSequence    sequence,
   Fixed            *rate );
```

```
Parameters
sequence
Contains the unique sequence identifier that
was returned by the
DecompressSequenceBegin
function.
rate
A pointer to the display direction. Negative
values represent backward display and positive values represent
forward display.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Gets the display time for a decompression sequence.

```
OSErr GetDSequenceNonScheduledDisplayTime (
   ImageSequence    sequence,
   TimeValue64      *displayTime,
   TimeScale        *displayTimeScale );
```

```
Parameters
sequence
Contains the unique sequence identifier that
was returned by the
DecompressSequenceBegin
function.
displayTime
A pointer to a variable to hold the display
time.
displayTimeScale
A pointer to a variable to hold the display
time scale.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns the advance decode time of a media.

```
TimeValue64 GetMediaAdvanceDecodeTime (
   Media    theMedia );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
```

##### Return Value

A 64-bit time value
that represents the media’s advance decode time. A media’s advance
decode time is the absolute value of the greatest-magnitude negative
display offset of its samples, or 0 if there are no samples with
negative display offsets. This is the amount that the decode time
axis must be adjusted ahead of the display time axis to ensure that
no sample’s adjusted decode time is later than its display time.
For media without nonzero display offsets, the advance decode time
is 0.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Determines the size, in bytes, of the sample data in a
media segment.

```
OSErr GetMediaDataSizeTime64 (
   Media          theMedia,
   TimeValue64    startDisplayTime,
   TimeValue64    displayDuration,
   SInt64         *dataSize );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
startDisplayTime
A 64-bit time value that specifies the starting
point of the segment in media display time.
displayDuration
A 64-bit time value that specifies the duration
of the segment in media display time.
dataSize
A pointer to a variable to receive the size,
in bytes, of the sample data in the defined media segment.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. You can access Movie Toolbox error returns through `GetMoviesError` and `GetMoviesStickyError`,
as well as in the function result.

```
Discussion
The only difference between this function and
GetMediaDataSize64
is
that this function uses 64-bit time values and returns a 64-bit
size.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the decode duration of a media.

```
TimeValue64 GetMediaDecodeDuration (
   Media    theMedia );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
```

##### Return Value

A 64-bit time value
that repre sents the media’s decode duration. A media’s decode
duration is the sum of the decode durations of its samples.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the display duration of a media.

```
TimeValue64 GetMediaDisplayDuration (
   Media    theMedia );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
```

##### Return Value

A 64-bit time value
that represents the media’s display duration. A media’s display
duration is its display end time minus its display start time. For
media without nonzero display offsets, the decode duration and display
duration are the same.

```
Discussion
When inserting media with display offsets into a track, use
display time:
InsertMediaIntoTrack( track,
0,                                   // track start time
GetMediaDisplayStartTime( media ),   // media start time
GetMediaDisplayDuration( media ),
fixed1 );
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the display end time of a media.

```
TimeValue64 GetMediaDisplayEndTime (
   Media    theMedia );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
```

##### Return Value

A 64-bit time value
that represents the media’s display end time. A media’s display
end time is the sum of the display time and decode duration of the
sample with the greatest display time. For media without nonzero
display offsets, the display end time is the same as the media’s decode
duration.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the display start time of a media.

```
TimeValue64 GetMediaDisplayStartTime (
   Media    theMedia );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
```

##### Return Value

A 64-bit time value
that represents the media’s display start time. A media’s display
start time is the earliest display time of any of its samples. For
media without nonzero display offsets, the display start time is
always 0.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Searches for decode times of interest in a media.

```
void GetMediaNextInterestingDecodeTime (
   Media          theMedia,
   short          interestingTimeFlags,
   TimeValue64    decodeTime,
   Fixed          rate,
   TimeValue64    *interestingDecodeTime,
   TimeValue64    *interestingDecodeDuration );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
interestingTimeFlags
Flags that determine the search criteria.
Note that you may set only one of the
nextTimeMediaSample
,
nextTimeMediaEdit
,
or
nextTimeSyncSample
flags to 1.
Set unused flags to 0:
nextTimeMediaSample
Set this flag to 1 to search for the next sample.
nextTimeMediaEdit
Set this flag to 1 to search for the next group of samples.
nextTimeSyncSample
Set this flag to 1 to search for the next sync sample.
nextTimeEdgeOK
Set this flag to 1 to accept information about elements
that begin or end at the time specified by the
decodeTime
parameter.
When this flag is set the function returns valid information about
the beginning and end of a media.
decodeTime
Specifies the starting point for the search
in decode time. This time value must be expressed in the media’s
time scale.
rate
The search direction. Negative values cause
the Movie Toolbox to search backward from the starting point specified
in the
time
parameter. Other values
cause a forward search.
interestingDecodeTime
On return, a pointer to a 64-bit time value
in decode time. The Movie Toolbox returns the first time value it
finds that meets the search criteria specified in the
flags
parameter.
This time value is in the media’s time scale. If there are no
times that meet the search criteria you specify, the Movie Toolbox
sets this value to –1. Set this parameter to
NULL
if
you are not interested in this information.
interestingDecodeDuration
On return, a pointer to a 64-bit time value
in decode time. The Movie Toolbox returns the duration of the interesting
time in the media’s time coordinate system. Set this parameter
to
NULL
if you don’t
want this information; this lets the function works faster.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Searches for display times of interest in a media.

```
void GetMediaNextInterestingDisplayTime (
   Media          theMedia,
   short          interestingTimeFlags,
   TimeValue64    displayTime,
   Fixed          rate,
   TimeValue64    *interestingDisplayTime,
   TimeValue64    *interestingDisplayDuration );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
interestingTimeFlags
Flags that determine the search criteria.
Note that you may set only one of the
nextTimeMediaSample
,
nextTimeMediaEdit
,
or
nextTimeSyncSample
flags to 1.
Set unused flags to 0:
nextTimeMediaSample
Set this flag to 1 to search for the next sample.
nextTimeMediaEdit
Set this flag to 1 to search for the next group of samples.
nextTimeSyncSample
Set this flag to 1 to search for the next sync sample.
nextTimeEdgeOK
Set this flag to 1 to accept information about elements
that begin or end at the time specified by the
decodeTime
parameter.
When this flag is set the function returns valid information about
the beginning and end of a media.
displayTime
Specifies the starting point for the search
in display time. This time value must be expressed in the media’s
time scale.
rate
The search direction. Negative values cause
the Movie Toolbox to search backward from the starting point specified
in the
time
parameter. Other values
cause a forward search.
interestingDisplayTime
On return, a pointer to a 64-bit time value
in display time. The Movie Toolbox returns the first time value
it finds that meets the search criteria specified in the
flags
parameter.
This time value is in the media’s time scale. If there are no
times that meet the search criteria you specify, the Movie Toolbox
sets this value to –1. Set this parameter to
NIL
if
you are not interested in this information.
interestingDisplayDuration
On return, a pointer to a 64-bit time value
in display time. The Movie Toolbox returns the duration of the interesting
time in the media’s time coordinate system. Set this parameter
to
NIL
if you don’t
want this information; this lets the function works faster.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Retrieves sample data from a media file.

```
OSErr GetMediaSample2 (
   Media                      theMedia,
   UInt8                      *dataOut,
   ByteCount                  maxDataSize,
   ByteCount                  *size,
   TimeValue64                decodeTime,
   TimeValue64                *sampleDecodeTime,
   TimeValue64                *decodeDurationPerSample,
   TimeValue64                *displayOffset,
   SampleDescriptionHandle    sampleDescriptionH,
   ItemCount                  *sampleDescriptionIndex,
   ItemCount                  maxNumberOfSamples,
   ItemCount                  *numberOfSamples,
   MediaSampleFlags           *sampleFlags );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
dataOut
A pointer to a buffer to receive sample data.
The buffer must be large enough to contain at least
maxDataSize
bytes.
If you do not want to receive sample data, pass
NULL
.
maxDataSize
The maximum number of bytes allocated to hold
the sample data.
size
A pointer to memory where the function returns
the number of bytes of sample data returned in the memory area specified
by
dataOut
. Set this parameter to
NULL
if
you are not interested in this information.
decodeTime
The starting time of the sample to be retrieved
in decode time. You must specify this value in the media’s time
scale.
sampleDecodeTime
A pointer to a time value in decode time.
The function updates this time value to indicate the actual time
of the returned sample data. (The returned time may differ from
the time you specified with the
time
parameter.
This will occur if the time you specified falls in the middle of
a sample.) If you are not interested in this information, set this
parameter to
NULL
.
decodeDurationPerSample
A pointer to a time value in decode time.
The Movie Toolbox returns the duration of each sample in the media.
Set this parameter to
NULL
if
you don’t want this information.
displayOffset
A pointer to a time value. The function updates
this time value to indicate the display offset of the returned sample.
This time value is expressed in the media’s time scale. Set this
parameter to
NULL
if
you don’t want this information.
sampleDescriptionH
A handle to a
SampleDescription
structure.
The function returns the sample description corresponding to the
returned sample data. The function resizes this handle as appropriate.
If you don’t want a
SampleDescription
structure,
set this parameter to
NIL
.
sampleDescriptionIndex
A pointer to a long integer. The function
returns an index value to the
SampleDescription
structure
that corresponds to the returned sample data. You can retrieve the
structure by calling
GetMediaSampleDescription
and passing
this index in the
descH
parameter.
If you don’t want this information, set this parameter to
NIL
.
maxNumberOfSamples
The maximum number of samples to be returned.
The Movie Toolbox does not return more samples than you specify
with this parameter. If you set this parameter to 0, the Movie Toolbox
uses a value that is appropriate for the media, and returns that
value in the field referenced by the
numberOfSamples
parameter.
numberOfSamples
A pointer to a long integer. The function
updates the field referred to by this parameter with the number
of samples it actually returns. If you don’t want this information,
set this parameter to
NULL
.
sampleFlags
A pointer to a short integer in which the
function returns flags that describe the sample. Unused flags are
set to 0. If you don’t want this information, set this parameter
to
NULL
:
mediaSampleNotSync
This flag is set to 1 if the sample is not a sync sample
and to 0 if the sample is a sync sample.
```

##### Return Value

You can access this
function's error returns through `GetMoviesError` and `GetMoviesStickyError`.
It returns `paramErr` if there is a bad
parameter value, `maxSizeToGrowTooSmall` if
the sample data is larger than _maxDataSize_,
or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if there is no error.

```
Discussion
Whereas
GetMediaSample
takes
a resizable Handle and a
maxSizeToGrow
parameter,
GetMediaSample2
takes
a pointer and a
maxDataSize
parameter.
If you want to read a sample into a Handle, you can use the following
code:
OSErr GetMediaSampleUsingHandle (Media theMedia, Handle dataHOut,
ByteCount maxSizeToGrow, ByteCount *size,
TimeValue64 decodeTime, TimeValue64 *sampleDecodeTime,
TimeValue64 *decodeDurationPerSample,
TimeValue64 *displayOffset,
SampleDescriptionHandle sampleDescriptionH,
ItemCount *sampleDescriptionIndex,
ItemCount maxNumberOfSamples,
ItemCount *numberOfSamples,
MediaSampleFlags *sampleFlags)
{
OSErr err = noErr;
ByteCount actualSize = 0;
err = GetMediaSample2(theMedia,
*dataHOut,
GetHandleSize(dataHOut),
&actualSize,
decodeTime,
sampleDecodeTime,
decodeDurationPerSample,
displayOffset,
sampleDescriptionH,
sampleDescriptionIndex,
maxNumberOfSamples,
numberOfSamples,
sampleFlags);
if ((maxSizeToGrowTooSmall == err)
&& ((0 == maxSizeToGrow) || (actualSize <= maxSizeToGrow)) {
SetHandleSize(dataHOut, actualSize);
err = MemError();
if (err) goto bail;
err = GetMediaSample2(theMedia,
*dataHOut,
GetHandleSize(dataHOut),
&actualSize,
decodeTime,
sampleDecodeTime,
decodeDurationPerSample,
displayOffset,
sampleDescriptionH,
sampleDescriptionIndex,
maxNumberOfSamples,
numberOfSamples,
sampleFlags);
}
if( size )
*size = actualSize;
bail:
return err;
}
```

```
Version Notes
Introduced in QuickTime 7. This function extends and supersedes
GetMediaSample
.
It will only return multiple samples that all have the same decode
duration per sample, the same display offset, the same sample description,
and the same size per sample.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the balance value for the audio mix of a movie
currently playing.

```
OSStatus GetMovieAudioBalance (
   Movie      m,
   Float32    *leftRight,
   UInt32     flags );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
leftRight
On return, a pointer to the current balance
setting for the movie. The balance setting is a 32-bit floating-point
value that controls the relative volume of the left and right sound
channels. A value of 0 sets the balance to neutral. Positive values
up to 1.0 shift the balance to the right channel, negative values
up to –1.0 to the left channel.
flags
Not used; set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The movie’s balance setting is not stored in the movie;
it is used only until the movie is closed. See
SetMovieAudioBalance
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the current audio context for a movie.

```
OSStatus GetMovieAudioContext (
   Movie                movie,
   QTAudioContextRef    *audioContext);
```

```
Parameters
movie
The movie.
audioContext
A pointer to a variable to receive the audio
context.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the current frequency meter levels of a movie
mix.

```
OSStatus GetMovieAudioFrequencyLevels (
   Movie                     m,
   FourCharCode              whatMixToMeter,
   QTAudioFrequencyLevels    *pAveragePowerLevels );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
whatMixToMeter
The applicable mix of audio channels in the
movie; see
“Movie Audio Mixes”
.
pAveragePowerLevels
A pointer to a
QTAudioFrequencyLevels
structure
(page 339)
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
In the structure pointed to by
pAveragePowerLevels
,
the
numChannels
field must be set
to the number of channels in the movie mix being metered and the
numBands
field
must be set to the number of bands being metered (as previously
configured). Enough memory for the structure must be allocated to
hold 32-bit values for all bands in all channels. This function
returns the current frequency meter levels in the
level
field
of the structure, with all the band levels for the first channel
first, all the band levels for the second channel next and so on.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the chosen middle frequency for each band in the
configured frequency metering of a particular movie mix.

```
OSStatus GetMovieAudioFrequencyMeteringBandFrequencies (
   Movie           m,
   FourCharCode    whatMixToMeter,
   UInt32          numBands,
   Float32         *outBandFrequencies );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
whatMixToMeter
The applicable mix of audio channels in the
movie; see
“Movie Audio Mixes”
.
numBands
The number of bands to examine.
outBandFrequencies
A pointer to an array of frequencies, each
expressed in Hz.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
You can use this function to label a visual meter in a user
interface.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the number of frequency bands being metered for
a movie’s specified audio mix.

```
OSStatus GetMovieAudioFrequencyMeteringNumBands (
   Movie           m,
   FourCharCode    whatMixToMeter,
   UInt32          *outNumBands );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
whatMixToMeter
The applicable mix of audio channels in the
movie; see
“Movie Audio Mixes”
.
outNumBands
A pointer to memory that stores the number
of frequency bands currently being metered for the movie’s specified
audio mix.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
See
SetMovieAudioFrequencyMeteringNumBands
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the gain value for the audio mix of a movie currently
playing.

```
OSStatus GetMovieAudioGain (
   Movie      m,
   Float32    *gain,
   UInt32     flags );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
gain
A 32-bit floating-point gain value of 0 or
 greater. 0.0 is silent, 0.5 is –6 dB, 1.0 is 0 dB (the audio
from the movie is not modified), 2.0 is +6 dB, etc.  The gain level
can be set higher than 1.0 to allow quiet movies to be boosted in volume.
Gain settings higher than 1.0 may result in audio clipping.
flags
Not used; set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The movie gain setting is not stored in the movie; it is used
only until the movie is closed. See
SetMovieAudioGain
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the mute value for the audio mix of a movie currently
playing.

```
OSStatus GetMovieAudioMute (
   Movie      m,
   Boolean    *muted,
   UInt32     flags );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
muted
Returns
TRUE
if
the movie audio is currently muted,
FALSE
otherwise.
flags
Not used; set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The movie mute setting is not stored in the movie; it is used
only until the movie is closed. See
SetMovieAudioMute
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the current volume meter levels of a movie.

```
OSStatus GetMovieAudioVolumeLevels (
   Movie                  m,
   FourCharCode           whatMixToMeter,
   QTAudioVolumeLevels    *pAveragePowerLevels,
   QTAudioVolumeLevels    *pPeakHoldLevels );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
whatMixToMeter
The applicable mix of audio channels in the
movie; see
“Movie Audio Mixes”
.
pAveragePowerLevels
A pointer to a
QTAudioVolumeLevels
structure
that stores the average power level of each channel in the mix,
measured in decibels. 0.0 dB for each channel means full volume,
–6.0 dB means half volume, –12.0 dB means quarter volume, and
–infinite dB means silence. Pass
NULL
for
this parameter if you are not interested in average power levels.
pPeakHoldLevels
A pointer to a
QTAudioVolumeLevels
structure
that stores the peak hold  level of each channel in the mix, measured
in decibels. 0.0 dB for each channel means full volume, –6.0 dB
means half volume, –12.0 dB means quarter volume, and –infinite
dB means silence. Pass
NULL
for
this parameter if you are not interested in peak hold levels.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
If either
pAveragePowerLevels
or
pPeakHoldLevels
returns
non-
NULL
, it  must have
the
numChannels
field in its
QTAudioVolumeLevels
structure
set to the number of channels in the movie mix being metered and
the memory allocated for the structure must be large enough to hold
levels for all those channels.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the enabled or disabled status of volume metering
of a particular audio mix of a movie.

```
OSStatus GetMovieAudioVolumeMeteringEnabled (
   Movie           m,
   FourCharCode    whatMixToMeter,
   Boolean         *enabled );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
whatMixToMeter
The applicable mix of audio channels in the
movie; see
“Movie Audio Mixes”
.
enabled
Returns
TRUE
if
audio volume metering is enabled,
FALSE
if
it is disabled.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
See
SetMovieAudioVolumeMeteringEnabled
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the brightness adjustment for the movie.

```
OSStatus GetMovieVisualBrightness (
   Movie movie,
   Float32 *brightnessOut,
   UInt32 flags );
```

```
Parameters
movie
The movie.
brightnessOut
Current brightness adjustment.
flags
Reserved. Pass 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The brightness adjustment for the movie. The value is a Float32
for which -1.0 means full black, 0.0 means no adjustment, and 1.0
means full white. The setting is not stored in the movie. It is
only used until the movie is closed, at which time it is not saved.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the current visual context for a movie.

```
OSStatus GetMovieVisualContext (
   Movie      movie,
   QTVisualContextRef    *visualContext;
```

```
Parameters
movie
The movie.
visualContext
A pointer to a variable to receive the visual
context.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. Returns `memFullErr` if memory
cannot be allocated. Returns `kQTVisualContextRequiredErr` if
the movie is not using a visual context. Returns `paramErr` if
the movie or _visualContextOut_ is `NULL`.

```
Discussion
Returns the QTVisualContext object associated with the movie.
You are responsible for retaining and releasing the object as needed
(that is, if the returned object has not been retained for you).
If the visual context was set to
NULL
(see
SetMovieVisualContext
),
noErr
is
returned and
visualContextOut
receives
NULL
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the contrast adjustment for the movie.

```
OSStatus GetMovieVisualContrast (
   Movie           movie,
   Float32         *contrastOut,
   UInt32          flags );
```

```
Parameters
movie
The movie.
contrastOut
Current contrast adjustment.
flags
Reserved. Pass 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The contrast adjustment for the movie. The value is a Float32
percentage (1.0f = 100%), such that 0.0 gives solid grey.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the hue adjustment for the movie.

```
OSStatus GetMovieVisualHue (
   Movie movie,
   Float32 *hueOut,
   UInt32 flags );
```

```
Parameters
movie
The movie.
hueOut
Current hue adjustment. (Float32)
flags
Reserved. Pass 0. (UInt32)
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The hue adjustment for the movie. The value is a Float32 between
-1.0 and 1.0, with 0.0 meaning no adjustment. This adjustment wraps
around, such that -1.0 and 1.0 yield the same result. The setting
is not stored in the movie. It is only used until the movie is closed, at
which time it is not saved.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the color saturation adjustment for the movie.

```
OSStatus GetMovieVisualSaturation (
   Movie movie,
   Float32 *saturationOut,
   UInt32 flags );
```

```
Parameters
movie
The movie.
saturationOut
Current saturation adjustment.(Float32)
flags
Reserved. Pass 0. (UInt32)
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The color saturation adjustment for the movie. The value is
a Float32 percentage (1.0f = 100%), such that 0.0 gives grayscale.
The setting is not stored in the movie. It is only used until the
movie is closed, at which time it is not saved.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the gain value for the audio mix of a track currently
playing.

```
OSStatus GetTrackAudioGain (
   Track      t,
   Float32    *gain,
   UInt32     flags );
```

```
Parameters
t
A track identifier, which your application
obtains from such functions as
NewMovieTrack
and
GetMovieTrack
.
gain
A 32-bit floating-point gain value of 0 or
greater. 0.0 is silent, 0.5 is –6 dB, 1.0 is 0 dB (the audio from
the track is not modified), 2.0 is +6 dB, etc.  The gain level can
be set higher than 1.0 to allow quiet tracks to be boosted in volume.
Gain settings higher than 1.0 may result in audio clipping.
flags
Not used; set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The track gain setting is not stored in the movie; it is used
only until the movie is closed. See
SetTrackAudioGain
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the mute value for the audio mix of a track currently
playing.

```
OSStatus GetTrackAudioMute (
   Track      t,
   Boolean    *muted,
   UInt32     flags );
```

```
Parameters
t
A track identifier, which your application
obtains from such functions as
NewMovieTrack
and
GetMovieTrack
.
muted
Returns
TRUE
if
the track’s audio is currently muted,
FALSE
otherwise.
flags
Not used; set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The track’s mute setting is not stored in the movie; it
is used only until the movie is closed. See
SetTrackAudioMute
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the rate of the track edit of a specified track
at an indicated time.

```
Fixed GetTrackEditRate64 (
   Track          theTrack,
   TimeValue64    atTime );
```

```
Parameters
theTrack
A track identifier, which your application
obtains from such functions as
NewMovieTrack
and
GetMovieTrack
.
atTime
A 64-bit time value that indicates the time
at which the rate of a track edit (of a track identified in the
parameter
theTrack
) is to be determined.
```

##### Return Value

The rate of the track
edit of the specified track at the specified time.

```
Discussion
This function is useful if you are stepping through track
edits directly in your application or if you are a client of QuickTime’s
base media handler.
```

```
Version Notes
Introduced in QuickTime 7. This function is a 64-bit replacement
for
GetTrackEditRate
.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Changes the views attributes.

```
OSStatus HIMovieViewChangeAttributes (
   HIViewRef inView,
   OptionBits inAttributesToSet,
   OptionBits inAttributesToClear );
```

```
Parameters
inView
The HIMovieView.
inAttributesToSet
Attributes to set.
inAttributesToClear
Attributes to clear.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
Setting an attribute takes precedence over clearing the attribute.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
HIMovieView.h
```


Creates an HIMovieView object.

```
OSStatus HIMovieViewCreate (
   Movie inMovie,
   OptionBits inAttributes,
   HIViewRef *outMovieView );
```

```
Parameters
inMovie
Initial movie to view; may be
NULL
.
inAttributes
Initial HIMovieView attributes.
outMovieView
Points to variable to receive new HIMovieView.
```

##### Return Value

Undocumented.

```
Discussion
If successful, the created view will have a single retain
count.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
HIMovieView.h
```


Returns the view’s current attributes.

```
OptionBits HIMovieViewGetAttributes (
   HIViewRef inView );
```

```
Parameters
inView
The HIMovieView.
```

##### Return Value

Undocumented.

```
Discussion
The view’s current attributes are returned.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
HIMovieView.h
```


Returns the size of the visible movie controller bar.

```
HISize HIMovieViewGetControllerBarSize (
   HIViewRef inView );
```

```
Parameters
inView
The HIMovieView.
```

##### Return Value

Undocumented.

```
Discussion
The size of the visible movie controller bar is returned.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
HIMovieView.h
```


Returns the view’s current movie.

```
Movie HIMovieViewGetMovie (
   HIViewRef inView );
```

```
Parameters
inView
The HIMovieView.
```

##### Return Value

Undocumented.

```
Discussion
The view’s current movie is returned.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
HIMovieView.h
```


Returns the view’s current movie controller.

```
MovieController HIMovieViewGetMovieController (
   HIViewRef inView );
```

```
Parameters
inView
The HIMovieView.
```

##### Return Value

Undocumented.

```
Discussion
The view’s current movie controller is returned.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
HIMovieView.h
```


Pauses the view’s current movie.

```
OSStatus HIMovieViewPause (
   HIViewRef movieView );
```

```
Parameters
movieView
The movie view.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This is a convenience routine to pause the view’s current
movie. If the movie is already paused, this function does nothing.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
HIMovieView.h
```


Plays the view’s current movie.

```
OSStatus HIMovieViewPlay (
   HIViewRef movieView );
```

```
Parameters
movieView
The movie view.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This is a convenience routine to play the view’s current
movie. If the movie is already playing, this function does nothing.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
HIMovieView.h
```


Sets the view’s current movie.

```
OSStatus HIMovieViewSetMovie (
   HIViewRef inView,
   Movie inMovie );
```

```
Parameters
inView
The HIMovieView.
inMovie
The new movie to display.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This routine sets the view’s current movie.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
HIMovieView.h
```


Creates a frame compression options object.

```
OSStatus ICMCompressionFrameOptionsCreate (
   CFAllocatorRef                  allocator,
   ICMCompressionSessionRef        session,
   ICMCompressionFrameOptionsRef   *options );
```

```
Parameters
allocator
An allocator. Pass
NULL
to
use the default allocator.
session
A compression session reference. This reference
is returned by
ICMCompressionSessionCreate
.
options
On return, a reference to a new frame compression
options object.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Copies a frame compression options object.

```
OSStatus ICMCompressionFrameOptionsCreateCopy (
   CFAllocatorRef                  allocator,
   ICMCompressionFrameOptionsRef   originalOptions,
   ICMCompressionFrameOptionsRef   *copiedOptions );
```

```
Parameters
allocator
An allocator. Pass
NULL
to
use the default allocator.
originalOptions
A frame compression options reference. This
reference is returned by
ICMCompressionFrameOptionsCreate
.
copiedOptions
On return, a reference to a copy of the frame
compression options object passed in
originalOptions
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the force key frame flag.

```
Boolean ICMCompressionFrameOptionsGetForceKeyFrame (
   ICMCompressionFrameOptionsRef   options );
```

```
Parameters
options
A compression frame options reference. This
reference is returned by
ICMCompressionFrameOptionsCreate
.
```

##### Return Value

Returns `TRUE` if
frames are forced to be compressed as key frames, `FALSE` otherwise.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the `frame` type
setting.

```
ICMFrameType ICMCompressionFrameOptionsGetFrameType (
   ICMCompressionFrameOptionsRef   options );
```

```
Parameters
options
A compression frame options reference. This
reference is returned by
ICMCompressionFrameOptionsCreate
.
```

##### Return Value

On return, one of
the `frame` types listed below.

```
Discussion
This function can return one of these constants:
kICMFrameType_I
= 'I'
An I frame.
kICMFrameType_P
= 'P'
A P frame.
kICMFrameType_B
= 'B'
A B frame.
kICMFrameType_Unknown
= 0
A frame of unknown type.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the value of a specific property of a compression
frame options object.

```
OSStatus ICMCompressionFrameOptionsGetProperty (
   ICMCompressionFrameOptionsRef   options,
   ComponentPropertyClass          inPropClass,
   ComponentPropertyID             inPropID,
   ByteCount                       inPropValueSize,
   ComponentValuePtr               outPropValueAddress,
   ByteCount                       *outPropValueSizeUsed );
```

```
Parameters
options
A compression frame options reference. This
reference is returned by
ICMCompressionFrameOptionsCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueAddress
A pointer to a variable to receive the returned
property’s value.
outPropValueSizeUsed
On return, a pointer to the number of bytes
actually used to store the property.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves information about properties of a compression
frame options object.

```
OSStatus ICMCompressionFrameOptionsGetPropertyInfo (
   ICMCompressionFrameOptionsRef   options,
   ComponentPropertyClass          inPropClass,
   ComponentPropertyID             inPropID,
   ComponentValueType              *outPropType,
   ByteCount                       *outPropValueSize,
   UInt32                          *outPropertyFlags );
```

```
Parameters
options
A compression frame options reference. This
reference is returned by
ICMCompressionFrameOptionsCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueSize
A pointer to the size of the returned property’s
value.
outPropFlags
On return, a pointer to flags representing
the requested information about the property.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns the type ID for the current frame compression
options object.

```
CFTypeID ICMCompressionFrameOptionsGetTypeID ( void );
```

##### Return Value

A `CFTypeID` value.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Decrements the retain count of a frame compression options
object.

```
void ICMCompressionFrameOptionsRelease (
   ICMCompressionFrameOptionsRef    options );
```

```
Parameters
options
A reference to a frame compression options
object.This reference is returned by
ICMCompressionFrameOptionsCreate
. If
you pass
NULL
, nothing
happens.
```

```
Discussion
If the retain count drops to 0, the object is disposed.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Increments the retain count of a frame compression options
object.

```
ICMCompressionFrameOptionsRef ICMCompressionFrameOptionsRetain (
   ICMCompressionFrameOptionsRef    options );
```

```
Parameters
options
A reference to a frame compression options
object.This reference is returned by
ICMCompressionFrameOptionsCreate
. If
you pass
NULL
, nothing
happens.
```

##### Return Value

A copy of the object
reference passed in _options_, for
convenience.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Forces frames to be compressed as key frames.

```
OSStatus ICMCompressionFrameOptionsSetForceKeyFrame (
   ICMCompressionFrameOptionsRef   options,
   Boolean                         forceKeyFrame );
```

```
Parameters
options
A compression frame options reference. This
reference is returned by
ICMCompressionFrameOptionsCreate
.
forceKeyFrame
Pass
TRUE
to
force frames to be compressed as key frames,
FALSE
otherwise.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The compressor must obey this flag if set. By default it is
set
FALSE
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Requests a frame be compressed as a particular frame type.

```
OSStatus ICMCompressionFrameOptionsSetFrameType (
   ICMCompressionFrameOptionsRef   options,
   ICMFrameType                    frameType );
```

```
Parameters
options
A compression frame options reference. This
reference is returned by
ICMCompressionFrameOptionsCreate
.
frameType
A constant that identifies a frame type. Pass
one of the following but do not assume that there are no other frame
types:
kICMFrameType_I
= 'I'
An I frame.
kICMFrameType_P
= 'P'
A P frame.
kICMFrameType_B
= 'B'
A B frame.
kICMFrameType_Unknown
= 0
A frame of unknown type.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The frame type setting may be ignored by the compressor if
it is not appropriate. By default it is set to
kICMFrameType_Unknown
.
Do not assume that
kICMFrameType_I
sets
a key frame; if you need a key frame, call
ICMCompressionFrameOptionsSetForceKeyFrame
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets the value of a specific property of a compression
frame options object.

```
OSStatus ICMCompressionFrameOptionsSetProperty (
   ICMCompressionFrameOptionsRef   options,
   ComponentPropertyClass          inPropClass,
   ComponentPropertyID             inPropID,
   ByteCount                       inPropValueSize,
   ConstComponentValuePtr          inPropValueAddress );
```

```
Parameters
options
A compression frame options reference. This
reference is returned by
ICMCompressionFrameOptionsCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
inPropValueSize
The size of the property value to be set.
inPropValueAddress
A pointer to the value of the property to
be set.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Announces the start of a specific compression pass.

```
OSStatus ICMCompressionSessionBeginPass (
   ICMCompressionSessionRef      session,
   ICMCompressionPassModeFlags   passModeFlags,
   UInt32                        flags );
```

```
Parameters
session
A compression session reference. This reference
is returned by
ICMCompressionSessionCreate
.
passModeFlags
Flags that describe how the compressor should
behave in this pass of multipass encoding:
kICMCompressionPassMode_OutputEncodedFrames
= 1L<<0
Output encoded frames.
kICMCompressionPassMode_NoSourceFrames
= 1L<<1
The client need not provide source frame buffers.
kICMCompressionPassMode_WriteToMultiPassStorage
= 1L<<2
The compressor may write private data to multipass storage.
kICMCompressionPassMode_ReadFromMultiPassStorage
= 1L<<3
The compressor may read private data from multipass storage.
flags
Reserved. Set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The source frames and frame options for each display time
should be the same across passes. During multipass compression,
valid
displayTimeStamp
values must
be passed to
ICMCompressionSessionEncodeFrame
,
because they are used to index the compressor’s stored state.
During an analysis pass (
kICMCompressionPassMode_WriteToMultiPassStorage
),
the compressor does not output encoded frames but records compressor-private
information for each frame. During repeated analysis passes and
the encoding pass (
kICMCompressionPassMode_ReadFromMultiPassStorage
),
the compressor may refer to this information for other frames and
use it to improve encoding. During an encoding pass (
kICMCompressionPassMode_OutputEncodedFrames
),
the compressor must output encoded frames. If the compressor sets
the
kICMCompressionPassMode_NoSourceFrames
flag
for the pass, the client may pass
NULL
pixel
buffers to
ICMCompressionSessionEncodeFrame
.
By default, the ICM provides local storage that lasts only
until the compression session is disposed. If the client provides
custom multipass storage, passes may be performed at different times
or on different machines; segments of each pass may even be distributed.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Forces a compression session to complete encoding frames.

```
OSStatus ICMCompressionSessionCompleteFrames (
   ICMCompressionSessionRef    session,
   Boolean                     completeAllFrames,
   TimeValue64                 completeUntilDisplayTimeStamp,
   TimeValue64                 nextDisplayTimeStamp );
```

```
Parameters
session
A reference to a video compression session,
returned by a previous call to
ICMCompressionSessionCreate
.
completeAllFrames
Pass
TRUE
to
direct the session to complete all pending frames.
completeUntilDisplayTimeStamp
A 64-bit time value that represents the display
time up to which to complete frames. This value is ignored if
completeAllFrames
is
TRUE
.
nextDisplayTimeStamp
A 64-bit time value that represents the display
time of the next frame that should be passed to
EncodeFrame
.
This value is ignored unless
ICMCompressionSessionOptionsSetDurationsNeeded
set
TRUE
and
kICMValidTime_DisplayDurationIsValid
was
0 in
validTimeFlags
in the last call
to
ICMCompressionSessionEncodeFrame
.
```

##### Return Value

Returns an error code,
or 0 if there is no error. The function may return before frames
are completed if the encoded frame callback routine returns an error.

```
Discussion
Call this function to force a compression session to complete
encoding frames. Set
completeAllFrames
to
direct the session to complete all pending frames. If
completeAllFrames
is
false, only frames with display time stamps up to and including
the time passed in
completeUntilDisplayTimeStamp
will
be encoded. If
ICMCompressionSessionOptionsSetDurationsNeeded
set
TRUE
and
you are passing valid display timestamps but not display durations
to
ICMCompressionSessionEncodeFrame
, pass
in
nextDisplayTimeStamp
the display
timestamp of the next frame that would be passed to
EncodeFrame
.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Creates a compression session for a specified codec type.

```
OSStatus ICMCompressionSessionCreate (
   CFAllocatorRef                     allocator,
   int                                width,
   int                                height,
   CodecType                          cType,
   TimeScale                          timescale,
   ICMCompressionSessionOptionsRef    compressionOptions,
   CFDictionaryRef                    sourcePixelBufferAttributes,
   ICMEncodedFrameOutputRecord        *encodedFrameOutputRecord,
   ICMCompressionSessionRef           *compressionSessionOut );
```

```
Parameters
allocator
An allocator for the session. Pass
NULL
to
use the default allocator.
width
The width of frames. Pass 0 to let the compressor
control the width.
height
The height of frames. Pass 0 to let the compressor
control the height.
cType
The codec type.
timescale
The timescale to be used for all time stamps
and durations used in the session.
compressionOptions
A reference to a settings object that configures
the session. You create such an object by calling
ICMCompressionSessionOptionsCreate
.
You can then use these constants to set its properties:
kICMUnlimitedFrameDelayCount
No limit on the number of frames in the compression window.
kICMUnlimitedFrameDelayTime
No time limit on the frames in the compression window.
kICMUnlimitedCPUTimeBudget
No CPU time limit on compression.
sourcePixelBufferAttributes
Required attributes for source pixel buffers,
used when creating a pixel buffer pool for source frames. If you
do not want the ICM to create one for you, pass
NULL
.
Using pixel buffers not allocated by the ICM may increase the chance
that it will be necessary to copy image data.
encodedFrameOutputRecord
The callback that will receive encoded frames.
compressionSessionOut
Points to a variable to receive the created
session object.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
Some compressors do not support arbitrary source dimensions,
and may override the suggested width and height.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Presents video frames to a compression session.

```
OSStatus ICMCompressionSessionEncodeFrame (
   ICMCompressionSessionRef           session,
   CVPixelBufferRef                   pixelBuffer,
   TimeValue64                        displayTimeStamp,
   TimeValue64                        displayDuration,
   ICMValidTimeFlags                  validTimeFlags,
   ICMCompressionFrameOptionsRef      frameOptions,
   ICMSourceTrackingCallbackRecord    *sourceTrackingCallback,
   void                               *sourceFrameRefCon );
```

```
Parameters
session
A reference to a video compression session,
returned by a previous call to
ICMCompressionSessionCreate
.
pixelBuffer
A reference to a buffer containing a source
image to be compressed, which must have a nonzero reference count.
The session will retain it as long as necessary. The client should
not modify the pixel buffer’s pixels until the pixel buffer release
callback is called. In a multipass encoding session pass, where
the compressor suggested the flag
kICMCompressionPassMode_NoSourceFrames
,
you may pass
NULL
in
this parameter.
displayTimeStamp
A 64-bit time value that represents the display
time of the frame, using the time scale passed to
ICMCompressionSessionCreate
.
If you pass a valid value, set the
kICMValidTime_DisplayTimeStampIsValid
flag
in the
validTimeFlags
parameter (below).
displayDuration
A 64-bit time value that represents the display
duration of the frame, using the time scale passed to
ICMCompressionSessionCreate
.
If you pass a valid value, set the
kICMValidTime_DisplayDurationIsValid
flag
in the
validTimeFlags
parameter (below).
validTimeFlags
Flags to indicate which of the values passed
in
displayTimeStamp
and
displayDuration
are
valid:
kICMValidTime_DisplayTimeStampIsValid
The time value passed in
displayTimeStamp
is
valid.
kICMValidTime_DisplayDurationIsValid
The time value passed in
displayDuration
is
valid.
frameOptions
Options for this frame. Currently not used;
pass
NULL
.
sourceTrackingCallback
A pointer to a callback to be notified about
the status of this source frame. Pass
NULL
if
you do not require notification.
sourceFrameRefCon
A reference constant to be passed to your
callback. Use this parameter to point to a data structure containing
any information your callback needs.
```

##### Return Value

Returns an error code,
or 0 if there is no error. Encoded frames may or may not be output
before the function returns.

```
Discussion
The session will retain the pixel buffer as long as necessary,
and the client should not modify the pixel data until the session
releases it. The most practical way to deal with this is by allocating
pixel buffers from a pool. The client may fill in both, either,
or neither of
displayTimeStamp
and
displayDuration
,
but should set the appropriate flags to indicate which are valid.
If the client needs to track the progress of a source frame, it
should provide a source tracking callback. If multipass compression
is enabled, calls to this function must be bracketed by calls to
ICMCompressionSessionBeginPass
and
ICMCompressionSessionEndPass
.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Announces the end of a pass.

```
OSStatus ICMCompressionSessionEndPass (
   ICMCompressionSessionRef   session );
```

```
Parameters
session
A compression session reference. This reference
is returned by
ICMCompressionSessionCreate
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the image description for a video compression
session.

```
OSStatus ICMCompressionSessionGetImageDescription (
   ICMCompressionSessionRef    session,
   ImageDescriptionHandle      *imageDescOut );
```

```
Parameters
session
A reference to a video compression session,
returned by a previous call to
ICMCompressionSessionCreate
.
imageDescOut
A handle to an
ImageDescription
structure.
The caller must
not
dispose of this handle;
the ICM will dispose of it when the compression session is disposed.
```

##### Return Value

Returns an error code,
or 0 if there is no error. For some codecs, this function may fail
if called before the first frame is compressed.

```
Discussion
Multiple calls to this function return the same handle.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns a pool that can provide ideal source pixel buffers
for a compression session.

```
CVPixelBufferPoolRef ICMCompressionSessionGetPixelBufferPool (
   ICMCompressionSessionRef   session );
```

```
Parameters
session
A compression session reference. This reference
is returned by
ICMCompressionSessionCreate
.
```

##### Return Value

A reference to a pool
of pixel buffers. The compression session creates this pixel buffer
pool based on the compressor’s pixel buffer attributes and any pixel
buffer attributes passed to `[ICMCompressionSessionCreate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jingug33nobzgk43tnfxw4u3fonzws33oinzgkylumu)`.

```
Discussion
A new compression session builds this pixel buffer pool based
on the compressor’s pixel buffer attributes and any pixel buffer
attributes passed in to
ICMCompressionSessionCreate
.
If the source pixel buffer attributes and the compressor pixel buffer
attributes cannot be reconciled, the pool is based on the source
pixel buffer attributes and the ICM converts each pixel buffer internally.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the value of a specific property of a compression
session.

```
OSStatus ICMCompressionSessionGetProperty (
   ICMCompressionSessionRef   session,
   ComponentPropertyClass     inPropClass,
   ComponentPropertyID        inPropID,
   ByteCount                  inPropValueSize,
   ComponentValuePtr          outPropValueAddress,
   ByteCount                  *outPropValueSizeUsed );
```

```
Parameters
session
A compression session reference. This reference
is returned by
ICMCompressionSessionCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueAddress
A pointer to a variable to receive the returned
property’s value.
outPropValueSizeUsed
On return, a pointer to the number of bytes
actually used to store the property.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves information about properties of a compression
session.

```
OSStatus ICMCompressionSessionGetPropertyInfo (
   ICMCompressionSessionRef   session,
   ComponentPropertyClass     inPropClass,
   ComponentPropertyID        inPropID,
   ComponentValueType         *outPropType,
   ByteCount                  *outPropValueSize,
   UInt32                     *outPropertyFlags );
```

```
Parameters
session
A compression session reference. This reference
is returned by
ICMCompressionSessionCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueSize
A pointer to the size of the returned property’s
value.
outPropFlags
On return, a pointer to flags representing
the requested information about the property.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the time scale for a compression session.

```
TimeScale ICMCompressionSessionGetTimeScale (
   ICMCompressionSessionRef   session );
```

```
Parameters
session
A compression session reference. This reference
is returned by
ICMCompressionSessionCreate
.
```

##### Return Value

The time scale for
the compression session.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns the type ID for the current compression session.

```
CFTypeID ICMCompressionSessionGetTypeID ( void );
```

##### Return Value

A `CFTypeID` value.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Creates a compression session options object.

```
OSStatus ICMCompressionSessionOptionsCreate (
   CFAllocatorRef                    allocator,
   ICMCompressionSessionOptionsRef   *options );
```

```
Parameters
allocator
An allocator. Pass
NULL
to
use the default allocator.
options
On return, a reference to a new compression
session options object.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Copies a compression session options object.

```
OSStatus ICMCompressionSessionOptionsCreateCopy (
   CFAllocatorRef                    allocator,
   ICMCompressionSessionOptionsRef   originalOptions,
   ICMCompressionSessionOptionsRef   *copiedOptions );
```

```
Parameters
allocator
An allocator. Pass
NULL
to
use the default allocator.
originalOptions
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
copiedOptions
On return, a reference to a copy of the compression
session options object passed in
originalOptions
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the allow frame reordering flag.

```
Boolean ICMCompressionSessionOptionsGetAllowFrameReordering (
   ICMCompressionSessionOptionsRef   options );
```

```
Parameters
options
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
```

##### Return Value

Returns `TRUE` if
frame reordering is allowed, `FALSE` otherwise.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the allow frame time changes flag.

```
Boolean ICMCompressionSessionOptionsGetAllowFrameTimeChanges (
   ICMCompressionSessionOptionsRef   options );
```

```
Parameters
options
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
```

##### Return Value

Returns `TRUE` if
the compressor is allowed to modify frame times, `FALSE` otherwise.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the allow temporal compression flag.

```
Boolean ICMCompressionSessionOptionsGetAllowTemporalCompression (
   ICMCompressionSessionOptionsRef   options );
```

```
Parameters
options
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
```

##### Return Value

Returns `TRUE` if
temporal compression is allowed, `FALSE` otherwise.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the durations needed flag.

```
Boolean ICMCompressionSessionOptionsGetDurationsNeeded (
   ICMCompressionSessionOptionsRef   options );
```

```
Parameters
options
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
```

##### Return Value

Returns `TRUE` if
the durations of outputted frames must be calculated, `FALSE` otherwise.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the maximum key frame interval.

```
SInt32 ICMCompressionSessionOptionsGetMaxKeyFrameInterval (
   ICMCompressionSessionOptionsRef   options );
```

```
Parameters
options
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
```

##### Return Value

Returns the maximum
key frame interval.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the value of a specific property of a compression
session options object.

```
OSStatus ICMCompressionSessionOptionsGetProperty (
   ICMCompressionSessionOptionsRef   options,
   ComponentPropertyClass            inPropClass,
   ComponentPropertyID               inPropID,
   ByteCount                         inPropValueSize,
   ComponentValuePtr                 outPropValueAddress,
   ByteCount                         *outPropValueSizeUsed );
```

```
Parameters
options
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueAddress
A pointer to a variable to receive the returned
property’s value.
outPropValueSizeUsed
On return, a pointer to the number of bytes
actually used to store the property.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves information about properties of a compression
session options object.

```
OSStatus ICMCompressionSessionOptionsGetPropertyInfo (
   ICMCompressionSessionOptionsRef   options,
   ComponentPropertyClass            inPropClass,
   ComponentPropertyID               inPropID,
   ComponentValueType                *outPropType,
   ByteCount                         *outPropValueSize,
   UInt32                            *outPropertyFlags );
```

```
Parameters
options
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueSize
A pointer to the size of the returned property’s
value.
outPropFlags
On return, a pointer to flags representing
the requested information about the property.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns the type ID for the current compression session
options object.

```
CFTypeID ICMCompressionSessionOptionsGetTypeID ( void );
```

##### Return Value

A `CFTypeID` value.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Decrements the retain count of a compression session options
object.

```
void ICMCompressionSessionOptionsRelease (
   ICMCompressionSessionOptionsRef    options );
```

```
Parameters
options
A reference to a compression session options
object. This reference is returned by
ICMCompressionSessionOptionsCreate
.
If you pass
NULL
, nothing
happens.
```

```
Discussion
If the retain count drops to 0, the object is disposed.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Increments the retain count of a compression session options
object.

```
ICMCompressionSessionOptionsRef ICMCompressionSessionOptionsRetain (
   ICMCompressionSessionOptionsRef    options );
```

```
Parameters
options
A reference to a compression session options
object. This reference is returned by
ICMCompressionSessionOptionsCreate
.
If you pass
NULL
, nothing
happens.
```

##### Return Value

A copy of the object
reference passed in _options_, for
convenience.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Enables frame reordering.

```
OSStatus ICMCompressionSessionOptionsSetAllowFrameReordering (
   ICMCompressionSessionOptionsRef   options,
   Boolean                           allowFrameReordering );
```

```
Parameters
options
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
allowFrameReordering
Pass
TRUE
to
enable frame reordering,
FALSE
to
disable it.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
To encode B-frames a compressor must reorder frames, which
means that the order in which they will be emitted and stored (the
decode order) is different from the order in which they were presented
to the compressor (the display order). By default, frame reordering
is disabled. To encode using B-frames, you must call this function,
passing
TRUE
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Allows the compressor to modify frame times.

```
OSStatus ICMCompressionSessionOptionsSetAllowFrameTimeChanges (
   ICMCompressionSessionOptionsRef   options,
   Boolean                           allowFrameTimeChanges );
```

```
Parameters
options
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
allowFrameTimeChanges
Pass
TRUE
to
let the compressor to modify frame times,
FALSE
to
prohibit it.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
Some compressors are able to identify and coalesce runs of
identical frames and output single frames with longer durations,
or output frames at a different frame rate from the original. This
feature is controlled by the allow frame time changes flag. By default,
this flag is set to false, which forces compressors to emit one
encoded frame for every source frame and preserve frame display
times.
This function replaces the practice of having compressors
return special high similarity values to indicate that frames could
be dropped.
If you want to let the compressor modify frame times in order
to improve compression performance, you should allow frame time
changes.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Enables temporal compression.

```
OSStatus ICMCompressionSessionOptionsSetAllowTemporalCompression (
   ICMCompressionSessionOptionsRef   options,
   Boolean                           allowTemporalCompression );
```

```
Parameters
options
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
allowTemporalCompression
Pass
TRUE
to
enable temporal compression,
FALSE
to
disable it.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
By default, temporal compression is disabled. If you want
temporal compression for P-frames or B-frames you must call this
function and pass
TRUE
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Indicates that the durations of outputted frames must
be calculated.

```
OSStatus ICMCompressionSessionOptionsSetDurationsNeeded (
   ICMCompressionSessionOptionsRef   options,
   Boolean                           decodeDurationsNeeded );
```

```
Parameters
options
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
decodeDurationsNeeded
Pass
TRUE
to
indicate that durations must be calculated,
FALSE
otherwise.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
If this flag is set and source frames are provided with times
but not durations, then frames will be delayed so that durations
can be calculated as the difference between one frame’s time stamp
and the next frame’s time stamp. By default this flag is 0, so
frames will not be delayed in order to calculate durations.
If you are passing encoded frames to
AddMediaSampleFromEncodedFrame
,
you must call this function and pass
TRUE
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets the maximum interval between key frames.

```
OSStatus ICMCompressionSessionOptionsSetMaxKeyFrameInterval (
   ICMCompressionSessionOptionsRef   options,
   SInt32                            maxKeyFrameInterval );
```

```
Parameters
options
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
maxKeyFrameInterval
The maximum interval between key frames, also
known as the key frame rate.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
Compressors are allowed to generate key frames more frequently
if this would result in more efficient compression. The default
key frame interval is 0, which indicates that the compressor should
choose where to place all key frames.
This is a break with previous practice, which used a key frame
rate of 0 to disable temporal compression.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets the value of a specific property of a compression
session options object.

```
OSStatus ICMCompressionSessionOptionsSetProperty (
   ICMCompressionSessionOptionsRef   options,
   ComponentPropertyClass            inPropClass,
   ComponentPropertyID               inPropID,
   ByteCount                         inPropValueSize,
   ConstComponentValuePtr            inPropValueAddress );
```

```
Parameters
options
A compression session options reference. This
reference is returned by
ICMCompressionSessionOptionsCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
inPropValueSize
The size of the property value to be set.
inPropValueAddress
A pointer to the value of the property to
be set.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Lets the compressor perform processing between passes.

```
OSStatus ICMCompressionSessionProcessBetweenPasses (
   ICMCompressionSessionRef      session,
   UInt32                        flags,
   Boolean                       *interpassProcessingDoneOut,
   ICMCompressionPassModeFlags   *requestedNextPassModeFlagsOut );
```

```
Parameters
session
A compression session reference. This reference
is returned by
ICMCompressionSessionCreate
.
flags
Reserved. Set to 0.
interpassProcessingDoneOut
A pointer to a
Boolean
that
will be set to
FALSE
if
this function should be called again,
TRUE
if
not.
requestedNextPassModeFlagsOut
A pointer to
ICMCompressionPassModeFlags
that
will be set to the codec’s recommended mode flags for the next
pass.
kICMCompressionPassMode_OutputEncodedFrames
will
be set only if it recommends that the next pass be the final one:
kICMCompressionPassMode_OutputEncodedFrames
= 1L<<0
Output encoded frames.
kICMCompressionPassMode_NoSourceFrames
= 1L<<1
The client need not provide source frame buffers.
kICMCompressionPassMode_WriteToMultiPassStorage
= 1L<<2
The compressor may write private data to multipass storage.
kICMCompressionPassMode_ReadFromMultiPassStorage
= 1L<<3
The compressor may read private data from multipass storage.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
Call this function repeatedly until the compressor sets
interpassProcessingDoneOut
to
TRUE
to
indicate that it is done with this round of interpass processing.
When done, the compressor will indicate its preferred mode for the
next pass. At this point the client may choose to begin an encoding
pass, by OR-combining the
kICMCompressionPassMode_OutputEncodedFrames
flag,
regardless of the compressor’s request.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Decrements the retain count of a compression session.

```
void ICMCompressionSessionRelease (
   ICMCompressionSessionRef    session );
```

```
Parameters
session
A compression session reference. This reference
is returned by
ICMCompressionSessionCreate
.
If you pass
NULL
, nothing
happens.
```

```
Discussion
If the retain count drops to 0, the session is disposed.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Increments the retain count of a compression session.

```
ICMCompressionSessionRef ICMCompressionSessionRetain (
   ICMCompressionSessionRef    session );
```

```
Parameters
session
A compression session reference. This reference
is returned by
ICMCompressionSessionCreate
.
If you pass
NULL
, nothing
happens.
```

##### Return Value

A reference to the
object passed in _session_, for convenience.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets the value of a specific property of a compression
session.

```
OSStatus ICMCompressionSessionSetProperty (
   ICMCompressionSessionRef   session,
   ComponentPropertyClass     inPropClass,
   ComponentPropertyID        inPropID,
   ByteCount                  inPropValueSize,
   ConstComponentValuePtr     inPropValueAddress );
```

```
Parameters
session
A compression session reference. This reference
is returned by
ICMCompressionSessionCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
inPropValueSize
The size of the property value to be set.
inPropValueAddress
A pointer to the value of the property to
be set.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Queries whether a compression session supports multipass
encoding.

```
Boolean ICMCompressionSessionSupportsMultiPassEncoding (
   ICMCompressionSessionRef       session,
   UInt32                         multiPassStyleFlags,
   ICMCompressionPassModeFlags    *firstPassModeFlagsOut );
```

```
Parameters
session
A compression session reference. This reference
is returned by
ICMCompressionSessionCreate
.
multiPassStyleFlags
Reserved; set to 0.
firstPassModeFlagsOut
A pointer to a variable to receive the session’s
requested mode flags for the first pass. The client may modify these
flags, but should not set
kICMCompressionPassMode_NoSourceFrames
.
Pass
NULL
if you do not
want this information.
```

##### Return Value

Returns `TRUE` if
the compression session supports multipass encoding, `FALSE` otherwise.

```
Discussion
Even if this function returns
FALSE
,
if you passed
TRUE
to
ICMCompressionSessionOptionsSetMultiPass
,
you must call
ICMCompressionSessionBeginPass
and
ICMCompressionSessionEndPass
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Called by a compressor to notify the ICM that a source
frame has been dropped and will not contribute to any encoded frames.

```
OSStatus ICMCompressorSessionDropFrame (
   ICMCompressorSessionRef       session,
   ICMCompressorSourceFrameRef   sourceFrame );
```

```
Parameters
session
A reference to the compression session between
the ICM and an image compressor component.
sourceFrame
A reference to a frame that has been passed
in
sourceFrameRefCon
to
ICMCompressionSessionEncodeFrame
.
If you pass
NULL
, nothing happens.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
Calling this function does not automatically release the source
frame; if the compressor called
ICMCompressorSourceFrameRetain
it
should still call
ICMCompressorSourceFrameRelease
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Called by a compressor to output an encoded frame corresponding
to one or more source frames.

```
OSStatus ICMCompressorSessionEmitEncodedFrame (
   ICMCompressorSessionRef       session,
   ICMMutableEncodedFrameRef     encodedFrame,
   long                          numberOfSourceFrames,
   ICMCompressorSourceFrameRef   sourceFrames[] );
```

```
Parameters
session
A reference to the compression session between
the ICM and an image compressor component.
encodedFrame
A reference to an encoded frame object with
write capabilities.
numberOfSourceFrames
The number of source frames encoded in the
encoded frame.
sourceFrames
References to frames that have been passed
in
sourceFrameRefCon
to
ICMCompressionSessionEncodeFrame
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
Encoded frames may correspond to more than one source frame
only if
allowFrameTimeChanges
is
set in the compression session’s
compressionSessionOptions
.
After calling this function, the compressor should release
the encoded frame by calling
ICMEncodedFrameRelease
.
Calling this function does not automatically release the source frames;
if the compressor called
ICMCompressorSourceFrameRetain
it
should still call
ICMCompressorSourceFrameRelease
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves a source frames display number.

```
long ICMCompressorSourceFrameGetDisplayNumber (
   ICMCompressorSourceFrameRef   sourceFrame );
```

```
Parameters
sourceFrame
A reference to a frame that has been passed
in
sourceFrameRefCon
to
ICMCompressionSessionEncodeFrame
.
```

##### Return Value

The display number
of the source frame.

```
Discussion
The ICM tags source frames with display numbers in the order
that they are passed to
ICMCompressionSessionEncodeFrame
.
The first display number is 1. Compressors may compare these numbers
to work out whether prediction is forward or backward, even when
display times are not provided.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the display time stamp and duration of a source
frame.

```
OSStatus ICMCompressorSourceFrameGetDisplayTimeStampAndDuration (
   ICMCompressorSourceFrameRef    sourceFrame,
   TimeValue64                    *displayTimeStampOut,
   TimeValue64                    *displayDurationOut,
   TimeScale                      *timeScaleOut,
   ICMValidTimeFlags              *validTimeFlagsOut );
```

```
Parameters
sourceFrame
A reference to a frame that has been passed
in
sourceFrameRefCon
to
ICMCompressionSessionEncodeFrame
.
displayTimeStampOut
A pointer to the source frame’s display
time stamp.
displayDurationOut
A pointer to the source frame’s display
duration.
timeScaleOut
A pointer to the source frame’s display
time scale.
validTimeFlagsOut
A pointer to one of these display time flags
for the source frame:
kICMValidTime_DisplayTimeStampIsValid
    = 1L<<0
The value of
displayTimeStamp
is
valid.
kICMValidTime_DisplayDurationIsValid
     = 1L<<1
The value of
displayDuration
is
valid.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the frame compression options for a source frame.

```
ICMCompressionFrameOptionsRef ICMCompressorSourceFrameGetFrameOptions (
   ICMCompressorSourceFrameRef   sourceFrame );
```

```
Parameters
sourceFrame
A reference to a frame that has been passed
in
sourceFrameRefCon
to
ICMCompressionSessionEncodeFrame
.
```

##### Return Value

A compression session
frame options reference representing options for this frame. A frame
options object is created by `[ICMCompressionFrameOptionsCreate](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jingug33nobzgk43tnfxw4rtsmfwwkt3qoruw63ttinzgkylumu)`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves a source frames pixel buffer.

```
CVPixelBufferRef ICMCompressorSourceFrameGetPixelBuffer (
   ICMCompressorSourceFrameRef   sourceFrame );
```

```
Parameters
sourceFrame
A reference to a frame that has been passed
in
sourceFrameRefCon
to
ICMCompressionSessionEncodeFrame
.
```

##### Return Value

A reference to the
pixel buffer containing the source frame’s image being compressed.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns the type ID for the current source frame object.

```
CFTypeID ICMCompressorSourceFrameGetTypeID ( void );
```

##### Return Value

A `CFTypeID` value.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Decrements the retain count of a source frame object.

```
void ICMCompressorSourceFrameRelease (
   ICMCompressorSourceFrameRef    sourceFrame );
```

```
Parameters
sourceFrame
A reference to a frame that has been passed
in
sourceFrameRefCon
to
ICMCompressionSessionEncodeFrame
.
If you pass
NULL
, nothing happens.
```

```
Discussion
If the retain count drops to 0, the object is disposed.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Increments the retain count of a source frame object.

```
ICMCompressorSourceFrameRef ICMCompressorSourceFrameRetain (
   ICMCompressorSourceFrameRef    sourceFrame );
```

```
Parameters
sourceFrame
A reference to a frame that has been passed
in
sourceFrameRefCon
to
ICMCompressionSessionEncodeFrame
.
If you pass
NULL
, nothing happens.
```

##### Return Value

A reference to the
object passed in _sourceFrame_, for
convenience.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Creates a frame decompression options object.

```
OSStatus ICMDecompressionFrameOptionsCreate (
   CFAllocatorRef                    allocator,
   ICMDecompressionFrameOptionsRef   *options );
```

```
Parameters
allocator
An allocator. Pass
NULL
to
use the default allocator.
options
On return, a reference to a frame decompression
options object.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Copies a frame decompression options object.

```
OSStatus ICMDecompressionFrameOptionsCreateCopy (
   CFAllocatorRef                    allocator,
   ICMDecompressionFrameOptionsRef   originalOptions,
   ICMDecompressionFrameOptionsRef   *copiedOptions );
```

```
Parameters
allocator
An allocator. Pass
NULL
to
use the default allocator.
originalOptions
A reference to a frame decompression options
object. You can create this object by calling
ICMDecompressionFrameOptionsCreate
.
copiedOptions
On return, a reference to a copy of the frame
decompression options object passed in
originalOptions
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the value of a specific property of a decompression
frame options object.

```
OSStatus ICMDecompressionFrameOptionsGetProperty (
   ICMDecompressionFrameOptionsRef   options,
   ComponentPropertyClass            inPropClass,
   ComponentPropertyID               inPropID,
   ByteCount                         inPropValueSize,
   ComponentValuePtr                 outPropValueAddress,
   ByteCount                         *outPropValueSizeUsed );
```

```
Parameters
options
A decompression frame options reference. This
reference is returned by
ICMDecompressionFrameOptionsCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueAddress
A pointer to a variable to receive the returned
property’s value.
outPropValueSizeUsed
On return, a pointer to the number of bytes
actually used to store the property.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves information about properties of a decompression
frame options object.

```
OSStatus ICMDecompressionFrameOptionsGetPropertyInfo (
   ICMDecompressionFrameOptionsRef   options,
   ComponentPropertyClass            inPropClass,
   ComponentPropertyID               inPropID,
   ComponentValueType                *outPropType,
   ByteCount                         *outPropValueSize,
   UInt32                            *outPropertyFlags );
```

```
Parameters
options
A decompression frame options reference. This
reference is returned by
ICMDecompressionFrameOptionsCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueSize
A pointer to the size of the returned property’s
value.
outPropFlags
On return, a pointer to flags representing
the requested information about the frame option’s property.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns the type ID for the current frame decompression
options object.

```
CFTypeID ICMDecompressionFrameOptionsGetTypeID ( void );
```

##### Return Value

A `CFTypeID` value.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Decrements the retain count of a frame decompression options
object.

```
void ICMDecompressionFrameOptionsRelease (
   ICMDecompressionFrameOptionsRef    options );
```

```
Parameters
options
A reference to a frame decompression options
object. You can create this object by calling
ICMDecompressionFrameOptionsCreate
.
If you pass
NULL
, nothing
happens.
```

```
Discussion
If the retain count drops to 0, the object is disposed.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Increments the retain count of a frame decompression options
object.

```
ICMDecompressionFrameOptionsRef ICMDecompressionFrameOptionsRetain (
   ICMDecompressionFrameOptionsRef    options );
```

```
Parameters
options
A reference to a frame decompression options
object. You can create this object by calling
ICMDecompressionFrameOptionsCreate
.
If you pass
NULL
, nothing
happens.
```

##### Return Value

A reference to the
frame decompression options object passed in _options_,
for convenience.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets the value of a specific property of a decompression
frame options object.

```
OSStatus ICMDecompressionFrameOptionsSetProperty (
   ICMDecompressionFrameOptionsRef   options,
   ComponentPropertyClass            inPropClass,
   ComponentPropertyID               inPropID,
   ByteCount                         inPropValueSize,
   ConstComponentValuePtr            inPropValueAddress );
```

```
Parameters
options
A decompression frame options reference. This
reference is returned by
ICMDecompressionFrameOptionsCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
inPropValueSize
The size of the property value to be set.
inPropValueAddress
A pointer to the value of the property to
be set.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Creates a session for decompressing video frames.

```
OSStatus ICMDecompressionSessionCreate (
   CFAllocatorRef                       allocator,
   ImageDescriptionHandle               desc,
   ICMDecompressionSessionOptionsRef    decompressionOptions,
   CFDictionaryRef                      destinationPixelBufferAttributes,
   ICMDecompressionTrackingCallbackRecord    *trackingCallback,
   ICMDecompressionSessionRef                *decompressionSessionOut );
```

```
Parameters
allocator
An allocator for the session. Pass
NULL
to
use the default allocator.
desc
An image description for the source frames.
decompressionOptions
A decompression session options reference.
This reference is returned by
ICMDecompressionSessionOptionsCreate
.
The session will retain the object. You may change some options
during the session by modifying the object. You may also pass
NULL
.
destinationPixelBufferAttributes
Requirements for emitted pixel buffers. You
may pass
NULL
.
trackingCallback
A pointer to a structure that designates a
callback to be called for information about queued frames and pixel
buffers containing decompressed frames. See
ICMDecompressionTrackingCallbackRecord
and
ICMDecompressionTrackingCallbackProc
.
decompressionSessionOut
A pointer to a variable to receive a reference
to the new decompression session.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
Frames are returned through calls to the callback pointed
to by
trackingCallback
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Creates a session for decompressing video frames.

```
OSStatus ICMDecompressionSessionCreateForVisualContext (
   CFAllocatorRef allocator,
   /*can be NULL */ ImageDescriptionHandle desc,
   ICMDecompressionSessionOptionsRef decompressionOptions,
   /*can be NULL */ QTVisualContextRef visualContext,
   ICMDecompressionTrackingCallbackRecord *trackingCallback,
   ICMDecompressionSessionRef *decompressionSessionOut );
```

```
Parameters
allocator
An allocator for the session. Pass
NULL
to
use the default allocator.
desc
An image description for the source frames.
decompressionOptions
Options for the session. The session will
retain this options object. You may change some options during the
session by modifying the object.
visualContext
The target visual context.
trackingCallback
The callback to be called with information
about queued frames, and pixel buffers containing the decompressed
frames.
decompressionSessionOut
Points to a variable to receive the new decompression
session.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
Frames will be output to a visual context. If desired, the
trackingCallback
may attach additional data to pixel buffers before they are sent
to the visual context.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Queues a frame for decompression.

```
OSStatus ICMDecompressionSessionDecodeFrame (
   ICMDecompressionSessionRef         session,
   const UInt8                        *data,
   ByteCount                          dataSize,
   ICMDecompressionFrameOptionsRef    frameOptions,
   const ICMFrameTimeRecord           *frameTime,
   void                               *sourceFrameRefCon );
```

```
Parameters
session
A decompression session reference. This reference
is returned by
ICMDecompressionSessionCreate
.
data
A pointer to the compressed data for this
frame. The data must remain in this location until
ICMDecompressionTrackingCallbackProc
is
called with the
kICMDecompressionTracking_ReleaseSourceData
flag
set in
decompressionTrackingFlags
.
dataSize
The number of bytes of compressed data. You
may not pass 0 in this parameter.
frameOptions
A reference to a frame decompression options
object containing options for this frame. You can create this object
by calling
ICMDecompressionFrameOptionsCreate
.
frameTime
A pointer to a structure describing the frame’s
timing information.
sourceFrameRefCon
Your reference value for the frame.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Flushes the frames queued for a decompression session.

```
OSStatus ICMDecompressionSessionFlush (
   ICMDecompressionSessionRef   session );
```

```
Parameters
session
A decompression session reference. This reference
is returned by
ICMDecompressionSessionCreate
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The tracking callback will be called for each frame with the
result –1.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the value of a specific property of a decompression
session.

```
OSStatus ICMDecompressionSessionGetProperty (
   ICMDecompressionSessionRef   session,
   ComponentPropertyClass       inPropClass,
   ComponentPropertyID          inPropID,
   ByteCount                    inPropValueSize,
   ComponentValuePtr            outPropValueAddress,
   ByteCount                    *outPropValueSizeUsed );
```

```
Parameters
session
A decompression session reference. This reference
is returned by
ICMDecompressionSessionCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueAddress
A pointer to a variable to receive the returned
property’s value.
outPropValueSizeUsed
On return, a pointer to the number of bytes
actually used to store the property.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves information about the properties of a decompression
session.

```
OSStatus ICMDecompressionSessionGetPropertyInfo (
   ICMDecompressionSessionRef   session,
   ComponentPropertyClass       inPropClass,
   ComponentPropertyID          inPropID,
   ComponentValueType           *outPropType,
   ByteCount                    *outPropValueSize,
   UInt32                       *outPropertyFlags );
```

```
Parameters
session
A decompression session reference. This reference
is returned by
ICMDecompressionSessionCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueSize
A pointer to the size of the returned property’s
value.
outPropFlags
On return, a pointer to flags representing
the requested information about the property.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns the type ID for the current decompression session.

```
CFTypeID ICMDecompressionSessionGetTypeID ( void );
```

##### Return Value

A `CFTypeID` value.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Creates a decompression session options object.

```
OSStatus ICMDecompressionSessionOptionsCreate (
   CFAllocatorRef                      allocator,
   ICMDecompressionSessionOptionsRef   *options );
```

```
Parameters
allocator
An allocator. Pass
NULL
to
use the default allocator.
options
On return, a reference to a decompression
session options object.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Copies a decompression session options object.

```
OSStatus ICMDecompressionSessionOptionsCreateCopy (
   CFAllocatorRef                      allocator,
   ICMDecompressionSessionOptionsRef   originalOptions,
   ICMDecompressionSessionOptionsRef   *copiedOptions );
```

```
Parameters
allocator
An allocator. Pass
NULL
to
use the default allocator.
originalOptions
A decompression session options reference.
This reference is returned by
ICMDecompressionSessionOptionsCreate
.
copiedOptions
On return, a reference to a copy of the decompression
session options object passed in
originalOptions
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves information about properties of a decompression
session options object.

```
OSStatus ICMDecompressionSessionOptionsGetPropertyInfo (
   ICMDecompressionSessionOptionsRef   options,
   ComponentPropertyClass              inPropClass,
   ComponentPropertyID                 inPropID,
   ComponentValueType                  *outPropType,
   ByteCount                           *outPropValueSize,
   UInt32                              *outPropertyFlags );
```

```
Parameters
options
A decompression session options reference.
This reference is returned by
ICMDecompressionSessionOptionsCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueSize
A pointer to the size of the returned property’s
value.
outPropFlags
On return, a pointer to flags representing
the requested information about the property.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the value of a specific property of a decompression
session options object.

```
OSStatus ICMDecompressionSessionOptionsGetProperty (
   ICMDecompressionSessionOptionsRef   options,
   ComponentPropertyClass              inPropClass,
   ComponentPropertyID                 inPropID,
   ByteCount                           inPropValueSize,
   ComponentValuePtr                   outPropValueAddress,
   ByteCount                           *outPropValueSizeUsed );
```

```
Parameters
options
A decompression session options reference.
This reference is returned by
ICMDecompressionSessionOptionsCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
inPropValueSize
The size of the property value to be retrieved.
outPropValueAddress
A pointer to a variable to hold the value
of the property.
outPropValueSizeUsed
On return, a pointer to the number of bytes
actually used to store the property value.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns the type ID for the current decompression session
options object.

```
CFTypeID ICMDecompressionSessionOptionsGetTypeID ( void );
```

##### Return Value

A `CFTypeID` value.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Decrements the retain count of a decompression session
options object.

```
void ICMDecompressionSessionOptionsRelease (
   ICMDecompressionSessionOptionsRef   options );
```

```
Parameters
options
A reference to a decompression session options
object. This reference is returned by
ICMDecompressionSessionOptionsCreate
.
If you pass
NULL
, nothing
happens.
```

```
Discussion
If the retain count drops to 0, the object is disposed.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Increments the retain count of a decompression session
options object.

```
ICMDecompressionSessionOptionsRef ICMDecompressionSessionOptionsRetain (
   ICMDecompressionSessionOptionsRef   options );
```

```
Parameters
options
A reference to a decompression session options
object. This reference is returned by
ICMDecompressionSessionOptionsCreate
.
If you pass
NULL
, nothing
happens.
```

##### Return Value

A copy of the object
reference passed in _options_, for
convenience.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets the value of a specific property of a decompression
session options object.

```
OSStatus ICMDecompressionSessionOptionsSetProperty (
   ICMDecompressionSessionOptionsRef   options,
   ComponentPropertyClass              inPropClass,
   ComponentPropertyID                 inPropID,
   ByteCount                           inPropValueSize,
   ConstComponentValuePtr              inPropValueAddress );
```

```
Parameters
options
A decompression session options reference.
This reference is returned by
ICMDecompressionSessionOptionsCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
inPropValueSize
The size of the property value to be set.
inPropValueAddress
A pointer to the value of the property to
be set.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Increments the retain count of a decompression session.

```
ICMDecompressionSessionRef ICMDecompressionSessionRetain (
   ICMDecompressionSessionRef    session );
```

```
Parameters
session
A decompression session reference. This reference
is returned by
ICMDecompressionSessionCreate
.
If you pass
NULL
, nothing
happens.
```

##### Return Value

A copy of the reference
passed in _session_, for convenience.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Decrements the retain count of a decompression session.

```
void ICMDecompressionSessionRelease (
   ICMDecompressionSessionRef    session );
```

```
Parameters
session
A decompression session reference. This reference
is returned by
ICMDecompressionSessionCreate
.
If you pass
NULL
, nothing
happens.
```

```
Discussion
If the retain count drops to 0, the object is disposed.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets the direction for non-scheduled display time.

```
OSStatus ICMDecompressionSessionSetNonScheduledDisplayDirection (
   ICMDecompressionSessionRef   session,
   Fixed                        rate );
```

```
Parameters
session
A decompression session reference. This reference
is returned by
ICMDecompressionSessionCreate
.
rate
The display direction. Negative values represent
backward display and positive values represent forward display.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets the display time for a decompression session, and
requests display of the non-scheduled queued frame at that display
time, if there is one.

```
OSStatus ICMDecompressionSessionSetNonScheduledDisplayTime (
   ICMDecompressionSessionRef   session,
   TimeValue64                  displayTime,
   TimeScale                    displayTimeScale,
   UInt32                       flags );
```

```
Parameters
session
A decompression session reference. This reference
is returned by
ICMDecompressionSessionCreate
.
displayTime
A display time. Usually this is the display
time of a non-scheduled queued frame.
displayTimeScale
The timescale according to which
displayTime
should
be interpreted.
flags
Reserved; set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets the value of a specific property of a decompression
session.

```
OSStatus ICMDecompressionSessionSetProperty (
   ICMDecompressionSessionRef   session,
   ComponentPropertyClass       inPropClass,
   ComponentPropertyID          inPropID,
   ByteCount                    inPropValueSize,
   ConstComponentValuePtr       inPropValueAddress );
```

```
Parameters
session
A decompression session reference. This reference
is returned by
ICMDecompressionSessionCreate
.
inPropClass
Pass the following constant to define the
property class:
kComponentPropertyClassPropertyInfo	=
'pnfo'
The property information class.
inPropID
Pass one of these constants to define the
property ID:
kComponentPropertyInfoList		=
'list'
An array of
CFData
values, one
for each property.
kComponentPropertyCacheSeed		=
'seed'
A property cache seed value.
kComponentPropertyCacheFlags	=
'flgs'
One of the
kComponentPropertyCache
flags:
kComponentPropertyCacheFlagNotPersistent
Property
metadata should not be saved in persistent cache.
kComponentPropertyCacheFlagIsDynamic
Property
metadata should not cached at all.
kComponentPropertyExtendedInfo	=
'meta'
A
CFDictionary
with extended property
information.
inPropValueSize
The size in bytes of the property’s value.
inPropValueAddress
A pointer to the property value to be set.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Gets the size of an encoded frame’s data buffer.

```
ByteCount ICMEncodedFrameGetBufferSize (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

The physical size
in bytes of the encoded frame’s data buffer.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Called by a compressor to create an encoded-frame token
corresponding to a given source frame.

```
OSStatus ICMEncodedFrameCreateMutable (
   ICMCompressorSessionRef       session,
   ICMCompressorSourceFrameRef   sourceFrame,
   ByteCount                     bufferSize,
   ICMMutableEncodedFrameRef     *frameOut );
```

```
Parameters
session
A reference to the compression session between
the ICM and an image compressor component.
sourceFrame
A reference to a frame that has been passed
in
sourceFrameRefCon
to
ICMCompressionSessionEncodeFrame
.
bufferSize
The size of the frame buffer in bytes.
frameOut
On return, a reference to an encoded frame
object with write capabilities.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The encoded frame will initially show 0 for
mediaSampleFlags
;
if the frame is not a key frame, the compressor must call
ICMEncodedFrameSetMediaSampleFlags
to
set
mediaSampleNotSync
.
If the frame is droppable, the compressor should set
mediaSampleDroppable
.
If the frame is a partial key frame, the compressor should set
mediaSamplePartialSync
.
The encoded frame will initially have undefined
decodeTimeStamp
and
decodeDuration
values.
The compressor may set these directly by calling
ICMEncodedFrameSetDecodeTimeStamp
and
ICMEncodedFrameSetDecodeDuration
.
If these are not set by the compressor, the ICM will try to derive
values for them.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Gets the data buffer for an encoded frame.

```
UInt8 *ICMEncodedFrameGetDataPtr (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

A pointer to the object’s
data buffer.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Gets the data size of the compressed frame in an encoded
frame’s buffer.

```
ByteCount ICMEncodedFrameGetDataSize (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

The logical size in
bytes of the encoded frame’s data buffer, which may be less than
the physical size of the buffer.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves an encoded frame’s decode duration.

```
TimeValue64 ICMEncodedFrameGetDecodeDuration (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

The encoded frame’s
decode duration.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the decode number of an encoded frame.

```
UInt32 ICMEncodedFrameGetDecodeNumber (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

The decode number
of the encoded frame.

```
Discussion
The ICM automatically stamps ascending decode numbers on frames
after the compressor emits them. The first decode number in session
is 1. Compressors should not call this function.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves an encoded frame’s decode time stamp.

```
TimeValue64 ICMEncodedFrameGetDecodeTimeStamp (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

The encoded frame’s
decode time stamp.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves an encoded frame’s display duration.

```
TimeValue64 ICMEncodedFrameGetDisplayDuration (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

The encoded frame’s
display duration.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves an encoded frame’s display offset.

```
TimeValue64 ICMEncodedFrameGetDisplayOffset (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

The encoded frame’s
display offset. This is the time offset from decode time stamp to
display time stamp.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves an encoded frame’s display time stamp.

```
TimeValue64 ICMEncodedFrameGetDisplayTimeStamp (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

The encoded frame’s
display time stamp.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the `frame` type
for an encoded frame.

```
ICMFrameType ICMEncodedFrameGetFrameType (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

The encoded frame’s
frame type (see below).

```
Discussion
This function returns one of these values:
kICMFrameType_I
= 'I'
An I frame.
kICMFrameType_P
= 'P'
A P frame.
kICMFrameType_B
= 'B'
A B frame.
kICMFrameType_Unknown
= 0
A frame of unknown type.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the image description of an encoded frame.

```
OSStatus ICMEncodedFrameGetImageDescription (
   ICMEncodedFrameRef       frame,
   ImageDescriptionHandle   *imageDescOut );
```

```
Parameters
frame
A reference to an encoded frame object.
imageDescOut
A pointer to a handle containing the encoded
frame’s image description. The caller should not dispose of this
handle.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This function returns the same image description handle as
ICMCompressionSessionGetImageDescription
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the media sample flags for an encoded frame.

```
MediaSampleFlags ICMEncodedFrameGetMediaSampleFlags (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

The object’s media
sample flags. These flags are listed in the header file `Movies.h`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the similarity value for an encoded frame.

```
Float32 ICMEncodedFrameGetSimilarity (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

The encoded frame’s
similarity value. 1.0 means identical; 0.0 means not at all alike.
The default value is –1.0, which means unknown.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the reference value of an encoded frame’s
source frame.

```
void *ICMEncodedFrameGetSourceFrameRefCon (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

```
Discussion
The source frame’s reference value is copied from the session’s
sourceFrameRefCon
parameter
that was passed to
ICMCompressionSessionEncodeFrame
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves the timescale of an encoded frame.

```
TimeScale ICMEncodedFrameGetTimeScale (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

The time scale of
an encoded frame. This is always the same as the time scale of the
compression session.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns the type ID for the current encoded frame object.

```
CFTypeID ICMEncodedFrameGetTypeID ( void );
```

##### Return Value

A `CFTypeID` value.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retrieves an encoded frame’s flags indicating which
of its time stamps and durations are valid.

```
ICMValidTimeFlags ICMEncodedFrameGetValidTimeFlags (
   ICMEncodedFrameRef   frame );
```

```
Parameters
frame
A reference to an encoded frame object.
```

##### Return Value

One of the constants
listed below.

```
Discussion
This function returns one of these values:
kICMValidTime_DisplayTimeStampIsValid
    = 1L<<0
The value of
displayTimeStamp
is
valid.
kICMValidTime_DisplayDurationIsValid
     = 1L<<1
The value of
displayDuration
is
valid.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Decrements the retain count of an encoded frame object.

```
void ICMEncodedFrameRelease (
   ICMEncodedFrameRef    frame );
```

```
Parameters
frame
A reference to an encoded frame object. If
you pass
NULL
, nothing happens.
```

```
Discussion
If the retain count drops to 0, the object is disposed.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Increments the retain count of an encoded frame object.

```
ICMEncodedFrameRef ICMEncodedFrameRetain (
   ICMEncodedFrameRef    frame );
```

```
Parameters
frame
A reference to an encoded frame object. If
you pass
NULL
, nothing happens.
```

##### Return Value

A reference to the
object passed in _frame_, for convenience.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets the data size of the compressed frame in an encoded
frame’s buffer.

```
OSStatus ICMEncodedFrameSetDataSize (
   ICMMutableEncodedFrameRef   frame,
   ByteCount                   dataSize );
```

```
Parameters
frame
A reference to an encoded frame object with
write capabilities.
dataSize
The data size of the compressed frame in the
encoded frame object’s buffer.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets an encoded frame’s decode duration.

```
OSStatus ICMEncodedFrameSetDecodeDuration (
   ICMMutableEncodedFrameRef   frame,
   TimeValue64                 decodeDuration );
```

```
Parameters
frame
A reference to an encoded frame object with
write capabilities.
decodeDuration
The encoded frame’s decode duration.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This function automatically sets the
kICMValidTime_DecodeDurationIsValid
flag.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets an encoded frame’s decode time stamp.

```
OSStatus ICMEncodedFrameSetDecodeTimeStamp (
   ICMMutableEncodedFrameRef   frame,
   TimeValue64                 decodeTimeStamp );
```

```
Parameters
frame
A reference to an encoded frame object with
write capabilities.
decodeTimeStamp
The encoded frame’s decode time stamp.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This function automatically sets the
kICMValidTime_DecodeTimeStampIsValid
flag.
If the display time stamp is valid, it also sets the
kICMValidTime_DisplayOffsetIsValid
flag.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets an encoded frame’s display duration.

```
OSStatus ICMEncodedFrameSetDisplayDuration (
   ICMMutableEncodedFrameRef   frame,
   TimeValue64                 displayDuration );
```

```
Parameters
frame
A reference to an encoded frame object with
write capabilities.
displayDuration
The encoded frame’s display duration.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This function automatically sets the
kICMValidTime_DisplayDurationIsValid
flag.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets an encoded frame’s display time stamp.

```
OSStatus ICMEncodedFrameSetDisplayTimeStamp (
   ICMMutableEncodedFrameRef   frame,
   TimeValue64                 displayTimeStamp );
```

```
Parameters
frame
A reference to an encoded frame object with
write capabilities.
displayTimeStamp
The encoded frame’s display time stamp.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This function automatically sets the
kICMValidTime_DisplayTimeStampIsValid
flag.
If the decode time stamp is valid, it also sets the
kICMValidTime_DisplayOffsetIsValid
flag.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets an encoded frame’s flags that indicate which of
its time stamps and durations are valid.

```
OSStatus ICMEncodedFrameSetValidTimeFlags (
   ICMMutableEncodedFrameRef   frame,
   ICMValidTimeFlags           validTimeFlags );
```

```
Parameters
frame
A reference to an encoded frame object with
write capabilities.
validTimeFlags
One of the following constants:
kICMValidTime_DisplayTimeStampIsValid
    = 1L<<0
The value of
displayTimeStamp
is
valid.
kICMValidTime_DisplayDurationIsValid
     = 1L<<1
The value of
displayDuration
is
valid.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
Setting an encoded frame’s decode or display time stamp
or duration automatically sets the corresponding valid time flags.
For example, calling
ICMEncodedFrameSetDecodeTimeStamp
sets
kICMValidTime_DisplayTimeStampIsValid
.
If both the encoded frame’s decode time stamp and display time
stamp are valid,
kICMValidTime_DisplayOffsetIsValid
is
automatically set.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets the media sample flags for an encoded frame.

```
OSStatus ICMEncodedFrameSetMediaSampleFlags (
   ICMMutableEncodedFrameRef   frame,
   MediaSampleFlags            mediaSampleFlags );
```

```
Parameters
frame
A reference to an encoded frame object with
write capabilities.
mediaSampleFlags
The object’s media sample flags. These flags
are listed in the header file
Movies.h
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets the `frame` type
for an encoded frame.

```
OSStatus ICMEncodedFrameSetFrameType (
   ICMMutableEncodedFrameRef   frame,
   ICMFrameType                frameType );
```

```
Parameters
frame
A reference to an encoded frame object with
write capabilities.
frameType
The frame type to be set:
kICMFrameType_I
= 'I'
An I frame.
kICMFrameType_P
= 'P'
A P frame.
kICMFrameType_B
= 'B'
A B frame.
kICMFrameType_Unknown
= 0
A frame of unknown type.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets the similarity for an encoded frame.

```
OSStatus ICMEncodedFrameSetSimilarity (
   ICMMutableEncodedFrameRef   frame,
   Float32                     similarity );
```

```
Parameters
frame
A reference to an encoded frame object with
write capabilities.
similarity
The encoded frame’s similarity value to
be set. 1.0 means identical; 0.0 means not at all alike. The default
value is –1.0, which means unknown.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns a particular property of a image description handle.

```
OSStatus ICMImageDescriptionGetProperty (
   ImageDescriptionHandle inDesc,
   ComponentPropertyClass inPropClass,
   ComponentPropertyID inPropID,
   ByteCount inPropValueSize,
   ComponentValuePtr outPropValueAddress,
   ByteCount *outPropValueSizeUsed );
```

```
Parameters
inDesc
The image description handle being interrogated.
inPropClass
The class of property being requested.
inPropID
The ID of the property being requested.
inPropValueSize
The size of the property value buffer.
outPropValueAddress
Points to the buffer to receive the property
value.
outPropValueSizeUsed
Points to a variable to receive the actual
size of returned property value. (This can be
NULL
).
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This routine returns a particular property of a image description
handle.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns information about a particular property of a image
description.

```
OSStatus ICMImageDescriptionGetPropertyInfo (
   ImageDescriptionHandle inDesc,
   ComponentPropertyClass inPropClass,
   ComponentPropertyID inPropID,
   ComponentValueType *outPropType,
   /*can be NULL */ ByteCount *outPropValueSize,
   /*can be NULL */ UInt32 *outPropertyFlags );
```

```
Parameters
inDesc
The image description handle being interrogated.
inPropClass
The class of property being requested.
inPropID
The ID of the property being requested.
outPropType
The type of property is returned here. (This
can be
NULL
).
outPropValueSize
The size of property is returned here. (This
can be
NULL
).
outPropertyFlags
The property flags are returned here. (This
can be
NULL
).
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets a particular property of a image description handle.

```
OSStatus ICMImageDescriptionSetProperty (
   ImageDescriptionHandle inDesc,
   ComponentPropertyClass inPropClass,
   ComponentPropertyID inPropID,
   ByteCount inPropValueSize,
   ConstComponentValuePtr inPropValueAddress );
```

```
Parameters
inDesc
The image description handle being modified.
inPropClass
The class of property being set.
inPropID
The ID of the property being set.
inPropValueSize
The size of property value.
inPropValueAddress
Points to the property value buffer.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Called by a multipass-capable compressor to retrieve data
at a given time stamp.

```
OSStatus ICMMultiPassStorageCopyDataAtTimeStamp (
   ICMMultiPassStorageRef   multiPassStorage,
   TimeValue64              timeStamp,
   long                     index,
   CFMutableDataRef         *dataOut );
```

```
Parameters
multiPassStorage
The multipass storage object.
timeStamp
The time stamp at which the value should be
retrieved.
index
An index by which multiple values may be stored
at a time stamp. The meaning of individual indexes is private to
the compressor.
dataOut
A pointer to memory to receive the data at
the time stamp.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Assembles a multipass storage mechanism from callbacks.

```
OSStatus ICMMultiPassStorageCreateWithCallbacks (
   CFAllocatorRef                 allocator,
   ICMMultiPassStorageCallbacks   *callbacks,
   ICMMultiPassStorageRef         *multiPassStorageOut );
```

```
Parameters
allocator
An allocator for this task. Pass
NULL
to
use the default allocator.
callbacks
A structure containing a collection of callbacks
for creating a custom multipass storage object. See
ICMMultiPassStorageCallbacks
.
multiPassStorageOut
A reference to the new multipass storage object.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Creates multipass storage using a temporary file.

```
OSStatus ICMMultiPassStorageCreateWithTemporaryFile (
   CFAllocatorRef                     allocator,
   FSRef                              *directoryRef,
   CFStringRef                        fileName,
   ICMMultiPassStorageCreationFlags   flags,
   ICMMultiPassStorageRef             *multiPassStorageOut );
```

```
Parameters
allocator
An allocator for this task. Pass
NULL
to
use the default allocator.
directoryRef
A reference to a file directory. If you pass
NULL
,
the ICM will use the user’s Temporary Items folder.
fileName
A file name to use for the storage. If you
pass
NULL
, the ICM will
pick a unique name. If you pass the name of a file that already
exists, the ICM will assume you are continuing a previous multipass
session where you left off. This file will be deleted when the multipass
storage is released, unless you set the
kICMMultiPassStorage_DoNotDeleteWhenDone
flag.
flags
Flag controlling this process:
kICMMultiPassStorage_DoNotDeleteWhenDone
= 1L<<0
The temporary file should not be deleted when the multipass
storage is released.
multiPassStorageOut
A reference to the new multipass storage.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Called by a multipass-capable compressor to retrieve a
time stamp for which a value is stored.

```
OSStatus ICMMultiPassStorageGetTimeStamp (
   ICMMultiPassStorageRef    multiPassStorage,
   TimeValue64               fromTimeStamp,
   ICMMultiPassStorageStep   step,
   TimeValue64               *timeStampOut );
```

```
Parameters
multiPassStorage
The multipass storage object.
fromTimeStamp
The initial time stamp. This value is ignored
for some values of
step
.
step
Indicates the kind of time stamp search to
perform:
kICMMultiPassStorage_GetFirstTimeStamp
= 1
Requests the first time stamp at which a value is stored.
kICMMultiPassStorage_GetPreviousTimeStamp
= 2
Requests the previous time stamp before the time stamp specified
in
fromTimeStamp
at which a value
is stored.
kICMMultiPassStorage_GetNextTimeStamp
= 3
Requests the next time stamp after the time stamp specified in
fromTimeStamp
at
which a value is stored.
kICMMultiPassStorage_GetLastTimeStamp
= 4
Requests the last time stamp at which a value is stored.
timeStampOut
A pointer to a
TimeValue64
value
to receive the found time stamp. It will be set to –1 if no time
stamp is found.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns the type ID for the current multipass storage
object.

```
CFTypeID ICMMultiPassStorageGetTypeID ( void );
```

##### Return Value

A `CFTypeID` value.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Decrements the retain count of a multipass storage object.

```
void ICMMultiPassStorageRelease (
   ICMMultiPassStorageRef    multiPassStorage );
```

```
Parameters
multiPassStorageOut
A reference to a multipass storage object.
You can create this object using
ICMMultiPassStorageCreateWithTemporaryFile
or
ICMMultiPassStorageCreateWithCallbacks
.
If you pass
NULL
, nothing happens.
```

```
Discussion
If the retain count drops to 0, the object is disposed.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Increments the retain count of a multipass storage object.

```
ICMMultiPassStorageRef ICMMultiPassStorageRetain (
   ICMMultiPassStorageRef    multiPassStorage );
```

```
Parameters
multiPassStorageOut
A reference to a multipass storage object.
You can create this object using
ICMMultiPassStorageCreateWithTemporaryFile
or
ICMMultiPassStorageCreateWithCallbacks
.
If you pass
NULL
, nothing happens.
```

##### Return Value

A reference to the
object passed in _multiPassStorage_,
for convenience.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Called by a multipass-capable compressor to store data
at a given time stamp.

```
OSStatus ICMMultiPassStorageSetDataAtTimeStamp (
   ICMMultiPassStorageRef   multiPassStorage,
   TimeValue64              timeStamp,
   long                     index,
   CFDataRef                data );
```

```
Parameters
multiPassStorage
The multipass storage object.
timeStamp
The time stamp at which the value should be
stored.
index
An index by which multiple values may be stored
at a time stamp. The meaning of individual indexes is private to
the compressor.
data
The data to be stored, or
NULL
to
delete the value.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The new data replaces any previous data held at that time
stamp. If the value of
data
is
NULL
,
the data for that time stamp is deleted. The format of the data
is private to the compressor.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Notifies the compressor that it should operate in multipass
mode and use the given multipass storage.

```
ComponentResult ImageCodecBeginPass (
   ComponentInstance                ci,
   ICMCompressionPassModeFlags      passModeFlags,
   UInt32                           flags,
   ICMMultiPassStorageRef           multiPassStorage);
```

```
Parameters
ci
A component instance that identifies a connection
to an image codec component.
passModeFlags
Indicates how the compressor should operate
in this pass. If the
kICMCompressionPassMode_WriteToMultiPassStorage
flag
is set, the compressor may gather information of interest and store
it in
multiPassStorage
.
If the
kICMCompressionPassMode_ReadFromMultiPassStorage
flag
is set, the compressor may retrieve information from
multiPassStorage
.
If the
kICMCompressionPassMode_OutputEncodedFrames
flag
is set, the compressor must encode or
drop every frame by calling
ICMCompressorSessionDropFrame
or
ICMCompressorSessionEmitEncodedFrame
.
If that flag is not set, the compressor should not call these routines.
flags
Reserved. Ignore this parameter.
multiPassStorage
The multipass storage object that the compressor
should use to store and retrieve information between passes.
```

##### Return Value

An error code, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
ImageCodec.h
```


Directs the compressor to finish with a queued source
frame, either emitting or dropping it.

```
ComponentResult ImageCodecCompleteFrame (
   ComponentInstance                ci,
   ICMCompressorSourceFrameRef      sourceFrame,
   UInt32                           flags );
```

```
Parameters
ci
A component instance that identifies a connection
to an image codec component.
sourceFrame
The source frame that must be completed.
flags
Reserved; ignore.
```

##### Return Value

An error code, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This frame does not necessarily need to be the first or only
source frame emitted or dropped during this call, but the compressor
must call either
ICMCompressorSessionDropFrame
or
ICMCompressorSessionEmitEncodedFrame
with
this frame before returning. The ICM will call this function to
force frames to be encoded for the following reasons: (a) the maximum
frame delay count or maximum frame delay time in the
compressionSessionOptions
does
not permit frames to be queued; (b) the client has called
ICMCompressionSessionCompleteFrames
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Not supported
C interface file:
ImageCodec.h
```


Returns an `ImageSubCodecDecompressRecord` structure
for an image codec component.

```
ComponentResult ImageCodecDecodeBand (
   ComponentInstance                ci,
   ImageSubCodecDecompressRecord    *drp,
   unsigned long                    flags );
```

```
Parameters
ci
A component instance that identifies a connection
to an image codec component.
drp
A pointer to an
ImageSubCodecDecompressRecord
structure.
flags
Not used; set to 0.
```

##### Return Value

An error code, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Not supported
C interface file:
ImageCodec.h
```


Presents the compressor with a frame to encode.

```
ComponentResult ImageCodecEncodeFrame (
   ComponentInstance                ci,
   ICMCompressorSourceFrameRef      sourceFrame,
   unsigned long                    flags );
```

```
Parameters
ci
A component instance that identifies a connection
to an image codec component.
sourceFrame
The source frame to encode.
flags
Reserved; ignore.
```

##### Return Value

An error code, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The compressor may encode the frame immediately or queue it
for later encoding. If the compressor queues the frame for later
decode, it must retain it (by calling
ICMCompressorSourceFrameRetain
)
and release it when it is done with it (by calling
ICMCompressorSourceFrameRelease
).
Pixel buffers are guaranteed to conform to the pixel buffer attributes
returned by
ImageCodecPrepareToCompressFrames
.
During multipass encoding, if the compressor requested the
kICMCompressionPassMode_NoSourceFrames
flag, the
source frame pixel buffers may be
NULL
.
(Note: this replaces
ImageCodecBandCompress
.)
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Not supported
C interface file:
ImageCodec.h
```


Prepares the compressor to receive frames.

```
ComponentResult ImageCodecPrepareToCompressFrames (
   ComponentInstance                ci,
   ICMCompressorSessionRef          session,
   ICMCompressionSessionOptionsRef  compressionSessionOptions,
   ImageDescriptionHandle           imageDescription,
   void                             *reserved,
   CFDictionaryRef                      *compressorPixelBufferAttributesOut);
```

```
Parameters
ci
A component instance that identifies a connection
to an image codec component.
session
The compressor session reference. The compressor
should store this in its globals; it will need it when calling the
ICM back (for example, to call
ICMEncodedFrameCreateMutable
and
ICMCompressorSessionEmitEncodedFrame
).
This is not a CF type. Do not call
CFRetain
or
CFRelease
on
it.
compressionSessionOptions
The session options from the client. The compressor
should retain this and use the settings to guide compression.
imageDescription
The image description. The compressor may
add image description extensions.
reserved
Reserved for future use. Ignore this parameter.
compressorPixelBufferAttributesOut
The compressor should create a pixel buffer
attributes dictionary and set
compressorPixelBufferAttributesOut
to
it. The ICM will release it.
```

##### Return Value

An error code, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The compressor should record session and retain
compressionSessionOptions
for
use in later calls. The compressor may modify
imageDescription
at
this point. The compressor should create and return pixel buffer
attributes, which the ICM will release. (Note: this replaces
ImageCodecPreCompress
.)
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Not supported
C interface file:
ImageCodec.h
```


Provides the compressor with an opportunity to perform
processing between passes.

```
ComponentResult ImageCodecProcessBetweenPasses (
   ComponentInstance                ci,
   ICMMultiPassStorageRef           multiPassStorage,
   Boolean                          *interpassProcessingDoneOut,
   ICMCompressionPassModeFlags      *requestedNextPassModeFlagsOut );
```

```
Parameters
ci
A component instance that identifies a connection
to an image codec component.
multiPassStorage
The multipass storage object that the compressor
should use to store and retrieve information between passes.
interpassProcessingDoneOut
Points to a Boolean. Set this to
FALSE
if
you want your
ImageCodecProcessBetweenPasses
function
to be called again to perform more processing,
TRUE
if
not.
requestedNextPassModeFlagsOut
Set
*requestedNextPassModeFlagsOut
to
indicate the type of pass that should be performed next: To recommend
a repeated analysis pass, set it to
kICMCompressionPassMode_ReadFromMultiPassStorage| kICMCompressionPassMode_WriteToMultiPassStorage
.
To recommend a final encoding pass, set it to
kICMCompressionPassMode_ReadFromMultiPassStorage
| kICMCompressionPassMode_OutputEncodedFrames
.
If source frame buffers are not necessary for the recommended pass
(for example, because all the required data has been copied into
multipass storage), set
kICMCompressionPassMode_NoSourceFrames
.
```

##### Return Value

An error code, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This function will be called repeatedly until it returns
TRUE
in
*interpassProcessingDoneOut
.
The compressor may read and write to
multiPassStorage
.
The compressor should indicate which type of pass it would prefer
to perform next by setting
*requestedNextPassTypeOut
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Not supported.
C interface file:
ImageCodec.h
```


Invokes the specified property listener of a track.

```
void InvokeQTTrackPropertyListenerUPP (
   Track inTrack,
   QTPropertyClass inPropClass,
   QTPropertyID inPropID,
   void *inUserData,
   QTTrackPropertyListenerUPP userUPP );
```

```
Parameters
inTrack
The track of this operation.
inPropClass
A property class.
inPropID
A property ID.
inUserData
A pointer to user data that will be passed
to the callback.
userUPP
A
QTTrackPropertyListenerUPP
pointer.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Tests whether a media contains display offsets.

```
Boolean MediaContainsDisplayOffsets (
   Media    theMedia );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
```

##### Return Value

`TRUE` if
the media is valid and contains at least one sample with a nonzero display
offset; `FALSE` otherwise.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Finds the sample for a specified decode time.

```
void MediaDecodeTimeToSampleNum (
   Media          theMedia,
   TimeValue64    decodeTime,
   SInt64         *sampleNum,
   TimeValue64    *sampleDecodeTime,
   TimeValue64    *sampleDecodeDuration );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
decodeTime
A 64-bit time value that represents the decode
time for which you are retrieving sample information. You must specify
this value in the media's time scale.
sampleNum
A pointer to a variable that is to receive
the sample number. The function returns the sample number that identifies
the sample that contains data for the specified decode time, or
0 if it is not found.
sampleDecodeTime
A pointer to a time value. The function updates
this time value to indicate the decode time of the sample specified
by the
logicalSampleNum
parameter.
This time value is expressed in the media’s time scale. Set this parameter
to
NULL
if you do not
want this information.
sampleDecodeDuration
A pointer to a time value. The function updates
this time value to indicate the decode duration of the sample specified
by the
logicalSampleNum
parameter.
This time value is expressed in the media’s time scale. Set this parameter
to
NULL
if you do not
want this information.
```

```
Discussion
You can access this function's error returns through
GetMoviesError
and
GetMoviesStickyError
.
It returns
paramErr
if there is a bad
parameter value,
invalidTime
if
sampleDecodeTime
is
out of the decode time range, or
noErr
if
there is no error.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Fnds the sample number for a specified display time.

```
void MediaDisplayTimeToSampleNum (
   Media          theMedia,
   TimeValue64    displayTime,
   SInt64         *sampleNum,
   TimeValue64    *sampleDisplayTime,
   TimeValue64    *sampleDisplayDuration );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
displayTime
A 64-bit time value that represents the display
time for which you are retrieving sample information. You must specify
this value in the media’s time scale.
sampleNum
A pointer to a long integer that is to receive
the sample number. The function returns the sample number that identifies
the sample for the specified display time, or 0 if it is not found.
sampleDisplayTime
A pointer to a time value. The function updates
this time value to indicate the display time of the sample specified
by the
logicalSampleNum
parameter.
This time value is expressed in the media’s time scale. Set this parameter
to
NULL
if you do not
want this information.
sampleDisplayDuration
A pointer to a time value. The function updates
this time value to indicate the display duration of the sample specified
by the
logicalSampleNum
parameter.
This time value is expressed in the media’s time scale. Set this parameter
to
NULL
if you do not
want this information.
```

```
Discussion
You can access this function's error returns through
GetMoviesError
and
GetMoviesStickyError
.
It returns
paramErr
if there is a bad
parameter value, invalidTime if
sampleDisplayTime
is
out of the display time range, or
noErr
if
there is no error.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Begins a movie audio extraction session.

```
OSStatus MovieAudioExtractionBegin (
   Movie                      m,
   UInt32                     flags,
   MovieAudioExtractionRef    *outSession );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
flags
Reserved; must be 0.
outSession
A pointer to an opaque session object.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
You must call this function before doing any movie audio extraction,
because you will pass the object returned by
outSession
to
the other movie audio extraction functions. The format of the extracted
audio defaults to the summary channel layout of the movie (all right
channels mixed together, all left surround channels mixed together,
and so on.), 32-bit float, de-interleaved, with the sample rate
set to the highest sample rate found in the movie. You can set the
audio format to be something else, as long as it is uncompressed and
you do it before your first call to
MovieAudioExtractionFillBuffer
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Ends a movie audio extraction session.

```
OSStatus MovieAudioExtractionEnd (
   MovieAudioExtractionRef    session );
```

```
Parameters
session
The session object returned by
MovieAudioExtractionBegin
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
You must call this function when movie audio extraction is
complete.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Extracts audio from a movie.

```
OSStatus MovieAudioExtractionFillBuffer (
   MovieAudioExtractionRef    session,
   UInt32                     *ioNumFrames,
   AudioBufferList            *ioData,
   UInt32                     *outFlags );
```

```
Parameters
session
The session object returned by
MovieAudioExtractionBegin
.
ioNumFrames
A pointer to the number of PCM frames to be
extracted.
ioData
A pointer to an
AudioBufferList
allocated
by the caller to hold the extracted audio data.
outFlags
A bit flag that indicates when extraction
is complete:
kMovieAudioExtractionComplete
The extraction process is complete. Value is
(1L
<< 0)
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
You call this function repeatedly; each call continues extracting
audio where the last call left off. The function will extract as
many of the requested PCM frames as it can, given the limits of
the buffer supplied and the limits of the input movie.
ioNumFrames
will
be updated with the exact number of valid frames being returned.
When there is no more audio to extract from the movie, the function
will continue to return
noErr
but
will return no further audio data. In this case, the
outFlags
parameter
will have its
kMovieAudioExtractionComplete
bit
set. It is possible that the
kMovieAudioExtractionComplete
bit
will accompany the last buffer of valid data.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Gets a property of a movie audio extrraction session.

```
OSStatus MovieAudioExtractionGetProperty (
   MovieAudioExtractionRef    session,
   QTPropertyClass            inPropClass,
   QTPropertyID               inPropID,
   ByteCount                  inPropValueSize,
   QTPropertyValuePtr         outPropValueAddress,
   ByteCount                  *outPropValueSizeUsed);
```

```
Parameters
session
The session object returned by
MovieAudioExtractionBegin
.
inPropClass
Pass the following constant to define the
property class: Property of an audio presentation; value is
'audi'
.
inPropID
Pass one of these constants to define the
property ID:
kAudioPropertyID_ChannelLayout
The summary audio channel layout of a movie, or any
other grouping of audio streams. All like-labeled channels are combined,
without duplicates. For example, if there is a stereo (L/R) track,
5 single-channel tracks marked Left, Right, Left Surround, Right
Surround and Center, and a 4-channel track marked L/R/Ls/Rs, then
the summary AudioChannelLayout will be L/R/Ls/Rs/C, not L/R/L/R/Ls/Rs/C/L/R/Ls/Rs.
The value of this constant is
'clay'
.
inPropValueSize
The size of the buffer allocated to receive
the property value.
outPropValueAddress
A pointer to the buffer allocated to receive
the property value.
outPropValueSizeUsed
The actual size of the property value.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
You can get and set more than just the channel layout. There
are four properties, discussed below, all of which are gettable
and settable (with some having restrictions on not setting after
first calling
MovieAudioExtractionFillBuffer
).
Properties of the movie that is extracted from
kQTPropertyClass_MovieAudioExtraction_Movie
include
the following movie class IDs:
kQTMovieAudioExtractionMoviePropertyID_CurrentTime
.
The value is a
TimeRecord
, which
you can set and get. When setting, you set the timescale to anything
you want (for example, the output audio sample rate or the movie
timescale). When getting, the timescale will be output audio sample
rate for best accuracy.
kQTMovieAudioExtractionMoviePropertyID_AllChannelsDiscrete
.
The value is Boolean (which is settable and gettable). Set to implement
export of all audio channels without mixing. When this is set and
the extraction audio stream basic description (ASBD) or channel
layout are read back, you get information relating to the re-mapped movie.
Properties of the output audio extracted from
kQTPropertyClass_MovieAudioExtraction_Audio
include
the following output audio class properties:
kQTMovieAudioExtractionAudioPropertyID_AudioStreamBasicDescription
.
The value is an
AudioStreamBasicDescription
.
You can get any time and set before first the
MovieAudioExtractionFillBuffer
call.
If you get this property immediately after beginning an audio extraction
session, it will tell you the default extraction format for the
movie. This will include the number of channels in the default movie
mix. If you set the output
AudioStreamBasicDescription
,
it is recommended that you also set the output channel layout.
If your output ASBD has a different number of channels than  the
default extraction mix, you must set the output channel layout.
You can only set PCM output formats. Setting a compressed output
format will fail.
:
kQTMovieAudioExtractionAudioPropertyID_AudioChannelLayout
.
The value is
AudioChannelLayout
,
which you can get any time and set before first the
MovieAudioExtractionFillBuffer
call.
If you get this property immediately after beginning an audio extraction
session, it tells you what the channel layout is for the default
extraction mix.
The information in this discussion also applies to the following
functions:
MovieAudioExtractionGetPropertyInfo
MovieAudioExtractionSetProperty
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Gets information about a property of a movie audio extraction
session.

```
OSStatus MovieAudioExtractionGetPropertyInfo (
   MovieAudioExtractionRef    session,
   QTPropertyClass            inPropClass,
   QTPropertyID               inPropID,
   QTPropertyValueType        *outPropType,
   ByteCount                  *outPropValueSize,
   UInt32                     *outPropertyFlags );
```

```
Parameters
session
The session object returned by
MovieAudioExtractionBegin
.
inPropClass
Pass the following constant to define the
property class: Property of an audio presentation; value is
'audi
inPropID
Pass one of these constants to define the
property ID:
kAudioPropertyID_ChannelLayout
The summary audio channel layout of a movie, or any
other grouping of audio streams. All like-labeled channels are combined,
without duplicates. For example, if there is a stereo (L/R) track,
5 single-channel tracks marked Left, Right, Left Surround, Right
Surround and Center, and a 4-channel track marked L/R/Ls/Rs, then
the summary AudioChannelLayout will be L/R/Ls/Rs/C, not L/R/L/R/Ls/Rs/C/L/R/Ls/Rs.
The value of this constant is
'clay'
.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueSize
A pointer to the size of the returned property’s
value.
outPropFlags
On return, a pointer to flags representing
the requested information about the item’s property.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets a property of a movie audio extraction session.

```
OSStatus MovieAudioExtractionSetProperty (
   MovieAudioExtractionRef    session,
   QTPropertyClass            inPropClass,
   QTPropertyID               inPropID,
   ByteCount                  inPropValueSize,
   ConstQTPropertyValuePtr    inPropValueAddress );
```

```
Parameters
session
The session object returned by
MovieAudioExtractionBegin
.
inPropClass
Pass the following constant to define the
property class: Property of an audio presentation; value is
'audi'
.
inPropID
Pass one of these constants to define the
property ID:
kAudioPropertyID_SummaryChannelLayout
The summary audio channel layout of a movie, or any
other grouping of audio streams. All like-labeled channels are combined,
without duplicates. For example, if there is a stereo (L/R) track,
5 single-channel tracks marked Left, Right, Left Surround, Right
Surround and Center, and a 4-channel track marked L/R/Ls/Rs, then
the summary AudioChannelLayout will be L/R/Ls/Rs/C, not L/R/L/R/Ls/Rs/C/L/R/Ls/Rs.
The value of this constant is
'clay'
.
inPropValueSize
The size of the property value.
inPropValueAddress
A
const void
pointer
that points to the property value.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Allocates a new Universal Procedure Pointer for a `MovieExportStageReachedCallbackProc` callback.

```
MovieExportStageReachedCallbackUPP NewMovieExportStageReachedCallbackUPP (
   MovieExportStageReachedCallbackProcPtr    userRoutine );
```

```
Parameters
userRoutine
A pointer to your application-defined callback
function; see
ICMDecompressionTrackingCallbackProc
.
```

##### Return Value

A new Universal Procedure
Pointer that you will use to invoke your callback.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
QuickTimeComponents.h
```


Creates a new movie using movie properties.

```
OSStatus NewMovieFromProperties (
ItemCount                    inputPropertyCount,
QTNewMoviePropertyElement    *inputProperties,
ItemCount                    outputPropertyCount,
QTNewMoviePropertyElement    *outputProperties,
Movie                        *theMovie );
```

```
Parameters
inputPropertyCount
The number of properties in the array passed
in
inputProperties
.
inputProperties
A pointer to a property array describing how
to instantiate the movie. See
QTNewMoviePropertyElement
.
outputPropertyCount
The number of properties in the array passed
in
outputProperties
.
outputProperties
A pointer to a property array to receive output
parameters. See
QTNewMoviePropertyElement
.
You may pass
NULL
if
you don’t want this information. The caller is responsible for
calling the appropriate routines to dispose of any property values
returned here. Since callers specify the property classes and IDs,
they know who to call to dispose of the property values.
theMovie
A pointer to a variable that receives the
new movie.
```

##### Return Value

An error code. Returns `memFullErr` if
the function could not allocate memory, `paramErr` if _inputProperties_ or _theMovie_ is `NULL`,
or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if there is no error.

```
Discussion
This function can be used in all the cases where an existing
NewMovieFrom...
call
is used. When calling this function, you supply a set of input properties
that describe the information required to instantiate the movie
(its data reference, audio context, visual context, and so on).
You can also supply a set of output properties that you may be interested
in; for example, information about whether the data reference was
changed. See
New Movie Property Codes
.
This function verifies its input properties is as follows.
First, the
propStatus
field of both the input
and output property arrays is set to
kQTPropertyUnprocessedErr
.
Then the input properties are checked one by one. If there is no
problem with a property, its
propStatus
is
set to
noErr
(0). If there is a problem,
the
propStatus
for the property is set to 1
and the function returns
paramErr
.
It is an error if a property is not recognized;
paramErr
is returned
and the appropriate
propStatus
is set to
kQTPropertyNotSupportedErr
.
Another error is multiple data locations defined. In this case,
the property status for the second data location is set to
paramErr
.
It is not considered a fatal error if this function does not recognize
an output property; the property’s
propStatus
simply
remains
kQTPropertyUnprocessedErr
.
The only output properties currently defined are those that
support the behavior of functions of the form
NewMovieFrom...
.
For example, if you want to act upon the data reference being updated
during the opening process, you would pass in the
kQTMovieInstantiationPropertyID_ResultDataLocationChanged
property.
This function must be used with
kQTContextPropertyID_VisualContext
to
open a movie, for visual contexts to function with the movie. If
you want to use visual contexts with a movie but want to inspect
the movie prior to allocating the visual context to use (for instance
you want to get the movie box), use
kQTContextPropertyID_VisualContext
with a
NULL
value.
Otherwise, visual context calls with the movie will fail with an
error. Using
GWorld
structures with the movie
will also fail.
To handle special situations where this function cannot be
used by your application, there is a method to switch a movie from
GWorld mode to visual context mode.
SetMovieVisualContext
can
be used to set a
NULL
visual
context, which will disassociate the movie from its current visual
context or GWorld. At this time, either
SetMovieGWorld
or
SetMovieVisualContext
can
be used. If a movie is associated with a GWorld, visual context
calls such as
GetMovieVisualContext
will
fail. If a movie is a associated with a valid visual context, GWorld
calls such as
GetMovieGWorld
will fail.
If a call to this function succeeds using a visual context
or audio context, those objects will be explicitly retained for
use by the movie. The movie object is responsible for releasing them.
If you no longer need access to a context, it is safe to release
it.
If no data location property is specified, then this function
will behave like
NewMovie
, creating
an empty movie. Thus
NewMovieFromProperties(0,
nil, 0, nil, &movie)
is functionally equivalent
to
movie = NewMovie(0)
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Creates a new callback to monitor a track property.

```
QTTrackPropertyListenerUPP NewQTTrackPropertyListenerUPP (
   QTTrackPropertyListenerProcPtr userRoutine );
```

```
Parameters
userRoutine
A pointer to a QTTrackPropertyListenerProcPtr
callback.
```

##### Return Value

A new UPP; see Universal
Procedure Pointers in the `QuickTime API Reference`.

```
Discussion
This routine creates a new callback to monitor a track property.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Installs a callback to monitor a track property.

```
OSErr QTAddTrackPropertyListener (
   Track inTrack,
   QTPropertyClass inPropClass,
   QTPropertyID inPropID,
   QTTrackPropertyListenerUPP inListenerProc,
   void *inUserData );
```

```
Parameters
inTrack
The track for this operation.
inPropClass
A property class.
inPropID
A property ID.
inListenerProc
A Universal Procedure Pointer to a QTTrackPropertyListenerProc callback.
inUserData
A pointer to user data that will be passed
to the callback.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This routine installs a callback to monitor a track property.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Creates a QTAudioContext object that encapsulates a connection
to a CoreAudio output device.

```
OSStatus QTAudioContextCreateForAudioDevice (
   CFAllocatorRef allocator,
   CFStringRef coreAudioDeviceUID,
   CFDictionaryRef options,
   QTAudioContextRef *newAudioContextOut );
```

```
Parameters
allocator
Allocator used to create the audio context.
coreAudioDeviceUID
CoreAudio device UID.
NULL
means
the default device.
options
Reserved. Pass
NULL
.
newAudioContextOut
Points to a variable to receive the new audio
context.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This routine creates a QTAudioContext object that encapsulates
a connection to a CoreAudio output device. This object is suitable
for passing to
SetMovieAudioContext
or
NewMovieFromProperties
,
which targets the audio output of the movie to that device. A QTAudioContext
object cannot be associated with more than one movie. Each movie needs
its own connection to the device. In order to play more than one
movie to a particular device, create a QTAudioContext object for
each movie. You are responsible for releasing the QTAudioContext
object created by this routine. After calling
SetMovieAudioContext
or
NewMovieFromProperties
,
you can release the object since these APIs will retain it for their
own use.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Retains a movie’s metadata object and returns it.

```
OSStatus QTCopyMovieMetaData (
Movie            inMovie,
QTMetaDataRef    *outMetaData );
```

```
Parameters
inMovie
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
outMetaData
A pointer to an opaque metadata object wrapper
associated with the movie passed in
inMovie
.
```

##### Return Value

Returns `invalidMovie` if
the movie passed in _inMovie_ is invalid,
or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if there is no error.

```
Discussion
This function returns the metadata object associated with
a movie. The object has retain/release semantics. It has already
been retained before returning, but you should call
QTMetaDataRelease
when
you are done. Because the movie can be disposed of at any time, the
QTMetaDataRef
may
be valid when the movie no longer exists. In this case, the function will
fail with a
kQTMetaDataInvalidMetaDataErr
error.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Retains a track’s metadata object and returns it.

```
OSStatus QTCopyTrackMetaData (
Track            inTrack,
QTMetaDataRef    *outMetaData );
```

```
Parameters
inTrack
A track identifier, which your application
obtains from such functions as
NewMovieTrack
and
GetMovieTrack
.
outMetaData
A pointer to an opaque metadata object wrapper
associated with the track passed in
inTrack
.
```

##### Return Value

Returns `invalidMedia` if
the track passed in _inTrack_ is invalid,
or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if there is no error.

```
Discussion
This function returns the metadata object associated with
a track. The object has retain/release semantics. It has already
been retained before returning, but you should call
QTMetaDataRelease
when
you are done. Because the track can be disposed of at any time, the
QTMetaDataRef
may
be valid when the track no longer exists. In this case, the function will
fail with a
kQTMetaDataInvalidMetaDataErr
error.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Retains a media’s metadata object and returns it.

```
OSStatus QTCopyMediaMetaData (
Media            inMedia,
QTMetaDataRef    *outMetaData );
```

```
Parameters
inMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
outMetaData
A pointer to an opaque metadata object wrapper
associated with the media passed in
inMedia
.
```

##### Return Value

Returns `invalidMedia` if
the media passed in _inMedia_ is invalid,
or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if there is no error.

```
Discussion
This function returns the metadata object associated with
a media. The object has retain/release semantics. It has already
been retained before returning, but you should call
QTMetaDataRelease
when
you are done. Because the media can be disposed of at any time, the
QTMetaDataRef
may
be valid when the media no longer exists. In this case, the function will
fail with a
kQTMetaDataInvalidMetaDataErr
error.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the value of a specific track property.

```
OSErr QTGetTrackProperty (
   Track inTrack,
   QTPropertyClass inPropClass,
   QTPropertyID inPropID,
   ByteCount inPropValueSize,
   QTPropertyValuePtr outPropValueAddress,
   ByteCount *outPropValueSizeUsed );
```

```
Parameters
inTrack
The track for this operation.
inPropClass
A property class.
inPropID
A property ID.
inPropValueSize
The size of the buffer allocated to hold the
property value.
outPropValueAddress
A pointer to the buffer allocated to hold
the property value.
outPropValueSizeUsed
On return, the actual size of the value written
to the buffer.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This routine returns the value of a specific track property.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns information about the properties of a track.

```
OSErr QTGetTrackPropertyInfo (
   Track inTrack,
   QTPropertyClass inPropClass,
   QTPropertyID inPropID,
   QTPropertyValueType *outPropType,
   ByteCount *outPropValueSize,
   UInt32 *outPropertyFlags );
```

```
Parameters
inTrack
The track for this operation.
inPropClass
A property class.
inPropID
A property ID.
outPropType
A pointer to memory allocated to hold the
property
type
on return.
outPropValueSize
A pointer to memory allocated to hold the
size of the property value on return.
outPropertyFlags
A pointer to memory allocated to hold property
flags on return.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This routine returns information about the properties of a
track.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Adds an inline metadata item to the metadata storage format.

```
OSStatus QTMetaDataAddItem (
QTMetaDataRef              inMetaData,
QTMetaDataStorageFormat    inMetaDataFormat,
QTMetaDataKeyFormat        inKeyFormat,
const UInt8                *inKeyPtr,
ByteCount                  inKeySize,
const UInt8                *inValuePtr,
ByteCount                  inValueSize,
UInt32                     inDataType,
QTMetaDataItem             *outItem);
```

```
Parameters
inMetaData
The metadata object for this operation.
inMetaDataFormat
The metadata storage format used by the object
passed in
inMetaData
. The format
may be
UserData
storage, iTunes metadata storage,
or QuickTime metadata storage. Not all  objects will include all
forms of storage, and other storage formats may appear in the future.
You cannot pass
kQTMetaDataStorageFormatWildcard
to
target all storage formats.
inKeyFormat
The format of the key.
inKeyPtr
A pointer to the key of the item to be fetched
next. You may pass
NULL
in this
parameter if you are not interested in any specific key.
inKeySize
The size of the key in bytes.
inValuePtr
A pointer to the value to be added. This can
be
NULL
if
inValueSize
is
0.
inValueSize
The size of
inValuePtr
in
bytes. Pass 0 if you want to add an item with no value.
inDataType
A data type from the following list:
kQTMetaDataTypeBinary               = 0,
kQTMetaDataTypeUTF8                 = 1,
kQTMetaDataTypeUTF16BE              = 2,
kQTMetaDataTypeMacEncodedText       = 3,
kQTMetaDataTypeSignedIntegerBE      = 21,
kQTMetaDataTypeUnsignedIntegerBE    = 22,
kQTMetaDataTypeFloat32BE            = 23,
kQTMetaDataTypeFloat64BE            = 24
With
kQTMetaDataTypeSignedIntegerBE
and
kQTMetaDataTypeUnsignedIntegerBE
,
the size of the integer is determined by the value size.
outItem
On return, a pointer to an opaque, unique
UInt64
identifier
of the newly added item. Your application can use this to identify
the metadata item within a metadata object for other metadata functions.
You may pass
NULL
if
you are not interested in the identifier of the newly added item.
This identifier does not need to be disposed of.
```

##### Return Value

Returns `kQTMetaDataInvalidMetaDataErr` if
the metadata object or its reference is invalid, `kQTMetaDataInvalidStorageFormatErr` if
the metatada storage format is invalid, `kQTMetaDataInvalidKeyErr` if
the key or its format is invalid, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. See `[“Metadata Error Codes”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`.

```
Discussion
The data type of the metadata item is assumed to be binary.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the number of items in a metadata storage format
with a certain key.

```
OSStatus QTMetaDataGetItemCount (
QTMetaDataRef              inMetaData,
QTMetaDataStorageFormat    inMetaDataFormat,
QTMetaDataKeyFormat        inKeyFormat,
const UInt8                *inKeyPtr,
ByteCount                  inKeySize,
ItemCount                  *outCount);
```

```
Parameters
inMetaData
The metadata object for this operation.
inMetaDataFormat
The metadata storage format used by the object
passed in
inMetaData
. The format
may be
UserData
storage, iTunes metadata storage,
or QuickTime metadata storage. Not all  objects will include all
forms of storage, and other storage formats may appear in the future.
You cannot pass
kQTMetaDataStorageFormatWildcard
to
target all storage formats.
inKeyFormat
The format of the key.
inKeyPtr
A pointer to the key of the item to be fetched
next. You may pass
NULL
in this
parameter if you are not interested in any specific key.
inKeySize
The size of the key in bytes.
outCount
The number of items in the metadata storage
format that have the specified key.
```

##### Return Value

Returns `kQTMetaDataInvalidMetaDataErr` if
the metadata object or its reference is invalid, `kQTMetaDataInvalidStorageFormatErr` if
the metatada storage format is invalid, `kQTMetaDataInvalidKeyErr` if
the key or its format is invalid, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. See `[“Metadata Error Codes”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns a property of a metadata item.

```
OSStatus QTMetaDataGetItemProperty (
QTMetaDataRef         inMetaData,
QTMetaDataItem        inItem,
QTPropertyClass       inPropClass,
QTPropertyID          inPropID,
ByteCount             inPropValueSize,
QTPropertyValuePtr    outPropValueAddress,
ByteCount             *outPropValueSizeUsed );
```

```
Parameters
inMetaData
The metadata object for this operation.
inItem
The opaque, unique
UInt64
identifier
of the metadata item for this operation. Your application obtains
this item identifier from such functions as
QTMetaDataAddItem
and
QTMetaDataGetNextItem
.
inPropClass
The class of the property being asked about.
inPropID
The ID of the property being asked about.
inPropValueSize
Size of the buffer allocated to receive the
property value.
outPropValueAddress
A pointer to the buffer allocated to receive
the item’s property value.
outPropValueSizeUsed
On return, the actual size of buffer space
used.
```

##### Return Value

Returns `kQTMetaDataInvalidMetaDataErr` if
the metadata object or its reference is invalid, `kQTMetaDataInvalidItemErr` if
the metatada item ID is invalid, `errPropNotSupported` if
the metatada object does not support the property being asked about, `buffersTooSmall` if
the allocated buffer is too small to hold the property, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. See `[“Metadata Error Codes”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns information about a property of a metadata item.

```
OSStatus QTMetaDataGetItemPropertyInfo (
QTMetaDataRef          inMetaData,
QTMetaDataItem         inItem,
QTPropertyClass        inPropClass,
QTPropertyID           inPropID,
QTPropertyValueType    *outPropType,
ByteCount              *outPropValueSize,
UInt32                 *outPropFlags );
```

```
Parameters
inMetaData
The metadata object for this operation.
inItem
The opaque, unique
UInt64
identifier
of the metadata item for this operation. Your application obtains
this item identifier from such functions as
QTMetaDataAddItem
and
QTMetaDataGetNextItem
.
inPropClass
The class of the property being asked about.
inPropID
The ID of the property being asked about.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueSize
A pointer to the size of the returned property’s
value.
outPropFlags
On return, a pointer to flags representing
the requested information about the item’s property.
```

##### Return Value

Returns `kQTMetaDataInvalidMetaDataErr` if
the metadata object or its reference is invalid, `kQTMetaDataInvalidItemErr` if
the metatada item ID is invalid, `errPropNotSupported` if
the metatada object does not support the item property being asked
about, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if there is no error.
See `[“Metadata Error Codes”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the value of a metadata item from an item identifier.

```
OSStatus QTMetaDataGetItemValue (
QTMetaDataRef     inMetaData,
QTMetaDataItem    inItem,
UInt8             *outValuePtr,
ByteCount         inValueSize,
ByteCount         *outActualSize );
```

```
Parameters
inMetaData
The metadata object for this operation.
inItem
The opaque, unique
UInt64
identifier
of the metadata item for this operation. Your application can obtain
this item identifier from such functions as
QTMetaDataAddItem
.
outValuePtr
A pointer to the first value of the item.
You may pass
NULL
in
this parameter if you just want to find out the size of the buffer
needed.
inValueSize
The number of bytes in the
outValuePtr
buffer.
You may pass 0 if you just want to find out the size of the buffer
needed.
outActualSize
The actual size of the value if this parameter
is not
NULL
.
```

##### Return Value

Returns `kQTMetaDataInvalidMetaDataErr` if
the metadata object or its reference is invalid, `kQTMetaDataInvalidItemErr` if
the metatada item ID is invalid, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. See `[“Metadata Error Codes”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`.

```
Discussion
You can use this function to get the value of a metadata item
that has a known item identifier.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the next metadata item corresponding to a specified
key.

```
OSStatus QTMetaDataGetNextItem (
QTMetaDataRef              inMetaData,
QTMetaDataStorageFormat    inMetaDataFormat,
QTMetaDataItem             inCurrentItem,
QTMetaDataKeyFormat        inKeyFormat,
const UInt8                *inKeyPtr,
ByteCount                  inKeySize,
QTMetaDataItem             *outNextItem );
```

```
Parameters
inMetaData
The metadata object for this operation.
inMetaDataFormat
The metadata storage format used by the object
passed in
inMetaData
. The format
may be
UserData
storage, iTunes metadata storage,
or QuickTime metadata storage. Not all  objects will include all
forms of storage, and other storage formats may appear in the future.
Pass
kQTMetaDataStorageFormatWildcard
to
target all storage formats.
inCurrentItem
The opaque, unique
UInt64
identifier
of the current metadata item to start the search. Your application
obtains this item identifier from such functions as
QTMetaDataAddItem
.
inKeyFormat
The format of the key.
inKeyPtr
A pointer to the key of the item to be fetched
next. You may pass
NULL
in this
parameter if you are not interested in any specific key.
inKeySize
The size of the key in bytes.
outNextItem
The ID of the next metadata item after the
item specified by
inCurrentItem
that
has the specified key.
```

##### Return Value

Returns `kQTMetaDataInvalidMetaDataErr` if
the metadata object or its reference is invalid, `kQTMetaDataInvalidItemErr` if
the metatada item ID is invalid, `kQTMetaDataInvalidStorageFormatErr` if
the metatada storage format is invalid, `kQTMetaDataInvalidKeyErr` if
the key or its format is invalid, `kQTMetaDataNoMoreItemErr` if
the last item has been fetched, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. See `[“Metadata Error Codes”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`.

```
Discussion
If the item designated by
inCurrentItem
is
kQTMetaDataItemUninitialized
,
the function returns the first item with the specified key in the
storage format. If it refers to a valid item in the storage format,
the function will return the next item with the key after the item designated
by
inCurrentItem
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns a property of a metadata object.

```
OSStatus QTMetaDataGetProperty (
QTMetaDataRef         inMetaData,
QTPropertyClass       inPropClass,
QTPropertyID          inPropID,
ByteCount             inPropValueSize,
QTPropertyValuePtr    outPropValueAddress,
ByteCount             *outPropValueSizeUsed );
```

```
Parameters
inMetaData
The metadata object for this operation.
inPropClass
The class of the property being asked about.
inPropID
The ID of the property being asked about.
inPropValueSize
Size of the buffer allocated to receive the
property value.
outPropValueAddress
A pointer to the buffer allocated to receive
the property value.
outPropValueSizeUsed
On return, the actual size of buffer space
used.
```

##### Return Value

Returns `kQTMetaDataInvalidMetaDataErr` if
the metadata object or its reference is invalid, `errPropNotSupported` if
the metatada object does not support the property being asked about, `buffersTooSmall` if
the allocated buffer is too small to hold the property, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. See `[“Metadata Error Codes”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns information about a property of a metadata object.

```
OSStatus QTMetaDataGetPropertyInfo (
QTMetaDataRef          inMetaData,
QTPropertyClass        inPropClass,
QTPropertyID           inPropID,
QTPropertyValueType    *outPropType,
ByteCount              *outPropValueSize,
UInt32                 *outPropFlags );
```

```
Parameters
inMetaData
The metadata object for this operation.
inPropClass
The class of the property being asked about.
inPropID
The ID of the property being asked about.
outPropType
A pointer to the type of the returned property’s
value.
outPropValueSize
A pointer to the size of the returned property’s
value.
outPropFlags
On return, a pointer to flags representing
the requested information about the property.
```

##### Return Value

Returns `kQTMetaDataInvalidMetaDataErr` if
the metadata object or its reference is invalid, `errPropNotSupported` if
the metatada object does not support the property being asked about,
or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if there is no error. See `[“Metadata Error Codes”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Increments the retain count of a metadata object.

```
QTMetaDataRef QTMetaDataRetain ( QTMetaDataRef inMetaData );
```

```
Parameters
inMetaData
A metadata object that you want to retain.
```

##### Return Value

If successful, returns
a metadata object that is the same as that passed in _inMetaData_.

```
Discussion
This function retains a metadata object by incrementing its
reference count. You should retain every metadata object when you
receive it from elsewhere and you want it to persist. If you retain
a metadata object you are responsible for releasing it by calling
QTMetaDataRelease
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Decrements the retain count of a metadata object.

```
void QTMetaDataRelease ( QTMetaDataRef inMetaData );
```

```
Discussion
This function releases a metadata object by decrementing its
reference count. When the count becomes 0 the memory allocated to
the object is freed and the object is destroyed. If you retain a
metadata object you are responsible for releasing it when you no
longer need it.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Removes a metadata item from a storage format.

```
OSStatus QTMetaDataRemoveItem (
QTMetaDataRef     inMetaData,
QTMetaDataItem    inItem );
```

```
Parameters
inMetaData
The metadata object for this operation.
inItem
The opaque, unique
UInt64
identifier
of the metadata item for this operation. Your application obtains
this item identifier from such functions as
QTMetaDataAddItem
and
QTMetaDataGetNextItem
.
```

##### Return Value

Returns `kQTMetaDataInvalidMetaDataErr` if
the metadata object or its reference is invalid, `kQTMetaDataInvalidItemErr` if
the metatada item ID is invalid, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. See `[“Metadata Error Codes”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Removes metadata items with a specific key from the storage
format.

```
OSStatus QTMetaDataRemoveItemsWithKey (
QTMetaDataRef              inMetaData,
QTMetaDataStorageFormat    inMetaDataFormat,
QTMetaDataKeyFormat        inKeyFormat,
const UInt8                *inKeyPtr,
ByteCount                  inKeySize);
```

```
Parameters
inMetaData
The metadata object for this operation.
inMetaDataFormat
The metadata storage format used by the object
passed in
inMetaData
. The format
may be
UserData
storage, iTunes metadata storage,
or QuickTime metadata storage. Not all  objects will include all
forms of storage, and other storage formats may appear in the future.
You can pass
kQTMetaDataStorageFormatWildcard
to
target all storage formats.
inKeyFormat
The format of the key.
inKeyPtr
A pointer to the key of the item to be removed.
You may pass
NULL
in
this parameter if you want to remove all items.
inKeySize
The size of the key in bytes.
```

##### Return Value

Returns `kQTMetaDataInvalidMetaDataErr` if
the metadata object or its reference is invalid, `kQTMetaDataInvalidStorageFormatErr` if
the metatada storage format is invalid, `kQTMetaDataInvalidKeyErr` if
the key or its format is invalid, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. See `[“Metadata Error Codes”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets the value of the metadata item from the item identifier.

```
OSStatus QTMetaDataSetItem (
QTMetaDataRef     inMetaData,
QTMetaDataItem    inItem,
UInt8             *inValuePtr,
ByteCount         inValueSize,
UInt32            inDataType);
```

```
Parameters
inMetaData
The metadata object for this operation.
inItem
The opaque, unique
UInt64
identifier
of the metadata item for this operation. Your application obtains
this item identifier from such functions as
QTMetaDataAddItem
and
QTMetaDataGetNextItem
.
inValuePtr
A pointer to the value to be set. This can
be
NULL
if
inValueSize
is
0.
inValueSize
The size of
inValuePtr
in
bytes. Pass 0 if you want to set an item with no value.
inDataType
A data type from the following list:
kQTMetaDataTypeBinary               = 0,
kQTMetaDataTypeUTF8                 = 1,
kQTMetaDataTypeUTF16BE              = 2,
kQTMetaDataTypeMacEncodedText       = 3,
kQTMetaDataTypeSignedIntegerBE      = 21,
kQTMetaDataTypeUnsignedIntegerBE    = 22,
kQTMetaDataTypeFloat32BE            = 23,
kQTMetaDataTypeFloat64BE            = 24
With kQTMetaDataTypeSignedIntegerBE
and kQTMetaDataTypeUnsignedIntegerBE, the size of the integer is determined
by the value size.
```

##### Return Value

Returns `kQTMetaDataInvalidMetaDataErr` if
the metadata object or its reference is invalid, `kQTMetaDataInvalidItemErr` if
the metatada item ID is invalid, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. See `[“Metadata Error Codes”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`.

```
Discussion
You can use this function to set the value of the metadata
item with a given item identifier. You can set an item with an empty
value by passing 0 in
inValueSize
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets a property of a metadata item.

```
OSStatus QTMetaDataSetItemProperty (
QTMetaDataRef              inMetaData,
QTMetaDataItem             inItem,
QTPropertyClass            inPropClass,
QTPropertyID               inPropID,
ByteCount                  inPropValueSize,
ConstQTPropertyValuePtr    inPropValueAddress );
```

```
Parameters
inMetaData
The metadata object for this operation.
inItem
The opaque, unique
UInt64
identifier
of the metadata item for this operation. Your application obtains
this item identifier from such functions as
QTMetaDataAddItem
and
QTMetaDataGetNextItem
.
inPropClass
The class of the property being set.
inPropID
The ID of the property being set.
inPropValueSize
Size of the buffer containing the property
value being set.
inPropValueAddress
A pointer to the buffer containing the item
property value being set.
```

##### Return Value

Returns `kQTMetaDataInvalidMetaDataErr` if
the metadata object or its reference is invalid, `kQTMetaDataInvalidItemErr` if
the metatada item ID is invalid, `errPropNotSupported` if
the metatada object does not support the property being set, `qtReadOnlyErr` if
the property being set is read-only, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. See `[“Metadata Error Codes”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets a property of a metadata object.

```
OSStatus QTMetaDataSetProperty (
QTMetaDataRef              inMetaData,
QTPropertyClass            inPropClass,
QTPropertyID               inPropID,
ByteCount                  inPropValueSize,
ConstQTPropertyValuePtr    inPropValueAddress);
```

```
Parameters
inMetaData
The metadata object for this operation.
inPropClass
The class of the property being set.
inPropID
The ID of the property being set.
inPropValueSize
Size of the buffer containing the property
value being set.
inPropValueAddress
A pointer to the buffer containing the property
value being set.
```

##### Return Value

Returns `kQTMetaDataInvalidMetaDataErr` if
the metadata object or its reference is invalid, `errPropNotSupported` if
the metatada object does not support the property being set, `qtReadOnlyErr` if
the property being set is read-only, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. See `[“Metadata Error Codes”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvheyds)`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Creates a new OpenGL texture context for a specified OpenGL
context and pixel format.

```
OSStatus QTOpenGLTextureContextCreate (
   CFAllocatorRef               allocator,
   CGLContextObj                cglContext,
   CGLPixelFormatObj            cglPixelFormat,
   CFDictionaryRef              attributes,
   QTOpenGLTextureContextRef    *newTextureContext );
```

```
Parameters
allocator
The allocator used to create the texture context.
cglContext
A pointer to an opaque
CGLPContextObj
structure
representing the OpenGL context used to create textures. You can
create this structure using
CGLCreateContext
.
cglPixelFormat
The pixel format object that specifies buffer
types and other attributes of the new context.
attributes
A dictionary of attributes.
newTextureContext
A pointer to a variable to receive the new
OpenGL texture context.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Creates a new pixel buffer context with the given attributes.

```
OSStatus QTPixelBufferContextCreate (
   CFAllocatorRef allocator,
   CFDictionaryRef attributes,
   QTVisualContextRef *newPixelBufferContext );
```

```
Parameters
allocator
Allocator used to create the pixel buffer
context.
attributes
Dictionary of attributes.
newPixelBufferContext
Points to a variable to receive the new pixel
buffer context.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This routine creates a new pixel buffer context with the given
attributes.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Removes a track property monitoring callback

```
OSErr QTRemoveTrackPropertyListener (
   Track inTrack,
   QTPropertyClass inPropClass,
   QTPropertyID inPropID,
   QTTrackPropertyListenerUPP inListenerProc,
   void *inUserData );
```

```
Parameters
inTrack
The track for this operation.
inPropClass
A property class.
inPropID
A property ID.
inListenerProc
A Universal Procedure Pointer to a QTTrackPropertyListenerProc callback.
inUserData
User data to be passed to the callback.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This routine removes a track property monitoring callback.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Adds a sample description to a sample table, returning
a sample description ID that can be used to refer to it.

```
OSStatus QTSampleTableAddSampleDescription (
   QTMutableSampleTableRef    sampleTable,
   SampleDescriptionHandle    sampleDescriptionH,
   long                       mediaSampleDescriptionIndex,
   QTSampleDescriptionID      *sampleDescriptionIDOut );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
sampleDescriptionH
A handle to a
SampleDescription
structure.
QuickTime will make its own copy of this handle.
mediaSampleDescriptionIndex
The sample description index of this sample
description in a media. Pass 0 for sample descriptions you add to
sample tables, to indicate that this was not retrieved from a media.
sampleDescriptionIDOut
A pointer to a variable to receive a sample
description ID.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
You can use the returned sample description ID when adding
samples to the sample table.
```

```
Special Considerations
Sample description IDs are local to each sample table. The
same sample description handle may have different IDs when referenced
in different sample tables.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Adds sample references to a sample table.

```
OSStatus QTSampleTableAddSampleReferences (
   QTMutableSampleTableRef    sampleTable,
   SInt64                     dataOffset,
   ByteCount                  dataSizePerSample,
   TimeValue64                decodeDurationPerSample,
   TimeValue64                displayOffset,
   SInt64                     numberOfSamples,
   MediaSampleFlags           sampleFlags,
   QTSampleDescriptionID      sampleDescriptionID,
   SInt64                     *newSampleNumOut );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
dataOffset
A 64-bit signed integer that specifies the
offset at which the first sample begins.
dataSizePerSample
The number of bytes of data per sample. You
must pass the data size per sample, not the total size of all the
samples as with some other APIs.
decodeDurationPerSample
A 64-bit time value that specifies the decode
duration of each sample.
displayOffset
A 64-bit time value that specifies the offset
from decode time to display time of each sample. If the decode times
and display times are the same, pass 0.
numberOfSamples
A 64-bit signed integer, which must be greater
than 0, that specifies the number of samples.
sampleFlags
Flags that indicate the
sync
status
of all samples:
mediaSampleNotSync
If set to 1, indicates that the sample to be added is
not a sync sample. Set this flag to 0 if the sample is a sync sample.
mediaSampleShadowSync
If set to 1, the sample is a shadow sync sample.
sampleDescriptionID
The ID of a sample description that has been
added to the sample table with
QTSampleTableAddSampleDescription
.
newSampleNumOut
A 64-bit signed integer that points to a variable
to receive the sample number of the first sample that was added.
Pass
NULL
if you don't
want this information.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Retrieves a sample description from a sample table.

```
OSStatus QTSampleTableCopySampleDescription (
   QTSampleTableRef           sampleTable,
   QTSampleDescriptionID      sampleDescriptionID,
   long                       *mediaSampleDescriptionIndexOut,
   SampleDescriptionHandle    *sampleDescriptionHOut );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
sampleDescriptionID
The sample description ID.
mediaSampleDescriptionIndexOut
A pointer to a variable to receive a media
sample description index. If the sample description came from a
media, this is the index that could be passed to
GetMediaSampleDescription
to
retrieve the same sample description handle. The index will be 0
if the sample description did not come directly from a media. Pass
NULL
if
you do not want to receive this information.
sampleDescriptionHOut
A pointer to a variable to receive a newly
allocated sample description handle. Pass
NULL
if
you do not want one. The caller is responsible for disposing the
returned sample description handle using
DisposeHandle
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Creates a new, empty sample table.

```
OSStatus QTSampleTableCreateMutable (
   CFAllocatorRef             allocator,
   TimeScale                  timescale,
   void                       *hints,
   QTMutableSampleTableRef    *newSampleTable );
```

```
Parameters
allocator
The allocator to use for the new sample table.
timescale
A long integer that represents the timescale
to use for durations and display offsets.
hints
Reserved; pass
NULL
.
newSampleTable
A pointer to a variable that receives a new
reference to an opaque sample table object.
```

##### Return Value

An error code. Returns `memFullErr` if
it could not allocate memory, `paramErr` if
the time scale is not positive or _newSampleTable_ is `NULL`,
or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if there is no error.

```
Discussion
The newly created sample table contains no sample references.
When sample references are added, their durations and display offsets
are interpreted according to the sample table’s current timescale.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Copies a sample table.

```
OSStatus QTSampleTableCreateMutableCopy (
   CFAllocatorRef             allocator,
   QTSampleTableRef           sampleTable,
   void                       *hints,
   QTMutableSampleTableRef    *newSampleTable );
```

```
Parameters
allocator
The allocator to use for the new sample table.
sampleTable
A reference to an opaque sample table object
to copy.
hints
Reserved; set to
NULL
.
newSampleTable
A pointer to a variable that receives a reference
to an opaque sample table object.
```

##### Return Value

An error code. Returns `memFullErr` if
it could not allocate memory, `paramErr` if
the time scale is not positive or _newSampleTable_ is `NULL`,
or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if there is no error.

```
Discussion
All the sample references and sample descriptions in the sample
table are copied.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the data offset of a sample.

```
SInt64 QTSampleTableGetDataOffset (
   QTSampleTableRef    sampleTable,
   SInt64              sampleNum );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
sampleNum
A 64-bit signed integer that represents a
sample number. The first sample’s number is 1.
```

##### Return Value

A 64-bit signed integer
that represents the offset to the sample. Returns 0 if _sampleTable_ is `NULL` or
if the sample number is out of range.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the data size of a sample.

```
ByteCount QTSampleTableGetDataSizePerSample (
   QTSampleTableRef    sampleTable,
   SInt64              sampleNum );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
sampleNum
A 64-bit signed integer that represents the
sample number. The first sample’s number is 1.
```

##### Return Value

The size of the sample
in bytes. Returns 0 if _samplTable_ is `NULL` or
if the sample number is out of range.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the decode duration of a sample.

```
TimeValue64 QTSampleTableGetDecodeDuration (
   QTSampleTableRef    sampleTable,
   SInt64              sampleNum );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
sampleNum
A 64-bit signed integer that represents the
sample number. The first sample’s number is 1.
```

##### Return Value

A 64-bit time value
that represents the decode duration of the sample. Returns 0 if _samplTable_ is `NULL` or
if the sample number is out of range.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the offset from decode time to display time of
a sample.

```
TimeValue64 QTSampleTableGetDisplayOffset (
   QTSampleTableRef    sampleTable,
   SInt64              sampleNum );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
sampleNum
A 64-bit signed integer that represents the
sample number. The first sample’s number is 1.
```

##### Return Value

A 64-bit time value
that represents the offset from decode time to display time of the
sample. Returns 0 if _samplTable_ is `NULL` or
if the sample number is out of range.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Finds the next sample number at which one or more of a
set of given sample attributes change.

```
OSStatus QTSampleTableGetNextAttributeChange (
   QTSampleTableRef          sampleTable,
   SInt64                    startSampleNum,
   QTSampleTableAttribute    attributeMask,
   SInt64                    *sampleNumOut );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
startSampleNum
A 64-bit signed integer that contains the
sample number to start searching from.
attributeMask
An unsigned 32-bit integer that contains flags
indicating which kinds of attribute changes to search for:
kQTSampleTableAttribute_DiscontiguousData
= 1L << 0
Set this flag to find the first sample number
num
such
that samples
num-1
and
num
are
not adjacent; that is,
dataOffset
of
num-1
+ dataSize
of
num-1 !=
dataOffset
of
num
.
kQTSampleTableAttribute_DataSizePerSampleChange
= 1L << 1
Set this flag to find the first sample with data size
per sample different from that of the starting sample.
kQTSampleTableAttribute_DecodeDurationChange
= 1L << 2
Set this flag to find the first sample with decode
duration different from that of the starting sample.
kQTSampleTableAttribute_DisplayOffsetChange
= 1L << 3
Set this flag to find the first sample with display
offset different from that of the starting sample.
kQTSampleTableAttribute_SampleDescriptionIDChange
= 1L << 4
Set this flag to find the first sample with sample
description ID different from that of the starting sample.
kQTSampleTableAttribute_SampleFlagsChange
= 1L << 5
Set this flag to find the first sample with any media
sample flags different from those of the starting sample.
kQTSampleTableAnyAttributeChange
= 0
If no flags are set, find the first sample with any
attribute different from the starting sample.
sampleNumOut
A 64-bit signed integer that points to a variable
to receive the next sample number after
startSampleNum
at
which any of the requested attributes change. If no attribute changes
are found, this variable is set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the number of samples in a sample table.

```
SInt64 QTSampleTableGetNumberOfSamples (
   QTSampleTableRef    sampleTable );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
```

##### Return Value

A 64-bit signed integer
that contains the number of samples, or 0 if _sampleTable_ is `NULL`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the value of a specific sample table property.

```
OSStatus QTSampleTableGetProperty (
   QTSampleTableRef      sampleTable,
   QTPropertyClass       inPropClass,
   QTPropertyID          inPropID,
   ByteCount             inPropValueSize,
   QTPropertyValuePtr    outPropValueAddress,
   ByteCount             *outPropValueSizeUsed );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
inPropClass
Pass the following constant to define the
property class:
kQTPropertyClass_SampleTable
= 'qtst'
Property of a sample table.
inPropID
Pass one of these constants to define the
property ID:
kQTSampleTablePropertyID_TotalDecodeDuration
= 'tded'
The total decode duration of all samples in the sample
table. Read-only.
kQTSampleTablePropertyID_MinDisplayOffset
= '<ddd'
The least display offset in the table. Negative offsets
are less than positive offsets. Read-only.
kQTSampleTablePropertyID_MaxDisplayOffset
= '>ddd'
The greatest display offset in the table. Positive
offsets are greater than negative offsets. Read-only.
kQTSampleTablePropertyID_MinRelativeDisplayTime
= '<dis'
The least display time of all samples in the table,
relative to the decode time of the first sample in the table. Read-only.
kQTSampleTablePropertyID_MaxRelativeDisplayTime
= '>dis'
The greatest display time of all samples in the table,
relative to the decode time of the first sample in the table. Read-only.
inPropValueSize
The size of the buffer allocated to receive
the property value.
outPropValueAddress
A pointer to the buffer allocated to receive
the property value.
outPropValueSizeUsed
On return, the actual size of the property
value written to the buffer.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns information about the properties of a sample table.

```
OSStatus QTSampleTableGetPropertyInfo (
   QTSampleTableRef       sampleTable,
   QTPropertyClass        inPropClass,
   QTPropertyID           inPropID,
   QTPropertyValueType    *outPropType,
   ByteCount              *outPropValueSize,
   UInt32                 *outPropertyFlags );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
inPropClass
Pass the following constant to define the
property class:
kQTPropertyClass_SampleTable
= 'qtst'
Property of a sample table.
inPropID
Pass one of these constants to define the
property ID:
kQTSampleTablePropertyID_TotalDecodeDuration
= 'tded'
The total decode duration of all samples in the sample
table. Read-only.
kQTSampleTablePropertyID_MinDisplayOffset
= '<ddd'
The least display offset in the table. Negative offsets
are less than positive offsets. Read-only.
kQTSampleTablePropertyID_MaxDisplayOffset
= '>ddd'
The greatest display offset in the table. Positive
offsets are greater than negative offsets. Read-only.
kQTSampleTablePropertyID_MinRelativeDisplayTime
= '<dis'
The least display time of all samples in the table,
relative to the decode time of the first sample in the table. Read-only.
kQTSampleTablePropertyID_MaxRelativeDisplayTime
= '>dis'
The greatest display time of all samples in the table,
relative to the decode time of the first sample in the table. Read-only.
outPropType
A pointer to memory allocated to hold the
property type on return: Pass
NULL
if
you do not want this information.
outPropValueSize
A pointer to memory allocated to hold the
size of the property value on return. Pass
NULL
if
you do not want this information.
outPropertyFlags
A pointer to memory allocated to hold property
flags on return. Pass
NULL
if
you do not want this information.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the sample description ID of a sample.

```
QTSampleDescriptionID QTSampleTableGetSampleDescriptionID (
   QTSampleTableRef    sampleTable,
   SInt64              sampleNum );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
sampleNum
A 64-bit signed integer that represents the
sample number. The first sample’s number is 1.
```

##### Return Value

The sample’s sample
description ID. Returns 0 if _samplTable_ is `NULL` or if
the sample number is out of range.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the media sample flags of a sample.

```
MediaSampleFlags QTSampleTableGetSampleFlags (
   QTSampleTableRef    sampleTable,
   SInt64              sampleNum );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
sampleNum
A 64-bit signed integer that represents the
sample number. The first sample’s number is 1.
```

##### Return Value

A constant that describes
characteristics of the sample (see below). Returns 0 if _samplTable_ is `NULL` or
if the sample number is out of range.

```
Discussion
This function can return one or more of the following constants:
mediaSampleNotSync
Sample is not a sync sample (for example, it is is frame
differenced).
mediaSampleShadowSync
Sample is a shadow sync sample.
mediaSampleDroppable
Sample does not need to be decoded for later samples
to be decoded properly.
mediaSamplePartialSync
Sample is a partial sync sample (for example, 1 frame
after open GOP).
mediaSampleHasRedundantCoding
Sample is known to contain redundant coding.
mediaSampleHasNoRedundantCoding
Sample is known not to contain redundant coding.
mediaSampleIsDependedOnByOthers
One or more other samples depend on this sample being
decoded.
mediaSampleIsNotDependedOnByOthers
Synonym for
mediaSampleDroppable
.
mediaSampleDependsOnOthers
Decoding this sample depends on decoding other samples.
mediaSampleDoesNotDependOnOthers
Decoding this sample does not depend on decoding other
samples.
mediaSampleEarlierDisplayTimesAllowed
Samples later in decode order may have earlier display
times.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the timescale of a sample table.

```
TimeScale QTSampleTableGetTimeScale (
   QTSampleTableRef    sampleTable );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
```

##### Return Value

A long integer that
represents the sample’s time scale, or 0 if _sampleTable_ is `NULL`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Returns the `CFTypeID` value
for the current sample table.

```
CFTypeID QTSampleTableGetTypeID ( void );
```

##### Return Value

A `CFTypeID` value.

```
Discussion
You could use this to test whether a
CFTypeRef
that
was extracted from a CF container such as a
CFArray
is
a
QTSampleTableRef
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Decrements the retain count of a sample table.

```
void QTSampleTableRelease (
   QTSampleTableRef    sampleTable );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
If you pass
NULL
in this parameter,
nothing happens.
```

```
Discussion
If the retain count decreases to zero, the sample table is
disposed.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Replaces a range of samples in a sample table with a range
of samples from another sample table.

```
OSStatus QTSampleTableReplaceRange (
   QTMutableSampleTableRef    destSampleTable,
   SInt64                     destStartingSampleNum,
   SInt64                     destSampleCount,
   QTSampleTableRef           sourceSampleTable,
   SInt64                     sourceStartingSampleNum,
   SInt64                     sourceSampleCount );
```

```
Parameters
destSampleTable
A reference to an opaque sample table object
to be modified.
destStartingSampleNum
A 64-bit signed integer that represents the
first sample number in
destSampleTable
to
be replaced or deleted, or the sample number at which samples should
be inserted.
destSampleCount
A 64-bit signed integer that represents the
number of samples to be removed from
destSampleTable
.
Pass 0 to insert samples without removing samples.
sourceSampleTable
A reference to an opaque sample table object
from which samples should be copied, or
NULL
to
delete samples.
sourceStartingSampleNum
A 64-bit signed integer that represents the
first sample number to be copied. This parameter is ignored when
deleting samples.
sourceSampleCount
A 64-bit signed integer that represents the
number of samples which should be copied. Pass 0 to delete samples.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This function removes
destSampleCount
samples
from
destSampleTable
starting with
destStartingSampleNum
,
and then inserts
sourceSampleCount
samples
from
sourceSampleTable
starting with
sourceStartingSampleNum
where
the removed samples were. Sample descriptions will be copied if
necessary and new sample description IDs defined. This function
can also be used to delete a range of samples, or to insert samples without
removing any.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Increments the retain count of a sample table.

```
QTSampleTableRef QTSampleTableRetain (
   QTSampleTableRef    sampleTable );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
If you pass
NULL
in this parameter,
nothing happens.
```

##### Return Value

A pointer to the `OpaqueQTSampleTable` structure
that is returned for your convenience, or `NULL` if
the function fails.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets the value of a specific sample table property.

```
OSStatus QTSampleTableSetProperty (
   QTSampleTableRef           sampleTable,
   QTPropertyClass            inPropClass,
   QTPropertyID               inPropID,
   ByteCount                  inPropValueSize,
   ConstQTPropertyValuePtr    inPropValueAddress );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
inPropClass
Pass the following constant to define the
property class:
kQTPropertyClass_SampleTable
= 'qtst'
Property of a sample table.
inPropID
Pass one of these constants to define the
property ID:
kQTSampleTablePropertyID_TotalDecodeDuration
= 'tded'
The total decode duration of all samples in the sample
table. Read-only.
kQTSampleTablePropertyID_MinDisplayOffset
= '<ddd'
The least display offset in the table. Negative offsets
are less than positive offsets. Read-only.
kQTSampleTablePropertyID_MaxDisplayOffset
= '>ddd'
The greatest display offset in the table. Positive
offsets are greater than negative offsets. Read-only.
kQTSampleTablePropertyID_MinRelativeDisplayTime
= '<dis'
The least display time of all samples in the table,
relative to the decode time of the first sample in the table. Read-only.
kQTSampleTablePropertyID_MaxRelativeDisplayTime
= '>dis'
The greatest display time of all samples in the table,
relative to the decode time of the first sample in the table. Read-only.
inPropValueSize
Pass the size of the property value.
inPropValueAddress
Pass a
const void
pointer
to the property value.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Changes the timescale of a sample table.

```
OSStatus QTSampleTableSetTimeScale (
   QTMutableSampleTableRef    sampleTable,
   TimeScale                  newTimeScale );
```

```
Parameters
sampleTable
A reference to an opaque sample table object.
newTimeScale
A long integer whose value is the time scale
to be set.
```

##### Return Value

An error code. Returns `paramErr` if
the time scale is not positive or _sampleTable_ is `NULL`,
or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if there is no error.

```
Discussion
The durations and display offsets of all the sample references
in the sample table are scaled from the old timescale to the new
timescale. No durations are scaled to a value less than 1. Display
offsets are adjusted to avoid display time collisions.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets the value of a specific track property.

```
OSErr QTSetTrackProperty (
   Track inTrack,
   QTPropertyClass inPropClass,
   QTPropertyID inPropID,
   ByteCount inPropValueSize,
   ConstQTPropertyValuePtr inPropValueAddress );
```

```
Parameters
inTrack
The track for this operation.
inPropClass
A property class.
inPropID
A property ID.
inPropValueSize
The size of the property value.
inPropValueAddress
A pointer to the the property value.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This routine sets the value of a specific track property.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Converts a sound description from one version to another.

```
OSStatus QTSoundDescriptionConvert (
QTSoundDescriptionKind    fromKind,
SoundDescriptionHandle    fromDescription,
QTSoundDescriptionKind    toKind,
SoundDescriptionHandle    *toDescription );
```

```
Parameters
fromKind
Reserved. Set to
kSoundDescriptionKind_Movie_AnyVersion
.
fromDescription
A handle to the sound description to be converted.
toKind
The version you want
fromDescription
to
be.
toDescription
A reference to the resulting
SoundDescription
structure.
 You must dispose of the reference using
DisposeHandle
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The
fromKind
parameter is reserved
for future expansion; at present you must set it to
kSoundDescriptionKind_Movie_AnyVersion
.
Depending on the value you pass in
toKind
, you
can specify that you would like a specific
SoundDescription
version,
the lowest possible version (given the constraints of the format
described by
fromDescription
), or any
version at all.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Creates a sound description structure of the requested
kind from an `AudioStreamBasicDescription`,
optional audio channel layout, and optional magic cookie.

```
OSStatus QTSoundDescriptionCreate (
AudioStreamBasicDescription    *inASBD,
AudioChannelLayout             *inLayout,
ByteCount                      inLayoutSize,
void                           *inMagicCookie
ByteCount                      inMagicCookieSize
QTSoundDescriptionKind         inRequestedKind
SoundDescriptionHandle         *outSoundDesc );
```

```
Parameters
inASBD
A description of the format.
inLayout
The audio channel layout (can be
NULL
if
there isn’t one).
inLayoutSize
The size of the audio channel layout (should
be 0 if
inLayout
is
NULL
).
inMagicCookie
The magic cookie for the decompressor (can
be
NULL
if the decompressor doesn’t
require one).
inMagicCookieSize
The size of the magic cookie (should be 0
if the
inMagicCookie
parameter is
NULL
).
inRequestedKind
The kind of sound description to create.
outSoundDesc
The resulting sound description. The caller
must dispose of it with
DisposeHandle
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Gets information about a particular property of a sound
description.

```
OSStatus QTSoundDescriptionGetPropertyInfo (
SoundDescriptionHandle     inDesc,
QTPropertyClass            inPropClass,
QTPropertyID               inPropID,
QTPropertyValueType        *outPropType,
ByteCount                  *outPropValueSize,
UInt32                      *outPropertyFlags);
```

```
Parameters
inDesc
The sound description being interrogated.
inPropClass
The class of the property being requested.
inPropID
The ID of the property being requested.
outPropType
The type of the property returned here (can
be
NULL
).
outPropValueSize
The size of the property  returned here (can
be
NULL
).
outPropertyFlags
The property flags returned here (can be
NULL
).
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The following constants identify sound description properties.
enum {
kQTSoundDescriptionPropertyID_AudioChannelLayout = 'clay',
kQTSoundDescriptionPropertyID_MagicCookie = 'kuki',
kQTSoundDescriptionPropertyID_AudioStreamBasicDescription = 'asbd',
kQTSoundDescriptionPropertyID_UserReadableText = 'text'
};
```

```
Special Considerations
kQTSoundDescriptionPropertyID_AudioChannelLayout
= 'clay'
Used to get or set an
AudioChannelLayout
value.
This is a variable-size property because it may contain an array
of Channel Descriptions.  You must get the size by calling
QTSoundDescriptionGetPropertyInfo
,
allocate a structure of that size, and then get the property.
kQTSoundDescriptionPropertyID_MagicCookie
= 'kuki'
Used to get or set opaque bytes. This is a variable-size
property, because it is completely defined by the codec that uses
the cookie. You must get the size by calling
QTSoundDescriptionGetPropertyInfo
,
allocate a structure of that size, and then get the property.
kQTSoundDescriptionPropertyID_AudioStreamBasicDescription
= 'asbd'
Used to get an
AudioStreamBasicDescription
value.
kQTSoundDescriptionPropertyID_UserReadableText
= 'text'
Used to get a
CFStringRef
value.
QTSoundDescriptionGetProperty
does
a
CFRetain
of the returned
CFString
on
behalf of the caller, so the caller is responsible for calling
CFRelease
on
the returned
CFString
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Gets a particular property of a sound description.

```
OSStatus QTSoundDescriptionGetProperty (
SoundDescriptionHandle     inDesc,
QTPropertyClass            inPropClass,
QTPropertyID               inPropID,
ByteCount                  inPropValueSize,
QTPropertyValuePtr         outPropValueAddress,
ByteCount                  *outPropValueSizeUsed);
```

```
Parameters
inDesc
The sound description being interrogated.
inPropClass
The class of the property being requested.
inPropID
The ID of the property being requested.
inPropValueSize
The size of the property value buffer.
outPropValueAddress
A pointer to the property value buffer.
outPropValueSizeUsed
The actual size of the returned property value
(can be
NULL
).
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The following constants identify sound description properties.
enum {
kQTSoundDescriptionPropertyID_AudioChannelLayout = 'clay',
kQTSoundDescriptionPropertyID_MagicCookie = 'kuki',
kQTSoundDescriptionPropertyID_AudioStreamBasicDescription = 'asbd',
kQTSoundDescriptionPropertyID_UserReadableText = 'text'
};
```

```
Special Considerations
kQTSoundDescriptionPropertyID_AudioChannelLayout
= 'clay'
Used to get or set an
AudioChannelLayout
value.
This is a variable-size property because it may contain an array
of Channel Descriptions.  You must get the size by calling
QTSoundDescriptionGetPropertyInfo
,
allocate a structure of that size, and then get the property.
kQTSoundDescriptionPropertyID_MagicCookie
= 'kuki'
Used to get or set opaque bytes. This is a variable-size
property, because it is completely defined by the codec that uses
the cookie. You must get the size by calling
QTSoundDescriptionGetPropertyInfo
,
allocate a structure of that size, and then get the property.
kQTSoundDescriptionPropertyID_AudioStreamBasicDescription
= 'asbd'
Used to get an
AudioStreamBasicDescription
value.
kQTSoundDescriptionPropertyID_UserReadableText
= 'text'
Used to get a
CFStringRef
value.
QTSoundDescriptionGetProperty
does
a
CFRetain
of the returned
CFString
on
behalf of the caller, so the caller is responsible for calling
CFRelease
on
the returned
CFString
.
kQTAudioPropertyID_FormatString
= 'fstr'
Used with
kQTPropertyClass_Audio
to
get a
CFStringRef
value containing a localized,
human readable string that describes an audio format; for example,
“MPEG Layer 3.” You may get this property from a
SoundDescription
handle
by calling
QTSoundDescriptionGetProperty
or from
a
StandardAudioCompression
(
scdi
or
audi
)
component instance by calling
QTGetComponentProperty
.
kQTAudioPropertyID_ChannelLayoutString
= 'lstr'
Used with
kQTPropertyClass_Audio
to
get a
CFStringRef
value containing a localized,
human readable string that describes an audio channel layout; for
example, “5.0 (L R C Ls Rs).” You may get this property from
a
SoundDescription
handle by calling
QTSoundDescriptionGetProperty
or
from a
StandardAudioCompression
(
scdi
or
audi
)
component instance by calling
QTGetComponentProperty
.
kQTAudioPropertyID_SampleRateString
= 'rstr'
Used to get a
CFStringRef
value
containing a localized, human readable string that describes an
audio sample rate; for example, “44.100 kHz.” You may get this
property from a
SoundDescription
handle by
calling
QTSoundDescriptionGetProperty
or
from a
StandardAudioCompression
(
scdi
or
audi
)
component instance by calling
QTGetComponentProperty
.
kQTAudioPropertyID_SampleSizeString
= 'sstr'
Used to get a
CFStringRef
value
containing a localized, human readable string that describes an
audio sample size; for example, “24-bit.” This property will
return a valid string only if the audio format is uncompressed (LPCM).
You may get this property from a
SoundDescription
handle
by calling
QTSoundDescriptionGetProperty
or
from a
StandardAudioCompression
(
scdi
or
audi
)
component instance by calling
QTGetComponentProperty
.
kQTAudioPropertyID_BitRateString
= 'bstr'
Used to get a
CFStringRef
value
containing a localized, human readable string that describes an
audio bit rate; for example, “12 kbps.” You may get this property
from a
StandardAudioCompression
(
scdi
or
audi
) component
instance by calling
QTGetComponentProperty
.
kQTAudioPropertyID_SummaryString
= 'asum'
Used to get a
CFStringRef
value
containing a localized, human readable string that summarizes an
audio format; for example, “16-bit Integer (Big Endian), Stereo
(L R), 48.000 kHz.” You may get this property from a
SoundDescription
handle
by calling
QTSoundDescriptionGetProperty
or from
a
StandardAudioCompression
(
scdi
or
audi
)
component instance by calling
QTGetComponentProperty
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets a particular property of a sound description.

```
OSStatus QTSoundDescriptionSetProperty (
SoundDescriptionHandle     inDesc,
QTPropertyClass            inPropClass,
QTPropertyID               inPropID,
ByteCount                  inPropValueSize,
ConstQTPropertyValuePtr   inPropValueAddress );
```

```
Parameters
inDesc
The sound description being modified.
inPropClass
The class of the property being set.
inPropID
The ID of the property being set.
inPropValueSize
The size of the property value buffer.
inPropValueAddress
A pointer to the property value buffer.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The following constants identify sound description properties.
enum {
kQTSoundDescriptionPropertyID_AudioChannelLayout = 'clay',
kQTSoundDescriptionPropertyID_MagicCookie = 'kuki',
kQTSoundDescriptionPropertyID_AudioStreamBasicDescription = 'asbd',
kQTSoundDescriptionPropertyID_UserReadableText = 'text'
};
```

```
Special Considerations
kQTSoundDescriptionPropertyID_AudioChannelLayout
= 'clay'
Used to get or set an
AudioChannelLayout
value.
This is a variable-size property because it may contain an array
of Channel Descriptions.  You must get the size by calling
QTSoundDescriptionGetPropertyInfo
,
allocate a structure of that size, and then get the property.
kQTSoundDescriptionPropertyID_MagicCookie
= 'kuki'
Used to get or set opaque bytes. This is a variable-size
property, because it is completely defined by the codec that uses
the cookie. You must get the size by calling
QTSoundDescriptionGetPropertyInfo
,
allocate a structure of that size, and then get the property.
kQTSoundDescriptionPropertyID_AudioStreamBasicDescription
= 'asbd'
Used to get an
AudioStreamBasicDescription
value.
kQTSoundDescriptionPropertyID_UserReadableText
= 'text'
Used to get a
CFStringRef
value.
QTSoundDescriptionGetProperty
does
a
CFRetain
of the returned
CFString
on
behalf of the caller, so the caller is responsible for calling
CFRelease
on
the returned
CFString
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Retrieves an image buffer from the visual context, indexed
by the provided time.

```
OSStatus QTVisualContextCopyImageForTime (
   QTVisualContextRef visualContext,
   CFAllocatorRef allocator,
   const CVTimeStamp *timeStamp,
   CVImageBufferRef *newImage );
```

```
Parameters
visualContext
The visual context.
allocator
Allocator used to create new CVImageBufferRef.
CVTimeStamp
*timeStamp
Time in question.  Pass
NULL
to
request the image at the current time.
newImage
Points to variable to receive the new image.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
You should not request image buffers further ahead of the
current time than the read-ahead time specified with the
kQTVisualContextExpectedReadAheadKey
attribute.You
may skip images by passing later times, but you may not pass an
earlier time than passed to a previous call to this function.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns a visual context attribute.

```
OSStatus QTVisualContextGetAttribute (
   QTVisualContextRef visualContext,
   CFStringRef attributeKey,
   CFTypeRef *attributeValueOut );
```

```
Parameters
visualContext
The visual context.
attributeKey
Identifier of attribute to get.
attributeValueOut
A pointer to a variable that will receive
the attribute value or
NULL
if
the attribute is not set.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
This routine returns a visual context attribute.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Returns the CFTypeID for QTVisualContextRef.

```
CFTypeID QTVisualContextGetTypeID (
   void );
```

##### Return Value

Undocumented.

```
Discussion
Use this function to test whether a CFTypeRef that extracted
from a CF container such as a CFArray was a
QTVisualContextRef
.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Queries whether a new image is available for a given time.

```
Boolean QTVisualContextIsNewImageAvailable (
   QTVisualContextRef visualContext,
   const CVTimeStamp *timeStamp );
```

```
Parameters
visualContext
The visual context.
CVTimeStamp
*timeStamp
Time in question.
```

##### Return Value

A Boolean.

```
Discussion
This function returns
TRUE
if
there is a image available for the specified time that is different
from the last image retrieved from
QTVisualContextCopyImageForTime
.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Sets a visual context attribute.

```
OSStatus QTVisualContextSetAttribute (
   QTVisualContextRef visualContext,
   CFStringRef attributeKey,
   CFTypeRef attributeValue );
```

```
Parameters
visualContext
The visual context.
attributeKey
Identifier of attribute to set
attributeValue
The value of the attribute to set, or
NULL
to
remove a value.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Installs a user-defined callback to receive notifications
when a new image becomes available.

```
OSStatus QTVisualContextSetImageAvailableCallback (
   QTVisualContextRef visualContext,
   QTVisualContextImageAvailableCallback imageAvailableCallback,
   void *refCon );
```

```
Parameters
visualContext
The visual context invoking the callback.
imageAvailableCallback
Time for which a new image has become available.
May be
NULL
.
refCon
A user-defined value passed to
QTImageAvailableCallback
.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
Due to unpredictible activity, such as user seeks or the arrival
of streaming video packets from a network, new images may become
available for times supposedly occupied by previous images. Applications
using the CoreVideo display link to drive rendering probably do
not need to install a callback of this type, since they will already
be checking for new images at a sufficient rate.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Releases a visual context object.

```
void QTVisualContextRelease ( QTVisualContextRef visualContext );
```

```
Parameters
visualContext
A reference to a visual context object. If
you pass
NULL
, nothing happens.
```

```
Discussion
When the retain count decreases to zero the visual context
is disposed.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Retains a visual context object.

```
QTVisualContextRef QTVisualContextRetain (
   QTVisualContextRef visualContext );
```

```
Parameters
visualContext
A reference to a visual context object. If
you pass
NULL
, nothing happens.
```

##### Return Value

On return, a reference
to the same visual context object, for convenience.

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Causes visual context to release internally held resources
for later re-use.

```
void QTVisualContextTask (
   QTVisualContextRef visualContext );
```

```
Parameters
visualContext
The visual context.
```

```
Discussion
For optimal resource management, this function should be called
in every  rendering pass, after old images have been released, new
images have been used and all rendering has been flushed to the
screen. This call is not mandatory.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
ImageCompression.h
```


Finds the decode time for a specified sample.

```
void SampleNumToMediaDecodeTime (
   Media          theMedia,
   SInt64         logicalSampleNum,
   TimeValue64    *sampleDecodeTime,
   TimeValue64    *sampleDecodeDuration );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
logicalSampleNum
A 64-bit signed integer that contains the
sample number.
sampleDecodeTime
A pointer to a time value. The function updates
this time value to indicate the decode time of the sample specified
by the
logicalSampleNum
parameter.
This time value is expressed in the media's time scale. Set this parameter
to
NULL
if you do not
want this information.
sampleDecodeDuration
A pointer to a time value. The function updates
this time value to indicate the decode duration of the sample specified
by the
logicalSampleNum
parameter.
This time value is expressed in the media's time scale. Set this parameter
to
NULL
if you do not
want this information.
```

```
Discussion
You can access this function’s error returns through
GetMoviesError
and
GetMoviesStickyError
.
It returns
paramErr
if there is a bad
parameter value, or
noErr
if there
is no error.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Finds the display time for a specified sample.

```
void SampleNumToMediaDisplayTime (
   Media          theMedia,
   SInt64         logicalSampleNum,
   TimeValue64    *sampleDisplayTime,
   TimeValue64    *sampleDisplayDuration );
```

```
Parameters
theMedia
The media for this operation. You obtain this
media identifier from such functions as
NewTrackMedia
and
GetTrackMedia
.
logicalSampleNum
A 64-bit signed integer that contains the
sample number.
sampleDisplayTime
A pointer to a time value. The function updates
this time value to indicate the display time of the sample specified
by the
logicalSampleNum
parameter.
This time value is expressed in the media's time scale. Set this parameter
to
NULL
if you do not
want this information.
sampleDisplayDuration
A pointer to a time value. The function updates
this time value to indicate the display duration of the sample specified
by the
logicalSampleNum
parameter.
This time value is expressed in the media’s time scale. Set this parameter
to
NULL
if you do not
want this information.
```

```
Discussion
You can access this function’s error returns through
GetMoviesError
and
GetMoviesStickyError
.
It returns
paramErr
if there is a bad
parameter value, or
noErr
if there
is no error.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Invokes the legacy code options dialog of an audio codec
component.

```
ComponentResult SCAudioInvokeLegacyCodecOptionsDialog (
   ComponentInstance    ci );
```

```
Parameters
ci
A component instance that identifies a connection
to an audio codec component.
```

##### Return Value

An error code, or `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
QuickTimeComponents.h
```


Creates a compression session options object based upon
the settings in the Standard Compression component.

```
ComponentResult SCCopyCompressionSessionOptions (
   ComponentInstance ci,
   ICMCompressionSessionOptionsRef *outOptions );
```

```
Parameters
ci
A component instance of Standard Compression
component.
outOptions
On return, a reference to a new compression
session options object.
```

##### Return Value

An error code. Returns `noErr` if
there is no error. _paramErr_ if
the client did not set the `scAllowEncodingWithCompressionSession` preference
flag.

```
Discussion
This function creates a new compression session options object
using the compression settings of the Standard Compression component
instance. You can use other Standard Compression component calls
to set up the compression settings. Then you call this function
to extract the compression settings in the form of a compression
session options object. The returned object can be used to create
a compression session object through
ICMCompressionSessionCreate()
.
The caller must indicate that he or she intends to use the
new ICM compression session API to perform the compression operation,
by setting the
scAllowEncodingWithCompressionSession
preference
flag through
SCSetInfo()
with
the
scPreferenceFlagsType
selector.
The caller of this function is expected to release the returned
compression session options object through
ICMCompressionSessionOptionsRelease
when
it is done.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
QuickTimeComponents.h
```


Sets the display direction for a decompress sequence.

```
OSErr SetDSequenceNonScheduledDisplayDirection (
   ImageSequence    sequence,
   Fixed            rate );
```

```
Parameters
sequence
Contains the unique sequence identifier that
was returned by the
DecompressSequenceBegin
function.
rate
The display direction to be set. Negative
values represent backward display and positive values represent
forward display.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
QuickTimeComponents.h
```


Sets the display time for a decompression sequence.

```
OSErr SetDSequenceNonScheduledDisplayTime (
   ImageSequence    sequence,
   TimeValue64      displayTime,
   TimeScale        displayTimeScale,
   UInt32           flags );
```

```
Parameters
sequence
Contains the unique sequence identifier that
was returned by the
DecompressSequenceBegin
function.
displayTime
The display time to be set.
displayTimeScale
The display time scale to be set.
flags
Not used; set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
QuickTimeComponents.h
```


Sets the balance level for the mixed audio output of a
movie.

```
OSStatus SetMovieAudioBalance (
   Movie      m,
   Float32    leftRight,
   UInt32     flags );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
leftRight
A pointer to the new balance setting for the
movie. The balance setting is a 32-bit floating-point value that
controls the relative volume of the left and right sound channels.
A value of 0 sets the balance to neutral. Positive values up to
1.0 shift the balance to the right channel, negative values up to –1.0
to the left channel.
flags
Not used; set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The movie’s balance setting is not stored in the movie;
it is used only until the movie is closed. See
GetMovieAudioBalance
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Targets a movie to render into an audio context.

```
OSStatus SetMovieAudioContext (
   Movie      movie,
   QTAudioContextRef    audioContext;
```

```
Parameters
movie
The movie.
audioContext
The audio context that the movie will render
into.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. .

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Configures frequency metering for a particular audio mix
in a movie.

```
OSStatus SetMovieAudioFrequencyMeteringNumBands (
   Movie           m,
   FourCharCode    whatMixToMeter,
   UInt32          *ioNumBands );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
whatMixToMeter
The applicable mix of audio channels in the
movie; see
“Movie Audio Mixes”
.
ioNumBands
A pointer to memory that stores the number
of bands being metered.  On calling this function, you specify the
number of frequency bands you want to meter. If that number is higher
than is possible (determined by factors such as the sample rate
of the audio being metered), the function will return the number
of bands it is actually going to meter. You can pass
NIL
or
a pointer to 0 to disable metering.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
See
GetMovieAudioFrequencyMeteringNumBands
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets the audio gain level for the mixed audio output of
a movie, altering the perceived volume of the movie’s playback.

```
OSStatus SetMovieAudioGain (
   Movie      m,
   Float32    gain,
   UInt32     flags );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
gain
A 32-bit floating-point gain value of 0 or
greater. 0.0 is silent, 0.5 is –6 dB, 1.0 is 0 dB (the audio from
the movie is not modified), 2.0 is +6 dB, etc.  The gain level can
be set higher than 1.0 to allow quiet movies to be boosted in volume.
Gain settings higher than 1.0 may result in audio clipping.
flags
Not used; set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The movie gain setting is not stored in the movie; it is used
only until the movie is closed. See
GetMovieAudioGain
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets the mute value for the audio mix of a movie currently
playing.

```
OSStatus SetMovieAudioMute (
   Movie      m,
   Boolean    muted,
   UInt32     flags );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
muted
Pass
TRUE
to
mute the movie audio,
FALSE
otherwise.
flags
Not used; set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The movie mute setting is not stored in the movie; it is used
only until the movie is closed. See
GetMovieAudioMute
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Enables or disables volume metering of a particular audio
mix of a movie.

```
OSStatus SetMovieAudioVolumeMeteringEnabled (
   Movie           m,
   FourCharCode    whatMixToMeter,
   Boolean         enabled );
```

```
Parameters
m
The movie for this operation. Your application
obtains this movie identifier from such functions as
NewMovie
,
NewMovieFromProperties
,
NewMovieFromFile
,
and
NewMovieFromHandle
.
whatMixToMeter
The applicable mix of audio channels in the
movie; see
“Movie Audio Mixes”
.
enabled
Pass
TRUE
to
enable audio volume metering; pass
FALSE
to
disable it.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
See
GetMovieAudioVolumeMeteringEnabled
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets the brightness adjustment for the movie.

```
OSStatus SetMovieVisualBrightness (
   Movie movie,
   Float32 brightness,
   UInt32 flags );
```

```
Parameters
movie
The movie.
brightness
New brightness adjustment.
flags
Reserved. Pass 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The brightness adjustment for the movie. The value is a Float32
for which -1.0 means full black, 0.0 means no adjustment, and 1.0
means full white. The setting is not stored in the movie. It is
only used until the movie is closed, at which time it is not saved.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Targets a movie to render into a visual context.

```
OSStatus SetMovieVisualContext (
   Movie      movie,
   QTVisualContextRef    visualContext;
```

```
Parameters
movie
The movie.
visualContext
The visual context that the movie will render
into. May be
NULL
..
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error. Returns `memFullErr` if memory
cannot be allocated. Returns `kQTVisualContextNotAllowed` if
the movie is not able to render using a visual context. Returns `paramErr` if
the movie is `NULL`.

```
Discussion
When
SetMovieVisualContext
succeeds,
it will retain the QTVisualContext object for its own use.  If
visualContext
is
NULL
,
the movie will not render any visual media.
SetMovieVisualContext
will
fail if a different movie is already using the visual context, so you
should first disassociate the other movie by calling
SetMovieVisualContext
with
a
NULL
visualContext
.
```

```
Special Considerations
Note that calling
SetMovieGWorld
on
a movie that is connected to a visual context will work, but it
may still keep a reference to the visual context. If you wish to
completely disconnect the visual context, make sure to first call
SetMovieVisualContext
with
a
NULL
visualContext
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets the contrast adjustment for the movie.

```
OSStatus SetMovieVisualContrast (
   Movie movie,
   Float32 contrast,
   UInt32 flags );
```

```
Parameters
movie
The movie.
contrast
The new contrast adjustment.
flags
Reserved. Pass 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The contrast adjustment for the movie. The value is a Float32
percentage (1.0f = 100%), such that 0.0 gives solid grey. The setting
is not stored in the movie. It is only used until the movie is closed,
at which time it is not saved.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets the hue adjustment for the movie.

```
OSStatus SetMovieVisualHue (
   Movie movie,
   Float32 hue,
   UInt32 flags );
```

```
Parameters
movie
The movie.
hue
New hue adjustment.
flags
Reserved. Pass 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The hue adjustment for the movie. The value is a Float32 between
-1.0 and 1.0, with 0.0 meaning no adjustment. This adjustment wraps
around, such that -1.0 and 1.0 yield the same result. The setting
is not stored in the movie. It is only used until the movie is closed, at
which time it is not saved.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets the color saturation adjustment for the movie.

```
OSStatus SetMovieVisualSaturation (
   Movie movie,
   Float32 saturation,
   UInt32 flags );
```

```
Parameters
movie
The movie.
saturation
The new saturation adjustment.
flags
Reserved. Pass 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The color saturation adjustment for the movie. The value is
a Float32 percentage (1.0f = 100%), such that 0.0 gives grayscale.
The setting is not stored in the movie. It is only used until the
movie is closed, at which time it is not saved.
```

```
Version Notes
Introduced in QuickTime 7
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Sets the audio gain level for the audio output of a track,
altering the perceived volume of the track’s playback.

```
OSStatus SetTrackAudioGain (
   Track      t,
   Float32    gain,
   UInt32     flags );
```

```
Parameters
t
A track identifier, which your application
obtains from such functions as
NewMovieTrack
and
GetMovieTrack
.
gain
A 32-bit floating-point gain value of 0 or
greater. 0.0 is silent, 0.5 is –6 dB, 1.0 is 0 dB (the audio from
the track is not modified), 2.0 is +6 dB, etc.  The gain level can
be set higher than 1.0 to allow quiet tracks to be boosted in volume.
Gain settings higher than 1.0 may result in audio clipping.
flags
Not used; set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The track’s gain setting is not stored in the movie; it
is used only until the movie is closed. See
GetTrackAudioGain
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Mutes or unmutes the audio output of a track.

```
OSStatus SetTrackAudioMute (
   Track      t,
   Boolean    muted,
   UInt32     flags );
```

```
Parameters
t
A track identifier, which your application
obtains from such functions as
NewMovieTrack
and
GetMovieTrack
.
muted
Pass
TRUE
to
mute the track’s audio,
FALSE
to
unmute it.
flags
Not used; set to 0.
```

##### Return Value

An error code. Returns `[noErr](../../../../Networking/Conceptual/NSL/NSL3/NSL36.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxw432fojza)` if
there is no error.

```
Discussion
The track mute setting is not stored in the movie; it is used
only until the movie is closed. See
GetTrackAudioMute
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


Converts a track’s time value to a display time value
that is appropriate to the track’s media, using the track’s
edit list.

```
TimeValue64 TrackTimeToMediaDisplayTime (
   TimeValue64    value,
   Track          theTrack );
```

```
Parameters
value
A 64-bit time value that represents the track’s
time value; it must be expressed in the time scale of the movie
that contains the track.
theTrack
A track identifier, which your application
obtains from such functions as
NewMovieTrack
and
GetMovieTrack
.
```

##### Return Value

A 64-bit time value
that represents the corresponding time in media display time, in
the media's time coordinate system. If the track time corresponds
to empty space, this function returns a value of –1.

```
Discussion
This function maps the track time through the track’s edit
list to come up with the media time. This time value contains the
track’s time value according to the media’s time coordinate
system. If the time you specified lies outside of the movie’s
active segment or corresponds to empty space in the track, this
function returns a value of –1. Hence you can use it to determine
whether a specified track edit is empty.
```

```
Version Notes
Introduced in QuickTime 7. This function is a 64-bit replacement
for
TrackTimeToMediaTime
.
```

```
Availability
Carbon status: Supported
C interface file:
Movies.h
```


The callback functions new to the QuickTime
7 API are documented alphabetically in this section.

The callback through which a client of an ICM decompression
session receives decoded frames and information about decoding.

```
typedef void (*ICMDecompressionTrackingCallback)(
void *decompressionTrackingRefCon, OSStatus result,  ICMDecompressionTrackingFlags decompressionTrackingFlags, CVPixelBufferRef  pixelBuffer, TimeValue64 displayTime,
TimeValue64 displayDuration, ICMValidTimeFlags validTimeFlags,
void *sourceFrameRefCon, void *reserved);

// Declaration of a typical application-defined function
Boolean MyICMDecompressionTrackingCallbackProc (
   void                             *decompressionTrackingRefCon,
   OSStatus                         result,
   ICMDecompressionTrackingFlags    decompressionTrackingFlags,
   CVPixelBufferRef                 pixelBuffer,
   TimeValue64                      displayTime,
   TimeValue64                      displayDuration,
   ICMValidTimeFlags                validTimeFlags,
   void                             *sourceFrameRefCon,
   void                             *reserved );
```

```
Parameters
decompressionTrackingRefCon
The callback’s reference value, copied from
the
decompressionTrackingRefCon
field
of an
ICMDecompressionTrackingCallbackRecord
structure.
result
Indicates whether there was an error in decompression.
decompressionTrackingFlags
One or more flags describing the a frame's
state transitions:
kICMDecompressionTracking_LastCall
            = 1L<<0
This is the last call for this
sourceFrameRefCon
.
kICMDecompressionTracking_ReleaseSourceData
   = 1L<<1
The session no longer needs the source data pointer.
kICMDecompressionTracking_EmittingFrame
       = 1L<<2
A frame is being emitted. The
pixelBuffer
parameter contains
the decompressed frame. If the decompression session is targetting
a visual context, the frame has not yet been sent to the visual
context but will be sent after the callback returns.
kICMDecompressionTracking_FrameDecoded
        = 1L<<3
This frame was decoded.
kICMDecompressionTracking_FrameDropped
        = 1L<<4
The codec decided to drop this frame.
kICMDecompressionTracking_FrameNeedsRequeueing
= 1L<<5
This frame will not be able to be displayed unless it
is queued for redecode ( this constant is also known as
FrameNotDisplayable
).
pixelBuffer
When the
kICMDecompressionTracking_EmittingFrame
flag
is set in
decompressionTrackingFlags
,
this parameter must reference a pixel buffer containing the decompressed
frame.
displayTime
If
kICMValidTime_DisplayTimeStampIsValid
is
set in
validTimeFlags
, this parameter
must pass the display time of the frame.
displayDuration
If
kICMValidTime_DisplayDurationIsValid
is
set in
validTimeFlags
, this parameter
must pass the display duration of the frame.
validTimeFlags
Indicates which of
displayTime
and
displayDuration
is
valid:
kICMValidTime_DisplayTimeStampIsValid
The time value passed in
displayTimeStamp
is
valid.
kICMValidTime_DisplayDurationIsValid
The time value passed in
displayDuration
is
valid.
sourceFrameRefCon
The frame’s reference value, copied from
the
sourceFrameRefCon
parameter passed
to
ICMDecompressionSessionDecodeFrame
.
reserved
Reserved for future use.
```

```
Discussion
This callback is referenced by an
ICMDecompressionTrackingCallbackRecord
.
```


Installed by `[NewMovieExportStageReachedCallbackUPP](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2omv3u233wnfsuk6dqn5zhiu3umftwkutfmfrwqzleinqwy3dcmfrwwvkqka)`.

```
typedef OSErr (*MovieExportStageReachedCallbackProcPtr)(OSType inStage, Movie  inMovie, ComponentInstance inDataHandler, Handle inDataRef,
OSType inDataRefType, void *refCon);

// Declaration of a typical application-defined function
Boolean MyMovieExportStageReachedCallbackProc (
   OSType               inStage,
   Movie                inMovie,
   ComponentInstance    inDataHandler,
   Handle               inDataRef,
   OSType               inDataRefType,
   void                 *refCon );
```

```
Parameters
inStage
A movie export stage.
inMovie
A movie.
inDataHandler
A data handler component.
inDataRef
A handle to a data reference.
inDataRefType
The type of the data reference.
refCon
A reference constant to be passed to the callback
specified in
NewMovieExportStageReachedCallbackUPP
.
Use this parameter to point to a data structure containing any information
your callback needs.
```


Provides access to a `SGAudioMediaType` channel’s
data at various point along the signal flow.

```
typedef OSStatus (*SGAudioCallbackProcPtr)
(SGChannel c, void  *inRefCon, SGAudioCallbackFlags *ioFlags, const  AudioTimeStamp *inTimeStamp, const UInt32 *inNumberPackets,
const AudioBufferList *inData, const AudioStreamPacketDescription  *inPacketDescriptions);

// Declaration of a typical application-defined function
OSStatus MySGAudioCallbackProc (
   SGChannel                             c,
   void                                  *inRefCon,
   SGAudioCallbackFlags                  *ioFlags,
   const AudioTimeStamp                  *inTimeStamp,
   const UInt32                          *inNumberPackets,
   const AudioBufferList                 *inData,
   const AudioStreamPacketDescription    *inPacketDescriptions );
```

```
Parameters
c
The sequence grabber channel that has originating
this callback.
inRefCon
A reference constant passed by the caller.
Use this parameter to point to a data structure containing any information
your callback needs.
ioFlags
Currently not used.
inTimeStamp
The time stamp associated with the first sample
passed in
inData
.
inNumberPackets
The number of data packets held in
inData
.
With LPCM formats the number of packets is the same as number of
frames.
inData
A bufferlist containing the requested sample
data.
inPacketDescriptions
If the packets contained in
inData
are
of variable size, this parameter should pass an array of
inNumberPackets
packet
descriptions.
```

```
Discussion
Use
QTSetComponentProperty
with
kQTPropertyClass_SGAudio
and
any of the following property IDs to specify which callback you
would like to receive:
kQTSGAudioPropertyID_PreMixCallback
kQTSGAudioPropertyID_PostMixCallback
kQTSGAudioPropertyID_PreConversionCallback
kQTSGAudioPropertyID_PostConversionCallback
Pass an
SGAudioCallbackStruct
as
the data payload. Clients define an
SGAudioCallbackProc
in
order to tap into a
SGAudioMediaType
channel,
gaining access to its data at various points along the signal flow
chain. Clients should be aware that they may be called back on threads
other than the thread on which they registered for the callback.
They should do as little work as possible inside their callback,
returning control as soon as possible to the channel.
```


Receives notifications when a new OpenGL texture becomes
available.

```
typedef void (*QTOpenGLTextureAvailableCallback)( QTOpenGLTextureContextRef  textureContext, const CVTimeStamp *timeStamp, void *refCon );

// Declaration of a typical application-defined function
OSStatus MyQTOpenGLTextureAvailableCallback (
   QTOpenGLTextureContextRef    textureContext,
   const CVTimeStamp            *timeStamp,
   void                         *refCon );
```

```
Parameters
textureContext
The OpenGL texture context invoking the callback.
timeStamp
Time for which a new texture has become available.
refCon
A reference constant passed by the caller.
Use this parameter to point to a data structure containing any information
your callback needs.
```

```
Discussion
Due to unpredictible activity, such as user seeks or the arrival
of streaming video packets from a network, new textures may become
available for times supposedly occupied by previous textures. Responsive
applications, therefore, should use this callback to discover as
soon as possible when a movie needs to be updated.
```


The public data structures new to the QuickTime
7 API are documented alphabetically in this section. Certain other
data structures are referenced by QuickTime 7 functions but are opaque.

Designates a tracking callback for an ICM decompression
session.

```
struct ICMDecompressionTrackingCallbackRecord {
   ICMDecompressionTrackingCallback    decompressionTrackingCallback;
   void                                *decompressionTrackingRefCon;
};
```

##### Fields

**`decompressionTrackingCallback`**
: The callback function pointer. See `[ICMDecompressionTrackingCallbackProc](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2jinguizldn5wxa4tfonzws33okrzgcy3lnfxgoq3bnrwgeyldnnihe33d)`.

**`decompressionTrackingRefCon`**
: The callback’s reference value.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported;
C interface file:
ImageCompression.h
```


Designates a collection of callbacks for creating a custom
multipass storage object.

```
struct ICMMultiPassStorageCallbacks {
   UInt32                                     version;
   void                                       *storageRefCon;
   ICMMultiPassSetDataAtTimeStampCallback     setDataAtTimeStampCallback;
   ICMMultiPassGetTimeStampCallback           getTimeStampCallback;
   ICMMultiPassCopyDataAtTimeStampCallback    copyDataAtTimeStampCallback;
   ICMMultiPassReleaseCallback                releaseCallback;
};
```

##### Fields

**`version`**
: The version of this structure. Set to `kICMMultiPassStorageCallbacksVersionOne`.

**`storageRefCon`**
: A pointer to a reference constant. Use this parameter
to point to a data structure containing any information your callback
needs.

**`setDataAtTimeStampCallback`**
: A callback for storing values.

**`getTimeStampCallback`**
: A callback for finding time stamps.

**`copyDataAtTimeStampCallback`**
: A callback for retrieving values.

**`releaseCallback`**
: A callback for disposing the callback's state
when done.

```
Discussion
This structure is used by
ICMMultiPassStorageCreateWithCallbacks
.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported;
C interface file:
ImageCompression.h
```


Stores the frequency meter level settings for the audio
channels in a movie mix.

```
struct QTAudioFrequencyLevels {
   UInt32     numChannels;
   UInt32     numFrequencyBands;
   Float32    level[1];
};
```

##### Fields

**`numChannels`**
: The number of audio channels.

**`numFrequencyBands`**
: The number of frequency bands for each channel.

**`level`**
: A 32-bit floating-point value for each frequency
band. The frequency bands for each channel are stored contiguously,
with all the band levels for the first channel first, all the band
levels for the second channel next, etc. The total number of 32-bit
values in this field equals `numFrequencyBands` times `numChannels`.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported;
C interface file:
Movies.h
```

##### Platform Considerations

Associated function: `[GetMovieAudioFrequencyLevels](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxum4tfof2wk3tdpfggk5tfnrzq)`

Stores the volume level settings for the audio channels
in a movie mix.

```
struct QTAudioVolumeLevels {
   UInt32     numChannels;
   Float32    level[1];
};
```

##### Fields

**`numChannels`**
: The number of audio channels.

**`level`**
: A 32-bit floating-point value for each channel’s
volume.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported;
C interface file:
Movies.h
```

##### Platform Considerations

Associated function: `[GetMovieAudioVolumeLevels](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxvm33movwwktdfozswy4y)`

Stores a movie property for `[NewMovieFromProperties](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2omv3u233wnfsum4tpnvihe33qmvzhi2lfom)`.

```
struct QTNewMoviePropertyElement {
   QTPropertyClass       propClass;
   QTPropertyID          propID;
   ByteCount             propValueSize;
   QTPropertyValuePtr    propValueAddress;
   OSStatus              propStatus;
};
```

##### Fields

**`propClass`**
: A four-character code designating the class of
a movie property. See [New Movie Property Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtmmrvhe3tm).

**`propID`**
: The ID of the property.

**`propValueSize`**
: The size in bytes of the property passed in `propValueAddress`.

**`propValueAddress`**
: A pointer to a movie property. Since the data
type is fixed for each element’s property class and ID, these
is no ambiguity about the data type for its property value.

**`propStatus`**
: Indicates any problems with the property. For
example, if a property is not understood by the function it is passed
to, this field is set appropriately. See the discussion in `[NewMovieFromProperties](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2omv3u233wnfsum4tpnvihe33qmvzhi2lfom)`.

```
Discussion
When you call
NewMovieFromProperties
,
you allocate and own arrays of these elements to pass to it, as
well as the property values that each element points to. You are
responsible for disposing of all of these memory allocations.
```

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported;
C interface file:
Movies.h
```

##### Platform Considerations

Associated function: `[NewMovieFromProperties](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2omv3u233wnfsum4tpnvihe33qmvzhi2lfom)`

Used to call an `[SGAudioCallbackProc](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ti5axkzdjn5bwc3dmmjqwg22qojxwg)`.

```
struct SGAudioCallbackStruct {
   SGAudioCallback    inputProc;
   void               *inputProcRefCon;
};
```

##### Fields

**`inputProc`**
: An `[SGAudioCallbackProc](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2ti5axkzdjn5bwc3dmmjqwg22qojxwg)`.

**`inputProcRefCon`**
: A reference constant. Use this parameter to point
to a data structure containing any information your callback needs.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported;
C interface file:
Movies.h
```


Provides version 2 of the `SoundDescription` data
structure.

```
struct SoundDescriptionV2 {
   SInt32     descSize;
   OSType     dataFormat;
   SInt32     resvd1;
   SInt16     resvd2;
   SInt16     dataRefIndex;
   SInt16     version;
   SInt16     revlevel;
   SInt32     vendor;
   SInt16     always3;
   SInt16     always16;
   SInt16     alwaysMinus2;
   SInt16     always0;
   UInt32     always65536;
   UInt32     sizeOfStructOnly;
   Float64    audioSampleRate;
   UInt32     numAudioChannels;
   SInt32     always7F000000;
   UInt32     constBitsPerChannel;
   UInt32     formatSpecificFlags;
   UInt32     constBytesPerAudioPacket;
   UInt32     constLPCMFramesPerAudioPacket;
   /* additional atom-based extensions ([long size, long type,
   some data], repeat) */
};
```

##### Fields

**`descSize`**
: Total size of this structure, including extra
data.

**`dataFormat`**
: Set to`'lpcm'` for
uncompressed data; otherwise set to the compression type. For a
list of compression type codes, see the [QuickTime API Reference](https://developer.apple.com/referencelibrary/API_Fundamentals/QuickTime-api-date.html).

**`resvd1`**
: Reserved; set to 0.

**`resvd2`**
: Reserved; set to 0.

**`dataRefIndex`**
: Reserved; set to 0.

**`version`**
: Version of this structure; set to 2.

**`revlevel`**
: Set to codec version number.

**`always3`**
: Reserved; set to 3.

**`always16`**
: Reserved; set to 16 (0x0010).

**`alwaysMinus2`**
: Reserved; set to –2 (0xFFFE).

**`always0`**
: Reserved; set to 0.

**`always65536`**
: Reserved; set to 65536 (0x00010000).

**`sizeOfStructOnly`**
: Set to `sizeof(SoundDescriptionV2)`,
equivalent to the offset to any structure extensions.

**`audioSampleRate`**
: Set to a 64-bit floating-point number representing
the number of audio frames per second; for example, 44100.0.

**`numAudioChannels`**
: Set to the number of audio channels; any channel
assignment info will be in an extension.

**`always7F000000`**
: Reserved; set to 7F000000.

**`constBitsPerChannel`**
: Set to the number of bits per channel only if
this value is constant and the audio is uncompressed. Otherwise
set to 0.

**`formatSpecificFlags`**
: See LPCM flag definitions in `CoreAudioTypes.h`.

**`constBytesPerAudioPacket`**
: Set to the number of bytes per packet only if
this value is constant. Otherwise set to 0.

**`constLPCMFramesPerAudioPacket`**
: Set to the number of PCM frames per packet only
if this value is constant. Otherwise set to 0.

```
Version Notes
Introduced in QuickTime 7.
```

```
Availability
Carbon status: Supported;
C interface file:
Movies.h
```

##### Platform Considerations

You should never have to know this definition, except for
debugging purposes. Use the new QuickTime sound description APIs
to treat sound descriptions as if they are opaque.

This section lists constants that are newly
defined in QuickTime 7.

The following values are used to select
options for ICM compression session objects:

```
kQTPropertyClass_ICMCompressionSessionOptions = 'icso',
kICMCompressionSessionOptionsPropertyID_AllowAsyncCompletion = 'asok',
kICMCompressionSessionOptionsPropertyID_AllowFrameReordering = 'b ok',
kICMCompressionSessionOptionsPropertyID_AllowFrameTimeChanges = '+ ok',
kICMCompressionSessionOptionsPropertyID_AllowTemporalCompression = 'p ok',
kICMCompressionSessionOptionsPropertyID_AverageDataRate = 'aver',
kICMCompressionSessionOptionsPropertyID_ColorTable = 'clut',
kICMCompressionSessionOptionsPropertyID_CompressorComponent = 'imco',
kICMCompressionSessionOptionsPropertyID_CompressorSettings = 'cost',
kICMCompressionSessionOptionsPropertyID_CPUTimeBudget = 'cput',
kICMCompressionSessionOptionsPropertyID_DataRateLimitCount = 'har#',
kICMCompressionSessionOptionsPropertyID_DataRateLimits = 'hard',
kICMCompressionSessionOptionsPropertyID_Depth = 'deep',
kICMCompressionSessionOptionsPropertyID_DurationsNeeded = 'need',
kICMCompressionSessionOptionsPropertyID_MaxDataRateLimits = 'mhar',
kICMCompressionSessionOptionsPropertyID_MaxFrameDelayCount = 'cwin',
kICMCompressionSessionOptionsPropertyID_MaxFrameDelayTime = 'cwit',
kICMCompressionSessionOptionsPropertyID_MaxKeyFrameInterval = 'kyfr',
kICMCompressionSessionOptionsPropertyID_MultiPassStorage = 'imps',
kICMCompressionSessionOptionsPropertyID_Quality = 'qual',
kICMCompressionSessionOptionsPropertyID_SourceFrameCount = 'frco',
kICMCompressionSessionOptionsPropertyID_WasCompressed = 'wasc'
```

**`kQTPropertyClass_ICMCompressionSessionOptions
= 'icso'`**
: Class identifier for compression session option object
properties.

**`kICMCompressionSessionOptionsPropertyID_AllowAsyncCompletion
= 'asok'`**
: Enables the compressor to call the encoded-frame callback
from a different thread. By default this option is `FALSE`,
which means that the compressor must call the encoded-frame callback
from the same thread as `[ICMCompressionSessionEncodeFrame](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4rlomnxwizkgojqw2zi)` and `[ICMCompressionSessionCompleteFrames](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4q3pnvygyzlumvdheylnmvzq)`.

**`kICMCompressionSessionOptionsPropertyID_AllowFrameReordering
= 'b ok'`**
: Enables frame reordering. To encode B-frames a compressor
must reorder frames, which may mean that the order in which they
are emitted and stored (the decode order) may be different from
the order in which they are presented to the compressor (the display
order). By default, frame reordering is disabled. To encode using
B-frames, you must enable frame reordering by passing `TRUE` in
this property.

**`kICMCompressionSessionOptionsPropertyID_AllowFrameTimeChanges
= '+ ok'`**
: Enables the compressor to modify frame times, improving
its performance. Some compressors are able to identify and coalesce
runs of identical frames and emit single frames with longer duration,
or emit frames at a different frame rate from the original. By default,
this flag is set to `FALSE`,
which forces the compressor to emit one encoded frame for every
source frame and to preserve frame display times. This option replaces
the practice of having compressors return special high similarity
values to indicate that frames can be dropped.

**`kICMCompressionSessionOptionsPropertyID_AllowTemporalCompression
= 'p ok'`**
: Enables temporal compression of P-frames and B-frames.
By default, temporal compression is disabled.

**`kICMCompressionSessionOptionsPropertyID_AverageDataRate
= 'aver'`**
: The long-term desired average data rate in bytes per
second. This is not an absolute limit. The default data rate is
zero, indicating that the setting of `kICMCompressionSessionOptionsPropertyID_Quality` should
determine the size of compressed data. Data rate settings have effect
only when timing information is provided for source frames. Some
codecs do not accept limiting to specified data rates.

**`kICMCompressionSessionOptionsPropertyID_ColorTable
= 'clut'`**
: The color table for compression, used with indexed-color
depths. Clients who are passed this property are responsible for
disposing the returned `CTabHandle`.

**`kICMCompressionSessionOptionsPropertyID_CompressorComponent
= 'imco'`**
: Sets a specific compressor component or component instance
to be used, or passes one of the wildcards `anyCodec`, `bestSpeedCodec`, `bestFidelityCodec`,
or `bestCompressionCodec`. Pass this
option to force the Image Compression Manager to use a specific
compressor component or compressor component instance. To allow
the Image Compression Manager to choose the compressor component,
set the compressorComponent to `anyCodec` (the
default), `bestSpeedCodec`, `bestFidelityCodec`,
or `bestCompressionCodec`. If you pass
in a component instance that you opened, the ICM will not close
that instance; you must do so after the compression session is released.

**`kICMCompressionSessionOptionsPropertyID_CompressorSettings
= 'cost'`**
: A handle containing compressor settings. The compressor
will be configured with these settings (by a call to `ImageCodecSetSettings`)
during the `[ICMCompressionSessionCreate](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4q3smvqxizi)` process.

**`kICMCompressionSessionOptionsPropertyID_CPUTimeBudget
= 'cput'`**
: Recommends a CPU time budget for a compressor in microseconds
per frame. Zero means to go as fast as possible. By default, this
is set to `kICMUnlimitedCPUTimeBudget`,
which sets no limit. This option provides only an advisory hint,
and some compressors may ignore it. Compressors are not compelled
to use the full time budget if they complete ahead of time. Multithreaded
compressors may use this amount of CPU time on each processor.

**`kICMCompressionSessionOptionsPropertyID_DataRateLimitCount
= 'har#'`**
: The current number of data rate limits.

**`kICMCompressionSessionOptionsPropertyID_DataRateLimits
= 'hard'`**
: Zero, one, or two hard limits on data rate. Each hard
limit is described by a data size in bytes and a duration in seconds.
It requires that the total size of compressed data for any contiguous
segment of that duration (in decode time) must not exceed the data
size. By default, no data rate limits are set. When setting this
property, the _inPropValueSize_ parameter
should be the number of data rate limits multiplied by `sizeof(ICMDataRateLimit)`.
Data rate settings have an effect only when timing information
is provided for source frames. Some codecs do not accept limiting
to specified data rates.

**`kICMCompressionSessionOptionsPropertyID_Depth
= 'deep'`**
: The depth for compression. If a compressor does not
support a specific depth, the closest supported depth will be used,
preferring deeper depths to shallower depths. The default depth
is `k24RGBPixelFormat`.

**`kICMCompressionSessionOptionsPropertyID_DurationsNeeded
= 'need'`**
: Indicates that durations of emitted frames are needed.
If this option is set and source frames are provided with times
but not durations, then frames will be delayed so that durations
can be calculated as the difference between one frame’s time stamp
and the next frame’s time stamp. By default, this flag is `FALSE`,
so frames will not be delayed in order to calculate durations. If
you pass encoded frames to `[AddMediaSampleFromEncodedFrame](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxuczdejvswi2lbknqw24dmmvdhe33nivxgg33emvsem4tbnvsq)`,
you must set this flag to `TRUE`.

**`kICMCompressionSessionOptionsPropertyID_MaxDataRateLimits
= 'mhar'`**
: The maximum allowed number of data rate limits, currently
2.

**`kICMCompressionSessionOptionsPropertyID_MaxFrameDelayCount
= 'cwin'`**
: The maximum frame delay count is the maximum number
of frames that a compressor is allowed to hold before it must output
a compressed frame. This value limits the number of frames that
may be held in the “compression window.” If the maximum frame
delay count is M, then before the call to encode frame N returns,
frame N-M must have been emitted. The default value is `kICMUnlimitedFrameDelayCount`,
which sets no limit on the compression window.

**`kICMCompressionSessionOptionsPropertyID_MaxFrameDelayTime
= 'cwit'`**
: The maximum frame delay time is the maximum difference
between a source frame’s display time and the corresponding encoded
frame»s decode time. This value limits the span of display time
that may be held in the “compression window.” If the maximum
frame delay time is TM, then before the call to encode a frame with
display time TN returns, all frames with display times up to and
including TN-TM must have been emitted. The default value is `kICMUnlimitedFrameDelayTime`,
which sets no time limit on the compression window.

**`kICMCompressionSessionOptionsPropertyID_MaxKeyFrameInterval
= 'kyfr'`**
: The maximum interval between key frames, also known
as the key frame rate. Compressors are allowed to generate key frames
more frequently if this would result in more efficient compression.
The default key frame interval is 0, which indicates that the compressor
should choose where to place all key frames. This differs from previous
practice, in which a key frame rate of zero disabled temporal compression.

**`kICMCompressionSessionOptionsPropertyID_MultiPassStorage
= 'imps'`**
: A multipass compression client must provide a storage
location for multipass data. Pass `[ICMMultiPassStorageCreateWithTemporaryFile](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2njv2wy5djkbqxg42torxxeylhmvbxezlborsvo2lunbkgk3lqn5zgc4tzizuwyzi)` to make
the ICM store multipass data in a temporary file. Pass `[ICMMultiPassStorageCreateWithCallbacks](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2njv2wy5djkbqxg42torxxeylhmvbxezlborsvo2lunbbwc3dmmjqwg23t)` to
manage the storage yourself. Note that the amount of multipass data
to be stored can be substantial; it could be greater than the size
of the output movie file. If this property is not `NULL`,
the client must call `[ICMCompressionSessionBeginPass](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4qtfm5uw4udbonzq)` and `[ICMCompressionSessionEndPass](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4rlomrigc43t)` around
groups of calls to `[ICMCompressionSessionEncodeFrame](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4rlomnxwizkgojqw2zi)`.
By default, this property is `NULL` and
multipass compression is not enabled. The compression session options
object retains the multipass storage object when one is set.

**`kICMCompressionSessionOptionsPropertyID_Quality
= 'qual'`**
: The compression quality. This value is always used to
set the spatial quality; if temporal compression is enabled, it
is also used to set temporal quality. The default quality is `codecNormalQuality`.

**`kICMCompressionSessionOptionsPropertyID_SourceFrameCount
= 'frco'`**
: Indicates the number of source frames, if known. If
nonzero, this value should equal the exact number of times that
the client calls `[ICMCompressionSessionEncodeFrame](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4rlomnxwizkgojqw2zi)` in
each pass. The default is 0, which indicates that the number of
source frames is not known.

**`kICMCompressionSessionOptionsPropertyID_WasCompressed
= 'wasc'`**
: Indicates that the source was previously compressed.
This property is an optional information hint to the compressor;
by default it is `FALSE`.

The following constants represent properties
of ICM compression sessions:

```
kQTPropertyClass_ICMCompressionSession = 'icse',
kICMCompressionSessionPropertyID_CompressorPixelBufferAttributes = 'batt',
kICMCompressionSessionPropertyID_ImageDescription = 'idsc',
kICMCompressionSessionPropertyID_PixelBufferPool = 'pool',
kICMCompressionSessionPropertyID_TimeScale = 'tscl'
```

**`kQTPropertyClass_ICMCompressionSession
= 'icse'`**
: Class identifier for compression session properties.

**`kICMCompressionSessionPropertyID_CompressorPixelBufferAttributes
= 'batt'`**
: The compressor’s pixel buffer attributes for the compression
session. You can use these to create a pixel buffer pool for source
pixel buffers. This is not the same as the `sourcePixelBufferAttributes` property
passed to `[ICMCompressionSessionCreate](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4q3smvqxizi)`.
Getting this property does not change its retain count.

**`kICMCompressionSessionPropertyID_ImageDescription
= 'idsc'`**
: The image description for a compression session. For
some codecs, the image description may not be available before the
first frame is compressed. Multiple calls to retrieve this property
will return the same handle. The ICM will dispose of this handle
when the compression session is disposed; the caller must not dispose
of it.

**`kICMCompressionSessionPropertyID_PixelBufferPool
= 'pool'`**
: A pool that can provide ideal source pixel buffers for
a compression session. The compression session creates this pixel
buffer pool based on the compressor’s pixel buffer attributes
and any pixel buffer attributes passed in to `[ICMCompressionSessionCreate](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxusq2ninxw24dsmvzxg2lpnzjwk43tnfxw4q3smvqxizi)`.
If the source pixel buffer attributes and the compressor pixel buffer
attributes can not be reconciled, the pool is based on the source
pixel buffer attributes and the ICM converts each `CVPixelBuffer` internally.

**`kICMCompressionSessionPropertyID_TimeScale
= 'tscl'`**
: The time scale for the compression session.

The following are values for `kQTVisualContextTypeKey`,
a read-only `CFStringRef` that defines the type
of the visual context:

**`kQTVisualContextType_PixelBuffer`**
: The value of `kQTVisualContextTypeKey` for
pixel buffer visual contexts.

**`kQTVisualContextType_OpenGLTexture`**
: The value of `kQTVisualContextTypeKey` for
OpenGL texture visual contexts.

**`kQTVisualContextColorSpaceKey`**
: A `CGColorSpaceRef` that defines
the color space of images produced by a visual context. If this
attribute is not set, images may use any color space.

**[kQTVisualContextExpectedReadAheadKey](https://developer.apple.com/library/archive/documentation/QuickTime/Reference/QT7-1_Update_Reference/Constants.html#//apple_ref/doc/c_ref/kQTVisualContextExpectedReadAheadKey)**
: A `CFNumberRef` that defines the
number of seconds ahead of real time that the client expects to
pull images out of a visual context. Applications using the Core
Video display link should set this attribute according to the value returned
by `CVDisplayLinkGetOutputVideoLatency`.

**[kQTVisualContextPixelBufferAttributesKey](https://developer.apple.com/library/archive/documentation/QuickTime/Reference/QT7-1_Update_Reference/Constants.html#//apple_ref/doc/c_ref/kQTVisualContextPixelBufferAttributesKey)**
: A `CFDictionaryRef` that defines
the dictionary containing pixel buffer attributes. See `kICMCompressionSessionPropertyID_PixelBufferPool` in `[ICM Compression Session Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtomjtgmydk)`.

**[kQTVisualContextTargetDimensionsKey](https://developer.apple.com/library/archive/documentation/QuickTime/Reference/QT7-1_Update_Reference/Constants.html#//apple_ref/doc/c_ref/kQTVisualContextTargetDimensionsKey)**
: A `CFDictionaryRef` that defines
the dictionary containing [kQTVisualContextTargetDimensions_WidthKey](https://developer.apple.com/library/archive/documentation/QuickTime/Reference/QT7-1_Update_Reference/Constants.html#//apple_ref/doc/c_ref/kQTVisualContextTargetDimensions_WidthKey) and [kQTVisualContextTargetDimensions_HeightKey](https://developer.apple.com/library/archive/documentation/QuickTime/Reference/QT7-1_Update_Reference/Constants.html#//apple_ref/doc/c_ref/kQTVisualContextTargetDimensions_HeightKey) values
(see below). This key is used as a hint to optimize certain media
types, such as text, that can be rendered at any resolution. If
this attribute is not set, the movie will be rendered at its native
resolution.

**[kQTVisualContextTargetDimensions_WidthKey](https://developer.apple.com/library/archive/documentation/QuickTime/Reference/QT7-1_Update_Reference/Constants.html#//apple_ref/doc/c_ref/kQTVisualContextTargetDimensions_WidthKey)**
: A `CFNumberRef` that defines the
width, in pixels, of the rendering target.

**[kQTVisualContextTargetDimensions_HeightKey](https://developer.apple.com/library/archive/documentation/QuickTime/Reference/QT7-1_Update_Reference/Constants.html#//apple_ref/doc/c_ref/kQTVisualContextTargetDimensions_HeightKey)**
: A `CFNumberRef` that defines the
height, in pixels, of the rendering target.

Three new four-character constants define
the mix of audio channels for several functions:

```
kQTAudioMeter_StereoMix = 'stmx'
kQTAudioMeter_DeviceMix = kQTAudioPropertyID_DeviceChannelLayout = 'dcly'
kQTAudioMeter_MonoMix = 'momx'
```

**`kQTAudioMeter_StereoMix`**
: Meter a stereo (two-channel) mix of the enabled sound
tracks in the movie. This option is offered only for MovieAudioFrequencyMetering.

**`kQTAudioMeter_DeviceMix`**
: Meter the movie’s mix to the `AudioChannelLayout` of
the device the movie is playing to. To determine the channel layout
of this mix, you call the `kAudioPropertyID_DeviceChannelLayout` movie
property.

**`kQTAudioMeter_MonoMix`**
: Meter the movie as if it had been mixed to monaural.
This option is offered only for MovieAudioFrequencyMetering.

The constants listed above are passed by the following QuickTime
7 functions:

- [GetMovieAudioFrequencyLevels](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxum4tfof2wk3tdpfggk5tfnrzq)
- [GetMovieAudioFrequencyMeteringBandFrequencies](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxum4tfof2wk3tdpfgwk5dfojuw4z2cmfxgirtsmvyxkzlomnuwk4y)
- [GetMovieAudioFrequencyMeteringNumBands](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxum4tfof2wk3tdpfgwk5dfojuw4z2oovwueylomrzq)
- [GetMovieAudioVolumeLevels](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxvm33movwwktdfozswy4y)
- [GetMovieAudioVolumeMeteringEnabled](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2hmv2e233wnfsuc5lenfxvm33movwwktlforsxe2lom5cw4ylcnrswi)
- [SetMovieAudioFrequencyMeteringNumBands](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2tmv2e233wnfsuc5lenfxum4tfof2wk3tdpfgwk5dfojuw4z2oovwueylomrzq)
- [SetMovieAudioVolumeMeteringEnabled](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2tmv2e233wnfsuc5lenfxvm33movwwktlforsxe2lom5cw4ylcnrswi)

The following values are used as `ComponentPropertyID` selectors.
Use these with the StandardCompressionSubTypeAudio (`'scdi'/'audi'`)
component. All property IDs are to be used in conjunction with the `kQTPropertyClass_SCAudio` property
class.

**`kQTSCAudioPropertyID_AvailableCompressionFormatList
= 'acf#'`**
: A read/listen C-style array of `OSType` values
that specifies the list of available output compression formats.
This list includes all the `kAudioEncoderComponentType` components
and `kSoundCompressor` type components
on the user’s system. You can restrict the list by using the `kQTSCAudioPropertyID_CompressionFormatList` property.
Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to discover
the number of bytes you should allocate for this array.

**`kQTSCAudioPropertyID_ClientRestrictedCompressionFormatList
= 'crf#'`**
: A read/write/listen C-style array of `OSType` values
that specifies a client-restricted set of output compression formats
that you should list as available. Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the number of bytes you should allocate to hold this array.

**`kQTSCAudioPropertyID_AvailableCompressionFormatNamesList
= 'cnm#'`**
: A read/write `CFArrayRef` structure
of `CFStringRef` structures that reference the
human-readable names of each item in a `kQTSCAudioPropertyID_AvailableCompressionFormatList`.
The caller assumes responsibility for calling `CFRelease` to
dispose of the `CFArrayRef` structure.

**`kQTSCAudioPropertyID_HasLegacyCodecOptionsDialog
= 'opn?'`**
: Some compression formats have format-specific properties
that are accessible only via a compressor-provided dialog. This
constant specifies a read/listen `Boolean` value
that lets you know if the current compression format has such a
dialog.

**`kQTSCAudioPropertyID_ConstantBitRateFormatsOnly
= '!vbr'`**
: By default, constant as well as variable bit rate compression
formats are shown in the available format list. This constant specifies
a read/write/listen `Boolean` value
that lets you restrict the available formats to constant bit rate
formats by setting this property to `TRUE`.

**`kQTSCAudioPropertyID_AvailableSampleRateList
= 'avr#'`**
: A read/listen C-style array of `AudioValueRange` values
that specifies a list of available output sample rates. This list
is specific to the compression format and takes into account any
restrictions imposed by a client using the `kQTSCAudioPropertyID_ClientRestrictedSampleRateList` property.
Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to discover
the number of bytes you should allocate to hold this array.

**`kQTSCAudioPropertyID_SampleRateRecommended
= 'reco'`**
: Clients not wishing to set an output sample rate manually
may set the output rate to the recommended rate. Some compressors
can perform rate conversion, and can pick optimal settings for a
desired bitrate (AAC is one example). For other formats, the recommended
rate is simply the closest output rate to the input rate that's
allowed by the output format. `kQTSCAudioPropertyID_SampleRateIsRecommended` is
read-only. To set the sample rate to recommended, a client sets
the `kQTSCAudioPropertyID_BasicDescription` with `mSampleRate` =
0.0. To unset the sample rate as recommended, the client sets the `kQTSCAudioPropertyID_BasicDescription` with
a non-zero `mSampleRate` field.

**`kQTSCAudioPropertyID_ApplicableSampleRateList
= 'avr#'`**
: A read/listen C-style array of `AudioValueRange` values
that specifies which of the value ranges in the `kQTSCAudioPropertyID_AvailableSampleRateList` are
currently applicable. The `kQTSCAudioPropertyID_AvailableSampleRateList` takes
into account client restrictions, and a compression format's general
sample rate restrictions. `kQTSCAudioPropertyID_ApplicableSampleRateList` further filters
the list to just those sample rates that are legal and valid given
the current codec configuration. Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the number of bytes you should allocate to hold the array.

**`kQTSCAudioPropertyID_ClientRestrictedSampleRateList
= 'crr#'`**
: A read/write/listen C-style array of `AudioValueRange` values
that specifies a client-restricted set of output sample rate ranges
that should be listed as available. Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the number of bytes you should allocate to hold this array.

**`kQTSCAudioPropertyID_InputMagicCookie
= 'ikki'`**
: A read/write/listen opaque data structure that contains
an untyped codec-specific data structure (a “magic cookie”),
which some decompressors use to decode their input. Cookies are
variable size, so you must call `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the size of the buffer you should allocate to hold the
cookie.

**`kQTSCAudioPropertyID_MagicCookie
= 'kuki'`**
: A read/write/listen opaque data structure that contains
an untyped codec-specific data structure (a “magic cookie”),
which some decompressors use to configure their output. Cookies
are variable size, so you must call `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the size of the buffer you should allocate to hold the
cookie.

**`kQTSCAudioPropertyID_ClientRestrictedLPCMBitsPerChannelList
= 'crb#'`**
: Specifies a client-restricted set of output bits per
channel that should be listed as available. Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the number of bytes you should allocate to hold the array.

**`kQTSCAudioPropertyID_AvailableLPCMBitsPerChannelList
= 'avb#'`**
: A read/listen C-style array of `UInt32` values
that contains a list of available bits per audio channel. This list
is specific to LPCM, and takes into account any restrictions imposed
by a client using the `kQTSCAudioPropertyID_LPCMBitsPerChannelList` property.
Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to discover
the number of bytes you should allocate to hold this array.

**`kQTSCAudioPropertyID_ApplicableLPCMBitsPerChannelList
= 'apb#'`**
: Specifies which of the values in the `kQTSCAudioPropertyID_AvailableLPCMBitsPerChannelList` are
currently applicable. The `kQTSCAudioPropertyID_AvailableLPCMBitsPerChannelList` takes
into account client restrictions, and LPCM’s general bits per
channel restrictions. `kQTSCAudioPropertyID_ApplicableLPCMBitsPerChannelList` further
filters the list to just those bits per channel that are legal and
valid given the current LPCM configuration. Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the number of bytes you should allocate to hold the array.

**`kQTSCAudioPropertyID_LPCMBitsPerChannelList
= 'sbc#'`**
: A read/write/listen C-style array of `UInt32` values
that contains a client-restricted set of output bits per channel,
which you should list as available. Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the number of bytes you should allocate to hold this array.

**`kQTSCAudioPropertyID_AvailableNumChannelsList
= 'anc#'`**
: A read/listen C-style array of `UInt32` values
that contains a list of available numbers of channels. This list
is specific to the compression format and takes into account any
restrictions imposed by a client using the `kQTSCAudioPropertyID_NumChannelsList` property.
Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to discover
the number of bytes you should allocate to hold this array.

**`kQTSCAudioPropertyID_NumChannelsList
= 'snc#'`**
: A read/write/listen C-style array of `UInt32` values
that contains a client-restricted set of numbers of channels that
you should list as available. Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the number of bytes you should allocate to hold this array.

**`kQTSCAudioPropertyID_InputChannelLayout
= 'icly'`**
: A read/write/listen variable-size `AudioChannelLayout` structure
that specifies the audio channel layout of the input description. `AudioChannelLayout` is
a variable-size structure, so you must use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the number of bytes you should allocate for it.

**`kQTSCAudioPropertyID_InputChannelLayoutName
= 'icln'`**
: A read-only `CFStringRef` structure
that specifies the human-readable name for a `kQTSCAudioPropertyID_InputChannelLayout` structure,
if one exists. The caller is responsible for calling `CFRelease` to
dispose of the resulting string.

**`kQTSCAudioPropertyID_ChannelLayout
= 'clay'`**
: A read/write/listen variable-size `AudioChannelLayout` structure
that specifies the audio channel layout of the output description. `AudioChannelLayout` is
a variable size structure, so you must use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the number of bytes you should allocate.

**`kQTSCAudioPropertyID_ChannelLayoutName
= 'clyn'`**
: A read-only `CFStringRef` structure
that specifies the human-readable name for a `kQTSCAudioPropertyID_ChannelLayout`,
if one exists. The caller is responsible for calling `CFRelease` to
dispose of the resulting string.

**`kQTSCAudioPropertyID_ClientRestrictedChannelLayoutTagList
= 'crl#'`**
: Specifies a client-restricted set of channel layout
tags that should be listed as available. Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the number of bytes you should allocate to hold the array.

**`kQTSCAudioPropertyID_AvailableChannelLayoutTagList
= 'acl#'`**
: A read/listen C-style array of `AudioChannelLayoutTag` values
that specifies a list of available audio channel layout tags. This
list is specific to the compression format and takes into account
any restrictions imposed by a client using the `kQTSCAudioPropertyID_ChannelLayoutTagList` property. Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the number of bytes you should allocate to hold this array.

**`kQTSCAudioPropertyID_ChannelLayoutTagList
= 'cly#'`**
: A read/write C-style array of `AudioChannelLayoutTag` values
that specifies a client-restricted set of channel layout tags, which
you should list as available. Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the number of bytes you should allocate to hold this array.

**`kQTSCAudioPropertyID_AvailableChannelLayoutTagNamesList
= 'cln#'`**
: A read-only `CFArrayRef` array that
specifies the human-readable names for the `AudioChannelLayoutTag` values
in a `kQTSCAudioPropertyID_AvailableChannelLayoutTagList`.
Each element in the array is a `CFStringRef` structure.
The caller is responsible for calling `CFRelease` to
dispose of this array.

**`kQTSCAudioPropertyID_ApplicableChannelLayoutTagNamesList
= 'apl#'`**
: Specifies which of the values in the `kQTSCAudioPropertyID_AvailableChannelLayoutTagList` are
currently applicable. The `kQTSCAudioPropertyID_AvailableChannelLayoutTagList` takes
into account client restrictions, and the current output format’s general
channel layout restrictions. `kQTSCAudioPropertyID_ApplicableChannelLayoutTagList` further
filters the list to just those channel layouts that are legal and
valid given the current codec configuration. Use `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the number of bytes you should allocate to hold the array.

**`kQTSCAudioPropertyID_ClientRestrictedPCMFlags
= 'crip'`**
: Specifies a client-restricted set of flags corresponding
to the `mFormatFlags` fields in an `AudioStreamBasicDescription`.
Data type is a `SCAudioFormatFlagsRestrictions` struct.
For instance, if a client wishes to specify to the StandardAudioCompression
component that their file format requires little endian pcm data,
the client may set this property, with `formatFlagsMask` set
to `kAudioFormatFlagIsBigEndian`, and `formatFlagsValues` set
to zero (indicating that the IsBigEndian bit should be interpreted
as LittleEndian only).

**`kQTSCAudioPropertyID_DiscreteChannelsOK
= 'dscr'`**
: A read/write/listen `Boolean` value
that lets you tell the `StandardCompressionSubTypeAudio` dialog
to not show “Discrete” as an available option. Each `AudioChannelLayout` structure
assigns specific spatial orientation to specific channels (for example,
Channel 1 = Left). “Discrete” is a special channel layout that
does not assign spatial characteristics to channels, but instead
labels them as distinct outputs. For example, the first channel
in the audio source is played through the first channel on the output
device, the second channel in the source is played through the second
channel, and so on. If this property is set to `FALSE`,
the `StandardCompressionSubTypeAudio` dialog
will not show “Discrete” as an available option.

**`kQTSCAudioPropertyID_LPCMSpecificFlagsMask
= 'sffm'`**
: A read/write/listen `UInt32` value
that specifies which flag fields in `kQTSCAudioPropertyID_FormatSpecificFlags` should
be made available in the `StandardCompressionSubTypeAudio` dialog.
For instance, a value of `0xFFFFFFFD` (all
bits except `kAudioFormatFlagIsBigEndian` set)
tells the `StandardCompressionSubTypeAudio` component
to disable any UI that would allow a choice between little and big
endian. This selector is valid only for PCM formats and is ignored
for others.

**`kQTSCAudioPropertyID_InputSoundDescription
= 'isdh'`**
: A read/write `SoundDescriptionHandle` value
that specifies the current input description as a `SoundDescriptionHandle` (lowest
possible version for the current format). When calling `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6i)`,
the caller passes a pointer to an unallocated `Handle` and
assumes responsibility for calling `DisposeHandle` when
done.

**`kQTSCAudioPropertyID_SoundDescription
= 'osdh'`**
: A read/write `SoundDescriptionHandle` value
that specifies the current output description as a `SoundDescriptionHandle` (lowest
possible version for the current format). When calling `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6i)`,
the caller passes a pointer to an unallocated `Handle` and
assumes responsibility for calling `DisposeHandle` when
done.

**`kQTSCAudioPropertyID_InputBasicDescription
= 'isbd'`**
: A read/write/`DataProc`/listen `AudioStreamBasicDescription` value
that specifies that the current input description is an `AudioStreamBasicDescription` value.

**`kQTSCAudioPropertyID_BasicDescription
= 'osbd'`**
: A read/write/`DataProc`/listen `AudioStreamBasicDescription` value
that specifies that the current output description is an `AudioStreamBasicDescription` value.

**`kQTSCAudioPropertyID_CodecSpecificSettingsArray
= 'cdst'`**
: A read/write `CFArrayRef` structure
that designates a `CFArray` of `CFDictionary` structures,
which describe various parameters specific to configuring a codec.
This array of dictionaries, which is published by some compressors,
can be parsed to generate UI information. When any value in the
array changes, a client should call `[QTSetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctmv2eg33nobxw4zloorihe33qmvzhi6i)`,
passing the entire array.

**`kQTSCAudioPropertyID_SettingsState
= scSettingsStateType`**
: A read/write `Handle` value that
is used to save the current state of the `StandardCompressionSubTypeAudio` component,
so that its state may be restored at a later time with a single
call. A `StandardCompressionSubTypeAudio` component
can accept a saved settings state from a legacy `StandardCompressionSubTypeSound` component
as write-only.

**`kQTSCAudioPropertyID_ExtendedProcs
= scExtendedProcsType`**
: A read/write/listen `SCExtendedProcs` value
that is used to get or set an `SCExtendedProcs` structure.

**`kQTSCAudioPropertyID_PreferenceFlags
= scPreferenceFlagsType`**
: A read/write/listen `SInt32` value
that is used to specify dialog preferences such as `scUseMovableModal`.

**`kQTSCAudioPropertyID_WindowOptions
= scWindowOptionsType`**
: A read/write/listen `SCWindowSettings` structure
that is used to set an `SCWindowSettings` structure,
which tells the dialog about its parent window so that it can draw
itself as a sheet on top of the parent.

The following constants are used by movie export `getProperty` functions
only (not `SCAudio`), so that variable
size properties can be handled in that API where there is no associated
size parameter. The `getProperty` function
can be asked the size first, then the caller can allocate memory
for the associated `SCAudio` property
and call `getProperty` again to get the
property.

```
enum {
  movieExportChannelLayoutSize  = 'clsz',                /* UInt32 */
  movieExportMagicCookieSize    = 'mcsz',                /* UInt32 */
  movieExportUseHighResolutionAudioProperties = 'hrau'   /* Boolean */
};
```

The `movieExportUseHighResolutionAudioProperties` constant
is not a size. It is how the exporter asks a propertyProc if it
is prepared to deal with high-res properties.

The `kPropertyClass_MovieExporter` constant
defines the movie exporter class:

```
enum {
    kPropertyClass_MovieExporter = 'spit'
};
```

The `kMovieExporterPropertyID_EnableHighResolutionAudioFeatures` constant
enables high-resolution audio features for `kPropertyClass_MovieExporter`.
Its value is `Boolean`:

```
enum {
    kMovieExporterPropertyID_EnableHighResolutionAudioFeatures = 'hrau'
};
```


Every `SGAudioMediaType` channel
uses standard QuickTime component property selectors to get, set,
and listen to properties. Each component property takes a property class
as well as a property ID. `SGAudioMediaType` channels
use the property classes listed in this section.

```
SGAudioMediaType                       = 'audi'
kQTPropertyClass_SGAudio                 = 'audo'
kQTPropertyClass_SGAudioRecordDevice     = 'audr'
kQTPropertyClass_SGAudioPreviewDevice    = 'audp'
```

**`'audo'`**
: Used with properties that pertain to the `SGChannel` as
a whole, or to the output of an `SGAudioChannel` (that
is, with the resulting track in a QuickTime movie).

**`'audr'`**
: Used with properties that pertain specifically to an `SGAudioChannel` recording
device’s physical settings.

**`'audp'`**
: Used with properties that pertain specifically to an `SGAudioChannel` preview
device’s physical settings.

For the property IDs used with these classes. see `[“SGAudio Component Property IDs”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjqhazts)`.

This section lists the property IDs for `SGAudioMediaType` channels.
Besides the IDs defined below, `SGAudioMediaType` channels
respond to `kComponentPropertyInfoList` and `kComponentPropertyClassPropertyInfo` selectors,
which return `CFDataRef` structures containing
arrays of `ComponentPropertyInfo` structures
as defined in the file `ImageCompression.h`.

**`kQTSGAudioPropertyID_DeviceListWithAttributes
= '#dva'`**
: Used with `kQTPropertyClass_SGAudio` in
read and listen modes to get an array of `CFDictionaryRef` structures.
Each dictionary represents the attributes of one audio device.
See `[Dictionary Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjsgq2to)` for
a list of supported dictionary keys. If the device list changes
(for example, if a device is hotplugged or unplugged), listeners
of this property will be notified. The caller is responsible for
calling `CFRelease` to release the resulting `CFArray`.

**`kQTSGAudioPropertyID_DeviceAttributes
= 'deva'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice` and `kQTPropertyClass_SGAudioPreviewDevice` in
read only mode to get a `CFDictionaryRef` structure
representing the attributes of a specified audio device (record
or preview). See `[Dictionary Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjsgq2to)` for a list of supported dictionary keys. Not all keys
are guaranteed to be present for a given device. The caller is responsible
for calling `CFRelease` to release the
resulting `CFDictionary`.

**`kQTSGAudioPropertyID_DeviceUID
= 'uid ' [last character is space]`**
: Used with `kQTPropertyClass_SGAudioRecordDevice` and `kQTPropertyClass_SGAudioPreviewDevice` in
read and write modes to get a `CFString` with
an audio device’s unique ID for the current recording or preview
or set the current recording or preview device to a specified audio device’s
unique ID. You can obtain a list of devices on the user’s system with `kQTSGAudioPropertyID_DeviceListWithAttributes`.
The caller is responsible for calling `CFRelease` to
release the resulting `CFString`.

**`kQTSGAudioPropertyID_ChannelLayout
= 'clay'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice`, `kQTPropertyClass_SGAudio`,
and `kQTPropertyClass_SGAudioPreviewDevice` in
read and write modes to get or set an `AudioChannelLayout` structure representing
the spatial or discrete channel layout. If used with `kQTPropertyClass_SGAudio`,
the `AudioChannelLayout` refers to the channels in
the resulting QuickTime movie sound track. If used with `kQTPropertyClass_SGAudioRecordDevice`,
the `AudioChannelLayout` refers to the input
channels on the record device. If used with `kQTPropertyClass_SGAudioPreviewDevice`,
the `AudioChannelLayout` refers to the preview
device’s output channels. `AudioChannelLayout` is
a variable size structure, so before calling `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6i)` you
should call `[QTGetComponentPropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6kjnztg6)` to
discover the size of the block of memory you must allocate to hold
the result.

**`kQTSGAudioPropertyID_MagicCookie
= 'kuki'`**
: Used with `kQTPropertyClass_SGAudio` in
read and write modes to access opaque data structures representing
get or set compressor-specific out-of-band settings. This property
is applicable only to compressed formats that use a cookie, such
as AAC and AMR.

**`kQTSGAudioPropertyID_ChannelMap
= 'cmap'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice` in
read and write modes to access a C-style array of `SInt32` structures
that let a client enable or disable channels on a recording device,
as well as reorder them or duplicate them to several output channels.
This property need not be set if a client wishes to capture all
channels from the record device; this is the default behavior.
Each element in the `SInt32` array represents
one output bus (into the `SGAudioChannel`) from
the record device. The value of each element is the zero-based source
channel on the input device that should feed the specified output.
Channel-disabling example: if you wish to capture just the 1st,
3rd, and 5th channels from a 6-channel input device, your channel
map should be `SInt32 map[3] = { 0, 2, 4 }`. Channel-reordering
example: if you wish to capture both channels from a stereo input
device, but you know the left and right channels are reversed in
the data source, set your channel map to
`SInt32 map[2] = { 1, 0 }`.
Channel-duplication example: if you wish to duplicate the second
source channel into 4 outputs, set your channel map to `SInt32
map[4] = { 1, 1, 1, 1` }. Empty channel example:
if you need to produce a conformant stream of audio (such as a 6-channel
stream to send to an external 5.1 AC3 encoder), but you have audio
only for the L, R, and C channels (on record device channels 0,
1, and 2), you may set your channel map to
`SInt32 map[6] = { 0, 1, 2, -1, -1, -1 }`.
The last 3 channels will be filled with silence.

**`kQTSGAudioPropertyID_StreamFormat
= 'frmt'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice`, `kQTPropertyClass_SGAudio`,
and `kQTPropertyClass_SGAudioPreviewDevice` in
read and write modes to access `AudioStreamBasicDescription` structures that
let you get or set the format of the audio as it will be written
to the destination QuickTime movie track. When used with `kQTPropertyClass_SGAudioRecordDevice`,
this property ID gets and sets the format of audio as it is physically
recorded on the device. The format must be one of the formats passed
in `kQTSGAudioPropertyID_StreamFormatList`. The `mChannelsPerFrame` of
the `StreamFormat` read from the record device will
not reflect channels that have been enabled or disabled with the `ChannelMap` property.

**`kQTSGAudioPropertyID_StreamFormatList
= '#frm'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice` and `kQTPropertyClass_SGAudioPreviewDevice` in
read-only mode to get an array of `AudioStreamBasicDescription` structures
that describe valid combinations of settings supported by the physical
device in its current configuration (sample rate, bit depth, number
of channels).

**`kQTSGAudioPropertyID_InputSelection
= 'inpt'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice` in
read and write modes to get an `OSType` value
that lets you change the current input selection in devices that
allow switching between data sources, such as analog, `adat`, `sdi`, `aes`/`ebu`,
and `spdif`. When the
input selection changes, the `StreamFormat` of
the device may change as well; in particular, the number of channels
may change.

**`kQTSGAudioPropertyID_InputListWithAttributes
= '#inp'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice` in
read-only mode to get a `CFArrayRef` structure
that represents the list of available input sources for a given
device. A `CFArrayRef` of `CFDictionaryRef` values
is returned, where each one represents the attributes of one input.
See `[“Dictionary Keys”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjsgq2to)` for
a list of valid keys. The caller is responsible for calling `CFRelease` to
release the returned array.

**`kQTSGAudioPropertyID_OutputSelection
= 'otpt'`**
: Used with `kQTPropertyClass_SGAudioPreviewDevice` in
read and write modes to get an `OSType` value
that lets you change the current output selection in devices that
allow switching between output destinations, such as analog, `adat`, `sdi`, `aes`/`ebu`,
and `spdif`. When the
output selection changes, the `StreamFormat` of
the device may change as well; in particular, the number of channels
may change.

**`kQTSGAudioPropertyID_OutputListWithAttributes
= '#otp'`**
: Used with `kQTPropertyClass_SGAudioPreviewDevice` in
read-only mode to get a `CFArrayRef` structure
that represents the list of available output destinations for a
given device. A `CFArrayRef` of `CFDictionaryRef` values is
returned, where each one represents the attributes of one output.
See `[“Dictionary Keys”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjsgq2to)` for
a list of valid keys. The caller is responsible for calling `CFRelease` to
release the returned array.

**`kQTSGAudioPropertyID_SoundDescription
= 'snds'`**
: Used with `kQTPropertyClass_SGAudio` in
read and write modes to get a `SoundDescriptionHandle` value
for the sound description that describes the data written to a QuickTime
movie track. A `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6i)` call allocates
the `SoundDescriptionHandle` for you. The caller
should declare the `SoundDescriptionHandle` and
set it to `NULL`, then
pass its address to `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6i)`.
The caller must call `DisposeHandle` to
dispose of the resulting `SoundDescriptionHandle` when
done with it.

**`kQTSGAudioPropertyID_LevelMetersEnabled
= 'lmet'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice`, `kQTPropertyClass_SGAudio`,
and `kQTPropertyClass_SGAudioPreviewDevice` in
read and write modes to access a `Boolean` value
that controls metering. When used with `kQTPropertyClass_SGAudioRecordDevice` or `kQTPropertyClass_SGAudioPreviewDevice`,
this property ID turns device level metering on or off. When used
with `kQTPropertyClass_SGAudio`, it turns
output level metering on or off. When level meters are enabled,
you can use `kQTSGAudioPropertyID_AveragePowerLevels` to
get instantaneous levels, or `kQTSGAudioPropertyID_PeakHoldLevels` to
get peak-hold style meters, which are better for clipping detection.
Level meters should be enabled only if you intend to poll for levels,
because they place an added load on the CPU when enabled.

**`kQTSGAudioPropertyID_PeakHoldLevels
= 'phlv'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice`, `kQTPropertyClass_SGAudio`,
and `kQTPropertyClass_SGAudioPreviewDevice` in
read-only mode to get a C-style array of `Float32` values
representing in dB the peak hold levels for each channel on a device
or output. This property ID may be used only when level meters are
enabled (by using `kQTSGAudioPropertyID_LevelMetersEnabled`).
Poll for peak hold levels as often as you would like, to update
the user interface or look for clipping. The number of elements
in the `Float32` array will be equal to the number of
input channels on your record device for `kQTPropertyClass_SGAudioRecordDevice`,
or the number of elements in your `kQTSGAudioPropertyID_ChannelMap`,
if you've set one. It will be equal to the number of output channels
on your preview device for `kQTPropertyClass_SGAudioPreviewDevice` and
equal to the number of channels in your `kQTSGAudioPropertyID_StreamFormat` (`format.mChannelsPerFrame`)
for `kQTPropertyClass_SGAudio`. If
no channel mixdown is being performed between record device and
output formats, then the `kQTSGAudioPropertyID_PeakHoldLevels` values
for `kQTPropertyClass_SGAudioRecordDevice` and `kQTPropertyClass_SGAudio` will
be equivalent. If you have requested hardware playthrough, level metering
will be unavailable.

**`kQTSGAudioPropertyID_AveragePowerLevels
= 'aplv'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice`, `kQTPropertyClass_SGAudio`,
and `kQTPropertyClass_SGAudioPreviewDevice` in
read-only mode to get a C-style array of `Float32` values
representing in dB the average power levels for each channel on
a device or output. This property ID may be used only when level
meters are enabled (by using `kQTSGAudioPropertyID_LevelMetersEnabled`).
Poll for average power levels as often as you would like, to update
the user interface. The number of elements in the `Float32` array
will be equal to the number of input channels on your record device
for `kQTPropertyClass_SGAudioRecordDevice`,
or the number of elements in your `kQTSGAudioPropertyID_ChannelMap`,
if you've set one. It will be equal to the number of output channels
on your preview device for `kQTPropertyClass_SGAudioPreviewDevice` and
equal to the number of channels in your `kQTSGAudioPropertyID_StreamFormat` (`format.mChannelsPerFrame`)
for `kQTPropertyClass_SGAudio`. If
no channel mixdown is being performed between record device and
output formats, then the `kQTSGAudioPropertyID_AveragePowerLevels` values
for `kQTPropertyClass_SGAudioRecordDevice` and `kQTPropertyClass_SGAudio` will
be equivalent. If you have requested hardware playthrough, level metering
will be unavailable.

**`kQTSGAudioPropertyID_Settings
= 'setu'`**
: Used with `kQTPropertyClass_SGAudio` in
read and write modes to access `UserData` values.
This property takes supersedes the `SGGet`/`SetChannelSettings` calls.
An `SGAudioMediaType` channel accepts old-style `'soun'` `SGChannel` settings
in a `[QTSetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctmv2eg33nobxw4zloorihe33qmvzhi6i)` call, but
always produces new-style settings in a `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6i)` call.

**`kQTSGAudioPropertyID_MasterGain
= 'mgan'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice`, `kQTPropertyClass_SGAudio`,
and `kQTPropertyClass_SGAudioPreviewDevice` in
read and write modes to access a `Float32` value
that represents the master gain on a physical recording device with
0.0 = minimum volume and 1.0 = the maximum volume of the device.
With `kQTPropertyClass_SGAudioPreviewDevice`,
this property gets or sets the master gain on the physical previewing
device with 0.0 = minimum volume and 1.0 = the maximum volume of
the device. With `kQTPropertyClass_SGAudio`,
this property gets or sets the master gain (volume) of the recorded
audio data in software (pre-mixdown) with minimum = 0.0, maximum
= unbounded. Normally you wouldn't set the volume greater than
1.0, but if the source sound level provided by the device is too
low, you may set a gain greater than 1.0 to boost the gain. Some devices
cannot respond to this property setting.

**`kQTSGAudioPropertyID_PerChannelGain
= 'cgan'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice`, `kQTPropertyClass_SGAudio`,
and `kQTPropertyClass_SGAudioPreviewDevice` in
read and write modes to access a C-style array of `Float32` value
that represents the gain of each channel on a physical recording
device. The number of channels in the array for `kQTPropertyClass_SGAudioRecordDevice` and `kQTPropertyClass_SGAudioPreviewDevice` is
equal to the total number of channels on the device, which can be
discovered using `kQTSGAudioPropertyID_StreamFormat`.
The number and order of channels in the array for the `kQTPropertyClass_SGAudio` class
must correspond to the valence of channels on the output (which
is affected by a channel map, if you've set one). With `kQTPropertyClass_SGAudio`,
this property gets and sets the gain (volume) of each channel of
recorded audio data in software. Levels set on the record device
or preview device must be in the range minimum = 0.0, maximum =
1.0. Levels set in software may be set to values greater than 1.0
in order to boost low signals. The caller may specify that a particular
channel gain level should be left alone by setting the value to
–1.0. For instance, to set the gain of channels 1, 2, and 3 to
0.5 on a 6 channel device, pass the following array values in a `SetProperty` call: `{
0.5, 0.5, 0.5, -1., -1., -1. }`.

**`kQTSGAudioPropertyID_HardwarePlaythruEnabled
= 'hard'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice` in
read and write modes to access a `Boolean` value
representing the state of hardware playthrough during `seqGrabPreview` or `seqGrabPlayDuringRecord` operations.
Setting this value will have no effect if the record device and preview
device are not the same. Some devices do not support hardware playthrough;
devices report whether or not they support this feature through
the `kQTSGAudioPropertyID_DeviceListWithAttributes` property.

**`kQTSGAudioPropertyID_ChunkSize
= 'chnk'`**
: Used with `kQTPropertyClass_SGAudio` in
read and write modes to access a `Float32` value
representing the number of seconds of audio that the `SGAudioChannel` should
buffer before writing.

**`kComponentPropertyInfoList
= 'list'`**
: Used with `kComponentPropertyClassPropertyInfo` in
read-only mode as defined in the file `ImageCompression.h`.

**`kQTSGAudioPropertyID_DeviceAlive
= 'aliv'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice` and `kQTPropertyClass_SGAudioPreviewDevice` in
read and listen modes to get a `Boolean` value
telling whether or not a device is alive. If the device is hot unplugged,
listeners of this property will be notified. If a record or preview operation
is in progress it will be stopped, but it is left to the client
to select a new device.

**`kQTSGAudioPropertyID_DeviceHogged
= 'hogg'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice` and `kQTPropertyClass_SGAudioPreviewDevice` in
read, write, and listen modes to get a `Boolean` value
telling whether a device has become hogged or unhogged by another
process. If so, listeners of this property will be notified. `SGAudioMediaType` channel
does not hog devices, but a client that has reason to gain exclusive
access to a device may set this property to `TRUE`.

**`kQTSGAudioPropertyID_DeviceInUse
= 'used'`**
: Used with `kQTPropertyClass_SGAudioRecordDevice` and `kQTPropertyClass_SGAudioPreviewDevice` in
read and listen modes to get a `Boolean` value
that tells whether a device is in use. If the device starts to be used
(for instance, when another process starts performing I/O with it), listeners
of this property will be notified.

**`kQTSGAudioPropertyID_MixerCoefficients
= 'mixc'`**
: Used with `kQTPropertyClass_SGAudio` in
read and write modes to access a C-style array of `Float32` values
representing a set of coefficients for mixdown. If you wish to perform
a custom mixdown from the incoming record device channel valence
(discoverable using a combination of `kQTPropertyClass_SGAudioRecordDevice`, `kQTSGAudioPropertyID_StreamFormat`, `kQTPropertyClass_SGAudioRecordDevice`,
and `kQTSGAudioPropertyID_ChannelMap`)
to a different output number of channels (using `kQTPropertyClass_SGAudio` and `kQTSGAudioPropertyID_StreamFormat`),
you may specify your own set of mixer coefficients which will be
set as volume values at each crosspoint in `SGAudioMediaType`’s
internal matrix mixer. The value you pass is a two-dimensional array
of `Float32` values where the first dimension
(rows) is the input channel and the second dimension (columns) is
the output channel. Each `Float32` value contains
one gain level to apply.

**`kQTSGAudioPropertyID_PreMixCallback
= '_mxc'`**
: Used with `kQTPropertyClass_SGAudio` in
read and write modes to access a pre-mix `[SGAudioCallbackStruct](#apple-f4xwc4dqnrsv64tfmyxwgl3umfts6u2hif2wi2lpinqwy3dcmfrwwu3uoj2wg5a)`. If you wish to
receive a callback when new audio samples become available from
a recording device (before they've been mixed down), set this property
using an `[SGAudioCallbackStruct](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvgr2bovsgs32dmfwgyytbmnvvg5dsovrxi)` containing
a pointer to your `SGAudioCallback` function
and a reference constant (_RefCon_).
If you have previously registered a callback and no longer wish
to receive it, call `[QTSetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctmv2eg33nobxw4zloorihe33qmvzhi6i)` again,
this time passing `NULL` for
your _inputProc_ and 0 for your _inputRefCon_.

**`kQTSGAudioPropertyID_PreMixCallbackFormat
= '_mcf'`**
: Used with `kQTPropertyClass_SGAudio` in
read-only mode to get an `AudioStreamBasicDescription` structure
representing the format of the audio that will be received by your
pre-mix `SGAudioCallback` function. Note
that the format may not be available until you've called `SGPrepare`.

**`kQTSGAudioPropertyID_PostMixCallback
= 'mx_c'`**
: Used with `kQTPropertyClass_SGAudio` in
read and write modes to access a post-mix `[SGAudioCallbackStruct](#apple-f4xwc4dqnrsv64tfmyxwgl3umfts6u2hif2wi2lpinqwy3dcmfrwwu3uoj2wg5a)`.If
you wish to receive a callback after audio samples have been mixed
(the first step after they are received from a recording device
by `SGAudioMediaType` channel), set this property
ID using an `SGAudioCallbackStruct` containing
a pointer to your `SGAudioCallback` function
and a reference constant (_RefCon_).
If you have previously registered a callback and no longer wish
to receive it, call `[QTSetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctmv2eg33nobxw4zloorihe33qmvzhi6i)` again,
this time passing `NULL` for
your _inputProc_ and 0 for your _inputRefCon_.

**`kQTSGAudioPropertyID_PostMixCallbackFormat
= 'm_cf'`**
: Used with `kQTPropertyClass_SGAudio` in
read-only mode to get an `AudioStreamBasicDescription` structure
representing the format of the audio that will be received by your
post-mix `SGAudioCallback` function. Note
that the format may not be available until you've called `SGPrepare`.

**`kQTSGAudioPropertyID_PreConversionCallback
= '_cvc'`**
: Used with `kQTPropertyClass_SGAudio` in
read and write modes to access a pre-conversion `[SGAudioCallbackStruct](#apple-f4xwc4dqnrsv64tfmyxwgl3umfts6u2hif2wi2lpinqwy3dcmfrwwu3uoj2wg5a)`. If you wish to
receive a callback just before audio samples are about to be sent
through an audio converter (for format conversion or compression),
set this property ID using an `SGAudioCallbackStruct` containing
a pointer to your `SGAudioCallback` function
and a reference constant (_RefCon_).
If you have previously registered a callback and no longer wish
to receive it, call `[QTSetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctmv2eg33nobxw4zloorihe33qmvzhi6i)` again,
this time passing `NULL` for
your _inputProc_ and 0 for your _inputRefCon_.

**`kQTSGAudioPropertyID_PreConversionCallbackFormat
= '_ccf'`**
: Used with `kQTPropertyClass_SGAudio` in
read-only mode to get an `AudioStreamBasicDescription` structure
representing the format of the audio that will be received by your
pre-conversion `SGAudioCallback` function.
Note that the format may not be available until you've called `SGPrepare`.

**`kQTSGAudioPropertyID_PostConversionCallback
= 'cv_c'`**
: Used with `kQTPropertyClass_SGAudio` in
read and write modes to access a post-conversion `[SGAudioCallbackStruct](#apple-f4xwc4dqnrsv64tfmyxwgl3umfts6u2hif2wi2lpinqwy3dcmfrwwu3uoj2wg5a)`. If you wish to
receive a callback right after audio samples have been sent through
an audio converter (for format conversion or compression), set this
property ID using an `SGAudioCallbackStruct` containing
a pointer to your `SGAudioCallback` function
and a reference constant (_RefCon_).
If you have previously registered a callback and no longer wish
to receive it, call `[QTSetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctmv2eg33nobxw4zloorihe33qmvzhi6i)` again,
this time passing `NULL` for
your _inputProc_ and 0 for your _inputRefCon_.

**`kQTSGAudioPropertyID_PostConversionCallbackFormat
= 'c_cf'`**
: Used with `kQTPropertyClass_SGAudio` in
read-only mode to get an `AudioStreamBasicDescription` structure
representing the format of the audio that will be received by your
post-conversion `SGAudioCallback` function.
Note that the format may not be available until you've called `SGPrepare`.

The following constants identify sound description
properties.

```
enum {
    kQTSoundDescriptionPropertyID_AudioChannelLayout = 'clay',
    kQTSoundDescriptionPropertyID_MagicCookie = 'kuki',
    kQTSoundDescriptionPropertyID_AudioStreamBasicDescription = 'asbd',
    kQTSoundDescriptionPropertyID_UserReadableText = 'text'
};
```

**`kQTSoundDescriptionPropertyID_AudioChannelLayout
= 'clay'`**
: Used to get or set an `AudioChannelLayout` value.
This is a variable-size property because it may contain an array
of Channel Descriptions. You must get the size by calling `[QTSoundDescriptionGetPropertyInfo](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctn52w4zcemvzwg4tjob2gs33oi5sxiudsn5ygk4tupfew4ztp)`,
allocate a structure of that size, and then get the property.

**`kQTSoundDescriptionPropertyID_MagicCookie
= 'kuki'`**
: Used to get or set opaque bytes. This is a variable-size
property, because it is completely defined by the codec that uses
the cookie. You must get the size by calling `[QTSoundDescriptionGetPropertyInfo](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctn52w4zcemvzwg4tjob2gs33oi5sxiudsn5ygk4tupfew4ztp)`,
allocate a structure of that size, and then get the property.

**`kQTSoundDescriptionPropertyID_AudioStreamBasicDescription
= 'asbd'`**
: Used to get an `AudioStreamBasicDescription` value.

**`kQTSoundDescriptionPropertyID_UserReadableText
= 'text'`**
: Used to get a `CFStringRef` value. `[QTSoundDescriptionGetProperty](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctn52w4zcemvzwg4tjob2gs33oi5sxiudsn5ygk4tupe)` does
a `CFRetain` of the returned `CFString` on
behalf of the caller, so the caller is responsible for calling `CFRelease` on
the returned `CFString`.

The following constants identify audio properties.

```
enum {
    kQTAudioPropertyID_Gain = 'gain',
    kQTAudioPropertyID_Mute = 'mute',
    kQTAudioPropertyID_Balance = 'bala',
    kQTAudioPropertyID_Fade = 'fade',
    kQTAudioPropertyID_SummaryChannelLayout = 'clay',
    kQTAudioPropertyID_DeviceChannelLayout = 'dcly',
    kQTAudioPropertyID_FormatString = 'fstr',
    kQTAudioPropertyID_ChannelLayoutString = 'lstr',
    kQTAudioPropertyID_SampleRateString = 'rstr',
    kQTAudioPropertyID_SampleSizeString = 'sstr',
    kQTAudioPropertyID_BitRateString = 'bstr',
    kQTAudioPropertyID_SummaryString = 'asum'
};
```

**`kQTAudioPropertyID_Gain
= 'gain'`**
: Used to get and set a `Float32` value
that represents the audio gain of a movie or track. The gain level
is multiplicative; eg. 0.0 is silent, 0.5 is –6dB, 1.0 is 0dB
(ie. the audio from the movie is not modified), 2.0 is +6dB, etc.
The gain level can be set higher than 1.0 in order to allow quiet
movies and tracks to be boosted in volume. Settings higher than
1.0 may result in audio clipping, of course. The setting is not
stored in the movie or track; it is used only until the movie or
track is disposed.

**`kQTAudioPropertyID_Mute
= 'mute'`**
: Used to get and set a `Boolean` value
that indicates the audio mute state of a movie or track. If TRUE,
the movie or track is muted. The setting is not stored in the movie
or track; it is used only until the movie or track is disposed.

**`kQTAudioPropertyID_Balance
= 'bala'`**
: Used to get and set a `Float32` value
that represents the audio balance of a movie. It is supported only
for movies, not tracks. –1.0 means full left, 0.0 means centered,
and 1.0 means full right. The setting is not stored in the movie;
it is used only until the movie is disposed.

**`kQTAudioPropertyID_Fade
= 'fade'`**
: Used to get and set a `Float32` value
that represents the audio fade of a movie. It is supported only
for movies, not tracks. 1.0 means full forward, 0.0 means centered,
and –1.0 means full rearward. The setting is not stored in the
movie; it is used only until the movie is disposed.

**`kQTAudioPropertyID_SummaryChannelLayout
= 'clay'`**
: Used to get an `AudioChannelLayout` value
that represents the summary audio channel layout of a movie or other
grouping of audio streams. All like-labelled channels are combined,
so there are no duplicates. For example, if there is a stereo (L/R)
track, 5 single-channel tracks marked Left, Right, Left Surround,
Right Surround and Center, and a 4 channel track marked L/R/Ls/Rs,
then the summary AudioChannelLayout will be L/R/Ls/Rs/C—It will
_not_ be L/R/L/R/Ls/Rs/C/L/R/Ls/Rs. This is a variable-size property,
because it it may contain an array of channel descriptions. You
must get the size by calling a function such as `[QTGetMoviePropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2e233wnfsva4tpobsxe5dzjfxgm3y)`,
allocate a structure of that size, and then get the property.

**`kQTAudioPropertyID_DeviceChannelLayout
= 'dcly'`**
: Used to get an `AudioChannelLayout` value
that represents the audio channel layout of the device a movie is
playing to. This is a variable-size property, because it it may
contain an array of channel descriptions. You must get the size
by calling a function such as `[QTGetMoviePropertyInfo](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2e233wnfsva4tpobsxe5dzjfxgm3y)`, allocate
a structure of that size, and then get the property.

**`kQTAudioPropertyID_FormatString
= 'fstr'`**
: Used with `kQTPropertyClass_Audio` to
get a `CFStringRef` value containing a localized,
human readable string that describes an audio format; for example,
“MPEG Layer 3.” You may get this property from a `SoundDescription` handle
by calling `[QTSoundDescriptionGetProperty](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctn52w4zcemvzwg4tjob2gs33oi5sxiudsn5ygk4tupe)` or from
a `StandardAudioCompression` (`scdi` or `audi`)
component instance by calling `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6i)`.

**`kQTAudioPropertyID_ChannelLayoutString
= 'lstr'`**
: Used with `kQTPropertyClass_Audio` to
get a `CFStringRef` value containing a localized,
human readable string that describes an audio channel layout; for
example, “5.0 (L R C Ls Rs).” You may get this property from
a `SoundDescription` handle by calling `[QTSoundDescriptionGetProperty](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctn52w4zcemvzwg4tjob2gs33oi5sxiudsn5ygk4tupe)` or
from a `StandardAudioCompression` (`scdi` or `audi`)
component instance by calling `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6i)`.

**`kQTAudioPropertyID_SampleRateString
= 'rstr'`**
: Used to get a `CFStringRef` value
containing a localized, human readable string that describes an
audio sample rate; for example, “44.100 kHz.” You may get this
property from a `SoundDescription` handle by
calling `[QTSoundDescriptionGetProperty](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctn52w4zcemvzwg4tjob2gs33oi5sxiudsn5ygk4tupe)` or
from a `StandardAudioCompression` (`scdi` or `audi`)
component instance by calling `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6i)`.

**`kQTAudioPropertyID_SampleSizeString
= 'sstr'`**
: Used to get a `CFStringRef` value
containing a localized, human readable string that describes an
audio sample size; for example, “24-bit.” This property will
return a valid string only if the audio format is uncompressed (LPCM).
You may get this property from a `SoundDescription` handle
by calling `[QTSoundDescriptionGetProperty](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctn52w4zcemvzwg4tjob2gs33oi5sxiudsn5ygk4tupe)` or
from a `StandardAudioCompression` (`scdi` or `audi`)
component instance by calling `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6i)`.

**`kQTAudioPropertyID_BitRateString
= 'bstr'`**
: Used to get a `CFStringRef` value
containing a localized, human readable string that describes an
audio bit rate; for example, “12 kbps.” You may get this property
from a `StandardAudioCompression` (`scdi` or `audi`) component
instance by calling `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6i)`.

**`kQTAudioPropertyID_SummaryString
= 'asum'`**
: Used to get a `CFStringRef` value
containing a localized, human readable string that summarizes an
audio format; for example, “16-bit Integer (Big Endian), Stereo
(L R), 48.000 kHz.” You may get this property from a `SoundDescription` handle
by calling `[QTSoundDescriptionGetProperty](#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvctn52w4zcemvzwg4tjob2gs33oi5sxiudsn5ygk4tupe)` or from
a `StandardAudioCompression` (`scdi` or `audi`)
component instance by calling `[QTGetComponentProperty](../../../WhatsNewQT6_4/Chap1/QT6WhatsNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df5rv64tfmyxvcvchmv2eg33nobxw4zloorihe33qmvzhi6i)`.

The dictionary keys listed in this section
are used with c ertain of the property IDs listed in `[“SGAudio Component Property IDs”](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrtfvbuqmzrgqwtknjqhazts)`. They may be used to parse CF dictionaries returned
by `kQTSGAudioPropertyID_DeviceListWithAttributes` and `kQTSGAudioPropertyID_DeviceAttributes` IDs
for `SGAudioMediaType` channels.

**`kQTAudioDeviceAttribute_DeviceUIDKey
= 'uid '`**
: A `CFStringRef` containing a unique
identifier for a device.

**`kQTAudioDeviceAttribute_DeviceNameKey
= 'name'`**
: A `CFStringRef` containing a device’s
printable name, suitable for the user interface.

**`kQTAudioDeviceAttribute_DeviceManufacturerKey
= 'manu'`**
: A `CFStringRef` containing a device
manufacturer’s printable name, suitable for the user interface.

**`kQTAudioDeviceAttribute_DeviceTransportTypeKey
= 'tran'`**
: A `CFNumberRef` that wraps an `OSType`;
for example, `'1394'` for `fw`.
See the file `IOAudioTypes.h`.

**`kQTAudioDeviceAttribute_DeviceAliveKey
= 'aliv'`**
: A `CFBooleanRef` value that is `TRUE` if
the device is present.

**`kQTAudioDeviceAttribute_DeviceCanRecordKey
= 'rec ' [last char = space]`**
: A `CFBooleanRef` value that is `TRUE` if
the device can be used for recording (some devices can only play
back).

**`kQTAudioDeviceAttribute_DeviceCanPreviewKey
= 'prev'`**
: A `CFBooleanRef` value that is `TRUE` if
the device can be used to preview a grabbed sequence.

**`kQTAudioDeviceAttribute_DeviceHoggedKey
= 'hogg'`**
: A `CFNumberRef` that wraps the unique
process ID that is hogging the device, or –1 if the device is
currently not being hogged. The process ID comes from a call to `getpid`.

**`kQTAudioDeviceAttribute_DeviceInUseKey
= 'used'`**
: A `CFBooleanRef` value that is `TRUE` if
the device is performing I/O in any process.

**`kQTAudioDeviceAttribute_DeviceSupportsHardwarePlaythruKey
= 'hard'`**
: A `CFBooleanRef` value that is `TRUE` if
the device supports hardware playthrough of inputs to outputs.

**`kQTAudioDeviceAttribute_DefaultInputDeviceKey
= 'dIn ' [last char = space]`**
: A `CFBooleanRef` value that’s `TRUE` if
the device is the user-selected default input in an audio MIDI setup.

**`kQTAudioDeviceAttribute_DefaultOutputDeviceKey
= 'dOut'`**
: A `CFBooleanRef` value that’s `TRUE` if
the device is the user-selected default output in an audio MIDI
setup.

**`kQTAudioDeviceAttribute_DefaultSystemOutputDeviceKey
= 'sOut'`**
: A `CFBooleanRef` value that’s `TRUE` if
the device is the user-selected device where system alerts play.

**`kQTAudioDeviceAttribute_IsCoreAudioDeviceKey
= 'hal!'`**
: A `CFBooleanRef` value that’s `TRUE` if
the device is a Core Audio device.

The following dictionary keys may be used
to parse CF dictionaries returned by `kQTSGAudioPropertyID_DeviceListWithAttributes` and `kQTSGAudioPropertyID_DeviceAttributes` IDs
for `SGAudioMediaType` channels.

**`kQTAudioDeviceAttribute_DeviceInputID
= 'inID'`**
: A `CFNumberRef` that wraps an `OSType` value.

**`kQTAudioDeviceAttribute_DeviceInputDescription
= 'inds'`**
: A `CFStringRef` that is suitable
for displaying to the user.

**`kQTAudioDeviceAttribute_DeviceOutputID
= 'otID'`**
: A `CFNumberRef` that wraps an `OSType` value.

**`kQTAudioDeviceAttribute_DeviceOutputDescription
= 'otds'`**
: A `CFStringRef` that is suitable
for displaying to the user.

The following setting codes are used by
sequence grabber channels of type `SGAudioMediaType`.

```
enum {
  sgcAudioRecordDeviceSettingsAtom  = kQTPropertyClass_SGAudioRecordDevice,
  sgcAudioPreviewDeviceSettingsAtom = kQTPropertyClass_SGAudioPreviewDevice,
  sgcAudioOutputSettingsAtom        = kQTPropertyClass_SGAudio,
  sgcAudioSettingsVersion           = 'vers',
  sgcAudioDeviceUID                 = kQTAudioDeviceAttribute_DeviceUIDKey,
  sgcAudioDeviceName                = kQTAudioDeviceAttribute_DeviceNameKey,
  sgcAudioStreamFormat              = kQTSGAudioPropertyID_StreamFormat,
  sgcAudioInputSelection            = kQTSGAudioPropertyID_InputSelection,
  sgcAudioOutputSelection           = kQTSGAudioPropertyID_OutputSelection,
  sgcAudioChannelMap                = kQTSGAudioPropertyID_ChannelMap,
  sgcAudioMasterGain                = kQTSGAudioPropertyID_MasterGain,
  sgcAudioPerChannelGain            = kQTSGAudioPropertyID_PerChannelGain,
  sgcAudioLevelMetersEnabled        =     kQTSGAudioPropertyID_LevelMetersEnabled,
  sgcAudioChannelLayout             = kQTSGAudioPropertyID_ChannelLayout,
  sgcAudioMixerCoefficients         = kQTSGAudioPropertyID_MixerCoefficients,
  sgcAudioMagicCookie               = kQTSGAudioPropertyID_MagicCookie
};
```


The format constants in this section are
used with functions of the form `QTMetaData`...

Following are constants for the `QTMetaDataStorageFormat` type:

**`kQTMetaDataStorageFormatQuickTime
= 'mdta'`**
: The QuickTime metadata storage format

**`kQTMetaDataKeyFormatQuickTime
= 'mdta'`**
: Reverse DNS format

**`kQTMetaDataStorageFormatiTunes
= 'itms'`**
: The iTunes metadata storage format

Following are constants for the `QTMetaDataKeyFormat` type:

**`kQTMetaDataKeyFormatiTunesShortForm
= 'itsk'`**
: A four-character code

**`kQTMetaDataKeyFormatiTunesLongForm
= 'itlk'`**
: Reverse DNS format

Following are constants for user data formats:

**`kQTMetaDataStorageFormatUserData
= 'udta'`**
: User data storage format

**`kQTMetaDataKeyFormatUserData
= 'udta',`**
: User data key storage format

The property IDs in this section are used
with functions of the form `QTMetaData`...

Following are constants for the `QTMetaDataRef` type:

**`kPropertyClass_QTMetaData
= 'meta'`**
: The QuickTime metadata property class.

**`kQTMetaDataPropertyID_StorageFormats
= 'fmts'`**
: The list of storage formats of type `QTMetaDataStorageFormat` associated with
a `QTMetaDataRef` object. The read-only return
value is a C-style array of `OSType` values.

**`kQTMetaDataPropertyID_OwnerType
= 'ownt'`**
: The owner type associated with a `QTMetaDataRef` object.
The read-only return value is an `OSType` (`QT_MOVIE_TYPE`, `QT_TRACK_TYPE`,
or `QT_MEDIA_TYPE`).

**`kQTMetaDataPropertyID_Owner
= 'ownr'`**
: The owner associated with a `QTMetaDataRef` object,
which does not necessarily need an owner. The read-only return value
is type `Movie`, `Track`,
or `Media`.

Following are constants for the `QTMetaDataItem` type:

**`kPropertyClass_QTMetaDataItem
= 'mdit'`**
: The metadata item property class ID

**`kQTMetaDataItemPropertyID_Value
= 'valu'`**
: The value of the metadata item. The read-only return
value is a C-style array of values of type `UInt8`.

**`kQTMetaDataItemPropertyID_DataType
= 'dtyp'`**
: The value type of the metadata item. The read/write
return value is type `UInt32`.

**`kQTMetaDataItemPropertyID_StorageFormat
= 'sfmt'`**
: The storage format of the metadata item. The read-only
return value is type `QTMetaDataStorageFormat`.

**`kQTMetaDataItemPropertyID_Key
= 'key '` [last char is space]**
: The key associated with the metadata item. The read/write
return value is a C-style array of values of type `UInt8`.

**`kQTMetaDataItemPropertyID_KeyFormat
= 'keyf'`**
: The format of the metadata item key. The read/write
return value is type `OSType`.

**`kQTMetaDataItemPropertyID_Locale
= 'loc '`**
: The locale identifier based on the naming convention
defined by the International Components for Unicode (ICU). The identifier
consists of two pieces of ordered information: a language code and
a region code. The language code is based on the ISO 639-1 standard,
which defines two-character codes, such as `en` and `fr`,
for the world’s most commonly used languages. If a two-letter
code is not available, then ISO 639-2 three-letter identifiers are
accepted as well; for example, `haw` for
Hawaiian. The region code is defined by ISO 3166-1. It is all uppercase
and is appended, with an underscore, after the language code; for
example `en_US`, `en_GB`,
and `fr_FR`. The read/write return
value is a C string of type `UInt32`.

The following key constants are used with
functions of the form `QTMetaData`...

```swift
// Pre-defined common keys
    kQTMetaDataCommonKeyAuthor         = 'auth'
    kQTMetaDataCommonKeyComment        = 'cmmt'
    kQTMetaDataCommonKeyCopyright      = 'cprt'
    kQTMetaDataCommonKeyDirector       = 'dtor'
    kQTMetaDataCommonKeyDisplayName    = 'name'
    kQTMetaDataCommonKeyInformation    = 'info'
    kQTMetaDataCommonKeyKeywords       = 'keyw'
    kQTMetaDataCommonKeyProducer       = 'prod'

// Mapping from common keys to user data identifiers:
    kQTMetaDataCommonKeyAuthor         -> kUserDataTextAuthor
    kQTMetaDataCommonKeyComment        -> kUserDataTextComment
    kQTMetaDataCommonKeyCopyright      -> kUserDataTextCopyright
    kQTMetaDataCommonKeyDirector       -> kUserDataTextDirector
    kQTMetaDataCommonKeyDisplayName    -> kUserDataTextFullName
    kQTMetaDataCommonKeyInformation    -> kUserDataTextInformation
    kQTMetaDataCommonKeyKeywords       -> kUserDataTextKeywords
    kQTMetaDataCommonKeyProducer       -> kUserDataTextProducer
```


The following error codes are returned by
functions of the form `QTMetaData`...

```
kQTMetaDataInvalidMetaDataErr         = -2173
kQTMetaDataInvalidItemErr             = -2174
kQTMetaDataInvalidStorageFormatErr    = -2175
kQTMetaDataInvalidKeyFormatErr        = -2176
kQTMetaDataNoMoreItemsErr             = -2177
```


The following codes are stored in the _propClass_ fields
of `[QTNewMoviePropertyElement](#apple-f4xwc4dqnrsv64tfmyxwgl3umfts6ukujzsxotlpozuwkudsn5ygk4tupfcwyzlnmvxhi)` data
structures, which pass them to `[NewMovieFromProperties](#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2omv3u233wnfsum4tpnvihe33qmvzhi2lfom)`.

```
kQTPropertyClass_DataLocation = 'dloc',
        kQTDataLocationPropertyID_DataReference             = 'dref',
           // DataReferenceRecord *
        kQTDataLocationPropertyID_CFStringNativePath        = 'cfnp',
           // CFStringRef *
        kQTDataLocationPropertyID_CFStringPosixPath         = 'cfpp',
           // CFStringRef *
        kQTDataLocationPropertyID_CFStringHFSPath           = 'cfhp',
           // CFStringRef *
        kQTDataLocationPropertyID_CFStringWindowsPath       = 'cfwp',
           // CFStringRef *
        kQTDataLocationPropertyID_CFURL                     = 'cfur',
           // CFURLRef *
        kQTDataLocationPropertyID_QTDataHandler             = 'qtdh',
           // DataHandler *
        kQTDataLocationPropertyID_Scrap                     = 'scrp',
           // NULL
        kQTDataLocationPropertyID_LegacyMovieResourceHandle = 'rezh',
           // Handle *
        kQTDataLocationPropertyID_MovieUserProc             = 'uspr',
           // QTNewMovieUserProcRecord *
        kQTDataLocationPropertyID_ResourceFork              = 'rfrk',
           // SInt16 *
        kQTDataLocationPropertyID_DataFork                  = 'dfrk',
           // SInt16 *

 kQTPropertyClass_Context = 'ctxt',
        kQTContextPropertyID_AudioContext       = 'audi',
           // QTAudioContextRef *
        kQTContextPropertyID_VisualContext      = 'visu',
           // QTVisualContextRef *

 kQTPropertyClass_MovieResourceLocator = 'rloc',
        kQTMovieResourceLocatorPropertyID_LegacyResID   = 'rezi',
           // SInt16 * (input/output property)
        kQTMovieResourceLocatorPropertyID_LegacyResName = 'rezn',
           // Str255   (output property)
        kQTMovieResourceLocatorPropertyID_FileOffset    = 'foff',
           // UInt64 *
        kQTMovieResourceLocatorPropertyID_Callback      = 'calb',
           // User-defined

 kQTPropertyClass_MovieInstantiation = 'mins',
        kQTMovieInstantiationPropertyID_DontResolveDataRefs         = 'rdrn',
           // Boolean *
        kQTMovieInstantiationPropertyID_DontAskUnresolvedDataRefs   = 'aurn',
           // Boolean *
        kQTMovieInstantiationPropertyID_DontAutoAlternates          = 'aaln',
           // Boolean *
        kQTMovieInstantiationPropertyID_DontUpdateForeBackPointers  = 'fbpn',
           // Boolean *
        kQTMovieInstantiationPropertyID_AsyncOK                     = 'asok',
           // Boolean *
        kQTMovieInstantiationPropertyID_IdleImportOK                = 'imok',
           // Boolean *
        kQTMovieInstantiationPropertyID_DontAutoUpdateClock         = 'aucl',
           // Boolean *
        kQTMovieInstantiationPropertyID_ResultDataLocationChanged   = 'dlch',
           // Boolean * (output property)

 kQTPropertyClass_NewMovieProperty = 'mprp',
        kQTNewMoviePropertyID_DefaultDataRef        = 'ddrf',
           // DataReferenceRecord *
        kQTNewMoviePropertyID_Active                = 'actv',
           // Boolean *
        kQTNewMoviePropertyID_DontInteractWithUser  = 'intn',
           // Boolean *
```

[Next](Document%20Revision%20History.md)[Previous](What%E2%80%99s%20New%20in%20QuickTime%207.md)

