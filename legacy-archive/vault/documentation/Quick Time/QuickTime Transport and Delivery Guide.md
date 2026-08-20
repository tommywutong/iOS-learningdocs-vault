---
title: QuickTime Transport and Delivery Guide
apple_id: TP40000861
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2006-01-10'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/A-Intro/1Introduction.html
archived_at: '2026-07-18T02:05:04.418838Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/B-Chapter/2AboutDataHandlerCom.html)

# Introduction to QuickTime Transport and Delivery Guide

This book describes the principal ways that QuickTime transports and delivers data to specific devices, by using data handler components and by using video output components:

- Data handler components read and write movie data to specific devices, such as HFS disk files or computer memory. These are extremely low-level pieces of software, and are normally transparent to applications. Applications use data handler components indirectly, by making calls to the movie toolbox or a sequence grabber component. Applications can call some data handler component functions directly, however, for more complete control of data retrieval and storage. Apple provides data handler components for most device types. If you need to read or write data to a new or unsupported device type, you may need to create a data handler component.
- Video output components allow you to send QuickTime video to devices that are not recognized as displays by your computer’s operating system. Video output components are used directly by applications that allow the user to send movie output to external devices. Manufacturers of video output hardware may need to create a video output component to use with their products. Applications use video output components by selecting a component, configuring it, and associating it with a graphics world.

You need to read this book if you plan to create a data handler component, a video output component, or a sequence grabber component. Sequence grabber components need to be able to select and use data handler components.

Applications programmers who think they may need to call data handler components directly should read the section [Using Data Handler Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/C-Chapter/3UsingDataHandlerCom.html#//apple_ref/doc/uid/TP40000861-UsingDataHandlerComponents-SW1). The section [About Data Handler Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/B-Chapter/2AboutDataHandlerCom.html#//apple_ref/doc/uid/TP40000861-AboutDataHandlerComponents-SW1) may also be of general interest to QuickTime developers.

Most developers should read the section [Video Output Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/D-Chapter/4VideoOutputComponen.html#//apple_ref/doc/uid/TP40000861-VideoOutputComponents-SW1) to understand what video output components are, and when they should be used. Applications developers who will use video output components should also read the section [Using Video Output Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/E-Chapter/5UsingVideoOutputCom.html#//apple_ref/doc/uid/TP40000861-UsingVideoOutputComponents-SW1) and refer to the [Functions Used To Control Video Output Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/F-Chapter/6FunctionsUsedToCont.html#//apple_ref/doc/uid/TP40000861-FunctionsUsedToControlVideoOutputComponents-SW1) section as necessary.

This book is divided into the following chapters:

- [About Data Handler Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/B-Chapter/2AboutDataHandlerCom.html#//apple_ref/doc/uid/TP40000861-AboutDataHandlerComponents-SW1) describes what data handler components are, what they do, and how they work. Diagrams are included which illustrate their different use during movie playback and movie capture.
- [Using Data Handler Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/C-Chapter/3UsingDataHandlerCom.html#//apple_ref/doc/uid/TP40000861-UsingDataHandlerComponents-SW1) describes how to use a data handler component. Developers writing sequence grabber components will use the interfaces described in this section. Developers writing data handler components will need to support these interfaces.
- [Video Output Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/D-Chapter/4VideoOutputComponen.html#//apple_ref/doc/uid/TP40000861-VideoOutputComponents-SW1) describes what video output components are, and what they do.
- [Using Video Output Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/E-Chapter/5UsingVideoOutputCom.html#//apple_ref/doc/uid/TP40000861-UsingVideoOutputComponents-SW1) explains how to use video output components in your software.
- [Functions Used To Control Video Output Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/F-Chapter/6FunctionsUsedToCont.html#//apple_ref/doc/uid/TP40000861-FunctionsUsedToControlVideoOutputComponents-SW1) discusses the functions used to control video output components.
- [Creating Video Output Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/G-Chapter/7CreatingVideoOutput.html#//apple_ref/doc/uid/TP40000861-CreatingVideoOutputComponents-SW1) describes the routines you must implement when creating a video output component.
- [Creating Data Handler Components](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/H-Chapter/8CreatingDataHandler.html#//apple_ref/doc/uid/TP40000861-CreatingDataHandlerComponents-SW1) describes the requirements for creating a data handler component.

The following Apple books cover related aspects of QuickTime programming:

- _[QuickTime Overview](QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs)_ gives you the starting information you need to do QuickTime programming.
- _[QuickTime Movie Basics](QuickTime%20Movie%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmby)_ introduces you to some of the basic concepts you need to understand when working with QuickTime movies.
- _[QuickTime Media Types and Media Handlers Guide](QuickTime%20Media%20Types%20and%20Media%20Handlers%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqojz)_ introduces the idea of QuickTime media handler components and provides details of the video, sound, text, timecode, and tween media handlers.
- _QuickTime Guide for Windows_ provides information specific to programming for QuickTime on the Windows platform.
- _QuickTime API Reference_ provides encyclopedic details of all the functions, callbacks, data types and structures, atom types, and constants in the QuickTime API.
[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/TransportDelivery/DataHandlerComp/B-Chapter/2AboutDataHandlerCom.html)

