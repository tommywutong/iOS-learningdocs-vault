---
title: 'init(dynamicProvider:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/init(dynamicprovider:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/init(dynamicprovider:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/init%28dynamicprovider%3A%29.json'
content_hash: 'sha256:fb0adb2b290cbe16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# init(dynamicProvider:)

<sub>Initializer</sub>

Creates a color object that uses the specified block to generate its color data dynamically.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(dynamicProvider: @escaping (UITraitCollection) -> UIColor)
```

## Parameters

- `dynamicProvider` — A block that determines the appropriate color values based on the specified traits. This block returns a [UIColor](../uicolor.md) object and takes a single parameter: - **traits** — The trait collection to use when generating the color information. Always use the traits in this collection, and not the traits of the current environment, when determining the color information.

## Return Value

A color object whose color information is provided by the specified block.

## Discussion

Use this method to create a color object whose component values change based on the currently active traits. The block you provide creates a new color object based on the traits in the provided trait collection.
