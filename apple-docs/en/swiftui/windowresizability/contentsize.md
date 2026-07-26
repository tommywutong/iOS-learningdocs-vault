---
title: contentSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowresizability/contentsize
source_url: 'https://developer.apple.com/documentation/swiftui/windowresizability/contentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowresizability/contentsize.json'
content_hash: 'sha256:34714c4c3177c71f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowResizability](../windowresizability.md)

# contentSize

<sub>Type Property</sub>

A window resizability that’s derived from the window’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var contentSize: WindowResizability { get set }
```

## Discussion

Windows that use this resizability have:

- A minimum size that matches the minimum size of the window’s content.
- A maximum size that matches the maximum size of the window’s content.

## See Also

### Getting the resizability

- [automatic](automatic.md) — The automatic window resizability.
- [contentMinSize](contentminsize.md) — A window resizability that’s partially derived from the window’s content.
