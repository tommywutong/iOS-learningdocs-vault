---
title: Getting Started with QuickTime
apple_id: TP30001099
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2007-02-20'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_QuickTime/_index.html
archived_at: '2026-07-18T02:39:26.540713Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Technology Overview

QuickTime provides a rich API that helps your applications display, import, export, modify, and capture many kinds of media, including audio, video, still images, text, Flash, MIDI, sprites, VR panoramas, and more. It works with local disk-based media, media accessed over a network, or streams of real-time data.

Using the QuickTime API, you can write programs that run on both Mac OS and Windows.

Similarly, media packaged as QuickTime movies play equally well on Mac OS and Windows, provided QuickTime is installed on the playback machine. A QuickTime movie can store any of the media types that QuickTime can play, including MP3 audio, JPEG images, MPEG-4 video, text, or any combination of such media.

Your application can use QuickTime to:

- Open and play video movies, audio files, still images, and other media
- Edit and modify multimedia
- Translate still images from one format to another
- Compress audio, video, and still images in various formats
- Synchronize multiple media to a common time line
- Capture audio and/or video from an external device
- Save output from your application as a QuickTime movie
- Stream media over a LAN or the Internet
- Create and display virtual reality objects and panoramas

You can extend QuickTime's capabilities by writing new QuickTime components, often without rewriting any application code. For example, you can add support for a new media type, compression algorithm, or video digitizer card, simply by writing QuickTime components. In many cases, added components become available to existing applications transparently.

### Start Here

Before you begin working with the QuickTime API, you should download a [software development kit](https://developer.apple.com/sdk/) for your platform. An SDK includes the necessary header files and libraries for you to create code that makes calls to QuickTime on your platform. There are QuickTime SDKs for Mac OS X, Windows, Java, and Java for Windows.

You should start your reading with the [QuickTime Overview](../../documentation/Quick%20Time/QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs); it’s okay to skim at this point. You might also want to read the “Overview” and “Movies” sections of [An Introduction to QuickTime](https://developer.apple.com/quicktime/qttutorial/index.html).

Windows programmers should then read the “Cross-Platform Development” section of [An Introduction to QuickTime](https://developer.apple.com/quicktime/qttutorial/index.html) and may want to skim through QuickTime for Windows Programmers as well.

### Choose a Learning Path

When you're ready to start delving into the API documentation, where you start depends on your choice of programming framework. You can then explore the parts of the QuickTime API designed to help with what you want to do, such as play movies or edit them, capture audio and video, or import and export media.

#### Learning About the QuickTime API

Most of the QuickTime API, and most of the documentation and sample code, are intended for procedural C or C++ programmers (Windows or Carbon frameworks).

If you are programming in Java or Objective-C, you have direct access to high-level QuickTime capabilities, but you may need to make calls to the C/C++ API for access to lower-level functions. You may also need to read some C/C++ documentation and sample code.

- __If you are a Java programmer__, start with [QuickTime for Java—Getting Started](https://developer.apple.com/quicktime/qtjava/getstarted.html)
- __If you are a Cocoa programmer__, start with [QuickTime Kit Programming Guide](../../documentation/Quick%20Time/QuickTime%20Kit%20Programming%20Guide/Introduction%20to%20QuickTime%20Kit%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenbv).
- __If you are a C/C++ (Carbon or Windows) programmer__, start with

  - [QuickTime Initialization Guide](../../documentation/Quick%20Time/QuickTime%20Initialization%20Guide/Introduction%20to%20QuickTime%20Initialization%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimzv)
  - [Component Manager for QuickTime](../../documentation/Quick%20Time/Component%20Manager%20for%20QuickTime/Introduction%20to%20Component%20Manager%20for%20QuickTime.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjy)
  - [QuickTime Movie Playback Programming Guide](../../documentation/Quick%20Time/QuickTime%20Movie%20Playback%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjz)
  - “QuickTime Components” in [Introduction to QuickTime](https://developer.apple.com/documentation/QuickTime/INMAC/INTROS/xxIntroductions.7.htm)
- __To see the most recent additions and changes to the QuickTime API__, see the latest [QuickTime Update Guide](https://developer.apple.com/referencelibrary/API_Fundamentals/QuickTime-fund-title.html).

#### Playing Movies, Including Audio and Still Images

To write a simple movie player application, read [QuickTime Movie Playback Programming Guide](../../documentation/Quick%20Time/QuickTime%20Movie%20Playback%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjz) then [Movie Controller Components](https://developer.apple.com/documentation/QuickTime/RM/MovieBasics/MovieContComp/index.html).

Windows programmers should also read [QuickTime and File System Pathnames](https://developer.apple.com/quicktime/icefloe/dispatch004.html).

You can find sample code in [QuickTime Movie Basics](https://developer.apple.com/samplecode/Sample_Code/QuickTime/Basics.htm) and in [Play Movie with Controller](https://developer.apple.com/samplecode/Play_Movie_with_Controller/index.html).

#### Editing Movies

To write a simple movie editor application, read the following documents from the [QuickTime Movie Basics](../../documentation/Quick%20Time/QuickTime%20Movie%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmby) documentation:

- [QuickTime Movie Playback Programming Guide](../../documentation/Quick%20Time/QuickTime%20Movie%20Playback%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjz)
- Movie Controller Components
- [Editing Movies](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTEditing/B-Chapter/2EditingMovies.html#//apple_ref/doc/uid/TP40000908-EditingMovies) in [QuickTime Movie Basics](../../documentation/Quick%20Time/QuickTime%20Movie%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmby)
- [Saving Movies](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTEditing/C-Chapter/3SavingMovies.html#//apple_ref/doc/uid/TP40000908-SavingMovies) in [QuickTime Movie Basics](../../documentation/Quick%20Time/QuickTime%20Movie%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmby)

You can find sample code in [QuickTime Movie Basics](https://developer.apple.com/samplecode/Sample_Code/QuickTime/Basics.htm).

#### Creating Movies

You can create movies by capturing audio and video from an external source, or by synthesizing sample data programmatically.

- __If you are capturing or digitizing sample data to create a movie__, read [Creating Movies](https://developer.apple.com/library/archive/documentation/QuickTime/RM/CreatingMovies/MTCreateMovies/B-Chapter/2CreatingMovies.html#//apple_ref/doc/uid/TP40000906-CreatingMovies) and [Sequence Grabber Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/CreatingMovies/MTCreateMovies/C-Chapter/3SequenceGrabberComp.html#//apple_ref/doc/uid/TP40000906-SequenceGrabberComponents) in [QuickTime Movie Creation Guide](../../documentation/Quick%20Time/QuickTime%20Movie%20Creation%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmbw).
- __If you are creating sample data programmatically to build a movie__, read [Creating Movies](https://developer.apple.com/library/archive/documentation/QuickTime/RM/CreatingMovies/MTCreateMovies/B-Chapter/2CreatingMovies.html#//apple_ref/doc/uid/TP40000906-CreatingMovies) in [QuickTime Movie Creation Guide](../../documentation/Quick%20Time/QuickTime%20Movie%20Creation%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmbw) and MovieExportFromProceduresToDataRef.
- __If you are a Windows programmer__, you should also read [Mixing Quickdraw and Win32 Drawing: GWorlds, HDCs, HBITMAPs, and DIB sections](https://developer.apple.com/quicktime/icefloe/dispatch016.html).

See also the sample code [CreateMovie](https://developer.apple.com/samplecode/CreateMovie/index.html) and [qtcapture](https://developer.apple.com/samplecode/qtcapture/index.html).

#### Learning More About the QuickTime API

Additional features of the QuickTime API that you may want to learn more about are:

- Importing and exporting media, in [QuickTime Import and Export Guide](../../documentation/Quick%20Time/QuickTime%20Import%20and%20Export%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmbt)
- Capturing movies from external sources such as video input cards, in [About Video Digitizer Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/CreatingMovies/MTCreateMovies/I-Chapter/9AboutVideoDigitizer.html#//apple_ref/doc/uid/TP40000906-AboutVideoDigitizerComponents) in [QuickTime Import and Export Guide](../../documentation/Quick%20Time/QuickTime%20Import%20and%20Export%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmbt)
- Streaming movies using real-time protocols, in [QuickTime Streaming Server Modules Programming Guide](../../documentation/Quick%20Time/QuickTime%20Streaming%20Server%20Modules%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbt)
- Adding interactivity using sprites and wired actions, in [QuickTime Interactivity](https://developer.apple.com/library/archive/documentation/QuickTime/IQ_InteractiveMovies/generalintro/1-General-Intro.html#//apple_ref/doc/uid/TP40000883-CH205) in [Interactive Movies](../../documentation/Quick%20Time/Interactive%20Movies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqobt)
- Working with virtual reality, in [QuickTime VR](../../documentation/Quick%20Time/QuickTime%20VR.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnbu)
- Writing new QuickTime components, in [QuickTime Component Creation Guide](../../documentation/Quick%20Time/QuickTime%20Component%20Creation%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqojy)

### Next Steps

A good source for recent articles, relevant SDKs, mailing lists, links, and documentation is the [ADC QuickTime topic page](https://developer.apple.com/quicktime/).

The [QuickTime Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000433) contains indispensable resources for developing QuickTime applications and components, and can be bookmarked for easy access.

- [Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP30000433)

  Conceptual and how-to information for QuickTime.
- [Reference](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000433)

  Focused, detailed descriptions in reference format for QuickTime.
- [Release Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000872-TP30000433)

  Late-breaking news and highlights of new or changed features in the latest release.
- [Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30000433)

  QuickTime sample code for Mac OS and Windows.
- [Technical Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000924-TP30000433)

  Late-breaking documents on timely technology issues.
- [Technical Q&As](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000926-TP30000433)

  Programming tips, code snippets, & FAQs by Apple’s support engineers.
- Mailing Lists

  The [quicktime-api](http://lists.apple.com/mailman/listinfo/quicktime-api) mailing list is an excellent place to discuss QuickTime programming and the QuickTime API. To discuss movie authoring and website development, you can join the [quicktime-users](http://lists.apple.com/mailman/listinfo/quicktime-users) mailing list. To discuss all aspects of Quicktime VR—photography, tools, authoring, and websites—join the [quicktime-vr](http://lists.apple.com/mailman/listinfo/quicktime-vr) mailing list.

These additional Apple resource pages may be helpful:

- [Tutorials](http://www.apple.com/quicktime/tutorials/)

  Tools, tips, and tutorials for web and movie authors
- [Tools and Utilities](https://developer.apple.com/quicktime/quicktimeintro/tools/)

  Free Apple tools for QuickTime programmers, movie authors, and website developers.
- [Letters from the Ice Floe](https://developer.apple.com/quicktime/icefloe/)

  Programming tips on important topics, by the QuickTime engineers
- [QuickTime Streaming Server and Darwin Streaming Server](http://www.apple.com/quicktime/products/qtss/)

  QuickTime’s real-time streaming server technology

