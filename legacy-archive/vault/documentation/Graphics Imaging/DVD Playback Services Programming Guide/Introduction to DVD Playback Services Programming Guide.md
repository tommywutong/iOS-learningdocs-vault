---
title: DVD Playback Services Programming Guide
apple_id: TP40002163
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: DVDPlayback
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/DVDPlaybackGuide/dvdguide_intro/dvdguide_intro.html
archived_at: '2026-07-15T07:35:41.745632Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Programming%20Concepts.md)

# Introduction to DVD Playback Services Programming Guide

This guide is written for developers who want to learn how to use DVD Playback Services, the programming interface for the DVD Playback framework. DVD Playback Services is a core technology introduced in OS X version 10.3.

You can use DVD Playback Services in a Mac app to display any DVD-Video recording located on an optical disc or a mass storage device such as a hard drive. The DVD Playback Services API makes it easy for applications to incorporate basic video playback features such as selecting a title from a menu and playing the title, as well as advanced features such as bookmarks. Apple's DVD Player application uses DVD Playback Services extensively.

You'll find this guide useful if you're working on:

- Applications used for authoring and publishing rich multimedia content. You can use DVD Playback Services to extend these applications to play DVD-Video content as part of a larger presentation.
- DVD-Video publishing systems. You can use DVD Playback Services for testing (or proofing) content that's under development.
- Software DVD-Video players. For example, you could use DVD Playback Services to add DVD-Video playback features to a general media player.

DVD is a big subject, and excellent technical documentation is available in bookstores and online to help you acquire a basic understanding of DVD concepts and terminology. This document assumes that you’re familiar with DVD basics.

To get the most out of this guide, you should read it in this order:

- [Programming Concepts](Programming%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnbzfvkfawcsivddcmbr) describes the most important programming features in DVD Playback Services.
- [Basic Programming Tasks](Basic%20Programming%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnjqfvkfawcsivddcmbr) shows how to implement basic DVD playback features.
- [Additional Programming Tasks](Additional%20Programming%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrtfvkfanbqgaydgmrsgawviucykjcummjqge) shows how to implement some other DVD playback features, and how to debug your code.

An appendix contains a glossary that defines many of the terms used in this guide. Readers new to DVD may find it useful to read through the glossary before diving into the programming concepts.

Apple offers some additional resources to supplement the information in this guide:

- _DVD Playback Framework Reference_ describes the functions, data types, and constants in DVD Playback Services.
- The sample code project _[CocoaDVDPlayer](../../../samplecode/CocoaDVDPlayer/CocoaDVDPlayer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzzgi)_ demonstrates how to write a Cocoa application that uses DVD Playback Services to play DVD-Video media.

Also explore these external (non-Apple) documents and websites:

- The book _DVD Demystified, Second Edition_ (McGraw-Hill Professional, ISBN0071350268), by Jim Taylor, is the authoritative guide to DVD technology.
- The website [DVD FAQ](http://dvddemystified.com/dvdfaq.html) (dvddemystified.com/dvdfaq.html) contains a list of frequently asked questions (and answers) about DVD technology, maintained by Jim Taylor.
- [DVD Forum](http://dvdforum.org/) (dvdforum.org) is the website of the primary industry association for the promotion of DVD technology.
[Next](Programming%20Concepts.md)

