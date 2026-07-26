---
title: MatchedTransitionSourceConfiguration
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/matchedtransitionsourceconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/matchedtransitionsourceconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/matchedtransitionsourceconfiguration.json'
content_hash: 'sha256:3987f1970f293afb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MatchedTransitionSourceConfiguration

<sub>Protocol</sub>

A configuration that defines the appearance of a matched transition source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol MatchedTransitionSourceConfiguration : Sendable
```

## Relationships

- **Inherits From**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [EmptyMatchedTransitionSourceConfiguration](emptymatchedtransitionsourceconfiguration.md)

## Topics

### Instance Methods

- [background(_:)](<matchedtransitionsourceconfiguration/background(__).md>) — Specifies a color that will be drawn behind the content within the matched transition source.
- [clipShape(_:)](<matchedtransitionsourceconfiguration/clipshape(__).md>) — Applies the specified shape as to the matched transition source, clipping its content.
- [shadow(color:radius:x:y:)](<matchedtransitionsourceconfiguration/shadow(color_radius_x_y_).md>) — Applies the specified shadow effect to the matched transition source.

## See Also

### Defining matched transitions

- [matchedTransitionSource(id:in:)](<view/matchedtransitionsource(id_in_).md>) — Identifies this view as the source of a navigation transition, such as a zoom transition.
- [matchedTransitionSource(id:in:configuration:)](<view/matchedtransitionsource(id_in_configuration_).md>) — Identifies this view as the source of a navigation transition, such as a zoom transition.
- [EmptyMatchedTransitionSourceConfiguration](emptymatchedtransitionsourceconfiguration.md) — An unstyled matched transition source configuration.
