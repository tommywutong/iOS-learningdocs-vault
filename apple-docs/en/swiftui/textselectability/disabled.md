---
title: disabled
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textselectability/disabled
source_url: 'https://developer.apple.com/documentation/swiftui/textselectability/disabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textselectability/disabled.json'
content_hash: 'sha256:c842753ae4b80d87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextSelectability](../textselectability.md)

# disabled

<sub>Type Property</sub>

A selectability value that disables text selection by the person using your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static var disabled: DisabledTextSelectability { get }
```

## Discussion

Use this property to disable text selection of views that you don’t want people to select and copy, even if contained within an overall context that allows text selection.

```swift
content // Content that might contain Text views.
   .textSelection(.disabled)
   .padding()
   .contentShape(Rectangle())
   .gesture(someGesture)
```

## See Also

### Getting selectability options

- [enabled](enabled.md) — A selectability value that enables text selection by a person using your app.
