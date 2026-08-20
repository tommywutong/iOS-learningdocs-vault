---
title: QTMusicToo
apple_id: DTS10000915
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-19'
source_url: https://developer.apple.com/library/archive/samplecode/QTMusicToo/Listings/_Instrument_Editor_Instrument_Editor_Menus_c.html
archived_at: '2026-07-18T03:21:06.499808Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTMusicToo](QTMusicToo.md)


[Next](%E2%80%A2Instrument%20Editor-Instrument%20Editor%20Menus.h.md)[Previous](%E2%80%A2Instrument%20Editor-Instrument%20Editor%20Filing.h.md)

# •Instrument Editor/Instrument Editor Menus.c

```c
/*
 * file: Instrument Editor Menus.c
 *
 * started 22 March 1992
 * david van brink
 *
 */

/*--------------------------
    Inclusions
--------------------------*/

#include <Memory.h>

#include "BigEasy2.h"
#include "BigEasyTextish.h"

#include "Instrument Editor.h"
#include "Instrument Editor Menus.h"


static void DoSomethingWithKnobs(TDoc *d);

/*--------------------------
    Kode
--------------------------*/


SynthListHandle GetSynthesizerList(void)
/*
 * Return a handle to a list of synths
 */
    {
    short synthCount;
    SynthListHandle result;
    SynthMenuEntry *sme;
    OSErr thisError;
    NoteAllocator na;

    na = OpenDefaultComponent(kNoteAllocatorType,0);

    synthCount = NAGetRegisteredMusicDevice(na,0,nil,nil,nil,nil);

    result = (void *)NewHandle(synthCount * sizeof(SynthMenuEntry) + sizeof(SynthList));
    HLock((void *)result);

    (**result).synthCount = synthCount;
    sme = &(**result).entry[0];

    while(synthCount)
        {
        MusicComponent mc;

        thisError = NAGetRegisteredMusicDevice(na,synthCount,
                &sme->synthType,
                sme->synthName,
                nil,
                &mc);
        if(!sme->synthName[0])      /* no registered name? */
            {
            SynthesizerDescription sd;

            MusicGetDescription(mc,&sd);
            BlockMove(sd.name,sme->synthName,sd.name[0]+1);
            }
        sme++;
        synthCount--;
        }

    CloseComponent(na);
    return result;
    }


void DoSomethingWithKnobs(TDoc *d)
    {
    Rect allControls;

    MakeControlsFromKnobList(d,&allControls);

    d->visibleSliderBounds.top = d->visibleSliderBounds.bottom
            = d->visibleSliderBounds.left = d->visibleSliderBounds.right = 0;
    d->virtualSliderBounds = allControls;

    UpdateSliderKnobs(d);


    FixForSize(d);
    }


void DoGlobalKnobs(short n, short menuItem, short menuRef)
    {
    TDoc *d;
    ComponentResult result;

    d = &gDoc[n - kFirstDocWindow];

    d->whichList = mGlobalKnobs;

    DisposeEasyControlList(d->ecl);
    d->ecl = NewEasyControlList(d->w,0);
    DoSomethingWithKnobs(d);

    FixUpMenus(d);
    }

void DoInstrumentKnobs(short n, short menuItem, short menuRef)
    {
    TDoc *d;
    ComponentResult result;

    d = &gDoc[n - kFirstDocWindow];

    d->whichList = mInstrumentKnobs;

    DisposeEasyControlList(d->ecl);
    d->ecl = NewEasyControlList(d->w,0);
    DoSomethingWithKnobs(d);

    FixUpMenus(d);
    }

void DoControllers(short n, short menuItem, short menuRef)
    {
    TDoc *d;
    ComponentResult result;

    d = &gDoc[n - kFirstDocWindow];

    d->whichList = mControllers;

    DisposeEasyControlList(d->ecl);
    d->ecl = NewEasyControlList(d->w,0);
    DoSomethingWithKnobs(d);

    FixUpMenus(d);
    }
```

[Next](%E2%80%A2Instrument%20Editor-Instrument%20Editor%20Menus.h.md)[Previous](%E2%80%A2Instrument%20Editor-Instrument%20Editor%20Filing.h.md)

