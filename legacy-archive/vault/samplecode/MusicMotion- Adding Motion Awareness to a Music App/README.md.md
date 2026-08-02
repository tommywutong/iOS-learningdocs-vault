---
title: 'MusicMotion: Adding Motion Awareness to a Music App'
apple_id: TP40016160
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreMotion
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/MusicMotion/Listings/README_md.html
archived_at: '2026-07-18T03:16:33.119733Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MusicMotion: Adding Motion Awareness to a Music App](MusicMotion-%20Adding%20Motion%20Awareness%20to%20a%20Music%20App.md)


[Next](LICENSE.txt.md)[Previous](MusicMotion-Song.swift.md)

# README.md

```
# MusicMotion: Adding Motion Awareness to a Music App

## About MusicMotion

CoreMotion provides great contextual awareness that can be used to make apps even smarter. This sample demonstrates best practices for CoreMotion API usage and provides an example of how to fuse different types of motion and fitness data to enable context aware application behavior.

## Structure

The project consists of 2 view controllers and 4 model classes.

### View Controllers

1) SongViewController
    - A music player's song queue.

2) HistoryViewController
    - A user's history view controller.

### Models

There are a few model classes that are used throughout the app:

1) Song
2) SongManager
3) Activity
4) MotionManager

## What's Important

This sample code is a mock music application that combines motion and fitness data to update a queued playlist. The application also allows you to review historical activity and pedometer data. The MotionManager class performs the following:

1. Checks for API availability.
2. Checks for Motion Activity authorization.
3. Requests live updates of activity, pedometer data, and altitude data (while running or walking).
3. Queries for historical motion activity and correlates with historical pedometer data.

The MotionManager also contains several application specific constants that should be tuned to your specific needs.

## Requirements

### Build
Xcode 8.0, iOS 10.0 SDK

### Runtime
iOS 9.0

Copyright (C) 2016 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](MusicMotion-Song.swift.md)

