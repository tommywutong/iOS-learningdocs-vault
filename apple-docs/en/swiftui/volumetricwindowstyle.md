---
title: VolumetricWindowStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/volumetricwindowstyle
source_url: 'https://developer.apple.com/documentation/swiftui/volumetricwindowstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/volumetricwindowstyle.json'
content_hash: 'sha256:b598dd62af42d09d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# VolumetricWindowStyle

<sub>Structure</sub>

A window style that creates a 3D volumetric window.

<sub>visionOS</sub>

```swift
struct VolumetricWindowStyle
```

## Overview

Use [volumetric](windowstyle/volumetric.md) to construct this style:

```swift
WindowGroup {
    ContentView()
}
.windowStyle(.volumetric)
```

## Relationships

- **Conforms To**: [WindowStyle](windowstyle.md)

## Topics

### Creating the window style

- [init()](<volumetricwindowstyle/init().md>)

## See Also

### Supporting types

- [DefaultWindowStyle](defaultwindowstyle.md) — The default window style.
- [HiddenTitleBarWindowStyle](hiddentitlebarwindowstyle.md) — A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [PlainWindowStyle](plainwindowstyle.md) — The plain window style.
- [TitleBarWindowStyle](titlebarwindowstyle.md) — A window style which displays the title bar section of the window.
