---
title: QuickTime Component Creation Guide
apple_id: TP40000898
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2007-01-08'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/RM/WritingQTComponents/MHCreating/A-Intro/1Introduction.html
archived_at: '2026-07-18T02:05:04.470892Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/WritingQTComponents/MHCreating/B-Chapter/2AboutQuickTimeMedia.html)

# Introduction to QuickTime Component Creation Guide

This book tells you how to build new components to extend the capabilities of QuickTime. The component types covered by this book include:

- _Media_ _handler_ components, which allow the Movie Toolbox to manipulate the data in a media. These media handlers isolate the Movie Toolbox (and the applications programmer) from the details of how and where a media is stored. They are also called _derived_ media handlers because they are derived from a base media handler, provided by Apple. The base media handler component handles most of the duties that are common to all media handlers, freeing the component developer to focus on the task of reading and writing a particular media type.
- _Preview_ components, which create or display a preview of a QuickTime movie file. The preview is typically displayed as part of an Open File dialog; it is normally an image, but it may contain text, sound, or other data. The preview may be contained in the movie file or it may be created on the fly by the preview component whenever it is needed.

In general, only developers who are creating a new media handler or preview component need to read this book.

This book contains the following chapters:

- [About QuickTime Media Handler Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/WritingQTComponents/MHCreating/B-Chapter/2AboutQuickTimeMedia.html#//apple_ref/doc/uid/TP40000898-AboutQuickTimeMediaHandlerComponents-SW1) describes what media handler components are and how they are used.
- [Creating a Derived Media Handler Component](https://developer.apple.com/library/archive/documentation/QuickTime/RM/WritingQTComponents/MHCreating/C-Chapter/3CreatingaDerivedMed.html#//apple_ref/doc/uid/TP40000898-CreatingaDerivedMediaHandlerComponent-SW1) describes the process of creating a derived media handler component.
- [Derived Media Handler Support](https://developer.apple.com/library/archive/documentation/QuickTime/RM/WritingQTComponents/MHCreating/D-Chapter/4DerivedMediaHandler.html#//apple_ref/doc/uid/TP40000898-DerivedMediaHandlerSupport-SW1) defines the functions you must support if you are creating a derived media handler, the functions that you may optionally support, and utility functions available to your component from the base media handler.
- [Creating Preview Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/WritingQTComponents/MHCreating/F-Chapter/6CreatingPreviewComp.html#//apple_ref/doc/uid/TP40000898-CreatingPreviewComponents-SW1) describes how to create your own preview component. A listing of a sample component is included.
- [Functions For Displaying Previews](https://developer.apple.com/library/archive/documentation/QuickTime/RM/WritingQTComponents/MHCreating/G-Chapter/7FunctionsForDisplay.html#//apple_ref/doc/uid/TP40000898-FunctionsForDisplayingPreviews-SW1) describes the functions for displaying previews, handling events in previews, and creating previews that are provided by preview components.

For general information about media handler components, see _[QuickTime Media Types and Media Handlers Guide](QuickTime%20Media%20Types%20and%20Media%20Handlers%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqojz)_. This book introduces the idea of QuickTime media handler components and provides details of the video, sound, text, timecode, and tween media handlers.

For general information about preview components, see _[QuickTime Movie Internals Guide](QuickTime%20Movie%20Internals%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjr)_. This book also covers some of the technology present inside QuickTime movies, including time management, modifier tracks, access keys, and movie posters.

Information about creating more types of QuickTime components (other than those covered in this book) is included in books about those components. See the following:

- Information about creating data handler components is in _[QuickTime Transport and Delivery Guide](QuickTime%20Transport%20and%20Delivery%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnrr)_.
- Information about creating movie data exchange components is in _[QuickTime Import and Export Guide](QuickTime%20Import%20and%20Export%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmbt)_.
- Information about creating image transcoder components is in _[QuickTime Compression and Decompression Guide](QuickTime%20Compression%20and%20Decompression%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnzy)_.
- Information about creating video effect components is in _[QuickTime Video Effects and Transitions Guide](QuickTime%20Video%20Effects%20and%20Transitions%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnry)_.
- Information about creating tween components is in _[QuickTime Media Types and Media Handlers Guide](QuickTime%20Media%20Types%20and%20Media%20Handlers%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqojz)_.
- Information about creating video digitizer components is in _[QuickTime Movie Creation Guide](QuickTime%20Movie%20Creation%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmbw)_.
- Information about creating video output components is in _[QuickTime Transport and Delivery Guide](QuickTime%20Transport%20and%20Delivery%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnrr)_.

The following additional Apple books cover related aspects of QuickTime programming:

- _[QuickTime Overview](QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs)_ gives you the starting information you need to do QuickTime programming.
- _[QuickTime Movie Basics](QuickTime%20Movie%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmby)_ introduces you to some of the basic concepts you need to understand when working with QuickTime movies.
- _QuickTime Guide for Windows_ provides information specific to programming for QuickTime on the Windows platform.
[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/WritingQTComponents/MHCreating/B-Chapter/2AboutQuickTimeMedia.html)

