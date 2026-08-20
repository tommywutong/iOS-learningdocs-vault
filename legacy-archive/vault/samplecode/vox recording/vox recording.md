---
title: vox recording
apple_id: DTS10000376
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/vox_recording/Introduction/Intro.html
archived_at: '2026-07-26T19:52:28.250265Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](VoxII.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# vox recording

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-03-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon Sound Manager 3.0 or later |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

This application uses Quad buffering for both recording and playback. Once a buffer is filled by the recording, the buffer is passed to the playback to be played. The playback has a small delay between the buffers which does not sound very good. The delay sounds a little like a skip in a record. The way to quit the application is to hold down the mouse button until the app quits. The recording is done with vox recording on, so it only records the sound which is at least of a certain level. Requirements: Sound Manager 3.0 or later Keywords: sound, buffer, vox recording

[Next](VoxII.c.md)

