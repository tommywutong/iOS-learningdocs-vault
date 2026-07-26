---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowresizability/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/windowresizability/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowresizability/automatic.json'
content_hash: 'sha256:adb0efa8529e6041'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowResizability](../windowresizability.md)

# automatic

<sub>Type Property</sub>

The automatic window resizability.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var automatic: WindowResizability { get set }
```

## Discussion

When you use automatic resizability, SwiftUI applies a resizing strategy that’s appropriate for the scene type:

- Windows from [WindowGroup](../windowgroup.md), [Window](../window.md), and [DocumentGroup](../documentgroup.md) scene declarations use the [contentMinSize](contentminsize.md) strategy.
- A window from a [Settings](../settings.md) scene declaration uses the [contentSize](contentsize.md) strategy.
- Windows on visionOS with a window style of [volumetric](../windowstyle/volumetric.md) use the [contentSize](contentsize.md) strategy.

Automatic resizability is the default if you don’t specify another value using the [windowResizability(_:)](<../scene/windowresizability(__).md>) scene modifier.

## See Also

### Getting the resizability

- [contentMinSize](contentminsize.md) — A window resizability that’s partially derived from the window’s content.
- [contentSize](contentsize.md) — A window resizability that’s derived from the window’s content.
