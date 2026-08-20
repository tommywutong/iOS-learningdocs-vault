---
title: Compression Sessions - Multipass encoding and the pass mode flags
apple_id: DTS10003831
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-10-02'
source_url: https://developer.apple.com/library/archive/qa/qa1457/_index.html
archived_at: '2026-07-18T02:30:52.441967Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1457

# Compression Sessions - Multipass encoding and the pass mode flags

## Q:  When performing multipass encoding how are the compression pass mode flags used with `ICMCompressionSessionBeginPass`?

A: QuickTime 7 defines five `ICMCompressionPassModeFlags` in ImageCompression.h:

- `kICMCompressionPassMode_OutputEncodedFrames` - Set during an encoding pass, the compressor must output encoded frames. This flag can only be set once the `kICMCompressionPassMode_NotReadyToOutputEncodedFrames` flag has been cleared.
- `kICMCompressionPassMode_NoSourceFrames` - If the compressor has set this flag for the pass, the client should not provide source frame buffers and may pass NULL pixel buffers to `ICMCompressionSessionEncodeFrame`.
- `kICMCompressionPassMode_WriteToMultiPassStorage` - Set during an analysis pass, the compressor does not output encoded frames but records compressor-private information for each frame to the multipass storage.
- `kICMCompressionPassMode_ReadFromMultiPassStorage` - Set during repeated analysis passes and the encoding pass, the compressor may refer to the compressor-private information and use it to improve encoding.
- `kICMCompressionPassMode_NotReadyToOutputEncodedFrames` - The compressor will set this flag to indicate that it will not be able to output encoded frames in the coming pass. Once this flag has been cleared, the client may set the `kICMCompressionPassMode_OutputEncodedFrames` flag when calling `ICMCompressionSessionBeginPass` to cut short a compression operation.

When multipass encoding is enabled (see [Technical Q&A QA1450, 'Compression Sessions - Enabling multi-pass encoding'](https://developer.apple.com/qa/qa2005/qa1450.html)), calls to `ICMCompressionSessionEncodeFrame` must be bracketed by `ICMCompressionSessionBeginPass` and `ICMCompressionSessionEndPass`.

During a multipass encoding session, a multipass capable compressor has a lot of latitude with the type of work it performs in each pass. The client doesn't really get to know the details of a pass, nor is it told ahead of time how many passes there will be.

The pass mode flags are used to communicate the compressors state in a given pass and allow the client to modify this state when calling `ICMCompressionSessionBeginPass`. For example, the client could choose to write out an "early generation preview" of pass 3 of a 5-pass export operation by setting the `kICMCompressionPassMode_OutputEncodedFrames` flag once the compressor has cleared the `kICMCompressionPassMode_NotReadyToOutputEncodedFrames` flag. Doing so can cut short a compression operation forcing the compressor to output frames before all of its passes are done.

Table 1 as an example shows a list of passes and their corresponding pass mode flags during a hypothetical encoding session. A client choosing to let the pass mode flags go though without modification would observe the results listed. Alternatively, the client could set the `kICMCompressionPassMode_OutputEncodedFrames` flag for pass 3 and either stop after that pass, or preview the results and continue on to later passes for better results.

__Table 1__  Pass mode flags during a hypothetical encoding session.

| Pass | Pass Mode Flags |
| 1 | kICMCompressionPassMode_WriteToMultiPassStorage | kICMCompressionPassMode_NotReadyToOutputEncodedFrames |
| 2 | kICMCompressionPassMode_ReadFromMultiPassStorage | kICMCompressionPassMode_WriteToMultiPassStorage I kICMCompressionPassMode_NotReadyToOutputEncodedFrames |
| 3 | kICMCompressionPassMode_ReadFromMultiPassStorage I kICMCompressionPassMode_WriteToMultiPassStorage |
| 4 | kICMCompressionPassMode_NoSourceFrames I kICMCompressionPassMode_ReadFromMultiPassStorage I kICMCompressionPassMode_OutputEncodedFrames |

The pass mode flags are used with three APIs:


```
Boolean ICMCompressionSessionSupportsMultiPassEncoding(ICMCompressionSessionRef session,
                                                       UInt32 multiPassStyleFlags,
                                                       ICMCompressionPassModeFlags *firstPassModeFlagsOut)
Discussion:

The client should make this call before starting a multipass compression operation to query whether
a compression session supports multipass encoding. If it does, this call returns the initial state of
the pass mode flags in the firstPassModeFlagsOut parameter.

Parameters:

multiPassStyleFlags - Reserved, set to 0

firstPassModeFlagsOut ( read ) - A pointer to a variable to receive the session’s recommended mode
flags for the first pass. The client may modify these flags, but should not set
kICMCompressionPassMode_NoSourceFrames. Pass NULL if you do not want this information.
```



```
OSStatus ICMCompressionSessionBeginPass(ICMCompressionSessionRef session,
                                        ICMCompressionPassModeFlags passModeFlags,
                                        UInt32 flags)

Discussion:

The client must make this call to signal the start of a specific compression pass. The client can
describe how the compressor should behave in this pass by passing in the pass mode flags in the
parameter passModeFlags.

Parameters:

passModeFlags ( write ) - Flags that describe how the compressor should behave in this pass.

flags - Reserved. Set to 0.
```



```
OSStatus ICMCompressionSessionProcessBetweenPasses(ICMCompressionSessionRef session,
                                                   UInt32 flags,
                                                   Boolean *interpassProcessingDoneOut,
                                                   ICMCompressionPassModeFlags *requestedNextPassModeFlagsOut)

Discussion:

The client must make this call after calling ICMCompressionSessionEndPass to let the compressor perform
processing between passes, but only if kICMCompressionPassMode_OutputEncodedFrames has not been set.

Parameters:

session - A compression session reference. This reference is returned by ICMCompressionSessionCreate.

flags - Reserved. Set to 0.

interpassProcessingDoneOut - A pointer to a Boolean that will be set to FALSE if this function
should be called again, TRUE if it should not be called again.

requestedNextPassModeFlagsOut ( read ) - A pointer to a variable that will be set to the
compressors recommended mode flags for the next pass. kICMCompressionPassMode_OutputEncodedFrames will
be set only if it recommends that the next pass be the final one.
```

The compressor drives the number of passes and communicates state though these flags and the client is not required to change them. For example, the compressor will set `kICMCompressionPassMode_NoSourceFrames` when it doesn't need pixel buffers from the client, or `kICMCompressionPassMode_OutputEncodedFrames` when it will output encoded frames on the next pass.

__Listing 1__  Pseudo code - Pass mode flags in use.

```
ICMCompressionPassModeFlags passModeFlags = 0;
Boolean multipassYES = false;
Boolean done = false;

...

// passModeFlags recieve the session's requested mode flags for the first pass
multipassYES = ICMCompressionSessionSupportsMultiPassEncoding(session,
                                                              0,
                                                              &passModeFlags);

while(!done) {

    if (multipassYES) {
        // passModeFlags describe how the compressor should behave in this pass
        // the client may modify the pass mode flags and set
        // kICMCompressionPassMode_OutputEncodedFrames to force frames to be output
        // prematurely if desired in this pass once the codec has cleared the
        // kICMCompressionPassMode_NotReadyToOutputEncodedFrames flag
        ICMCompressionSessionBeginPass(session, passModeFlags, 0);
    }

    // Feed all the frames to the compression session
    // The source frames and frame options for each display timestamp
    // must be the same across passes
    for (frameNumber = 1; frameNumber <= kFrameCount; frameNumber++) {

        if (0 == (passModeFlags & kICMCompressionPassMode_NoSourceFrames)) {
            // provide the source frames here - kICMCompressionPassMode_NoSourceFrames
            // is NOT set -- if it was set, then don't provide source frames to
            // ICMCompressionSessionEncodeFrame pass NULL for the pixelBuffer
            // parameter but make sure to supplying all the other information
            // consistently between passes

            ...
        }

        ICMCompressionSessionEncodeFrame(...)
    }

    ICMCompressionSessionCompleteFrames(...)

    if (multipassYES) {
        ICMCompressionSessionEndPass(session);

        if (passModeFlags & kICMCompressionPassMode_OutputEncodedFrames) {
             // the compressor has output encoded frames in this pass so we choose to be done
             // NOTE: a client could add code to provide an early preview and continue as documented in QA1457
             done = true;
        } else {
            Boolean interpassDone = false;

            while(!interpassDone) {
                // passModeFlags will be set to the sessions recommended mode flags
                // for the next pass. kICMCompressionPassMode_OutputEncodedFrames will
                // only be set if the codec recommends that the next pass be the last
                ICMCompressionSessionProcessBetweenPasses(session,
                                                          0,
                                                          &interpassDone,
                                                          &passModeFlags);
            }
        }
    } else {
        done = true;
    }
}
```


[QuickTime 7 Update Guide - Video Enhancements](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7UpdateGuide/Chapter02/chapter_2_section_7.html#//apple_ref/doc/uid/TP40001163-CH313-BBCGDBDF)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-10-02 | Editorial |
| 2006-01-18 | New document that discusses how the pass mode flags work when performing multipass compression operations. |

