---
title: value
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolltransitionphase/value
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltransitionphase/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltransitionphase/value.json'
content_hash: 'sha256:e4130587aa864560'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollTransitionPhase](../scrolltransitionphase.md)

# value

<sub>Instance Property</sub>

A phase-derived value that can be used to scale or otherwise modify effects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var value: Double { get }
```

## Discussion

Returns -1.0 when in the topLeading phase, zero when in the identity phase, and 1.0 when in the bottomTrailing phase.

## See Also

### Accessing the phase state

- [isIdentity](isidentity.md)
