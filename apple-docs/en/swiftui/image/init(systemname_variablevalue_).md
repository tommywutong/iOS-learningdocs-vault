---
title: 'init(systemName:variableValue:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/init(systemname:variablevalue:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/init(systemname:variablevalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/init%28systemname%3Avariablevalue%3A%29.json'
content_hash: 'sha256:ad5860b01a85e56a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# init(systemName:variableValue:)

<sub>Initializer</sub>

Creates a system symbol image with a variable value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(systemName: String, variableValue: Double?)
```

## Parameters

- `systemName` — The name of the system symbol image. Use the SF Symbols app to look up the names of system symbol images.

- `variableValue` — An optional value between `0.0` and `1.0` that the rendered image can use to customize its appearance, if specified. If the symbol doesn’t support variable values, this parameter has no effect. Use the SF Symbols app to look up which symbols support variable values.

## Discussion

This initializer creates an image using a system-provided symbol. The rendered symbol may alter its appearance to represent the value provided in `variableValue`. Use [SF Symbols](https://developer.apple.com/design/resources/#sf-symbols) (version 4.0 or later) to find system symbols that support variable values and their corresponding names.

The following example shows the effect of creating the `"chart.bar.fill"` symbol with different values.

```swift
HStack{
    Image(systemName: "chart.bar.fill", variableValue: 0.3)
    Image(systemName: "chart.bar.fill", variableValue: 0.6)
    Image(systemName: "chart.bar.fill", variableValue: 1.0)
}
.font(.system(.largeTitle))
```

![Three instances of the bar chart symbol, arranged horizontally.](../../../../attachments/b60576218ca849986d68d3e314163f02/Image-3@2x.png)

To create a custom symbol image from your app’s asset catalog, use [init(_:variableValue:bundle:)](<init(__variablevalue_bundle_).md>) instead.

## See Also

### Creating a system symbol image

- [init(systemName:)](<init(systemname_).md>) — Creates a system symbol image.
