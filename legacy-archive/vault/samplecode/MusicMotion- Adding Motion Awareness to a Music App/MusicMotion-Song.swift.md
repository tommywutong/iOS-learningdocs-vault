---
title: 'MusicMotion: Adding Motion Awareness to a Music App'
apple_id: TP40016160
resource_type: Sample Code
platform: iOS
topic: null
technology: CoreMotion
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/MusicMotion/Listings/MusicMotion_Song_swift.html
archived_at: '2026-07-18T03:16:33.088525Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MusicMotion: Adding Motion Awareness to a Music App](MusicMotion-%20Adding%20Motion%20Awareness%20to%20a%20Music%20App.md)


[Next](README.md.md)[Previous](MusicMotion-SongViewController.swift.md)

# MusicMotion/Song.swift

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
This class represents an instance of a single song.
*/

import Foundation
import UIKit

/**
    This struct is responsible for the storing the song metadata. The `SongManager`
    manages instances of this struct.
*/
struct Song: CustomDebugStringConvertible {
    // MARK: Properties

    var artist: String
    var title: String

    var albumImage: UIImage?

    // MARK: CustomDebugStringConvertible

    var debugDescription: String {
        return "Artist: \(artist), Title: \(title), Album Image: \(albumImage)"
    }
}
```

[Next](README.md.md)[Previous](MusicMotion-SongViewController.swift.md)

