---
title: QTMusicToo
apple_id: DTS10000915
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-19'
source_url: https://developer.apple.com/library/archive/samplecode/QTMusicToo/Listings/_Instrument_Editor_More_IE_Routines_c.html
archived_at: '2026-07-18T03:21:07.053607Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTMusicToo](QTMusicToo.md)


[Next](%E2%80%A2Instrument%20Editor-More%20IE%20Routines.h.md)[Previous](%E2%80%A2Instrument%20Editor-Instrument%20Tests.c.md)

# •Instrument Editor/More IE Routines.c

```c


#include "More IE Routines.h"
#include "BigEasyDialogs.h"


void SetMasterTuneDoc(short n,short menuItem, short menuRef)
    {
    TDoc *d;
    Boolean x;
    Fixed tune;

    d = &gDoc[n - kFirstDocWindow];

    tune = MusicGetMasterTune(d->ci);

    FlashResult(tune);

    x = EasyDialogGetNumber("\pRecall Instrument",
            "\pRecall instrument number:",
            &d->recallInstrument);

    if(x)
        {
        ComponentResult result;
        result = MusicSetMasterTune(d->ci,tune);
        FlashResult(result);
        }
    }


void SetDefaultInstrumentDoc(short n,short menuItem, short menuRef)
    {
    TDoc *d;
    short i;
    long t;

    d = &gDoc[n - kFirstDocWindow];

    for(i = 0; i < d->instrumentKnobCount; i++)
        {
        MusicSetPartKnob(d->ci,d->part,i+1,(*d->ikdList)[i].defaultValue);
        }

    MusicSetPartName(d->ci,d->part,"\pDefault Instrument");
    MusicGetPartName(d->ci,d->part,d->instrumentName);
    DrawStats(d);

    UpdateSliderKnobs(d);
    }
```

[Next](%E2%80%A2Instrument%20Editor-More%20IE%20Routines.h.md)[Previous](%E2%80%A2Instrument%20Editor-Instrument%20Tests.c.md)

