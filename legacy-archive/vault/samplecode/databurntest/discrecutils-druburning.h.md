---
title: databurntest
apple_id: DTS10000466
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: DiscRecording
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/databurntest/Listings/discrecutils_dru_burning_h.html
archived_at: '2026-07-18T03:29:03.136981Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [databurntest](databurntest.md)


[Next](discrecutils-drudevices.c.md)[Previous](discrecutils-druburning.c.md)

# discrecutils/dru_burning.h

```c
/*
    dru_burning.h

    Part of the Disc Recording Utility sources for command-line tools.  This
    code provides an example of prompting the user to select a device and/or
    insert media, and how to create a textual description of a device.
*/

#ifndef _H_dru_burning
#define _H_dru_burning

#include <DiscRecording/DiscRecording.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Handles an entire burn, including progress and error reporting.  Returns true if successful. */
int         druBurn(DRBurnRef burn, CFTypeRef layout);

/* Prints a localized failure message. */
void        druPrintFailureMessage(const char *task, CFDictionaryRef status);


/* Handles an entire erase, including progress and error reporting.  Returns true if successful. */
int         druErase(DRDeviceRef device, int fullErase);

#ifdef __cplusplus
}
#endif

#endif /* _H_dru_burning */
```

[Next](discrecutils-drudevices.c.md)[Previous](discrecutils-druburning.c.md)

