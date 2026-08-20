---
title: Using the ExtAudioFileSeek and ExtAudioFileTell Functions
apple_id: DTS40008022
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2008-09-29'
source_url: https://developer.apple.com/library/archive/qa/qa1609/_index.html
archived_at: '2026-07-18T02:32:42.136256Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1609

# Using the ExtAudioFileSeek and ExtAudioFileTell Functions

## Q:  Do the `ExtAudioFileSeek` and `ExtAudioFileTell` functions use the file sample rate or the client sample rate?

A: Do the `ExtAudioFileSeek` and `ExtAudioFileTell` functions use the file sample rate or the client sample rate?

The `ExtAudioFileSeek` and `ExtAudioFileTell` functions from Extended Audio File Services (`ExtendedAudioFile.h`) both use the file sample rate.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-29 | New document that describes how to use sample rate correctly when working with audio file positions. |

