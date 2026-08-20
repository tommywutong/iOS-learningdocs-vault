---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/Utility_TRandom_h.html
archived_at: '2026-07-18T02:59:54.100964Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](Document%20Revision%20History.md)[Previous](Utility-TRandom.cpp.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# Utility/TRandom.h

```c
/*
 <codex>
 <abstract>TRandom.h</abstract>
 <\codex>
*/
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  TRandom.h
//
//      a random number generator
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#include <CoreFoundation/CoreFoundation.h>

#ifndef __TRandom
#define __TRandom

#define kRandomSeed 161803398

UInt32  GetRandomLong(UInt32 inRange);
UInt32  GetRandomLong(UInt32 inLowerLimit, UInt32 inUpperLimit);


class TRandom
{
public:
    TRandom();
    TRandom(UInt32 n) {Seed(n);};

    void Seed(UInt32 n);

    UInt32 operator()(UInt32 inLimit) 
    {
        mIndex1 = (mIndex1 + 1) % 55;
        mIndex2 = (mIndex2 + 1) % 55;
        mTable[mIndex1] = mTable[mIndex1] - mTable[mIndex2];
        return mTable[mIndex1] % inLimit;
    };

protected:
    UInt32 mTable[55];
    long mIndex1;
    long mIndex2;
};

#endif      // __TRandom

/*
 *  $Log$
 *  Revision 1.2  2007/10/16 18:39:05  mtrivedi
 *  fix comment block
 *
 *  Revision 1.1  2007/04/20 19:34:31  mtrivedi
 *  first revision
 *  
 *  Revision 1.2  2005/03/31 18:23:51  luke
 *  TRandom.mm -> TRandom.cpp
 *  
 *  Revision 1.1  2003/07/08 22:48:46  luke
 *  new file
 *  
 */
```

[Next](Document%20Revision%20History.md)[Previous](Utility-TRandom.cpp.md)

