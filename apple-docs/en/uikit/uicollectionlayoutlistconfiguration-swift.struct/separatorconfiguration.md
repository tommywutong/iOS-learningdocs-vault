---
title: separatorConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/separatorconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/separatorconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/separatorconfiguration.json'
content_hash: 'sha256:44d3d9e59351bea9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutListConfiguration](../uicollectionlayoutlistconfiguration-swift.struct.md)

# separatorConfiguration

<sub>Instance Property</sub>

The section’s preferred configuration for list separators.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var separatorConfiguration: UIListSeparatorConfiguration { get set }
```

## Discussion

This configuration only takes effect if [showsSeparators](showsseparators.md) is [true](../../swift/true.md).

For more granular control over list separator appearance, use [itemSeparatorHandler](itemseparatorhandler-swift.property.md).

## See Also

### Configuring separators

- [showsSeparators](showsseparators.md) — A Boolean value that determines whether the list shows separators between cells.
- [UIListSeparatorConfiguration](../uilistseparatorconfiguration-swift.struct.md) — A configuration that controls the list separator appearance in a list section.
- [itemSeparatorHandler](itemseparatorhandler-swift.property.md) — The closure that provides granular control over the list separator appearance of each item.
- [ItemSeparatorHandler](itemseparatorhandler-swift.typealias.md) — A closure that provides granular control over list separator appearance.
