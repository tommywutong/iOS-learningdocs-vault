---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scenerestorationbehavior/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/scenerestorationbehavior/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenerestorationbehavior/automatic.json'
content_hash: 'sha256:d8738f185c374218'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SceneRestorationBehavior](../scenerestorationbehavior.md)

# automatic

<sub>Type Property</sub>

The automatic behavior. The scene’s windows will be restored as defined by the underlying platform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let automatic: SceneRestorationBehavior
```

## Discussion

On macOS, this behavior is governed by a system setting which can be toggled on and off by the user. On all other platforms, it is enabled by default.
