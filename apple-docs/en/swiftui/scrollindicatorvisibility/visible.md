---
title: visible
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollindicatorvisibility/visible
source_url: 'https://developer.apple.com/documentation/swiftui/scrollindicatorvisibility/visible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollindicatorvisibility/visible.json'
content_hash: 'sha256:82dfefa0862b2674'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollIndicatorVisibility](../scrollindicatorvisibility.md)

# visible

<sub>Type Property</sub>

Show the scroll indicators.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var visible: ScrollIndicatorVisibility { get }
```

## Discussion

The actual visibility of the indicators depends on platform conventions like auto-hiding behaviors in iOS or user preference behaviors in macOS.

## See Also

### Getting visibilties

- [automatic](automatic.md) — Scroll indicator visibility depends on the policies of the component accepting the visibility configuration.
- [hidden](hidden.md) — Hide the scroll indicators.
- [never](never.md) — Scroll indicators should never be visible.
