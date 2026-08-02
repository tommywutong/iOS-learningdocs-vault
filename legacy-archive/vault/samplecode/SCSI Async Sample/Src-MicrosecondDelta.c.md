---
title: SCSI Async Sample
apple_id: DTS10000022
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_Async_Sample/Listings/Src_MicrosecondDelta_c.html
archived_at: '2026-07-18T03:22:31.422343Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI Async Sample](SCSI%20Async%20Sample.md)


[Next](Src-MicrosecondTrap.h.md)[Previous](Src-LogManager.h.md)

# Src/MicrosecondDelta.c

```c
/*                                  MicrosecondDelta.c                              */
/*
 * MicrosecondDelta.c
 * Copyright © 1994 Apple Computer Inc. All rights reserved.
 */
#include "MicrosecondTrap.h"

/*
 * Convert an epoch to microseconds (use floating-point operations).
 * Note that 4294967296.0 is 2^32, which is represented accurately
 * in double-precision floating point. Note that this can loose
 * low-order bits.
 */
#define kTwoPower32 (4294967296.0)

double
MicrosecondToDouble(
        register const UnsignedWide *epochPtr
    )
{
        register double         result;

        result = (((double) epochPtr->hi) * kTwoPower32) + epochPtr->lo;
        return (result);
}

/*
 * Return the difference between two Microsecond Trap values.
 * Integer subtraction is used to preserve accuracy.
 */
void
MicrosecondDelta(
        register const UnsignedWide *startPtr,
        register const UnsignedWide *endPtr,
        register UnsignedWide       *result
    )
{
        if (endPtr->lo >= startPtr->lo)
            result->hi = endPtr->hi - startPtr->hi;
        else {
            result->hi = (endPtr->hi - 1) - startPtr->hi;
        }
        result->lo = endPtr->lo - startPtr->lo;
}
```

[Next](Src-MicrosecondTrap.h.md)[Previous](Src-LogManager.h.md)

