---
title: QuickTime Movie Playback Programming Guide
apple_id: TP40000919
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-06-01'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTOpenPlayMovies/1openplaymovies_Introduction/Introduction.html
archived_at: '2026-07-18T02:05:04.199712Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTOpenPlayMovies/2openplaymovies_Overview/Overview.html)

# Introduction To QuickTime Movie Playback Programming Guide

This document describes how to open and play stored media, including QuickTime movies and other formats that QuickTime can automatically import and play, from sources such as a file, URL, pointer, or handle.

This document supersedes and replaces "Opening and Playing Movies."

The information in this document is of interest to nearly all developers working with QuickTime.

This document is intended for programmers working in C or C++ using the Carbon or QuickTime for Windows frameworks. Cocoa developers should generally use the QuickTime Kit framework instead, but may have occasion to use the interfaces described here for access to low-level functions not duplicated in Cocoa.

This document contains the following sections:

- [Overview](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTOpenPlayMovies/2openplaymovies_Overview/Overview.html#//apple_ref/doc/uid/TP40000919-2-Overview)
- [Setting Up Graphics and Audio Output](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTOpenPlayMovies/3openplaymovies_output/SettingUpGraphicsand.html#//apple_ref/doc/uid/TP40000919-3-SettingUpGraphicsandAudioOutput)
- [Getting a Movie](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTOpenPlayMovies/4openplaymovies_getmovie/GettingaMovie.html#//apple_ref/doc/uid/TP40000919-4-GettingaMovie)
- [Monitoring the Load State](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTOpenPlayMovies/5openplaymovies_loadstate/MonitoringtheLoadSta.html#//apple_ref/doc/uid/TP40000919-5-MonitoringtheLoadState)
- [Playing a Movie](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTOpenPlayMovies/6openplaymovies_playmovie/PlayingaMovie.html#//apple_ref/doc/uid/TP40000919-6-PlayingaMovie)
- [Appendix A: File Types QuickTime Can Open as Movies](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTOpenPlayMovies/7openplaymovies_appendix/AppendixA.html#//apple_ref/doc/uid/TP40000919-7-FileTypesthatQuickTimeCanOpenasMovies)
- [Appendix B: Playing a Movie Using Low-Level Commands](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTOpenPlayMovies/7openplaymovies_appendix/AppendixA.html#//apple_ref/doc/uid/TP40000919-7-PlayingaMovieUsingLowLevelCommands)
- [Movie Playback Reference](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTOpenPlayMovies/8openplaymovies_reference/MoviePlaybackReferen.html#//apple_ref/doc/uid/TP40000919-8-MoviePlaybackReference)

Before you read this document, you should already be familiar with _[QuickTime Initialization Guide](QuickTime%20Initialization%20Guide/Introduction%20to%20QuickTime%20Initialization%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimzv)_ and _[QuickTime Overview](QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs)_. If you are new to QuickTime, see [Getting Started with QuickTime](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_QuickTime/_index.html#//apple_ref/doc/uid/TP30001099).

[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTOpenPlayMovies/2openplaymovies_Overview/Overview.html)

