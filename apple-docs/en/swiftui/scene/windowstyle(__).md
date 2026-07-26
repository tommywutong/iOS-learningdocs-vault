---
title: 'windowStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 11.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/windowstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/windowstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/windowstyle%28_%3A%29.json'
content_hash: 'sha256:1bca9b1f48e0aec9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# windowStyle(_:)

<sub>Instance Method</sub>

Sets the style for windows created by this scene.

<sub>macOS, visionOS</sub>

```swift
nonisolated func windowStyle<S>(_ style: S) -> some Scene where S : WindowStyle

```

## See Also

### Creating windows

- [WindowGroup](../windowgroup.md) — A scene that presents a group of identically structured windows.
- [Window](../window.md) — A scene that presents its content in a single, unique window.
- [UtilityWindow](../utilitywindow.md) — A specialized window scene that provides secondary utility to the content of the main scenes of an application.
- [WindowStyle](../windowstyle.md) — A specification for the appearance and interaction of a window.
