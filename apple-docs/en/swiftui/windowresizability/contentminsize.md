---
title: contentMinSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowresizability/contentminsize
source_url: 'https://developer.apple.com/documentation/swiftui/windowresizability/contentminsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowresizability/contentminsize.json'
content_hash: 'sha256:afba7829d6d1edf1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowResizability](../windowresizability.md)

# contentMinSize

<sub>Type Property</sub>

A window resizability that’s partially derived from the window’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var contentMinSize: WindowResizability { get set }
```

## Discussion

Windows that use this resizability have:

- A minimum size that matches the minimum size of the window’s content.
- No maximum size.

## See Also

### Getting the resizability

- [automatic](automatic.md) — The automatic window resizability.
- [contentSize](contentsize.md) — A window resizability that’s derived from the window’s content.
