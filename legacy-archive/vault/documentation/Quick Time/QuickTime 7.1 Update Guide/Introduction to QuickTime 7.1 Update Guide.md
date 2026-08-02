---
title: QuickTime 7.1 Update Guide
apple_id: TP40003543
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2007-03-06'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/Conceptual/QT7-1_Update_Guide/Content/1Introduction.html
archived_at: '2026-07-18T01:52:42.759780Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



# Introduction to QuickTime 7.1 Update Guide

QuickTime is the industry standard for multimedia programming and application development, with a rich and evolving API comprised of more than 2700 function calls. Its component-based architecture is highly extensible, enabling applications to display, import, export, modify, and capture a broad range of digital media, including audio, video, still images, text, Flash, MIDI, sprites, VR panoramas, among other media types. QuickTime is designed from the ground up to work with local disk-based media, media accessed over a network, or streams of real-time data.

This document provides detailed information about the new features, changes, and enhanced capabilities that are available in QuickTime 7.1 for Mac OS X version 10.4 and for Windows.

If you are a QuickTime API-level developer, content author, multimedia producer, or Webmaster who is currently working with QuickTime, you should read this document.

The document is written both for developers who use QuickTime on the Mac OS X and Windows platforms and want to learn the new programming features of QuickTime 7.1, and for beginning or experienced Cocoa programmers interested in using QuickTime in their application development.

This update guide is intended to provide QuickTime developers, as well as other developers new to the platform, with a comprehensive description of the changes and enhancements in this software release. Beyond this brief introductory chapter, the material discussed in [New Features, Changes and Enhancements in QuickTime 7.1](New%20Features%2C%20Changes%20and%20Enhancements%20in%20QuickTime%207.1.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknbtfvhgk52gmvqxi5lsmvzug2dbnztwk43bnzsek3timfxggzlnmvxhi43jnzixk2ldnnkgs3lfg4ys2u2xge) of the guide describes these changes and enhancements, along with the new functions available in QuickTime 7.1, with an emphasis on understanding their usage for application developers.

This document consists of a single chapter:

- [New Features, Changes and Enhancements in QuickTime 7.1](New%20Features%2C%20Changes%20and%20Enhancements%20in%20QuickTime%207.1.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknbtfvhgk52gmvqxi5lsmvzug2dbnztwk43bnzsek3timfxggzlnmvxhi43jnzixk2ldnnkgs3lfg4ys2u2xge) describes in detail the many new and enhanced features available in QuickTime 7.1. It is intended to provide developers with a conceptual overview, in addition to code samples and illustrations of usage, so that developers can take advantage of many of new features in QuickTime 7.1 in their applications.

For more detailed information about each of the new Procedural-C functions, constants and data types available in the QuickTime 7.1 release, refer the _[QuickTime 7.1 Update Reference](https://developer.apple.com/library/archive/documentation/QuickTime/Reference/QT7-1_Update_Reference/index.html#//apple_ref/doc/uid/TP40004221)_. For information about the new methods, attributes, and notifications available in the Objective-C (Cocoa) QTMovie and QTTrack classes, refer to the _[QuickTime Kit Framework Reference](https://developer.apple.com/documentation/qtkit)_.

For developers who want to take advantage of QuickTime features and functionality, the complete suite of documentation that describes the QuickTime API is available online in HTML and PDF at the [QuickTime Documentation](https://developer.apple.com/documentation/QuickTime/index.html) website.

QuickTime update guides are available with each new release of QuickTime Player and Pro. These guides are useful for developers who need to understand, at a conceptual level, the changes and enhancements in these releases. The following update guides document, in reverse order, the features available in these releases:

- _[QuickTime 7 for Windows Update Guide](../QuickTime%207%20for%20Windows%20Update%20Guide/Introduction%20to%20QuickTime%207%20for%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinzw)_
- _[QuickTime 7 Update Guide](../QuickTime%207%20Update%20Guide/Introduction%20to%20QuickTime%207.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrt)_
- _[QuickTime 7.1 User's Guide](http://images.apple.com/quicktime/pdf/QuickTime7_User_Guide.pdf)_
- _[QuickTime 6.3 + 3GPP](../QuickTime%206.3%20%2B%203GPP.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzy)_
- _[QuickTime 6](../QuickTime%206.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzx)_
- _[QuickTime 5](../QuickTime%205.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzw)_

If you are new to QuickTime, you should begin by referring to [Getting Started With QuickTime](https://developer.apple.com/referencelibrary/GettingStarted/GS_QuickTime/index.html), which describes the various starting points and learning paths for working with this rich, multimedia API.

Updates to the QuickTime technical documentation website are provided on a regular basis. Developers can also subscribe to various mailing lists for the latest news and information.

To sign up for any of Apple’s Developer Programs, go to: [Developer Membership](https://developer.apple.com/membership/index.html).

