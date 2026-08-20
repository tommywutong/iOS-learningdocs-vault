---
title: iPod Library Access Programming Guide
apple_id: TP40008765
resource_type: Guide
platform: tvOS|iOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Audio/Conceptual/iPodLibraryAccess_Guide/Introduction/Introduction.html
archived_at: '2026-07-15T05:20:53.854799Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20iPod%20Library%20Access.md)

# Introduction

iPod library access lets your application play a user’s songs, audio books, and audio podcasts. The API design makes basic playback very simple while also supporting advanced searching and playback control.

iPod library access opens up iOS to allow a wide range of music-related enhancements to your application. Here are just a few ideas for what you can do:

- Let a user assemble and play a soundtrack for your game or exercise app
- Let a user retrieve the names of their favorite artists, songs, and albums from their iPod library to send to a friend
- Provide a recommendation service for new music or artist touring schedules based on the content of a user’s iPod library

Before reading this document, you should already be comfortable with iOS development as described in _[Start Developing iOS Apps Today (Retired)](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/index.html#//apple_ref/doc/uid/TP40011343)_.

_iPod Library Access Guide_ complements _[Media Player Framework Reference](https://developer.apple.com/documentation/mediaplayer)_, which you may find helpful to refer to as you read this document.

This document includes the following chapters:

- [About iPod Library Access](About%20iPod%20Library%20Access.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donrvfvbuqmjqgmwvgvzz)—Provides a complete overview of music playback and iPod library access using this API.
- [Using Media Playback](Using%20Media%20Playback.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donrvfvbuqmjqgawvgvzr)—Explains how to create and use music players.
- [Using the Media Item Picker](Using%20the%20Media%20Item%20Picker.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donrvfvbuqmjqgqwvgvzr)—Shows how to invoke the picker and implement its delegate methods for retrieving the media items chosen by a user.
- [Using the iPod Library](Using%20the%20iPod%20Library.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donrvfvbuqmjqgewvgvzr)—Goes into depth on creating and using predicates and queries to retrieve media items from the device iPod library.
- [Glossary](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4donrvfvbuqmjqgiwvgvzw)—Defines terminology used in describing this API.

To get the most out of this technology, take advantage of these resources:

- _[Media Player Framework Reference](https://developer.apple.com/documentation/mediaplayer)_—complete reference documentation for the classes introduced in this document.
- _[AddMusic](../../../samplecode/AddMusic/AddMusic.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobugu)_—an iPhone sample project that you can download, study, adapt, and extend for use in your iOS applications.
- _[Audio Session Programming Guide](../Audio%20Session%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzv)_—explains how to configure the overall audio behavior for your application. Read this document if you are creating an application that uses your own audio along with iPod audio playback.
- _[Core Audio Overview](../../Music%20Audio/Core%20Audio%20Overview/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztknzx)_—explains how audio formats can mix in iOS and describes the available audio formats for application audio.
[Next](About%20iPod%20Library%20Access.md)

