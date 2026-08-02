---
title: SurfaceVertexProgram
apple_id: DTS10000547
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2003-07-07'
source_url: https://developer.apple.com/library/archive/samplecode/SurfaceVertexProgram/Listings/Classes_AudioDefs_h.html
archived_at: '2026-07-18T03:25:49.288099Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SurfaceVertexProgram](SurfaceVertexProgram.md)


[Next](Classes-BasicApplicationController.h.md)[Previous](Classes-AnalyzerOpenGLView.m.md)

# Classes/AudioDefs.h

```
#ifndef __AUDIODEFS__
#define __AUDIODEFS__

#if PRAGMA_STRUCT_ALIGN
    #pragma options align=mac68k
#elif PRAGMA_STRUCT_PACKPUSH
    #pragma pack(push, 2)
#elif PRAGMA_STRUCT_PACK
    #pragma pack(2)
#endif

typedef struct {
    AudioFormatAtom     formatData;
    AudioEndianAtom     endianData;
    AudioTerminatorAtom     terminatorData;
} AudioCompressionAtom, *AudioCompressionAtomPtr, **AudioCompressionAtomHandle;

#if PRAGMA_STRUCT_ALIGN
    #pragma options align=reset
#elif PRAGMA_STRUCT_PACKPUSH
    #pragma pack(pop)
#elif PRAGMA_STRUCT_PACK
    #pragma pack()
#endif

#define BailErr(x) {err = x; if(err != noErr) goto bail;}

enum {kMaxOutputBuffer = 64 * 1024}; // max size of output buffer

typedef enum { kFirstBuffer, kSecondBuffer } eBufferNumber;

typedef struct {
    ExtendedSoundComponentData  compData;
    Handle              hSource;            // source media buffer
    Media               sourceMedia;        // sound media identifier
    TimeValue           getMediaAtThisTime;
    TimeValue           sourceDuration;
    UInt32              maxBufferSize;
    Boolean             isThereMoreSource;
    Boolean             isSourceVBR;
} SCFillBufferData, *SCFillBufferDataPtr;

// functions
OSErr PlaySound(const FSSpec *inFileToPlay);

#endif // __AUDIODEFS__
```

[Next](Classes-BasicApplicationController.h.md)[Previous](Classes-AnalyzerOpenGLView.m.md)

