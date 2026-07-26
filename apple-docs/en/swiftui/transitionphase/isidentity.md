---
title: isIdentity
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transitionphase/isidentity
source_url: 'https://developer.apple.com/documentation/swiftui/transitionphase/isidentity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transitionphase/isidentity.json'
content_hash: 'sha256:a521a8f6a63525be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TransitionPhase](../transitionphase.md)

# isIdentity

<sub>Instance Property</sub>

A Boolean that indicates whether the transition should have an identity effect, i.e. not change the appearance of its view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isIdentity: Bool { get }
```

## Discussion

This is true in the `identity` phase.

## See Also

### Getting phase characteristics

- [value](value.md) — A value that can be used to multiply effects that are applied differently depending on the phase.
