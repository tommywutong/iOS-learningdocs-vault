---
title: 'textVariant(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/textvariant(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/textvariant(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/textvariant%28_%3A%29.json'
content_hash: 'sha256:2ab70dbf5db1b2bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# textVariant(_:)

<sub>Instance Method</sub>

Controls the way text size variants are chosen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func textVariant<V>(_ preference: V) -> some View where V : TextVariantPreference

```

## Discussion

Certain types of text, such as `Text(_:format:)`, can generate strings of different size to better fit the available space. By default, all text uses the widest available variant. Setting the variant to be [sizeDependent](../textvariantpreference/sizedependent.md) allows the text to take the available space into account when choosing what content to display.
