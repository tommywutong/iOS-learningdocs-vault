---
title: isFocusEffectEnabled
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/isfocuseffectenabled
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/isfocuseffectenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/isfocuseffectenabled.json'
content_hash: 'sha256:9e9441b1a54d2b2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# isFocusEffectEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the view associated with this environment allows focus effects to be displayed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isFocusEffectEnabled: Bool { get set }
```

## Discussion

The default value is `true`.

## See Also

### Configuring effects

- [focusEffectDisabled(_:)](<../view/focuseffectdisabled(__).md>) — Adds a condition that controls whether this view can display focus effects, such as a default focus ring or hover effect.
