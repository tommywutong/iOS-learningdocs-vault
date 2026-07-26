---
title: prominent
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/tabrole/prominent
source_url: 'https://developer.apple.com/documentation/swiftui/tabrole/prominent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabrole/prominent.json'
content_hash: 'sha256:51f4069b1ef48464'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabRole](../tabrole.md)

# prominent

<sub>Type Property</sub>

The prominent role.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var prominent: TabRole { get }
```

## Discussion

A tab role that provides prominent visual treatment to one of the tabs in supported tab bars. Only one tab can receive the prominent treatment. When there are no tabs with an explicit `.prominent` role, then a `.search` role tab may receive the prominent visual treatment by default.
