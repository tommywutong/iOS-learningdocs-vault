---
title: interactive
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dismissbehavior/interactive
source_url: 'https://developer.apple.com/documentation/swiftui/dismissbehavior/interactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dismissbehavior/interactive.json'
content_hash: 'sha256:6ebe73c9b5e679e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DismissBehavior](../dismissbehavior.md)

# interactive

<sub>Type Property</sub>

The interactive dismiss behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let interactive: DismissBehavior
```

## Discussion

Use this behavior when you want to dismiss a window in a manner that is similar to the standard system affordances for window dismissal - for example, when a user clicks the close button.

This is the default behavior on macOS and iOS.

On macOS, dismissing a window using this behavior will not dismiss a window which is currently showing a modal presentation, such as a sheet or alert. Additionally, a document window that is dismissed with this behavior will show the save dialog if there are unsaved changes to the document.

On iOS, dismissing a window using this behavior will dismiss it regardless of any modal presentations being shown.

## See Also

### Getting behaviors

- [destructive](destructive.md) — The destructive dismiss behavior.
