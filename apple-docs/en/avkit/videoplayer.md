---
title: VideoPlayer
framework: AVKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/videoplayer
source_url: 'https://developer.apple.com/documentation/avkit/videoplayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/videoplayer.json'
content_hash: 'sha256:071331ff202bbb8d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# VideoPlayer

<sub>Structure</sub>

A view that displays content from a player and a native user interface to control playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct VideoPlayer<VideoOverlay> where VideoOverlay : View
```

## Overview

```swift
import SwiftUI
import AVKit

struct ContentView: View {

    /// An optional player the view creates in a task modifier.
    ///
    /// Creating the player instance indirectly helps to avoid 
    /// performance issues and other side effects.
    @State private var player: AVPlayer?
    @State private var isPlaying = false

    var body: some View {
        VStack {
            if let player {
                VideoPlayer(player: player)
                    .frame(width: 320, height: 180, alignment: .center)

                Button {
                    isPlaying ? player.pause() : player.play()
                    isPlaying.toggle()
                    player.seek(to: .zero)
                } label: {
                    Image(systemName: isPlaying ? "stop" : "play")
                        .padding()
                }
            }
        }
        .task {
            // Use the task modifier to defer creating the player to ensure
            // SwiftUI creates it only once when it first presents the view.
            let url = // URL to local or remote media.
            player = AVPlayer(url: url)
        }
    }
}
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a video player

- [init(player:)](<videoplayer/init(player_).md>) — Creates a video-player user interface for the player object.
- [init(player:videoOverlay:)](<videoplayer/init(player_videooverlay_).md>) — Creates a video-player user interface for the player object.
