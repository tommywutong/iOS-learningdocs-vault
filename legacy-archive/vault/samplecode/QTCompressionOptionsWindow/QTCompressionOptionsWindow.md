---
title: QTCompressionOptionsWindow
apple_id: DTS10004627
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2008-02-22'
source_url: https://developer.apple.com/library/archive/samplecode/QTCompressionOptionsWindow/Introduction/Intro.html
archived_at: '2026-07-18T03:20:03.323493Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# QTCompressionOptionsWindow

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2008-02-22 Demonstrates how easy it is to manage QTCompressionOptions instances with a user interface. |
| __Build Requirements:__ | Mac OS X 10.5, QuickTime 7.4+ |
| __Runtime Requirements:__ | Mac OS X 10.5. QuickTime 7.4+ |

The QTCompressionOptionsWindow sample is based on QTKit Capture classes and acts as a test bed for the included QTCompressionOptionsWindow class. A Video Capture Device is required to run this sample.
QTCompressionOptionsWindow is a simple class that demonstrates one way to manage a user interface containing media compression options encapsulated in QTCompressionOptions objects. This re-usable class in completely self contained and has three parts; The nib file called QTCompressionOptionsWindow.nib, the Class Header called QTCompressionOptionsWindow.h and the implementation file called QTCompressionOptionsWindow.m. All three files must be included in any project using this object.
You can create a QTCompressionOptionsWindow instance by calling initWithMediaType: or by instantiating an instance in your Main.nib file and setting the delegate accordingly.
QTKit uses the QTCompressionOptions objects as a way to reference a set of compression settings for a particular type of media. QTCompressionOptions objects are used to describe compression settings for different types of media and are created from preset keys such as @"QTCompressionOptions120SizeH264Video" or @"QTCompressionOptionsHighQualityAACAudio". A set of currently supported keys may be returned dynamically using the compressionOptionsIdentifiersForMediaType method.

[Next](main.m.md)

