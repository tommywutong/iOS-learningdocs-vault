---
title: QuickTime File Format Specification
apple_id: TP40000939
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickTime
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/QTFF/QTFFAppenB/QTFFAppenB.html
archived_at: '2026-07-27T06:57:06.713958Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime File Format Specification](Introduction%20to%20QuickTime%20File%20Format%20Specification.md)


[Next](Random%20Access.md)[Previous](QuickTime%20Image%20File%20Format.md)

# Defining Media Data Layouts

The QuickTime file format provides a great deal of flexibility in how media data is physically arranged within a file. However, it also allows media layouts to be created that may be inefficient for playback on a given device. To complicate the matter, a media layout that is inefficient for one device may be, in fact, very efficient for another. The purpose of this appendix is to define some common uses of QuickTime files and describe the media layout in these circumstances.

## Using QuickTime Files and Media Layouts

A QuickTime file can reference media data stored in a number of files, including the file itself. If a QuickTime file references only media data contained within itself, the file is said to be self-contained. A QuickTime file can also reference media data stored in files that are not QuickTime files. This is because the QuickTime file format references media within a URL by file offset, rather than by a data structuring mechanism of a particular file format. This allows a QuickTime file to refer to data stored in any container format.

Often, it is convenient to store a single media stream per file, for example, when encoding content. It is also useful for purposes of reusing content. (To reuse an elementary stream, it is not necessary to extract it from a larger, possibly multiplexed file.)

Because QuickTime can reference media stored in any file, it is not required that media be stored in the QuickTime file format. However, this is recommended. Putting the elementary streams in a QuickTime file has several advantages, particularly in enabling interchange of the content between different tools. Further, the QuickTime file format adds very little overhead to the media—as little as a few hundred bytes in many cases—so there is no great penalty in storage space.

One of the issues facing any device (a server or a local workstation) that is attempting to play back a QuickTime file in real time is the number of file seeks that must be performed.

It is possible to arrange the data in a QuickTime file to minimize, and potentially eliminate, any seeks during the course of normal playback. (Of course, random access and other kinds of interactivity require seeks.) Minimizing seeks is accomplished by interleaving the media data in the QuickTime file in such a way that the layout of the media in the file corresponds to the order in which the media data will be required. It is expected that most servers, for example, will stream QuickTime media using the facilities of the hint tracks.

Take a scenario where the QuickTime file contains a single hint track that references an audio and a visual media stream. In order to eliminate all seeks, the hint track media must be interleaved with the audio and visual stream data. Because the hint track sample must always be read before the audio and visual media that it references, the hint track samples must always immediately precede the samples they reference.

A simple illustration of the ordering of data (that is, time and file offset increasing from left to right) is as follows:

```
H0 A0 H1 V1 H2 V2 H3 A1 H4 A2 V3 H5 V4
```

When a single hint sample references multiple pieces of media data, those pieces of media data must occur in the order that they are referenced.

[Next](Random%20Access.md)[Previous](QuickTime%20Image%20File%20Format.md)
