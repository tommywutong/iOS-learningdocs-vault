---
title: isPositionedByUser
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollposition/ispositionedbyuser
source_url: 'https://developer.apple.com/documentation/swiftui/scrollposition/ispositionedbyuser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollposition/ispositionedbyuser.json'
content_hash: 'sha256:6405275d7f83f08d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollPosition](../scrollposition.md)

# isPositionedByUser

<sub>Instance Property</sub>

Whether the scroll view has been positioned by the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isPositionedByUser: Bool { get set }
```

## Discussion

You can write to this property to control whether the scroll view acts as if it has been positioned by the user. If the position had a non-nil edge / point value, that value will become nil when setting this property to true.
