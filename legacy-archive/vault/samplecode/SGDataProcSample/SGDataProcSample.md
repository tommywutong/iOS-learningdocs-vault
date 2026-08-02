---
title: SGDataProcSample
apple_id: DTS10000807
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SGDataProcSample/Introduction/Intro.html
archived_at: '2026-07-18T03:22:38.603758Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Minimung.c.md)

# SGDataProcSample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Demonstrates how to run the Sequence Grabber in record mode using an SGDataProc to captured data. |
| __Build Requirements:__ | Carbon This sample can be built using the Metrowerks CodeWarrior Integrated Development Environment (IDE), version 4.2.6 or later and Project Builder Version 1.1.1 or later. For CodeWarrior you should be using at least Universal Interfaces 3.4.1 and CarbonLib 1.5. QuickTime 5 is recommended. |
| __Runtime Requirements:__ | Carbon This sample can be built using the Metrowerks CodeWarrior Integrated Development Environment (IDE), version 4.2.6 or later and Project Builder Version 1.1.1 or later. For CodeWarrior you should be using at least Universal Interfaces 3.4.1 and CarbonLib 1.5. QuickTime 5 is recommended. |

The SGDataProcSample contains three separate targets which demonstrate how to run the Sequence Grabber in record mode using a Sequence Grabber DataProc to get the captured data. This technique provides optimal performance, far better than using preview mode with SG bottlenecks. The principle technique this code demonstrates will help a lot when capturing from DV and should allow 30fps playthrough using DV capture. Targets: Minimung - Very simple example which decompresses captured data to an offscreen then draws into an onscreen window simulating a 'preview'. Munggrab - Slightly more robust example which draws statistical information on top of the captured image including the timestamp, frames per second and average frames per second captured. SonOfMunggrab - Expands on Munggrab by using the carbon event model for better performance on Mac OS X. It also demonstrates the use of Carbon Timers to schedule regular calls to SGIdle. Requirements: This sample can be built using the Metrowerks CodeWarrior Integrated Development Environment (IDE), version 4.2.6 or later and Project Builder Version 1.1.1 or later. For CodeWarrior you should be using at least Universal Interfaces 3.4.1 and CarbonLib 1.5. QuickTime 5 is recommended. Keywords: Sequence Grabber, DataProcs

[Next](Minimung.c.md)

