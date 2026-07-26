---
title: 'foregroundColor(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/text/foregroundcolor(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/foregroundcolor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/foregroundcolor%28_%3A%29.json'
content_hash: 'sha256:41211f7553ca3764'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# foregroundColor(_:)

<sub>Instance Method</sub>

Sets the color of the text displayed by this view.

> [!warning] Deprecated
> Use [foregroundStyle(_:)](<foregroundstyle(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func foregroundColor(_ color: Color?) -> Text
```

## Parameters

- `color` — The color to use when displaying this text.

## Return Value

A text view that uses the color value you supply.

## Discussion

Use this method to change the color of the text rendered by a text view.

For example, you can display the names of the colors red, green, and blue in their respective colors:

```swift
HStack {
    Text("Red").foregroundColor(.red)
    Text("Green").foregroundColor(.green)
    Text("Blue").foregroundColor(.blue)
}
```

![Three text views arranged horizontally, each containing](../../../../attachments/31654f673e42a4a453b46dbad7d32b61/SwiftUI-Text-foregroundColor@2x.png)
