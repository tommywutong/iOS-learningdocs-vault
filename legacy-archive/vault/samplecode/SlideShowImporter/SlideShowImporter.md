---
title: SlideShowImporter
apple_id: DTS10000901
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SlideShowImporter/Introduction/Intro.html
archived_at: '2026-07-18T03:24:49.701799Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.txt.md)

# SlideShowImporter

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Movie import component, constructs a movie from images, effect types, and audio files. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon QuickTime 5 |

This is an example of a movie import component that accepts as input an XML file, and constructs a movie from the elements in this file. The XML file consists of XML elements of the form: /\* An XML Element, i.e. <element attr="value" attr="value" ...> [contents] </element> or <element attr="value" attr="value" .../> \*/ Elements can be images, effect types, and audio files. Each image element consists of an image file attribute and a duration attribute. Each effect element consists of an effect type attribute and a duration attribute. Each audio element consists of an audio-only movie file attribute. The component parses each element in the file using the QuickTime XML parsing component, line by line, and constructs a movie from these elements. For example, given the following sample elements: <image src="sky01.jpg" dur="1" /><effect type = "dissolve" dur = "1" /> the program will construct a track media item from the image file "sky01.jpg", and add this media item to the video track of the movie (NOTE: in this sample, all our images are the same size - if you use different size images they will be scaled appropriately by QuickTime). The duration of this media item will be 1 as specified by the duration attribute. After adding the image element to the movie, the program will add the next element, the dissolve effect. After all images & effects are added this will result in a movie file which displays a series of images, with an effect as a transition between each image. In addition, an audio-only movie file will be played for the length of the movie as background music. Requirements: QuickTime 5 Keywords: xml movie import component

[Next](README.txt.md)

