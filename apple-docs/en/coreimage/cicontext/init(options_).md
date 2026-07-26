---
title: 'init(options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/init(options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/init(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/init%28options%3A%29.json'
content_hash: 'sha256:d53e4e43822c4c73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# init(options:)

<sub>Initializer</sub>

Initializes a context without a specific rendering destination, using the specified options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(options: [CIContextOption : Any]? = nil)
```

## Parameters

- `options` — A dictionary containing options for the context. For applicable keys and values, see [CIContextOption](../cicontextoption.md).

## Return Value

An initialized Core Image context.

## Discussion

If you create a context without specifying a rendering destination, Core Image automatically chooses and internally manages a rendering destination based on the current device’s capabilities and your settings in the `options` dictionary. You cannot use a context without an explicit destination for the methods listed in Drawing Images. Instead, use the methods listed in Rendering Images.

The `options` dictionary defines behaviors for the context, such as color space and rendering quality. For example, to create a CPU-based context, use the  [kCIContextUseSoftwareRenderer](../cicontextoption/usesoftwarerenderer.md) key.
