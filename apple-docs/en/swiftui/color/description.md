---
title: description
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/color/description
source_url: 'https://developer.apple.com/documentation/swiftui/color/description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/description.json'
content_hash: 'sha256:6b9b83b5e2ec1199'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# description

<sub>Instance Property</sub>

A textual representation of the color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var description: String { get }
```

## Discussion

Use this method to get a string that represents the color. The [print(_:separator:terminator:)](<../../swift/print(__separator_terminator_).md>) function uses this property to get a string representing an instance:

```swift
print(Color.red)
// Prints "red"
```
