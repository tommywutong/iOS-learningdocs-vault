---
title: Record sound specific rate
apple_id: DTS10000367
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/Record_sound_specific_rate/Introduction/Intro.html
archived_at: '2026-07-18T03:22:01.711985Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](headers-RecordSound.h.md)

# Record sound specific rate

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-03-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon Sound Manager 3.2 or later |

This sample shows how to use SPBRecord to record to memory, convert the sampling rate to some arbitrary rate, and then write the recorded, rate converted samples to disk, asynchronously, using PBWriteAsync. This sample is useful for those developers who wish more flexibility than what is offered with SPBRecordToFile, or for those wishing to record at a rate not supported by the sound input driver. Requirements: Sound Manager 3.2 or later Keywords: record, sound, disk, SPBRecord, SoundConvert

[Next](headers-RecordSound.h.md)

