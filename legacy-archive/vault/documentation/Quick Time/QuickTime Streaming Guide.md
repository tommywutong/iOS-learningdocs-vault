---
title: QuickTime Streaming Guide
apple_id: TP30001145
resource_type: Guide
platform: macOS
topic: null
technology: QuickTime
published: '2009-06-01'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/RM/Streaming/StreamingClient/A-Intro/1Introduction.html
archived_at: '2026-07-18T02:05:04.377960Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/Streaming/StreamingClient/B-Chapter/2AboutQuickTimeStrea.html)

# Introduction to QuickTime Streaming Guide

QuickTime streaming allows QuickTime movies to play on a client computer while being transmitted from a server. This document describes the basics of QuickTime streaming and the types of protocols supported.

The document also describes in detail the requirements for packetizer components that divide movies into packets for streaming and reassemble packets into movies for display on the receiving end. It lists the functions relevant to media packetizers and reassemblers, along with common streaming error codes.

You need to read this chapter if you want to do any of the following:

- play streamed movies within your application
- write RTP server software that transmits streamed QuickTime movies
- write a media packetizer
- write a media reassembler

This book is divided into the following chapters:

- [About QuickTime Streaming](https://developer.apple.com/library/archive/documentation/QuickTime/RM/Streaming/StreamingClient/B-Chapter/2AboutQuickTimeStrea.html#//apple_ref/doc/uid/TP30001145-AboutQuickTimeStreaming-SW1) discusses the basics of QuickTime streaming and the variety of protocols that can be used to stream QuickTime movies.
- [Using QuickTime Streaming](https://developer.apple.com/library/archive/documentation/QuickTime/RM/Streaming/StreamingClient/C-Chapter/3UsingQuickTimeStrea.html#//apple_ref/doc/uid/TP30001145-UsingQuickTimeStreaming-SW1) describes from a programming perspective how to create, send, and receive streamed movies.
- [Media Packetizers](https://developer.apple.com/library/archive/documentation/QuickTime/RM/Streaming/StreamingClient/D-Chapter/4MediaPacketizers.html#//apple_ref/doc/uid/TP30001145-MediaPacketizers-SW1) describes the media packetizer and packet builder, and tells you how to build a packetizer.
- [Packet Reassemblers](https://developer.apple.com/library/archive/documentation/QuickTime/RM/Streaming/StreamingClient/E-Chapter%20copy/5PacketReassemblers.html#//apple_ref/doc/uid/TP30001145-PacketReassemblers-SW1) tells you how to build a packet reassembler.

The following Apple books cover related aspects of QuickTime programming:

- _[QuickTime Overview](QuickTime%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojs)_ gives you the starting information you need to do QuickTime programming.
- _[QuickTime Movie Basics](QuickTime%20Movie%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmby)_ introduces you to some of the basic concepts you need to understand when working with QuickTime movies.
- _[QuickTime Movie Creation Guide](QuickTime%20Movie%20Creation%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmbw)_ describes some of the different ways your application can create a new QuickTime movie.
- _QuickTime API Reference_ provides encyclopedic details of all the functions, callbacks, data types and structures, atom types, and constants in the QuickTime API.
[Next](https://developer.apple.com/library/archive/documentation/QuickTime/RM/Streaming/StreamingClient/B-Chapter/2AboutQuickTimeStrea.html)

