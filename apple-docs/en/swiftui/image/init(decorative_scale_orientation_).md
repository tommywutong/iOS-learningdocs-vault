---
title: 'init(decorative:scale:orientation:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/init(decorative:scale:orientation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/init(decorative:scale:orientation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/init%28decorative%3Ascale%3Aorientation%3A%29.json'
content_hash: 'sha256:f0ab3e439f2e91e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# init(decorative:scale:orientation:)

<sub>Initializer</sub>

Creates an unlabeled, decorative image based on a Core Graphics image instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(decorative cgImage: CGImage, scale: CGFloat, orientation: Image.Orientation = .up)
```

## Parameters

- `cgImage` — The base graphical image.

- `scale` — The scale factor for the image, with a value like `1.0`, `2.0`, or `3.0`.

- `orientation` — The orientation of the image. The default is [Image.Orientation.up](orientation/up.md).

## Discussion

SwiftUI ignores this image for accessibility purposes.

## See Also

### Creating an image for decorative use

- [init(decorative:bundle:)](<init(decorative_bundle_).md>) — Creates an unlabeled, decorative image.
- [init(decorative:variableValue:bundle:)](<init(decorative_variablevalue_bundle_).md>) — Creates an unlabeled, decorative image, with a variable value.
