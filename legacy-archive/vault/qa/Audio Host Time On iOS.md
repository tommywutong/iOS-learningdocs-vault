---
title: Audio Host Time On iOS
apple_id: DTS40008801
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2014-01-15'
source_url: https://developer.apple.com/library/archive/qa/qa1643/_index.html
archived_at: '2026-07-18T02:33:10.081645Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1643

# Audio Host Time On iOS

## Q:  How do you work with Host Time on iOS, for example how do I get the current host time or clock frequency since `AudioGetCurrentHostTime` and `AudioGetHostClockFrequency` are not available?

A: While the best way to work with host time on iOS is using the __CAHostTimeBase__ helper class, iOS developers may simply call `mach_absolute_time` to retrieve the current host time.

__Listing 1__  Getting the current host time.

```
UInt64 theTime = mach_absolute_time();
```

The other important component of the host time is the frequency or timebase. By using the `mach_timebase_info` structure and `mach_timebase_info` (`usr/include/mach/mach_time.h`) you can figure out the length of every unit of absolute time.


```
struct mach_timebase_info {
    uint32_t	numer;
    uint32_t	denom;
};

typedef struct mach_timebase_info	*mach_timebase_info_t;
typedef struct mach_timebase_info	mach_timebase_info_data_t;
```


__Listing 2__  Getting the time base info.

```
# include <mach/mach_time.h>

mach_timebase_info_data_t theTimeBaseInfo;

mach_timebase_info(&theTimeBaseInfo);
```

For example, if the numerator returned is 1,000,000,000 and the denominator is 6,000,000, the frequency is 6,000,000ths of a second. Every unit of absolute time would be 166.67 nanoseconds and host time frequency in ticks per seconds may be calculated like this, `1.0e9 * (denom / numer)`.

Listing 3 demonstrates how the `CAHostTimeBase` helper class calculates frequency.

__Listing 3__  Snippet from `CAHostTimeBase`.

```c
#include "CAHostTimeBase.h"

Float64	CAHostTimeBase::sFrequency = 0;
UInt32	CAHostTimeBase::sToNanosNumerator = 0;
UInt32	CAHostTimeBase::sToNanosDenominator = 0;

...

// get the info about Absolute time
struct mach_timebase_info theTimeBaseInfo;
mach_timebase_info(&theTimeBaseInfo);

sToNanosNumerator = theTimeBaseInfo.numer;
sToNanosDenominator = theTimeBaseInfo.denom;

...

// the frequency of that clock is: (sToNanosDenominator / sToNanosNumerator) * 10^9
sFrequency = static_cast<Float64>(sToNanosDenominator) / static_cast<Float64>(sToNanosNumerator);
sFrequency *= 1000000000.0;
```

As previously mentioned, the best way to work with host time on iOS is by taking advantage of the __CAHostTimeBase__ helper class (`CAHostTimeBase.h and CAHostTimeBase.cpp`) provided as part of the [Core Audio Utility Classes](https://developer.apple.com/library/mac/samplecode/CoreAudioUtilityClasses/Introduction/Intro.html).

`CAHostTimeBase` provides the following public methods:


```
ConvertToNanos(inHostTime);
ConvertFromNanos(inNanos);

GetCurrentTime();

GetCurrentTimeInNanos();
GetCurrentTimeInSeconds();

GetFrequency();
GetMinimumDelta()

AbsoluteHostDeltaToNanos(inStartTime, inEndTime);
HostDeltaToNanos(inStartTime, inEndTime);
```

Here's an easy and useful example of using `CAHostTimeBase` along with `AudioQueueStart` to start the playback of an Audio Queue object 5 seconds in the future.

`AudioQueueStart` takes a pointer to an `AudioTimeStamp` structure as the `inStartTime` parameter indicating at which time the audio queue should start and we'll use the `mHostTime` field to specify our wanted start time.

__Listing 4__  Creating a host time 5 seconds in the future for `AudioQueueStart`.

```c
#include "CAHostTimeBase.h"

AudioTimeStamp myAudioQueueStartTime = {0};
UInt32 theNumberOfSecondsInTheFuture = 5;

Float64 hostTimeFreq = CAHostTimeBase::GetFrequency();
UInt64 startHostTime = CAHostTimeBase::GetCurrentTime() + theNumberOfSecondsInTheFuture * hostTimeFreq;

myAudioQueueStartTime.mFlags = kAudioTimeStampHostTimeValid;
myAudioQueueStartTime.mHostTime = startHostTime;

AudioQueueStart(myAudioQueue, &myAudioQueueStartTime);
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-01-15 | Editorial |
| 2009-05-18 | New document that describes how to work with Host Time on iOS. |

