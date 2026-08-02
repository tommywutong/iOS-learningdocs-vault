---
title: The Default Output Audio Units
apple_id: DTS40007940
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2008-08-21'
source_url: https://developer.apple.com/library/archive/qa/qa1577/_index.html
archived_at: '2026-07-18T02:32:19.766478Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1577

# The Default Output Audio Units

## Q:  What is the difference between the Default Output and System Output audio units?

A: What is the difference between the Default Output and System Output audio units?

The __System Output unit__ (`kAudioUnitSubType_SystemOutput`) is for alerts and user interface sound effects. The __Default Output unit__ (`kAudioUnitSubType_DefaultOutput`) is for all other audio output.

Using the Audio MIDI Setup application (in the Utilities folder), a user can direct the output of each of these audio units separately.

For more information on these Mac OS X audio units, refer to the headers in the Audio Unit framework (`AudioUnit.framework`).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-08-21 | New document that describes the Mac OS X output audio units and their purposes. |

