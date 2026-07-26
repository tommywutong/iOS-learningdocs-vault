---
title: 'init(sectionProvider:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewcompositionallayout/init(sectionprovider:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcompositionallayout/init(sectionprovider:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcompositionallayout/init%28sectionprovider%3A%29.json'
content_hash: 'sha256:bc2c155ae988eb4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCompositionalLayout](../uicollectionviewcompositionallayout.md)

# init(sectionProvider:)

<sub>Initializer</sub>

Creates a compositional layout object with a section provider to supply the layout’s sections.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(sectionProvider: @escaping UICollectionViewCompositionalLayoutSectionProvider)
```

## See Also

### Observing data in collection view layouts

- [UICollectionViewCompositionalLayoutSectionProvider](../uicollectionviewcompositionallayoutsectionprovider.md) — A closure that creates and returns each of the layout’s sections.
- [- initWithSectionProvider:configuration:](<init(sectionprovider_configuration_).md>) — Creates a compositional layout object with a section provider and an additional configuration.
