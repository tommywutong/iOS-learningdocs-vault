---
title: CarbonSndPlayDB
apple_id: DTS10000361
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/CarbonSndPlayDB/Introduction/Intro.html
archived_at: '2026-07-18T03:03:15.465883Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CarbonSndPlayDB.c.md)

# CarbonSndPlayDB

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-03-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon Sound Manager 3.x, Carbon 1.5+ to run as a carbon compiled library, Project Builder 1.1.1, CodeWarrior IDE |

This is a set of functions which reproduce the functionality of SndPlayDoubleBuffer in the Carbon environment, giving developers who use SndPlayDoubleBuffer a simpler transition to Carbon. This sample shows how to parse the input structures to SndPlayDoubleBuffer and set up a sequence of bufferCmd and callBackCmd commands to play sounds and call the user's/application's SndPlayDoubleBufferCallBack function. This sample does not have to be run under Carbon, it works just fine under Classic as well and can also be adapted to be useful to developers who would like to have better control over synchronization of sounds or playback and recording. CodeWarrior 5, 7 and Project Builder projects are included. Requirements: Sound Manager 3.x, Carbon 1.5+ to run as a carbon compiled library, Project Builder 1.1.1, CodeWarrior IDE Keywords: SndPlayDoubleBuffer, Carbon

[Next](CarbonSndPlayDB.c.md)

