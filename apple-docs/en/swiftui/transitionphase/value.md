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
doc_path: /documentation/swiftui/transitionphase/value
source_url: 'https://developer.apple.com/documentation/swiftui/transitionphase/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transitionphase/value.json'
content_hash: 'sha256:2b410ea5efec0af5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TransitionPhase](../transitionphase.md)

# value

<sub>Instance Property</sub>

A value that can be used to multiply effects that are applied differently depending on the phase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var value: Double { get }
```

## Return Value

Zero when in the `identity` case, -1.0 for `willAppear`, and 1.0 for `didDisappear`.

## See Also

### Getting phase characteristics

- [isIdentity](isidentity.md) — A Boolean that indicates whether the transition should have an identity effect, i.e. not change the appearance of its view.
