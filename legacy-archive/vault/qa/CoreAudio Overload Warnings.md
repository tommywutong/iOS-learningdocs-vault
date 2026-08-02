---
title: CoreAudio Overload Warnings
apple_id: DTS10003908
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2006-03-29'
source_url: https://developer.apple.com/library/archive/qa/qa1467/_index.html
archived_at: '2026-07-18T02:30:56.952764Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1467

# CoreAudio Overload Warnings

## Q:  CoreAudio is sending me occasional overload warnings when processing audio. What do these warnings mean, and what should I do to help eliminate these problems?

A: CoreAudio is sending me occasional overload warnings when processing audio. What do these warnings mean, and what should I do to help eliminate these problems?

The HAL IOProc is a time-limited, high-priority thread. CoreAudio will generate an overload warning in order to indicate that a recent I/O cycle took too long to complete. This happens when the time allocated, by the HAL, expires before the IOProc returns. These types of warnings can be commonplace under high cpu load and/or low memory conditions. Some kernel-level tasks may also be causing your IOProc to be preempted, VM paging being a big one, especially when memory is sparse.

__Optimize! Optimize! Optimize!__

If you have Apple's CHUD tools installed you can use Shark and/or Saturn to profile your IOProc. These tools will allow you to determine any bottlenecks or IOProc preemptions caused by your code. Tools and documentation are available online under [Performance & Debugging.](https://developer.apple.com/tools/performance/)

Apple also provides the HALLab utility (/Developer/Examples/CoreAudio/HAL/HALLab). You can use this application to monitor the statistics of your I/O cycle to get a better idea of where in the cycle the overload is occurring. This information can found in the IO Telemetry window (File->New:).

__Process audio outside the HAL thread__

If applicable to your situation, it is recommended that you create a separate thread for preparing audio data for the IOProc. For example, file or network I/O, codec decompression, or other tasks that may induce a high-level of latency can be done from a lower priority thread. The resultant data can then be fed to the IOProc.

__Some simple tips:__

- __Don't__ take locks if the action of acquiring the lock could be unbounded.
- __Do__ examine the size of buffer you're supplying to CoreAudio. It's possible it is larger than the device can handle in a single cycle.
- __Don't__ allocate memory from your IOProc. This can lead to VM paging.
- __Don't__ call the BSD layer from your IOProc. Many of these API's take kernel-locks which can cause your IOProc to be preempted. This includes printf and its family members.
- __Do__ take a look at the PublicUtility framework (/Developer/Examples/CoreAudio/PublicUtility/). It provides many handy wrappers for I/O cycle and latency timing.

- [CoreAudio Documentation](https://developer.apple.com/documentation/MusicAudio/CoreAudio-date.html)
- [CoreAudio Mailing List](http://lists.apple.com/mailman/listinfo/coreaudio-api)
- HALLab - /Developer/Examples/CoreAudio/HAL/HALLab
- PublicUtility - /Developer/Examples/CoreAudio/PublicUtility
- PlaySequence - /Developer/Examples/CoreAudio/Services/PlaySequence
- Example AudioUnits - /Developer/Examples/CoreAudio/AudioUnits

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-03-29 | New document that describes CoreAudio overload warnings what they mean and how to avoid them. |

