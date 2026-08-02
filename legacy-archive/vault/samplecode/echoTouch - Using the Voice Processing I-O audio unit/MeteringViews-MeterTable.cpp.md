---
title: echoTouch - Using the Voice Processing I/O audio unit
apple_id: TP40017575
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/echoTouch/Listings/MeteringViews_MeterTable_cpp.html
archived_at: '2026-07-18T03:29:07.430255Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [echoTouch - Using the Voice Processing I/O audio unit](echoTouch%20-%20Using%20the%20Voice%20Processing%20I-O%20audio%20unit.md)


[Next](MeteringViews-AVLevelMeter.h.md)[Previous](MeteringViews-PowerMeter.h.md)

# MeteringViews/MeterTable.cpp

```c
/*
 </samplecode>
*/

#include "MeterTable.h"

inline double DbToAmp(double inDb) { return pow(10., 0.05 * inDb); }

MeterTable::MeterTable(float inMinDecibels, size_t inTableSize, float inRoot)
    : mMinDecibels(inMinDecibels),
    mDecibelResolution(mMinDecibels / (inTableSize - 1)), 
    mScaleFactor(1. / mDecibelResolution)
{
    if (inMinDecibels >= 0.) {
        printf("MeterTable inMinDecibels must be negative");
        return;
    }

    mTable = (float*)malloc(inTableSize*sizeof(float));

    double minAmp = DbToAmp(inMinDecibels);
    double ampRange = 1. - minAmp;
    double invAmpRange = 1. / ampRange;

    double rroot = 1. / inRoot;
    for (size_t i = 0; i < inTableSize; ++i) {
        double decibels = i * mDecibelResolution;
        double amp = DbToAmp(decibels);
        double adjAmp = (amp - minAmp) * invAmpRange;
        mTable[i] = pow(adjAmp, rroot);
    }
}

MeterTable::~MeterTable()
{
    free(mTable);
}
```

[Next](MeteringViews-AVLevelMeter.h.md)[Previous](MeteringViews-PowerMeter.h.md)

