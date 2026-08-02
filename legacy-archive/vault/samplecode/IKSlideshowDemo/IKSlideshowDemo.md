---
title: IKSlideshowDemo
apple_id: DTS10004050
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2012-08-31'
source_url: https://developer.apple.com/library/archive/samplecode/IKSlideshowDemo/Introduction/Intro.html
archived_at: '2026-07-18T03:12:03.653762Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# IKSlideshowDemo

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2012-08-31 Update to use ARC and latest Developer Tools. Fixed deprecation warnings. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimbvgawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.4 |
| __Runtime Requirements:__ | Mac OS X 10.6 |

This small sample project shows how to use the ImageKit Slideshow to display images or PDFs.

The simple AppController implements the IKSlideshowDataSource protocol and implements the required methods:

- (NSUInteger)numberOfSlideshowItems; - (id)slideshowItemAtIndex: (NSUInteger)index;

The UI allows the user to pick one of the following two options:

1) Path to single PDF file

In this mode, a single PDF file will be displayed in Slideshow. The item is passed as a path to a PDF document.

2) Images

Images from the App bundle are passed to the Slideshow.

The 'Start' button invokes then -[runSlideshowWithDataSource:options] method of IKSlideshow.

[Next](main.m.md)

