---
title: UIConfigurationColorTransformerPreferredTint
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconfigurationcolortransformerpreferredtint
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformerpreferredtint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationcolortransformerpreferredtint.json'
content_hash: 'sha256:094e4e812e7e77f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIConfigurationColorTransformerPreferredTint

<sub>Global Variable</sub>

A color transformer that returns the preferred system accent color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern const UIConfigurationColorTransformer UIConfigurationColorTransformerPreferredTint;
```

## Discussion

This color transformer returns the original color on platforms without a system accent color, or when the system accent color is set to Multicolor. When the system accent color is set to any other color, this color transformer returns that system accent color.

## See Also

### Creating a color transformer

- [UIConfigurationColorTransformerGrayscale](uiconfigurationcolortransformergrayscale.md) — A color transformer that returns a grayscale version of the color.
- [UIConfigurationColorTransformerMonochromeTint](uiconfigurationcolortransformermonochrometint.md) — A color transformer that returns the color with a monochrome tint.
