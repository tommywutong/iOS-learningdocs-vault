---
title: 'Preview(_:traits:body:)'
framework: UIKit
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/preview(_:traits:body:)-c7kr'
source_url: 'https://developer.apple.com/documentation/uikit/preview(_:traits:body:)-c7kr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/preview%28_%3Atraits%3Abody%3A%29-c7kr.json'
content_hash: 'sha256:b6040965172d34a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# Preview(_:traits:body:)

<sub>Macro</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@freestanding(declaration) macro Preview(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., @PreviewMacroBodyBuilder<UIView> body: @escaping @MainActor () -> UIView)
```

## See Also

### Macros

- [Preview(_:traits:body:)](<preview(__traits_body_)-en9c.md>)
- [UIKIT_HAS_UIFOUNDATION_SYMBOLS](uikit_has_uifoundation_symbols.md)
