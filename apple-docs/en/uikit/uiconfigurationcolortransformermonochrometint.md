---
title: UIConfigurationColorTransformerMonochromeTint
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconfigurationcolortransformermonochrometint
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformermonochrometint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationcolortransformermonochrometint.json'
content_hash: 'sha256:3d2cf165690dd359'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIConfigurationColorTransformerMonochromeTint

<sub>Global Variable</sub>

A color transformer that returns the color with a monochrome tint.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern const UIConfigurationColorTransformer UIConfigurationColorTransformerMonochromeTint;
```

## Discussion

Use this color transformer to deemphasize a tinted item. The tinted item remains monochrome regardless of the system accent color.

## See Also

### Creating a color transformer

- [UIConfigurationColorTransformerGrayscale](uiconfigurationcolortransformergrayscale.md) — A color transformer that returns a grayscale version of the color.
- [UIConfigurationColorTransformerPreferredTint](uiconfigurationcolortransformerpreferredtint.md) — A color transformer that returns the preferred system accent color.
