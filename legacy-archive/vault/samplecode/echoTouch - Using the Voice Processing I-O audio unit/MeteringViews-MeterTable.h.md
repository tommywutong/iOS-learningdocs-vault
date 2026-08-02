---
title: echoTouch - Using the Voice Processing I/O audio unit
apple_id: TP40017575
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/echoTouch/Listings/MeteringViews_MeterTable_h.html
archived_at: '2026-07-18T03:29:07.468022Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [echoTouch - Using the Voice Processing I/O audio unit](echoTouch%20-%20Using%20the%20Voice%20Processing%20I-O%20audio%20unit.md)


[Next](MeteringViews-GLLevelMeter.h.md)[Previous](MeteringViews-LevelMeter.m.md)

# MeteringViews/MeterTable.h

```c
/*
 </samplecode>
*/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

class MeterTable
{
public:
// MeterTable constructor arguments: 
// inNumUISteps - the number of steps in the UI element that will be drawn. 
//                  This could be a height in pixels or number of bars in an LED style display.
// inTableSize - The size of the table. The table needs to be large enough that there are no large gaps in the response.
// inMinDecibels - the decibel value of the minimum displayed amplitude.
// inRoot - this controls the curvature of the response. 2.0 is square root, 3.0 is cube root. But inRoot doesn't have to be integer valued, it could be 1.8 or 2.5, etc.

MeterTable(float inMinDecibels = -80., size_t inTableSize = 400, float inRoot = 2.0);   
~MeterTable();

    float ValueAt(float inDecibels)
    {
        if (inDecibels < mMinDecibels) return  0.;
        if (inDecibels >= 0.) return 1.;
        int index = (int)(inDecibels * mScaleFactor);
        return mTable[index];
    }
private:
    float   mMinDecibels;
    float   mDecibelResolution;
    float   mScaleFactor;
    float   *mTable;
};
```

[Next](MeteringViews-GLLevelMeter.h.md)[Previous](MeteringViews-LevelMeter.m.md)

