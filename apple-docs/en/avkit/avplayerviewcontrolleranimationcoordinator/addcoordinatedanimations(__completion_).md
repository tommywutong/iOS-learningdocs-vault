---
title: 'addCoordinatedAnimations(_:completion:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 11.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrolleranimationcoordinator/addcoordinatedanimations(_:completion:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrolleranimationcoordinator/addcoordinatedanimations(_:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrolleranimationcoordinator/addcoordinatedanimations%28_%3Acompletion%3A%29.json'
content_hash: 'sha256:61e99b5d3d403560'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerAnimationCoordinator](../avplayerviewcontrolleranimationcoordinator.md)

# addCoordinatedAnimations(_:completion:)

<sub>Instance Method</sub>

Adds animations to perform alongside the playback controls’ visibility animation.

<sub>tvOS</sub>

```swift
func addCoordinatedAnimations(_ animations: (() -> Void)?, completion: (@Sendable (Bool) -> Void)? = nil)
```

<sub>tvOS</sub>

```swift
func addCoordinatedAnimations(_ animations: (() -> Void)?) async -> Bool
```

## Parameters

- `animations` — The animations to execute.

- `completion` — A closure to execute after the main animation completes. The system runs the specified animations in the same animation context as the main animation.
