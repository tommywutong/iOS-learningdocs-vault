---
title: 'effectWithPreview:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointereffect-c.class/effectwithpreview:'
source_url: 'https://developer.apple.com/documentation/uikit/uipointereffect-c.class/effectwithpreview:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointereffect-c.class/effectwithpreview%3A.json'
content_hash: 'sha256:7ec0d8d2c1e8e50d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerEffect](../uipointereffect-c.class.md)

# effectWithPreview:

<sub>Type Method</sub>

Creates a pointer content effect with the given preview’s view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) effectWithPreview:(UITargetedPreview *) preview;
```

## Discussion

`UIPointerEffect` attempts to determine the appropriate effect for the given preview automatically. Use one of its subclasses to request a specific system-provided effect.
