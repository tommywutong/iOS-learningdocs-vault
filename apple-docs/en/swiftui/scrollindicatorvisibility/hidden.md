---
title: hidden
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollindicatorvisibility/hidden
source_url: 'https://developer.apple.com/documentation/swiftui/scrollindicatorvisibility/hidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollindicatorvisibility/hidden.json'
content_hash: 'sha256:fd75709a8cb43a28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollIndicatorVisibility](../scrollindicatorvisibility.md)

# hidden

<sub>Type Property</sub>

Hide the scroll indicators.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var hidden: ScrollIndicatorVisibility { get }
```

## Discussion

By default, scroll views in macOS show indicators when a mouse is connected. Use [never](never.md) to indicate a stronger preference that can override this behavior.

## See Also

### Getting visibilties

- [automatic](automatic.md) — Scroll indicator visibility depends on the policies of the component accepting the visibility configuration.
- [never](never.md) — Scroll indicators should never be visible.
- [visible](visible.md) — Show the scroll indicators.
