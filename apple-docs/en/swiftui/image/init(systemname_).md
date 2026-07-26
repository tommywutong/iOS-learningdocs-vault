---
title: 'init(systemName:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/init(systemname:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/init(systemname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/init%28systemname%3A%29.json'
content_hash: 'sha256:65f234c50606db16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# init(systemName:)

<sub>Initializer</sub>

Creates a system symbol image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(systemName: String)
```

## Parameters

- `systemName` — The name of the system symbol image. Use the SF Symbols app to look up the names of system symbol images.

## Discussion

This initializer creates an image using a system-provided symbol. Use [SF Symbols](https://developer.apple.com/design/resources/#sf-symbols) to find symbols and their corresponding names.

To create a custom symbol image from your app’s asset catalog, use [init(_:bundle:)](<init(__bundle_).md>) instead.

## See Also

### Creating a system symbol image

- [init(systemName:variableValue:)](<init(systemname_variablevalue_).md>) — Creates a system symbol image with a variable value.
