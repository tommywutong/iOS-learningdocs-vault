---
title: 'immersiveContentBrightness(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/immersivecontentbrightness(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/immersivecontentbrightness(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/immersivecontentbrightness%28_%3A%29.json'
content_hash: 'sha256:5f025b4c3a608c2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# immersiveContentBrightness(_:)

<sub>Instance Method</sub>

Sets the content brightness of an immersive space.

<sub>visionOS</sub>

```swift
nonisolated func immersiveContentBrightness(_ brightness: ImmersiveContentBrightness) -> some Scene

```

## Parameters

- `brightness` — The level of content brightness that you prefer.

## Return Value

A scene that has the specified content brightness.

## Discussion

Pass one of the standard brightness levels defined in [ImmersiveContentBrightness](../immersivecontentbrightness.md) or a custom one that you create with the [custom(_:)](<../immersivecontentbrightness/custom(__).md>) method to this scene modifier to set a preference for the content brightness in an [ImmersiveSpace](../immersivespace.md). The system takes the value that you set into account, but might not be able to honor a specific preference.

When you do this to create an environment that’s suitable for video playback, the standard brightness values provide good results for most use cases. To optimize further, you can create a custom brightness using a normalized value that expresses the linear brightness ratio between a standard dynamic range white video frame and the background that surrounds the player window.

> [!important] Important
> This modifier doesn’t affect scenes other than immersive spaces.

## See Also

### Adjusting content brightness

- [ImmersiveContentBrightness](../immersivecontentbrightness.md) — The content brightness of an immersive space.
