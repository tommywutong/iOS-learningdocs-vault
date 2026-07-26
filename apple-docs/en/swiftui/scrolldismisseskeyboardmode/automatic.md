---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolldismisseskeyboardmode/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/scrolldismisseskeyboardmode/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolldismisseskeyboardmode/automatic.json'
content_hash: 'sha256:2dff8ee131828a3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollDismissesKeyboardMode](../scrolldismisseskeyboardmode.md)

# automatic

<sub>Type Property</sub>

Determine the mode automatically based on the surrounding context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
static var automatic: ScrollDismissesKeyboardMode { get }
```

## Discussion

By default, a [TextEditor](../texteditor.md) is interactive while a [List](../list.md) of scrollable content always dismiss the keyboard on a scroll, when linked against iOS 16 or later.

## See Also

### Getting modes

- [immediately](immediately.md) — Dismiss the keyboard as soon as scrolling starts.
- [interactively](interactively.md) — Enable people to interactively dismiss the keyboard as part of the scroll operation.
- [never](never.md) — Never dismiss the keyboard automatically as a result of scrolling.
