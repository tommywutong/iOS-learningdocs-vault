---
title: ImageProducing
apple_id: DTS10000955
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-05-05'
source_url: https://developer.apple.com/library/archive/samplecode/ImageProducing/Introduction/Intro.html
archived_at: '2026-07-18T03:12:45.253835Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](src-ImageProducing.java.md)

# ImageProducing

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2006-05-05 Support for XCode 2. Modified project layout for platform independent distribution and compilation. |
| __Build Requirements:__ | XCode 2.2, or Java 2 SDK for Windows, and QuickTime 7 |
| __Runtime Requirements:__ | Java 1.5 and QuickTime 7, or later, recommended |

Demonstrates the QTImageProducer and interaction with Java's ImageProducing model. The QTImageProducer is responsible for getting the QT movie and producing the pixels for a java.awt.Image. The QTImageProducer feeds the pixels to any java.image.ImageConsumers, that are registered with it and, in a format that they are able to deal with. Swing buttons control the movie playback.
The IPJComponent, a convenience class, is provided as an example of this interaction for creating a custom JComponent. The QTImageProducer can be used directly by any of Java's built in ImageConsumers (such as the java.awt.Component). It demonstrates how the QTImageProducer can be used directly as a pixel resource for a swing component.
To achieve this, the IPJComponent creates the Image and tells the QTImageProducer object to produce pixels. Then, the IPJComponent paints its image onto the component space using the java drawing commands. In this scenario QuickTime is not drawing directly to the screen.

[Next](src-ImageProducing.java.md)

