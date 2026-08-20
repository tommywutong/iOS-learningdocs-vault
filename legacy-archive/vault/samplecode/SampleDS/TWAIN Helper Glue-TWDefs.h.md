---
title: SampleDS
apple_id: DTS10000657
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ImageCaptureCore
published: '2003-07-10'
source_url: https://developer.apple.com/library/archive/samplecode/SampleDS/Listings/TWAIN_Helper_Glue_TWDefs_h.html
archived_at: '2026-07-18T03:22:59.953897Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleDS](SampleDS.md)


[Next](TWAIN%20Helper%20Glue-TWGlue.c.md)[Previous](TWAIN%20Helper%20Glue-TWAcquire.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/ImageCaptureDeviceModulesReference/index.html%23//apple_ref/doc/uid/TP40006079](https://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/ImageCaptureDeviceModulesReference/index.html#//apple_ref/doc/uid/TP40006079)

# TWAIN Helper Glue/TWDefs.h

```
// ===========================================================================
//  TWDefs.c            TWAIN 1.9               ©1991-2001 TWAIN Working Group
// ===========================================================================
//
//  General definitions.

#ifndef _TWDEFS_
#define _TWDEFS_
#pragma once

/* States */

#define STATE_PRETW             10
#define STATE_DSMLOADED         20
#define STATE_DSMOPEN           30
#define STATE_DSSELECTED        34
#define STATE_DSLOADED          35
#define STATE_DSOPEN            40
#define STATE_DSENABLED         50
#define STATE_DSDISABLED        55
#define STATE_XFERREADY         60
#define STATE_XFER              70
#define STATE_DSCLOSED          80
#define STATE_DSMCLOSEDUNLOADED 90


/* Miscellaneous Constants */

#ifndef OKAY
#define OKAY            0
#endif

#ifndef TWERR
#define TWERR           -1
#endif

#ifndef TRUE
#define TRUE            1
#endif

#ifndef FALSE
#define FALSE           0
#endif

#ifndef ON
#define ON              1
#endif

#ifndef OFF
#define OFF             0
#endif

#ifndef NULL
#define NULL            0L
#endif

#define DSMR_type   'DSMR'
#define DSRC_type   'DSRC'      // File type for old 68k data sources
#define DSrc_type   'DSrc'      // File type for new PowerPC data sources

#endif
```

[Next](TWAIN%20Helper%20Glue-TWGlue.c.md)[Previous](TWAIN%20Helper%20Glue-TWAcquire.h.md)

