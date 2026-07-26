---
title: image
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/asyncimagephase/image
source_url: 'https://developer.apple.com/documentation/swiftui/asyncimagephase/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/asyncimagephase/image.json'
content_hash: 'sha256:d7d65db2f81c58dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AsyncImagePhase](../asyncimagephase.md)

# image

<sub>Instance Property</sub>

The loaded image, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var image: Image? { get }
```

## Discussion

If this value isn’t `nil`, the image load operation has finished, and you can use the image to update the view. You can use the image directly, or you can modify it in some way. For example, you can add a [resizable(capInsets:resizingMode:)](<../image/resizable(capinsets_resizingmode_).md>) modifier to make the image resizable.
