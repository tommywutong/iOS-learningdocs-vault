---
title: viewID
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollposition/viewid
source_url: 'https://developer.apple.com/documentation/swiftui/scrollposition/viewid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollposition/viewid.json'
content_hash: 'sha256:8997c03c09bc9115'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollPosition](../scrollposition.md)

# viewID

<sub>Instance Property</sub>

The type-erased id of the view positioned in the scroll view if configured to be in that position or the user has scrolled past a view with an id of matching type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var viewID: (any Hashable & Sendable)? { get }
```
