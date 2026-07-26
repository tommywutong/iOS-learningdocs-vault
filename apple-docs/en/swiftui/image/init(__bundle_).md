---
title: 'init(_:bundle:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/init(_:bundle:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/init(_:bundle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/init%28_%3Abundle%3A%29.json'
content_hash: 'sha256:292512df7d2be409'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# init(_:bundle:)

<sub>Initializer</sub>

Creates a labeled image that you can use as content for controls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ name: String, bundle: Bundle? = nil)
```

## Parameters

- `name` — The name of the image resource to lookup, as well as the localization key with which to label the image.

- `bundle` — The bundle to search for the image resource and localization content. If `nil`, SwiftUI uses the main `Bundle`. Defaults to `nil`.

## See Also

### Creating an image

- [init(_:variableValue:bundle:)](<init(__variablevalue_bundle_).md>) — Creates a labeled image that you can use as content for controls, with a variable value.
- [init(_:)](<init(__).md>) — Initialize an `Image` with an image resource.
