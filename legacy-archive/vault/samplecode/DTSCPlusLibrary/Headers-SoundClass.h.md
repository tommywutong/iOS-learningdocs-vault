---
title: DTSCPlusLibrary
apple_id: DTS10000731
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/DTSCPlusLibrary/Listings/Headers_SoundClass_h.html
archived_at: '2026-07-18T03:05:53.445624Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DTSCPlusLibrary](DTSCPlusLibrary.md)


[Next](Headers-SpinCursor.h.md)[Previous](Headers-Random.h.md)

# Headers/SoundClass.h

```c
/*
    File:       SoundClass.h

    Contains:   TSound is a simple object that plays sounds     
                TSound.h contains the TSound class definitions. 

    Written by: Kent Sandvik    

    Copyright:  Copyright © 1992-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/18/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
// Declare label for this header file
#ifndef _SOUND_
#define _SOUND_

#ifndef _DTSCPLUSLIBRARY_
#include "DTSCPlusLibrary.h"
#endif

#ifndef __RESOURCES__
#include <Resources.h>
#endif

#ifndef __SOUND__
#include <Sound.h>
#endif

const OSType kSoundType = 'snd ';               // our resource type definition


// _________________________________________________________________________________________________________ //
//  TSound Class Interface.

class TSound
// A simple sound class used for playing sounds synchonously (in future asynch as well).
{
public:
    // CONSTRUCTORS AND DESTRUCTORS
    TSound(char* name);                         // construct an object based on the name of the sound resource
    TSound(short resID);                        // construct an object based on the resource ID
    virtual~ TSound();                          // default destructor

    // MAIN INTERFACE
    virtual void Play();                        // play the sound

    // FIELDS
    Handle fSoundHandle;                        // handle where the sound resource is stored
    OSErr fError;                               // latest error
    char* fSound;                               // name of the sound wave
    short fSoundID;                             // ID of the sound wave
};


#endif

// _________________________________________________________________________________________________________ //


/*  Change History (most recent last):
  No        Init.   Date        Comment
  1         khs     12/21/92    New file
  2         khs     1/14/93     Cleanup
*/
```

[Next](Headers-SpinCursor.h.md)[Previous](Headers-Random.h.md)

