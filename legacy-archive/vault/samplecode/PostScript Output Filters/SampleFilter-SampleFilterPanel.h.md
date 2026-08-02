---
title: PostScript Output Filters
apple_id: DTS10000297
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/PostScript_Output_Filters/Listings/SampleFilter_SampleFilterPanel_h.html
archived_at: '2026-07-18T03:19:27.498689Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PostScript Output Filters](PostScript%20Output%20Filters.md)


[Next](SampleFilter-SampleFilterResources.h.md)[Previous](SampleFilter-SampleFilterPanel.c.md)

# SampleFilter/SampleFilterPanel.h

```
/*
**  File:           SampleFilterPanel.h
**
**  Description:    Header file describing the panel specific routines
**                  of SampleFilter.
**
**  Version:        1.0
**
**  Copyright 1999 Apple Computer. All rights reserved.
**
**  You may incorporate this sample code into your applications without
**  restriction, though the sample code has been provided "AS IS" and the
**  responsibility for its operation is 100% yours.  However, what you are
**  not permitted to do is to redistribute the source as "ABC Sample Code"
**  after having made changes. If you're going to re-distribute the source,
**  we require that you make it clear in the source that the code was
**  descended from Apple Sample Code, but that you've made changes.
**
*/

OSStatus samplePrSpecificInitData(void *dataP, Collection plugInPrInfo);
OSStatus samplePrSpecificCloseData(void *dataP, Boolean doIt);
OSStatus sampleCloseData(void *dataP, Boolean doIt);
OSStatus samplePrSpecificInit(void *dataP, DialogPtr dp, short offset);
OSStatus samplePrSpecificClose(void *dataP, DialogPtr dp, short offset);
OSStatus sampleInit(void *dataP, DialogPtr dp, short offset);
OSStatus sampleClose(void *dataP, DialogPtr dp, short offset);
OSStatus sampleItem(void *dataP, DialogPtr dp, short item, short offset, short ctlVal);
OSStatus sampleFilter(void *dataP, DialogPtr dp, short offset, EventRecord *ep, short *itemP, Boolean *weHandledItP);
OSStatus sampleCheckRange(void *dataP, DialogPtr dp, short offset, Boolean *doItP);
OSStatus sampleSaveButton(void *dataP, Collection plugInPrInfo);
OSStatus sampleAddMenu(void *dataP, StringPtr s, unsigned long bufSize, Boolean *addItP);
OSStatus sampleRegisterPanel(short *ditlIDP, void **dataH, void *libDataP);
OSStatus sampleInitData(void *dataP, Collection plugInHints);
```

[Next](SampleFilter-SampleFilterResources.h.md)[Previous](SampleFilter-SampleFilterPanel.c.md)

