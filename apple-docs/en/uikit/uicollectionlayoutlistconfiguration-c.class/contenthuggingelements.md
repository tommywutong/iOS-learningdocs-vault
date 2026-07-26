---
title: contentHuggingElements
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-c.class/contenthuggingelements
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-c.class/contenthuggingelements'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-c.class/contenthuggingelements.json'
content_hash: 'sha256:c10dbd3e50ae366d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutListConfiguration](../uicollectionlayoutlistconfiguration-c.class.md)

# contentHuggingElements

<sub>Instance Property</sub>

A setting that determines which type of items tightly hug their content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) UICollectionLayoutListContentHuggingElements contentHuggingElements;
```

## Discussion

The default value of this property is [UICollectionLayoutListContentHuggingElementsSupplementaryHeader](../uicollectionlayoutlistcontenthuggingelements/uicollectionlayoutlistcontenthuggingelementssupplementaryheader.md) in visionOS, and [UICollectionLayoutListContentHuggingElementsNone](../uicollectionlayoutlistcontenthuggingelements/uicollectionlayoutlistcontenthuggingelementsnone.md) on all other platforms.

When the value of this property is [UICollectionLayoutListContentHuggingElementsSupplementaryHeader](../uicollectionlayoutlistcontenthuggingelements/uicollectionlayoutlistcontenthuggingelementssupplementaryheader.md), header views tightly hug their content. This means header views don’t stretch to fill the width of the collection view if its content’s intrinsic content size is less than the collection view’s width.

## See Also

### Managing content-hugging behavior

- [UICollectionLayoutListContentHuggingElements](../uicollectionlayoutlistcontenthuggingelements.md) — Constants that determine which types of items in a collection view tightly hug their content.
