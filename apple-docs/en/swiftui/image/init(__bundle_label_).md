---
title: 'init(_:bundle:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/init(_:bundle:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/init(_:bundle:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/init%28_%3Abundle%3Alabel%3A%29.json'
content_hash: 'sha256:7d21b410229d3bad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# init(_:bundle:label:)

<sub>Initializer</sub>

Creates a labeled image that you can use as content for controls, with the specified label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ name: String, bundle: Bundle? = nil, label: Text)
```

## Parameters

- `name` — The name of the image resource to lookup

- `bundle` — The bundle to search for the image resource. If `nil`, SwiftUI uses the main `Bundle`. Defaults to `nil`.

- `label` — The label associated with the image. SwiftUI uses the label for accessibility.

## See Also

### Creating an image for use as a control

- [init(_:variableValue:bundle:label:)](<init(__variablevalue_bundle_label_).md>) — Creates a labeled image that you can use as content for controls, with the specified label and variable value.
- [init(_:scale:orientation:label:)](<init(__scale_orientation_label_).md>) — Creates a labeled image based on a Core Graphics image instance, usable as content for controls.
