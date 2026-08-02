---
title: qtmoviefromprocs
apple_id: DTS10000899
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtmoviefromprocs/Introduction/Intro.html
archived_at: '2026-07-26T19:52:50.360158Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](QTMovieFromProcs.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# qtmoviefromprocs

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Create QuickTime movie with video and audio tracks; Video from series of individual frames |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

This sample code has been updated for QuickTime 5.0 README - QTMovieFromProcs QuickTime 3.0 provides functions that allow you to create a movie using data supplied by one or more application-defined procedures. In particular, you use the function MovieExportAddDataSource to add a track-generating procedure and you use the function MovieExportFromProceduresToDataRef to do the actual movie exporting. In this example, we will create a QuickTime movie with a video track and an audio track; we generate the video track by drawing a series of individual frames, and we generate the audio track by generating 10 seconds of silence. Enjoy, QuickTime Team

[Next](QTMovieFromProcs.c.md)

