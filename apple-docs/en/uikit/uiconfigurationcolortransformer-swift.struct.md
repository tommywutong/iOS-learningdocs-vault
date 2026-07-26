---
title: UIConfigurationColorTransformer
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconfigurationcolortransformer-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformer-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationcolortransformer-swift.struct.json'
content_hash: 'sha256:782575f6600531c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIConfigurationColorTransformer

<sub>Structure</sub>

A transformer that generates a modified output color from an input color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIConfigurationColorTransformer
```

## Overview

A color transformer takes an input color and modifies it to produce a different output color. For example, you might have a color transformer that returns a grayscale or reduced alpha version of the input color.

Because color transformers can use the same base input color to produce a number of variants of that color, you can create different appearances for different states of your views.

## Topics

### Creating a color transformer

- [init(_:)](<uiconfigurationcolortransformer-swift.struct/init(__).md>) — Creates a color transformer with the specified closure.
- [grayscale](uiconfigurationcolortransformer-swift.struct/grayscale.md) — Creates a color transformer that generates a grayscale version of the color.
- [preferredTint](uiconfigurationcolortransformer-swift.struct/preferredtint.md) — A color transformer that returns the preferred system accent color.
- [monochromeTint](uiconfigurationcolortransformer-swift.struct/monochrometint.md) — A color transformer that returns the color with a monochrome tint.

### Calling the color transformer

- [transform](uiconfigurationcolortransformer-swift.struct/transform.md) — The transform closure of the color transformer.
- [callAsFunction(_:)](<uiconfigurationcolortransformer-swift.struct/callasfunction(__).md>) — Calls the transform closure of the color transformer.
