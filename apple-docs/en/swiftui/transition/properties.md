---
title: properties
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transition/properties
source_url: 'https://developer.apple.com/documentation/swiftui/transition/properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transition/properties.json'
content_hash: 'sha256:657c7c45266668b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Transition](../transition.md)

# properties

<sub>Type Property</sub>

Returns the properties this transition type has.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency static var properties: TransitionProperties { get }
```

## Discussion

Defaults to `TransitionProperties()`.

## Default Implementations

### Transition Implementations

- [properties](properties-3v8pe.md) — Returns the properties this transition type has.

## See Also

### Configuring a transition

- [animation(_:)](<animation(__).md>) — Attaches an animation to this transition.
