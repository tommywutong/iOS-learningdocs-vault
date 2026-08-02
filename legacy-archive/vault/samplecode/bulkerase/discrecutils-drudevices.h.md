---
title: bulkerase
apple_id: DTS10000463
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: DiscRecording
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/bulkerase/Listings/discrecutils_dru_devices_h.html
archived_at: '2026-07-18T03:29:01.934588Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [bulkerase](bulkerase.md)


[Next](discrecutils-druprogress.c.md)[Previous](discrecutils-drudevices.c.md)

# discrecutils/dru_devices.h

```c
/*
    dru_devices.h

    Part of the Disc Recording Utility sources for command-line tools.  This
    code provides an example of prompting the user to select a device and/or
    insert media, and how to create a textual description of a device.
*/

#ifndef _H_dru_devices
#define _H_dru_devices

#include <DiscRecording/DiscRecording.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Filter proc returns true to allow, false to suppress */
typedef int (*druDeviceFilterProc)(DRDeviceRef device);
int druFilter_AnyBurner(DRDeviceRef device);
int druFilter_AnyEraser(DRDeviceRef device);
int druFilter_CDBurners(DRDeviceRef device);
int druFilter_DVDBurners(DRDeviceRef device);

/* Displays a prompt asking for a device. Optional filter to constrain the choices. */
DRDeviceRef druPromptForDevice(char *promptString, druDeviceFilterProc filter);

/* Displays a prompt asking for blank media in a device. */
void        druPromptForBlankMediaInDevice(DRDeviceRef device);

/* Displays a prompt asking for erasable media in a device. */
void        druPromptForErasableMediaInDevice(DRDeviceRef device);

/* Displays a list of devices. */
void        druDisplayDeviceList(CFArrayRef deviceArray);

/* Returns true if the device contains blank media. */
int         druDeviceContainsBlankMedia(DRDeviceRef device);

/* Returns true if the device contains erasable media. */
int         druDeviceContainsErasableMedia(DRDeviceRef device);

/* Returns true if the device is spinning up (ie, the tray was just closed) */
int         druDeviceIsBecomingReady(DRDeviceRef device);

/* Returns true if the media in the device is reserved for this processes use */
int         druMediaIsReserved(DRDeviceRef device);

/* Returns a standard device description - VENDOR PRODUCT via BUS */
char *      druGetDeviceDescription(DRDeviceRef device, char *buffer, size_t bufSize);

/* Returns a short device description - VENDOR PRODUCT */
char *      druGetDeviceShortDescription(DRDeviceRef device, char *buffer, size_t bufSize);

/* Returns a long device description - VENDOR PRODUCT (FIRMWARE) via BUS */
char *      druGetDeviceLongDescription(DRDeviceRef device, char *buffer, size_t bufSize);


#ifdef __cplusplus
}
#endif

#endif /* _H_dru_devices */
```

[Next](discrecutils-druprogress.c.md)[Previous](discrecutils-drudevices.c.md)

