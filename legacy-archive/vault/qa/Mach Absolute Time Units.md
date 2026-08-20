---
title: Mach Absolute Time Units
apple_id: DTS10003470
resource_type: QA
platform: macOS
topic: Data Management
technology: null
published: '2005-01-06'
source_url: https://developer.apple.com/library/archive/qa/qa1398/_index.html
archived_at: '2026-07-18T02:30:31.519992Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1398

# Mach Absolute Time Units

## Q:  I'm trying to get precise timing measurements using `mach_absolute_time`. What time units does it use? Specifically, if I take two time measurements and subtract the earlier from the later, how do I convert the result to a real world value?

A: I'm trying to get precise timing measurements using `mach_absolute_time`. What time units does it use? Specifically, if I take two time measurements and subtract the earlier from the later, how do I convert the result to a real world value?

This function returns its result in terms of the Mach __absolute time unit__. This unit is CPU dependent, so you can't just multiply it by a constant to get a real world value. Rather, you should call a system-provided conversion function to convert it to a real world value.

The easiest conversion functions to use are `AbsoluteToNanoseconds` and `AbsoluteToDuration` from the CoreServices framework. You can also go in the other direction using `NanosecondsToAbsolute` and `DurationToAbsolute`. Listing 1 shows an example of how to get real world timing results using `mach_absolute_time`.

__Listing 1__  Converting Mach absolute time to nanoseconds using AbsoluteToNanoseconds

```c
#include <assert.h> #include <CoreServices/CoreServices.h> #include <mach/mach.h> #include <mach/mach_time.h> #include <unistd.h>  uint64_t GetPIDTimeInNanoseconds(void) {     uint64_t        start;     uint64_t        end;     uint64_t        elapsed;     Nanoseconds     elapsedNano;      // Start the clock.      start = mach_absolute_time();      // Call getpid. This will produce inaccurate results because      // we're only making a single system call. For more accurate      // results you should call getpid multiple times and average      // the results.      (void) getpid();      // Stop the clock.      end = mach_absolute_time();      // Calculate the duration.      elapsed = end - start;      // Convert to nanoseconds.      // Have to do some pointer fun because AbsoluteToNanoseconds      // works in terms of UnsignedWide, which is a structure rather      // than a proper 64-bit integer.      elapsedNano = AbsoluteToNanoseconds( *(AbsoluteTime *) &elapsed );      return * (uint64_t *) &elapsedNano; }
```

If your program cannot use the CoreServices framework, you can perform an equivalent conversion using the information returned by `mach_timebase_info`, as shown in Listing 2.

__Listing 2__  Converting Mach absolute time to nanoseconds using mach_timebase_info

```c
#include <assert.h> #include <CoreServices/CoreServices.h> #include <mach/mach.h> #include <mach/mach_time.h> #include <unistd.h>  uint64_t GetPIDTimeInNanoseconds(void) {     uint64_t        start;     uint64_t        end;     uint64_t        elapsed;     uint64_t        elapsedNano;     static mach_timebase_info_data_t    sTimebaseInfo;      // Start the clock.      start = mach_absolute_time();      // Call getpid. This will produce inaccurate results because      // we're only making a single system call. For more accurate      // results you should call getpid multiple times and average      // the results.      (void) getpid();      // Stop the clock.      end = mach_absolute_time();      // Calculate the duration.      elapsed = end - start;      // Convert to nanoseconds.      // If this is the first time we've run, get the timebase.     // We can use denom == 0 to indicate that sTimebaseInfo is      // uninitialised because it makes no sense to have a zero      // denominator is a fraction.      if ( sTimebaseInfo.denom == 0 ) {         (void) mach_timebase_info(&sTimebaseInfo);     }      // Do the maths. We hope that the multiplication doesn't      // overflow; the price you pay for working in fixed point.      elapsedNano = elapsed * sTimebaseInfo.numer / sTimebaseInfo.denom;      return elapsedNano; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-01-06 | New document that describes how to convert Mach absolute time units to real time, and vice versa. |

