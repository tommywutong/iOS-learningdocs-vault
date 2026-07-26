---
title: 'init(rect:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltershape/init(rect:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltershape/init(rect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltershape/init%28rect%3A%29.json'
content_hash: 'sha256:da8eba3cf3e09f70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterShape](../cifiltershape.md)

# init(rect:)

<sub>Initializer</sub>

Initializes a filter shape object with a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(rect r: CGRect)
```

## Parameters

- `r` — A rectangle. Core Image uses the rectangle specified by integer parts of the values in the `CGRect` data structure.

## Return Value

An initialized CIFilterShape object, or `nil` if the method fails.
