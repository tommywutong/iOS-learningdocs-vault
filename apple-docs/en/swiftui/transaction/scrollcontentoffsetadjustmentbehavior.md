---
title: scrollContentOffsetAdjustmentBehavior
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transaction/scrollcontentoffsetadjustmentbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/transaction/scrollcontentoffsetadjustmentbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transaction/scrollcontentoffsetadjustmentbehavior.json'
content_hash: 'sha256:16c5a9fdef9e1eee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Transaction](../transaction.md)

# scrollContentOffsetAdjustmentBehavior

<sub>Instance Property</sub>

The behavior a scroll view will have regarding content offset adjustments for the current transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var scrollContentOffsetAdjustmentBehavior: ScrollContentOffsetAdjustmentBehavior { get set }
```

## Discussion

A scroll view may automatically adjust its content offset based on the current context. The absolute offset may be adjusted to keep content in relatively the same place. For example, when scrolled to the bottom, a scroll view may keep the bottom edge scrolled to the bottom when the overall size of its content changes.

Use this property to disable these kinds of adjustments when needed.
