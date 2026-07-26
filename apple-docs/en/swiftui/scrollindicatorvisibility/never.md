---
title: never
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollindicatorvisibility/never
source_url: 'https://developer.apple.com/documentation/swiftui/scrollindicatorvisibility/never'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollindicatorvisibility/never.json'
content_hash: 'sha256:8c35599fac1c2acd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollIndicatorVisibility](../scrollindicatorvisibility.md)

# never

<sub>Type Property</sub>

Scroll indicators should never be visible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var never: ScrollIndicatorVisibility { get }
```

## Discussion

This value behaves like [hidden](hidden.md), but overrides scrollable views that choose to keep their indicators visible. When using this value, provide an alternative method of scrolling. The typical horizontal swipe gesture might not be available, depending on the current input device.

## See Also

### Getting visibilties

- [automatic](automatic.md) — Scroll indicator visibility depends on the policies of the component accepting the visibility configuration.
- [hidden](hidden.md) — Hide the scroll indicators.
- [visible](visible.md) — Show the scroll indicators.
