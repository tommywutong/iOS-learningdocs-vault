---
title: usher
apple_id: DTS10001057
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/usher/Listings/sources_SourcingSupport_h.html
archived_at: '2026-07-26T19:53:08.768467Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [usher](usher.md)


[Next](sources-usher.r.md)[Previous](sources-SourcingSupport.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# sources/SourcingSupport.h

```swift
/*
    File:       SourcingSupport.h

    Copyright:  © 2000-2001 by Apple Computer, Inc., all rights reserved.

*/

#ifndef __SOURCINGSUPPORT__
#define __SOURCINGSUPPORT__

// ---------------------------------------------------------------------------
//      D E F I N I T I O N S
// ---------------------------------------------------------------------------

#define kSignature_StandardSourceHandler    FOUR_CHAR_CODE('stsh')
#define kSignature_NoSourceHandler          FOUR_CHAR_CODE('null')

struct StandardSourceHandler {
    OSType              signature;              // identifies the structure
    OSType              standardSignature;      // identifies structure as standard handler
};
typedef struct StandardSourceHandler StandardSourceHandler;

struct SourceMediaParams {
    GWorldPtr       gWorld;
    GDHandle        gdHandle;
    Rect            localDisplayRect;   // just for local display, not what's sent out
};
typedef struct SourceMediaParams SourceMediaParams;

enum  {
    kCharacteristic_WantsPresNotifications  = FOUR_CHAR_CODE('notf')
};

// ---------------------------------------------------------------------------
//      P R O T O T Y P E S
// ---------------------------------------------------------------------------

void SourcingSupport_DisposeHandler(StandardSourceHandler *inHandler);

void SourcingSupport_Idle(StandardSourceHandler *inHandler, Boolean inPlaying);
void SourcingSupport_SetEnable(StandardSourceHandler *inHandler, Boolean inEnableMode);

void SourcingSupport_HandleNotification(StandardSourceHandler *inHandler, OSType inNotificationType, void *inParams);

void SourcingSupport_HasCharacteristic(StandardSourceHandler *inHandler, OSType inCharacteristic, Boolean *outHasIt);

OSErr SourcingSupport_GetInfo(StandardSourceHandler *inHandler, OSType inSelector, void *ioParams);
OSErr SourcingSupport_SetInfo(StandardSourceHandler *inHandler, OSType inSelector, void *ioParams);

OSErr SourcingSupport_DoCommand(StandardSourceHandler *inHandler, OSType inCommand, void *ioCommandParams);

#endif /* __SOURCINGSUPPORT__ */
```

[Next](sources-usher.r.md)[Previous](sources-SourcingSupport.c.md)

