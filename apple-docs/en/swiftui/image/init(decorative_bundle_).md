---
title: 'init(decorative:bundle:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/init(decorative:bundle:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/init(decorative:bundle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/init%28decorative%3Abundle%3A%29.json'
content_hash: 'sha256:1ba26fabf500f9d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# init(decorative:bundle:)

<sub>Initializer</sub>

Creates an unlabeled, decorative image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(decorative name: String, bundle: Bundle? = nil)
```

## Parameters

- `name` — The name of the image resource to lookup

- `bundle` — The bundle to search for the image resource. If `nil`, SwiftUI uses the main `Bundle`. Defaults to `nil`.

## Discussion

SwiftUI ignores this image for accessibility purposes.

## See Also

### Creating an image for decorative use

- [init(decorative:variableValue:bundle:)](<init(decorative_variablevalue_bundle_).md>) — Creates an unlabeled, decorative image, with a variable value.
- [init(decorative:scale:orientation:)](<init(decorative_scale_orientation_).md>) — Creates an unlabeled, decorative image based on a Core Graphics image instance.
