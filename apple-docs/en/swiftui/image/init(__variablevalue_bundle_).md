---
title: 'init(_:variableValue:bundle:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/init(_:variablevalue:bundle:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/init(_:variablevalue:bundle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/init%28_%3Avariablevalue%3Abundle%3A%29.json'
content_hash: 'sha256:c3e09bd5adf145cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# init(_:variableValue:bundle:)

<sub>Initializer</sub>

Creates a labeled image that you can use as content for controls, with a variable value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ name: String, variableValue: Double?, bundle: Bundle? = nil)
```

## Parameters

- `name` — The name of the image resource to lookup, as well as the localization key with which to label the image.

- `variableValue` — An optional value between `0.0` and `1.0` that the rendered image can use to customize its appearance, if specified. If the symbol doesn’t support variable values, this parameter has no effect.

- `bundle` — The bundle to search for the image resource and localization content. If `nil`, SwiftUI uses the main `Bundle`. Defaults to `nil`.

## Discussion

This initializer creates an image using a using a symbol in the specified bundle. The rendered symbol may alter its appearance to represent the value provided in `variableValue`.

> [!note] Note
> See WWDC22 session [10158: Adopt variable color in SF Symbols](https://developer.apple.com/wwdc22/10158/) for details on how to create symbols that support variable values.

## See Also

### Creating an image

- [init(_:bundle:)](<init(__bundle_).md>) — Creates a labeled image that you can use as content for controls.
- [init(_:)](<init(__).md>) — Initialize an `Image` with an image resource.
