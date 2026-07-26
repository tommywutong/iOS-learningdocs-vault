---
title: WindowStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowstyle
source_url: 'https://developer.apple.com/documentation/swiftui/windowstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowstyle.json'
content_hash: 'sha256:79e98c7237c6c088'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WindowStyle

<sub>Protocol</sub>

A specification for the appearance and interaction of a window.

<sub>macOS, visionOS</sub>

```swift
protocol WindowStyle
```

## Relationships

- **Conforming Types**: [DefaultWindowStyle](defaultwindowstyle.md), [HiddenTitleBarWindowStyle](hiddentitlebarwindowstyle.md), [PlainWindowStyle](plainwindowstyle.md), [TitleBarWindowStyle](titlebarwindowstyle.md), [VolumetricWindowStyle](volumetricwindowstyle.md)

## Topics

### Getting built-in window styles

- [automatic](windowstyle/automatic.md) — The default window style.
- [hiddenTitleBar](windowstyle/hiddentitlebar.md) — A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [plain](windowstyle/plain.md) — The plain window style.
- [titleBar](windowstyle/titlebar.md) — A window style which displays the title bar section of the window.
- [volumetric](windowstyle/volumetric.md) — A window style that creates a 3D volumetric window.

### Supporting types

- [DefaultWindowStyle](defaultwindowstyle.md) — The default window style.
- [HiddenTitleBarWindowStyle](hiddentitlebarwindowstyle.md) — A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [PlainWindowStyle](plainwindowstyle.md) — The plain window style.
- [TitleBarWindowStyle](titlebarwindowstyle.md) — A window style which displays the title bar section of the window.
- [VolumetricWindowStyle](volumetricwindowstyle.md) — A window style that creates a 3D volumetric window.

## See Also

### Creating windows

- [WindowGroup](windowgroup.md) — A scene that presents a group of identically structured windows.
- [Window](window.md) — A scene that presents its content in a single, unique window.
- [UtilityWindow](utilitywindow.md) — A specialized window scene that provides secondary utility to the content of the main scenes of an application.
- [windowStyle(_:)](<scene/windowstyle(__).md>) — Sets the style for windows created by this scene.
