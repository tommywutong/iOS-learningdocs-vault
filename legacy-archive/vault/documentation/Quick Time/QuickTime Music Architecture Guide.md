---
title: QuickTime Music Architecture Guide
apple_id: TP40000941
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2009-06-01'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/RM/MusicAndAudio/qtma/A-Intro/1Introduction.html
archived_at: '2026-07-18T02:05:04.332149Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MusicAndAudio/qtma/B-Chapter/2TheQuickTimeMusicAr.html)

# Introduction to QuickTime Music Architecture Guide

The QuickTime Music Architecture (QTMA) allows QuickTime movies, applications, and other software to play individual musical notes, sequences of notes, and a broad range of sounds from a variety of instruments and synthesizers. With QTMA, you can also import Standard MIDI files and convert them into a QuickTime movie for easy playback.

You can use the General MIDI component for playing music on a MIDI device attached to a serial port.

Before reading this document, you should already be familiar with QuickTime and QuickTime components.

You need to read this document if you are writing an application that creates QuickTime movies and you want to incorporate music tracks as part of the movie, either by importing MIDI files or by programmatically generating musical sequences. If you want to create a music component or add an instrument to the existing library of instruments, you also need to read this document. If you are creating new instruments, you should be familiar with QT atoms and atom containers.

This document is presented in two chapters:

- [The QuickTime Music Architecture](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MusicAndAudio/qtma/B-Chapter/2TheQuickTimeMusicAr.html#//apple_ref/doc/uid/TP40000941-TheQuickTimeMusicArchitecture-SW1) describes the features and capabilities of the QuickTime music architecture.
- [Using the QuickTime Music Architecture](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MusicAndAudio/qtma/C-Chapter/3UsingtheQuickTimeMu.html#//apple_ref/doc/uid/TP40000941-UsingtheQuickTimeMusicArchitecture-SW1) describes the functions that allow applications to control all aspects of playing music tracks and generating musical sounds in QuickTime movies.

The following Apple books cover other aspects of QuickTime programming:

- _[QuickTime Overview](QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs)_ gives you the starting information you need to do QuickTime programming.
- _[QuickTime Movie Basics](QuickTime%20Movie%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmby)_ introduces you to some of the basic concepts you need to understand when working with QuickTime movies.
- _[QuickTime Movie Creation Guide](QuickTime%20Movie%20Creation%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmbw)_ describes some of the different ways your application can create a new QuickTime movie.
- _QuickTime Guide for Windows_ provides information specific to programming for QuickTime on the Windows platform.
- _QuickTime API Reference_ provides encyclopedic details of all the functions, callbacks, data types and structures, atom types, and constants in the QuickTime API.
[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MusicAndAudio/qtma/B-Chapter/2TheQuickTimeMusicAr.html)

