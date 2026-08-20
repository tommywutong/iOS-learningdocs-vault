---
title: BrightContrastEngine
apple_id: DTS10000067
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/BrightContrastEngine/Listings/BCEngine_h.html
archived_at: '2026-07-18T03:02:18.336916Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BrightContrastEngine](BrightContrastEngine.md)


[Next](BCEngine.i.c.md)[Previous](BCDemo.c.md)

# BCEngine.h

```
//****************************************************************************************
// BCEngine.h
//
// Copyright 1999 by Apple Computer, Inc.
//----------------------------------------------------------------------------------------


#ifndef __BCENGINE__
#define __BCENGINE__

#if PRAGMA_ONCE
#pragma once
#endif

#ifdef __cplusplus
extern "C" {
#endif

#if PRAGMA_IMPORT
#pragma import on
#endif

#if PRAGMA_STRUCT_ALIGN
    #pragma options align=mac68k
#elif PRAGMA_STRUCT_PACKPUSH
    #pragma pack(push, 2)
#elif PRAGMA_STRUCT_PACK
    #pragma pack(2)
#endif

//----------------------------------------------------------------------------------------
// Public Constants
//----------------------------------------------------------------------------------------

// Brightness/Contrast Engine SubType
enum {
    kContrastEngineComponentSubType             = 'cont',
    kOldContrastEngineComponentSubType          = 'bice'
};

// Notification Constants
enum {
    kContrastChanged            = FOUR_CHAR_CODE('cchn'),
    kBrightnessChanged          = FOUR_CHAR_CODE('bchn'),
    kAVNotifyDeviceReset        = FOUR_CHAR_CODE('rset')    
};

// Brightness/Contrast Engine Interface Version
enum {
    kContrastEngineComponentInterfaceRev        = 1L
};

// Brightness/Contrast Engine Component selectors
enum {
    kContrastEngineGetBrightnessRangeSelect     = 0,
    kContrastEngineGetBrightnessSelect          = 1,
    kContrastEngineSetBrightnessSelect          = 2,
    kContrastEngineGetContrastRangeSelect       = 3,
    kContrastEngineGetContrastSelect            = 4,
    kContrastEngineSetContrastSelect            = 5
};


//----------------------------------------------------------------------------------------
// Public Types
//----------------------------------------------------------------------------------------

typedef ComponentInstance               ContrastEngineComponent;
typedef ComponentResult                 ContrastEngineResult;


//----------------------------------------------------------------------------------------
// Public Prototypes
//----------------------------------------------------------------------------------------

pascal ContrastEngineResult
ContrastEngineGetBrightnessRange (ComponentInstance     ec,
                                 short *                min,
                                 short *                max)                                FIVEWORDINLINE(0x2F3C, 0x0008, 0x0000, 0x7000, 0xA82A);

pascal ContrastEngineResult
ContrastEngineGetBrightness     (ComponentInstance      ec,
                                 short *                brightness)                         FIVEWORDINLINE(0x2F3C, 0x0004, 0x0001, 0x7000, 0xA82A);

pascal ContrastEngineResult
ContrastEngineSetBrightness     (ComponentInstance      ec,
                                 short                  brightness)                         FIVEWORDINLINE(0x2F3C, 0x0002, 0x0002, 0x7000, 0xA82A);

pascal ContrastEngineResult
ContrastEngineGetContrastRange  (ComponentInstance      ec,
                                 short *                min,
                                 short *                max)                                FIVEWORDINLINE(0x2F3C, 0x0008, 0x0003, 0x7000, 0xA82A);

pascal ContrastEngineResult
ContrastEngineGetContrast       (ComponentInstance      ec,
                                 short *                contrast)                           FIVEWORDINLINE(0x2F3C, 0x0004, 0x0004, 0x7000, 0xA82A);

pascal ContrastEngineResult
ContrastEngineSetContrast       (ComponentInstance      ec,
                                 short                  contrast)                           FIVEWORDINLINE(0x2F3C, 0x0002, 0x0005, 0x7000, 0xA82A);



#if PRAGMA_STRUCT_ALIGN
    #pragma options align=reset
#elif PRAGMA_STRUCT_PACKPUSH
    #pragma pack(pop)
#elif PRAGMA_STRUCT_PACK
    #pragma pack()
#endif

#ifdef PRAGMA_IMPORT_OFF
#pragma import off
#elif PRAGMA_IMPORT
#pragma import reset
#endif

#ifdef __cplusplus
}
#endif

#endif // __BCENGINE__
```

[Next](BCEngine.i.c.md)[Previous](BCDemo.c.md)

