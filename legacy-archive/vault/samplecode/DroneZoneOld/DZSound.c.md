---
title: DroneZoneOld
apple_id: DTS10000051
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/DroneZoneOld/Listings/DZSound_c.html
archived_at: '2026-07-18T03:07:19.824621Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DroneZoneOld](DroneZoneOld.md)


[Next](DZSound.h.md)[Previous](DZResource.h.md)

# DZSound.c

```c
/*
 *  File:       DZSound.c
 *
 *  Contents:   Handles some of the sound stuff.
 *
 *  Copyright © 1996 Apple Computer, Inc.
 */

#include <assert.h>
#include <math.h>

#include <Controls.h>
#include <Dialogs.h>
#include <Sound.h>

#include "SoundSprocket.h"

#include "DZSound.h"
#include "DZResource.h"
#include "DZUtils.h"

static SSpListenerReference gSoundListener          = NULL;


/* =============================================================================
 *      Sound_Init (external)
 *
 *  Initializes the sound stuff.
 * ========================================================================== */
void Sound_Init(
    void)
{
    NumVersion              version;

    // Check the sound manager version
    version = SndSoundManagerVersion();
    //¥ IF YOU CAN'T COMPILE THE PREVIOUS LINE, YOU MUST EDIT YOUR Sound.h TO
    //¥ MAKE SndSoundManagerVersion RETURN THE TYPE NumVersion.

    if (!CheckVersionNumber(&version, 3, 2, 1))
    {
        StopAlert(kAlrtID_SoundMgrVersion, NULL);
        //¥ TODO: QUIT or disable sound
    }

    // Create the listener
    SSpListener_New(&gSoundListener);
    assert(gSoundListener != NULL);

    SSpListener_SetMetersPerUnit(gSoundListener, 5.0);
}


/* =============================================================================
 *      Sound_Exit (external)
 *
 *  Prepares for exit.
 * ========================================================================== */
void Sound_Exit(
    void)
{
    if (gSoundListener != NULL)
    {
        SSpListener_Dispose(gSoundListener);
        gSoundListener = NULL;
    }
}


/* =============================================================================
 *      Sound_GetListener (external)
 *
 *  Returns the game listener object, which is the "head" position for 3D sound.
 * ========================================================================== */
SSpListenerReference Sound_GetListener(
    void)
{
    assert(gSoundListener != NULL);
    return gSoundListener;
}


/* =============================================================================
 *      Sound_Configure (external)
 *
 *  Presents the modal dialog to configure the 3D sound stuff..
 * ========================================================================== */
void Sound_Configure(
    void)
{
    SSpConfigureSpeakerSetup(NULL);
}
```

[Next](DZSound.h.md)[Previous](DZResource.h.md)

