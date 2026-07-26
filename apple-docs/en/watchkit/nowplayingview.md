---
title: NowPlayingView
framework: WatchKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/watchkit/nowplayingview
source_url: 'https://developer.apple.com/documentation/watchkit/nowplayingview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/watchkit/nowplayingview.json'
content_hash: 'sha256:431882296daed46c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WatchKit](../watchkit.md)

# NowPlayingView

<sub>Structure</sub>

A view that displays the system’s Now Playing interface so that the user can control audio.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency struct NowPlayingView
```

## Overview

With a Now Playing view, users can control current or recently played audio without leaving your app. The Now Playing view displays information about the current audio source, such as another app on the user’s Apple Watch or iPhone. For example, users can play and pause music from their Apple Watch’s Music app or control the volume of a podcast on their iPhone.

The system automatically selects the source. If the user is listening to audio on their watch or phone, the system selects that audio source. Otherwise, the system selects the most recently used source.

Always present the Now Playing view so that it fills the screen in a nonscrolling container. Don’t add any other elements to the view.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a Now Playing View

- [init()](<nowplayingview/init().md>) — Creates a view that displays the system’s Now Playing interface.

## See Also

### User interface

- [Storyboard support](storyboard-support.md) — Connect your code to storyboard elements using interface controllers, interface objects, and event handlers.
