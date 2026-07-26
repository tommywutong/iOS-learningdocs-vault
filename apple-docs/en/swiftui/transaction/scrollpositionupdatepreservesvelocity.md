---
title: scrollPositionUpdatePreservesVelocity
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transaction/scrollpositionupdatepreservesvelocity
source_url: 'https://developer.apple.com/documentation/swiftui/transaction/scrollpositionupdatepreservesvelocity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transaction/scrollpositionupdatepreservesvelocity.json'
content_hash: 'sha256:6a3a4370384c324a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Transaction](../transaction.md)

# scrollPositionUpdatePreservesVelocity

<sub>Instance Property</sub>

Whether a programmatic update to the scroll position of a scroll view preserves the current velocity of any active scroll of the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var scrollPositionUpdatePreservesVelocity: Bool { get set }
```

## Discussion

By default, when a scroll view sees a programmatic update to its scroll position, it will stop any active scrolls for unanimated scrolls. If a programmatic update is animated, this property is ignored.
