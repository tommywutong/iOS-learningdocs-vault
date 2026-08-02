---
title: QuickTime Media Types and Media Handlers Guide
apple_id: TP40000899
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/A-Intro/1Introduction.html
archived_at: '2026-07-18T02:05:04.119398Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/B-Chapter/2AboutMediaHandlers.html)

# Introduction to QuickTime Media Types and Media Handlers Guide

This book introduces the idea of QuickTime media handler components and provides details of the video, sound, text, timecode, and tween media handlers.

The last half of this book describes the media handler components that perform tween operations, sometimes called tweeners. It also describes tween operations performed by QuickTime for tween types that are native to QuickTime.

A tween operation lets you algorithmically generate an output value for any point in a time interval. The input for a tween is a small number of values, often as few as one or two, from which a range of values can be derived. You can use output from a tween either to modify tracks in a QuickTime movie or to perform actions unrelated to movies.

For a general overview of media handler technology in QuickTime, read [About Media Handlers](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/B-Chapter/2AboutMediaHandlers.html#//apple_ref/doc/uid/TP40000899-AboutMediaHandlers-SW1). The rest of this book is of interest primarily to developers who need to develop new media handlers for QuickTime. You need to read the last five chapters of this book if you are a developer planning to work with or create QuickTime tween components.

This book is divided into nine chapters:

- [About Media Handlers](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/B-Chapter/2AboutMediaHandlers.html#//apple_ref/doc/uid/TP40000899-AboutMediaHandlers-SW1) describes media handlers, components that are responsible for interpreting and manipulating a media’s sample data.
- [Video and Sound Media Handlers](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/C-Chapter/3VideoandSoundMediaH.html#//apple_ref/doc/uid/TP40000899-VideoandSoundMediaHandlers-SW1) describes the media handlers that interpret and manipulate video data.
- [Text Media Handlers](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/D-Chapter/4TextMediaHandlers.html#//apple_ref/doc/uid/TP40000899-TextMediaHandlers-SW1) describes media handlers that you can use to add plain or styled text samples to a movie, indicate scrolling and highlighting properties for the text, search for text, and highlight specified text runs.
- [Timecode Media Handlers](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/E-Chapter%20copy%205/5TimecodeMediaHandle.html#//apple_ref/doc/uid/TP40000899-TimecodeMediaHandlers-SW1) describe media handlers that let QuickTime movies store timing information derived from a movie’s original source material, such as SMPTE timecodes.
- [Tweens and Tween Operations](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/F-Chapter%20copy%204/6TweensandTweenOpera.html#//apple_ref/doc/uid/TP40000899-TweensandTweenOperations-SW1) introduces tweens and their uses, and provides an overview of the tween operations that are possible.
- [Using Tween Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/H-Chapter%20copy%202/8UsingTweenComponent.html#//apple_ref/doc/uid/TP40000899-UsingTweenComponents-SW1) describes how to create tween containers that the tween media handler uses.
- [Creating a Tween Component](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/J-Chapter%20copy/10CreatingaTweenCompo.html#//apple_ref/doc/uid/TP40000899-CreatingaTweenComponent-SW1) explains how to create a tween component for a new data type, a new interpolation algorithm, or both.
- [Tween Components and Native Tween Types](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/I-Chapter%20copy%201/9TweenComponentsandN.html#//apple_ref/doc/uid/TP40000899-TweenComponentsandNativeTweenTypes-SW1) describes the native tween types handled by QuickTime; the tween components included in QuickTime; and the constants, data types, and routines associated with tween components.
- [Tween Media Handlers](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/G-Chapter%20copy%203/7TweenMediaHandlers.html#//apple_ref/doc/uid/TP40000899-TweenMediaHandlers-SW1) describes media handlers that are used to send tween values from a tween track to a receiving track, such as a video track or a sound track.

For a discussion of QuickTime movie time management, see _[QuickTime Movie Internals Guide](QuickTime%20Movie%20Internals%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjr)_.

The following Apple books cover aspects of QuickTime programming related to media handlers:

- _[QuickTime Overview](QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs)_ gives you the starting information you need to do QuickTime programming.
- _[QuickTime Movie Basics](QuickTime%20Movie%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmby)_ introduces you to some of the basic concepts you need to understand when working with QuickTime movies.
- _QuickTime Guide for Windows_ provides information specific to programming for QuickTime on the Windows platform.
- _[QuickTime Compression and Decompression Guide](QuickTime%20Compression%20and%20Decompression%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnzy)_ introduces you to the QuickTime Image Compression Manager and its associated components, which provide image-compression and image-decompression services to applications and to other QuickTime components.
- _[QuickTime Video Effects and Transitions Guide](QuickTime%20Video%20Effects%20and%20Transitions%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnry)_ tells you how to program QuickTime video effects and transitions between movie tracks and graphic images.
- _[QuickTime Component Creation Guide](QuickTime%20Component%20Creation%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqojy)_ tells you how to build new components to extend the capabilities of QuickTime, including media handlers and preview components.
- _QuickTime API Reference_ provides encyclopedic details of all the functions, callbacks, data types and structures, atom types, and constants in the QuickTime API.
[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MediaTypesAndHandlers/MHFundamentals/B-Chapter/2AboutMediaHandlers.html)

