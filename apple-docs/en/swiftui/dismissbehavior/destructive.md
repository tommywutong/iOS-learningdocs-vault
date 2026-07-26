---
title: destructive
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dismissbehavior/destructive
source_url: 'https://developer.apple.com/documentation/swiftui/dismissbehavior/destructive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dismissbehavior/destructive.json'
content_hash: 'sha256:e1e8104948a26850'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DismissBehavior](../dismissbehavior.md)

# destructive

<sub>Type Property</sub>

The destructive dismiss behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let destructive: DismissBehavior
```

## Discussion

Use this behavior when you want to dismiss a window regardless of any conditions that would normally prevent the dismissal. Dismissing windows in this matter may result in loss of state.

On macOS, this behavior will cause windows to dismiss even when they are currently showing a modal presentation, such as a sheet or alert. Additionally, a document window will not show the save dialog when there are unsaved changes and the window is dismissed with this behavior.

On iOS, this behavior behaves the same as `interactive`.

## See Also

### Getting behaviors

- [interactive](interactive.md) — The interactive dismiss behavior.
