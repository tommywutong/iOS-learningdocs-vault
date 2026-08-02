---
title: QTAudioExtractionPanel
apple_id: DTS10003728
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2005-06-27'
source_url: https://developer.apple.com/library/archive/samplecode/QTAudioExtractionPanel/Introduction/Intro.html
archived_at: '2026-07-18T03:19:56.946492Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# QTAudioExtractionPanel

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2005-06-27 Enhances the QTKitPlayer to add an Audio Channel Mapping and Extraction panel |
| __Build Requirements:__ | QuickTime 7.0 or higher, OSX 10.3.9 or 10.4 |
| __Runtime Requirements:__ | QuickTime 7.0 or higher (QT 7.0.1 or higher recommended) |

QTAudioExtractionPanel adds a specialized Audio Extraction panel to the QTKitPlayer sample application. This panel provides access to some of the advanced audio capabilities introduced in QuickTime 7, including:
\* multi-channel audio tracks
\* spatially-labeled audio channels
\* movie audio mixing using spatial characteristics
\* audio device channel layout display (and editing, through Audio/MIDI Setup)
\* movie and track level property listeners and accessors
\* movie audio extraction configuration, preview, and export
\* multi-threaded audio preview and export
This sample application was developed to accompany WWDC 2005 Session 201 "Harnessing the Audio Capabilities of QuickTime 7"
The Audio Extraction panel is useful for gaining an understanding of how the movie mixer operates on spatially labeled data, but the chief purpose of this code is to demonstrate good practices in using the new QuickTime Audio APIs.

[Next](main.m.md)

