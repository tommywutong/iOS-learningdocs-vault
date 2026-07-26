---
title: 'seek(to:tolerance:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy/seek(to:tolerance:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy/seek(to:tolerance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy/seek%28to%3Atolerance%3A%29.json'
content_hash: 'sha256:f5767b9c9054885a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceTimeControllable](../avplaybackuserinterfacetimecontrollable-50vcy.md)

# seek(to:tolerance:)

<sub>Instance Method</sub>

Requests a seek to the specified position.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor func seek(to position: CMTime, tolerance: CMTime)
```

## Parameters

- `position` — The position to seek to.

- `tolerance` — How close to `position` the actual seek must land. Pass `CMTime.zero` for exact frame-accurate seeking or `CMTime.positiveInfinity` for fast approximate seeking.
