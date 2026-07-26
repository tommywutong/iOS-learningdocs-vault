---
title: scenePhase
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/scenephase
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/scenephase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/scenephase.json'
content_hash: 'sha256:eccaf941fefb7abc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# scenePhase

<sub>Instance Property</sub>

The current phase of the scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var scenePhase: ScenePhase { get set }
```

## Discussion

The system sets this value to provide an indication of the operational state of a scene or collection of scenes. The exact meaning depends on where you access the value. For more information, see [ScenePhase](../scenephase.md).

## See Also

### Monitoring scene life cycle

- [ScenePhase](../scenephase.md) — An indication of a scene’s operational state.
