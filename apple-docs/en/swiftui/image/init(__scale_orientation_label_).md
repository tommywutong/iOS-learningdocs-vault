---
title: 'init(_:scale:orientation:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/init(_:scale:orientation:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/init(_:scale:orientation:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/init%28_%3Ascale%3Aorientation%3Alabel%3A%29.json'
content_hash: 'sha256:866c622caed0df5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# init(_:scale:orientation:label:)

<sub>Initializer</sub>

Creates a labeled image based on a Core Graphics image instance, usable as content for controls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ cgImage: CGImage, scale: CGFloat, orientation: Image.Orientation = .up, label: Text)
```

## Parameters

- `cgImage` — The base graphical image.

- `scale` — The scale factor for the image, with a value like `1.0`, `2.0`, or `3.0`.

- `orientation` — The orientation of the image. The default is [Image.Orientation.up](orientation/up.md).

- `label` — The label associated with the image. SwiftUI uses the label for accessibility.

## See Also

### Creating an image for use as a control

- [init(_:bundle:label:)](<init(__bundle_label_).md>) — Creates a labeled image that you can use as content for controls, with the specified label.
- [init(_:variableValue:bundle:label:)](<init(__variablevalue_bundle_label_).md>) — Creates a labeled image that you can use as content for controls, with the specified label and variable value.
