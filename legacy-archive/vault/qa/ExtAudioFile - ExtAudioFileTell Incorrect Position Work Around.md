---
title: ExtAudioFile - ExtAudioFileTell Incorrect Position Work Around
apple_id: DTS40009410
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2009-12-07'
source_url: https://developer.apple.com/library/archive/qa/qa1678/_index.html
archived_at: '2026-07-18T02:33:46.470532Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1678

# ExtAudioFile - ExtAudioFileTell Incorrect Position Work Around

## Q:  I'm calling `ExtAudioFileTell` for a .m4a file containing AAC audio (immediately after I set the client format) and the API returns a value of -2112 instead of 0. Is this a know issue?

A: I'm calling `ExtAudioFileTell` for a .m4a file containing AAC audio (immediately after I set the client format) and the API returns a value of -2112 instead of 0. Is this a know issue?

`ExtAudioFileTell` currently always returns a value which is the number of priming-frames too small.

The `ExtAudioFile` APIs __should__ take care of this priming offset on behalf of the client however, as the AAC bitstream contains 2112 priming frames, `ExtAudioFileTell` returns a value which is priming-frames too small, in this case -2112 instead of 0 (zero).

The work around requires the client to compensate:

- Make an initial call to `ExtAudioFileTell` immediately after opening the file and setting the client format.
- If the returned position is negative, all future calls to `ExtAudioFileTell` will be off by this value and the client should compensate.

__Listing 1__  Figure out the offset correction value.

```
...      // call ExtAudioFileTell immediately after opening the file and setting the client format     // and get the correction value to add to all future calls     SInt64 frameOffset = 0;     SInt64 frameOffsetCorrection = 0;      ExtAudioFileTell(sourceFile, &frameOffset);      if (frameOffset < 0) frameOffsetCorrection = -frameOffset;  ...
```


__Listing 2__  As a general work around always add this correction when calling `ExtAudioFileTell`.

```
...      ExtAudioFileTell(sourceFile, &frameOffset);     frameOffset += frameOffsetCorrection;  ...
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-12-07 | New document that discusses how to work around a bug in ExtAudioFileTell where the returned value may be priming-frames too small. |

