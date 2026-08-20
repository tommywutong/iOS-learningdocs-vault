---
title: QuickTime Movie Internals Guide
apple_id: TP40000911
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieInternals/MTTimeSpace/A-Intro/1Introduction.html
archived_at: '2026-07-18T02:05:04.239850Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieInternals/MTTimeSpace/B-Chapter/2MovieTimeandSpace.html)

# Introduction to QuickTime Movie Internals Guide

This book covers some of the technology present inside QuickTime movies, including time management, modifier tracks, access keys, posters, and movie and file previews.

You should read this book if you are going to work with QuickTime movies.

This book consists of the following chapters:

- [Movie Time and Space](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieInternals/MTTimeSpace/B-Chapter/2MovieTimeandSpace.html#//apple_ref/doc/uid/TP40000911-MovieTimeandSpace-SW1) describes the functions of the movie toolbox that your application will use to manipulate the timebase and spatial characteristics of movies, tracks, and media.
- [Clock Components Overview](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieInternals/MTTimeSpace/C-Chapter/3ClockComponentsOver.html#//apple_ref/doc/uid/TP40000911-ClockComponentsOverview-SW1) describes the general features and uses of clock components, and provides diagrams showing the relationship between clock components, applications, and the Movie Toolbox.
- [Movie Clocks, Sound Clocks, and Video Output](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieInternals/MTTimeSpace/D-Chapter/4MovieClocksSoundClo.html#//apple_ref/doc/uid/TP40000911-MovieClocksSoundClocksandVideoOutput-SW1) describes how to set a movie’s master clock, how a movie’s default clock is chosen, the use of the sound clock, and how to use `SetMovieMasterClock` with video output components.
- [Clock Component Functions](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieInternals/MTTimeSpace/E-Chapter/5ClockComponentFunct.html#//apple_ref/doc/uid/TP40000911-ClockComponentFunctions-SW1) describes the functions which clock components must support, the callback functions that a clock component may optionally support, and functions which QuickTime uses to alert a clock component of changes in the environment. Applications programmers may be interested in the current time function and the callback functions. The other functions are of interest to developers who wish to create new components.
- [Modifier Tracks](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieInternals/MTTimeSpace/F-Chapter/6ModifierTracks.html#//apple_ref/doc/uid/TP40000911-ModifierTracks-SW1) explains track references and modifier tracks, which create dynamic relationships between tracks in a QuickTime movie. You need to read this chapter if your application programmatically creates movies that contain modifier tracks, effects, filters, transitions, or alternate tracks.
- [Movie Toolbox Access Keys](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieInternals/MTTimeSpace/G-Chapter/7MovieToolboxAccessK.html#//apple_ref/doc/uid/TP40000911-MovieToolboxAccessKeys-SW1) describes QuickTime’s mechanism that lets an application that supplies data to register a password for the data with QuickTime and let a user enter the password to gain access to the data.
- [Movie Posters and Movie Previews](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieInternals/MTTimeSpace/H-Chapter/8MoviePostersandMovi.html#//apple_ref/doc/uid/TP40000911-MoviePostersandMoviePreviews-SW1) describes the functions your application can use to work with posters and previews. A poster is a still frame from a movie, while a preview is a short excerpt.
- [Previewing Files](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieInternals/MTTimeSpace/I-Chapter/9PreviewingFiles.html#//apple_ref/doc/uid/TP40000911-PreviewingFiles-SW1) describes how to create and display file previews shown as part of the Open File dialog. A file preview is typically a thumbnail image taken from the movie that is displayed in an Open File dialog. Some sample code is included. Read this if you would like to include preview thumbnails of movies.

The following Apple books cover related aspects of QuickTime programming:

- _[QuickTime Overview](QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs)_ gives you the starting information you need to do QuickTime programming.
- _[QuickTime Movie Basics](QuickTime%20Movie%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmby)_ introduces you to some of the basic concepts you need to understand when working with QuickTime movies.
- _[QuickTime Movie Creation Guide](QuickTime%20Movie%20Creation%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmbw)_ describes some of the different ways your application can create a new QuickTime movie.
- _QuickTime Guide for Windows_ provides information specific to programming for QuickTime on the Windows platform.
- _QuickTime API Reference_ provides encyclopedic details of all the functions, callbacks, data types and structures, atom types, and constants in the QuickTime API.
[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieInternals/MTTimeSpace/B-Chapter/2MovieTimeandSpace.html)

