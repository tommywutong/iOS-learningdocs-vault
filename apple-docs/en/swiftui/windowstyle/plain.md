---
title: plain
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowstyle/plain
source_url: 'https://developer.apple.com/documentation/swiftui/windowstyle/plain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowstyle/plain.json'
content_hash: 'sha256:8f0665c6c635e5ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowStyle](../windowstyle.md)

# plain

<sub>Type Property</sub>

The plain window style.

<sub>macOS, visionOS</sub>

```swift
@export(implementation) static var plain: PlainWindowStyle { get }
```

## Discussion

Unlike [automatic](automatic.md), a plain window does not receive a glass background in visionOS or window chrome in macOS. Use this style if you want more control over how these elements are used in your window.

## See Also

### Getting built-in window styles

- [automatic](automatic.md) — The default window style.
- [hiddenTitleBar](hiddentitlebar.md) — A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [titleBar](titlebar.md) — A window style which displays the title bar section of the window.
- [volumetric](volumetric.md) — A window style that creates a 3D volumetric window.
