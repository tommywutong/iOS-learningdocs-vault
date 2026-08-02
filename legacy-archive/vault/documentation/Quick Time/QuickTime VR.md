---
title: QuickTime VR
apple_id: TP40000944
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2009-06-01'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/0Preface/QTVR-preface.html
archived_at: '2026-07-18T02:04:19.377989Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/1Chap/1-General-Intro.html)

# Introduction to QuickTime VR

This book is a comprehensive guide to building and developing interactive QuickTime movies using QuickTime VR, and is part of Apple’s _Inside QuickTime: Technical Reference Library_. It is intended primarily for content authors, Webmasters, and tool developers who need to understand the fundamentals of QuickTime interactivity and, specifically, how they can incorporate QuickTime VR into their own applications.

This book supersedes all existing documentation, including _Programming with QuickTime VR 2.1_. It extends the content in those volumes and brings it up to date with the current software release of QuickTime 6.

The book is written as a companion volume to the _QuickTime API Reference_ and supplements the latest documentation and updates to QuickTime that are available at

[http://developer.apple.com/documentation/QuickTime/QuickTime.html](https://developer.apple.com/documentation/QuickTime/QuickTime.html)

The book is divided into the following chapters:

- [Chapter 1, QuickTime Interactivity,](https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/1Chap/1-General-Intro.html#//apple_ref/doc/uid/TP40000944-CH205-BABECEDE) presents a general introduction to QuickTime interactivity, as well as a brief overview of QuickTime basics and the underlying QuickTime software architecture. It is intended for developers who are new to QuickTime, or need to refresh their understanding of QuickTime fundamentals.
- [Chapter 2, QuickTime VR Panoramas and Object Movies,](https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/2Chap/2-QTVR-Authoring.html#//apple_ref/doc/uid/TP40000944-CH206-BAJGAGFA) introduces developers and programmers to QuickTime VR, the QuickTime technology developed by Apple that allows users to interactively explore and examine photorealistic, three-dimensional virtual worlds. If you are new to QuickTime VR, you need to read this chapter for a conceptual overview of VR and to understand the techniques you can apply in producing VR-based content for the Web.
- [Chapter 3, Creating QuickTime VR Panoramas and Object Movies,](https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/3Chap/3-QTVR-Programming.html#//apple_ref/doc/uid/TP40000944-CH207-BCIGFDGC) discusses some of the tools and techniques needed to produce VR content for the Web.
- [Chapter 4, QuickTime VR Programming,](https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/4Chap/4-QTVR-Manager.html#//apple_ref/doc/uid/TP40000944-CH208-CJBGGDIA) is aimed at programmers and tool developers who want to incorporate QTVR movies in their applications, both on the Web and as standalone programs. It discusses the QuickTime VR Manager, which you can use in conjunction with QuickTime to open and display QuickTime VR objects and panoramas, change the viewing angle or zoom level, handle mouse events for QuickTime VR movies, and perform other operations.
- [Chapter 5, QuickTime VR Movie Structure,](https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/6Chap/6-Creating-QTVR-Movies.html#//apple_ref/doc/uid/TP40000944-CH209-BCIBDDFI) describes the format of the tracks that make up a QuickTime VR movie file. The information in this chapter, combined with the information in [Chapter 7, QTVR Atom Containers,](https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/7Chap/7-QTVR-atoms-file-format.html#//apple_ref/doc/uid/TP40000944-CH211-BAJJCAGC) and the overview from [Chapter 2, QuickTime VR Panoramas and Object Movies,](https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/2Chap/2-QTVR-Authoring.html#//apple_ref/doc/uid/TP40000944-CH206-BAJGAGFA) will enable you to add to your application the ability to create QuickTime VR movies.
- [Chapter 6, Cubic QuickTime VR Movies,](https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/5Chap/5-QTVR-Movie-Controller.html#//apple_ref/doc/uid/TP40000944-CH210-BAJEDFFD) discusses how to create cubic QuickTime VR movies. It also explains some of the techniques you can use to convert a panoramic image into a QuickTime VR panoramic movie.
- [Chapter 7, QTVR Atom Containers,](https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/7Chap/7-QTVR-atoms-file-format.html#//apple_ref/doc/uid/TP40000944-CH211-BAJJCAGC) describes the VR world and node information atom containers. You need to know about the various atoms contained in the VR world and node information atom containers if you want to extract information from a QuickTime VR file that cannot be obtained using VR Manager functions.
- Appendix A, [Wired Actions and QuickTime VR Movies](https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/AppA/appendix_a.html#//apple_ref/doc/uid/TP40000944-CH212-BBCDGEHH) explains in detail, step-by-step, how you can add wired actions to a QuickTime VR movie, working through a QuickTime code sample. The programming tasks involved are outlined in this appendix.
- Appendix B, [Understanding Panoramic Resolution](https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/AppB/appendix_b.html#//apple_ref/doc/uid/TP40000944-CH213-BBCDGEHH) discusses one of the most frequently misunderstood concepts in QuickTime VR––panoramic resolution––and the issues and questions that typically arise in any discussion of the topic.
- A Bibliography lists the volumes of QuickTime developer documentation that are available online for download from Apple’s QuickTime Technical Publications website––the most current and up-to-date source for all QuickTime developer documentation. The QuickTime technical documentation suite totals more than 10,000 pages.
- An Index is provided with page references to the terms, concepts, and functions in the book.

This book provides various conventions to present information. Words that require special treatment appear in specific fonts or font styles. Certain types of information, such as parameter blocks, use special fonts so that you can scan them quickly.

All code listings, reserved words, and the names of actual data structures, constants, fields, parameters, and functions are shown in Letter Gothic `(this is Letter Gothic)`.

Words that appear in boldface are key terms or concepts that are defined in the glossary.

There are several types of notes used in this book.

The functions described in this book are available using C interfaces. How you access them depends on the development environment you are using.

Code listings in this book are shown in ANSI C. They suggest methods of using various functions and illustrate techniques for accomplishing particular tasks. Although most code listings have been compiled and tested, Apple Computer Inc., does not intend for you to use these code samples in your application.

For any online updates to this book, check the QuickTime developers’ page on the World Wide Web at

[http://developer.apple.com/documentation/QuickTime/QuickTime.html](https://developer.apple.com/documentation/QuickTime/QuickTime.html)

or you can go directly to the documentation page at

[http://developer.apple.com/documentation/QuickTime/WiredMoviesandSprites-date.html](https://developer.apple.com/documentation/QuickTime/WiredMoviesandSprites-date.html)

For information about membership in Apple’s developer program, you should go to this URL:

[http://developer.apple.com/index.html](https://developer.apple.com/index.html)

For technical support, go to this URL:

[http://developer.apple.com/products/techsupport/index.html](https://developer.apple.com/products/techsupport/index.html)

For information on registering signatures, file types, and other technical information, contact

Macintosh Developer Technical Support Apple Computer, Inc. 1 Infinite Loop, M/S 303-2T Cupertino, CA 95014

[Next](https://developer.apple.com/library/archive/documentation/QuickTime/InsideQT_QTVR/1Chap/1-General-Intro.html)

