---
title: Apple Core Audio Format Specification 1.0
apple_id: TP40001862
resource_type: Guide
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2011-10-12'
source_url: https://developer.apple.com/library/archive/documentation/MusicAudio/Reference/CAFSpec/CAF_intro/CAF_intro.html
archived_at: '2026-07-15T08:18:03.367634Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/MusicAudio/Reference/CAFSpec/CAF_overview/CAF_overview.html)

# Introduction

Apple’s Core Audio Format (CAF) is a file format for storing and transporting digital audio data. It simplifies the management and manipulation of many types of audio data without the file-size limitations of other audio file formats.

Starting in iOS 5.0, you can use CAF files created in OS X that define patches, or musical voice configurations, for software-based music synthesizers such as the iOS Sample Player audio unit.

This document is intended for anyone who needs to understand the structure of CAF files. You can use the information in this document, for example, to write a CAF parser or to extend the types of data stored in CAF files. Because CAF files offer many advantages over other audio file formats, anyone writing an application for iOS or OS X that reads or writes audio files should read at least the overview chapter ([CAF File Overview](https://developer.apple.com/library/archive/documentation/MusicAudio/Reference/CAFSpec/CAF_overview/CAF_overview.html#//apple_ref/doc/uid/TP40001862-CH209-TPXREF101)) to gain an understanding of the features of CAF files. In addition, you need the information in this document if you want to use CAF files on other platforms.

End users of professional audio software may be interested in this document to learn more about the capabilities of software that supports CAF.

This document contains the following chapters:

- [CAF File Overview](https://developer.apple.com/library/archive/documentation/MusicAudio/Reference/CAFSpec/CAF_overview/CAF_overview.html#//apple_ref/doc/uid/TP40001862-CH209-TPXREF101) provides a brief overview of the Core Audio file format.
- [Core Audio Format Specification](https://developer.apple.com/library/archive/documentation/MusicAudio/Reference/CAFSpec/CAF_spec/CAF_spec.html#//apple_ref/doc/uid/TP40001862-CH210-TPXREF101) describes the CAF specification in detail.

The following documents provide additional information:

- _[Audio & Video Starting Point](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/AudioVideoStartingPoint_iOS/index.html#//apple_ref/doc/uid/TP40007298)_ introduces the resources available for music and audio developers in iOS.
- _[Multimedia Programming Guide](../Audio%20Video/Multimedia%20Programming%20Guide/About%20Audio%20and%20Video.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrx)_ describes the interfaces available to add audio features to apps in iOS.
[Next](https://developer.apple.com/library/archive/documentation/MusicAudio/Reference/CAFSpec/CAF_overview/CAF_overview.html)

