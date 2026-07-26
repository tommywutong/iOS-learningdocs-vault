---
title: init()
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontext/init()
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/init%28%29.json'
content_hash: 'sha256:afa66688d10ab9ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# init()

<sub>Initializer</sub>

Initializes a context without a specific rendering destination, using default options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init()
```

## Return Value

An initialized Core Image context.

## Discussion

If you create a context without specifying a rendering destination, Core Image automatically chooses and internally manages a rendering destination based on the current device’s capabilities. You cannot use a context without an explicit destination for the methods listed in Drawing Images. Instead, use the methods listed in Rendering Images.

To specify additional options for the context, use the [contextWithOptions:](contextwithoptions_.md) initializer instead.
