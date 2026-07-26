---
title: contentHuggingElements
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/contenthuggingelements-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/contenthuggingelements-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/contenthuggingelements-swift.property.json'
content_hash: 'sha256:94aaffd133e34446'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutListConfiguration](../uicollectionlayoutlistconfiguration-swift.struct.md)

# contentHuggingElements

<sub>Instance Property</sub>

A setting that determines which type of items tightly hug their content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentHuggingElements: UICollectionLayoutListConfiguration.ContentHuggingElements { get set }
```

## Discussion

The default value of this property is [supplementaryHeader](contenthuggingelements-swift.struct/supplementaryheader.md) in visionOS, and `[]` on all other platforms.

When the value of this property is [supplementaryHeader](contenthuggingelements-swift.struct/supplementaryheader.md), header views tightly hug their content. This means header views don’t stretch to fill the width of the collection view if its content’s intrinsic content size is less than the collection view’s width.

## See Also

### Managing content-hugging behavior

- [ContentHuggingElements](contenthuggingelements-swift.struct.md) — Constants that determine which types of items in a collection view tightly hug their content.
