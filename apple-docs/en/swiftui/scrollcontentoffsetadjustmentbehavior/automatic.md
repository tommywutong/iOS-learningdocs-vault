---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollcontentoffsetadjustmentbehavior/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/scrollcontentoffsetadjustmentbehavior/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollcontentoffsetadjustmentbehavior/automatic.json'
content_hash: 'sha256:66717ae598389de4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollContentOffsetAdjustmentBehavior](../scrollcontentoffsetadjustmentbehavior.md)

# automatic

<sub>Type Property</sub>

The automatic behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var automatic: ScrollContentOffsetAdjustmentBehavior { get }
```

## Discussion

A scroll view may automatically adjust its content offset based on the current context. The absolute offset may be adjusted to keep content in relatively the same place. For example, when scrolled to the bottom, a scroll view may keep the bottom edge scrolled to the bottom when the overall size of its content changes.
