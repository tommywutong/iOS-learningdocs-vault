---
title: UICollectionLayoutListConfiguration.HeaderMode.firstItemInSection
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/firstiteminsection
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/firstiteminsection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/firstiteminsection.json'
content_hash: 'sha256:afa693106385ceb3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionLayoutListConfiguration](../../uicollectionlayoutlistconfiguration-swift.struct.md) · [HeaderMode](../headermode-swift.enum.md)

# UICollectionLayoutListConfiguration.HeaderMode.firstItemInSection

<sub>Case</sub>

A header mode that styles the first item in a section as a header.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case firstItemInSection
```

## Discussion

Choose this header mode when you’re using hierarchical data sources if you want to be able to expand and collapse the header.

When you use this header mode, a [UICollectionViewListCell](../../uicollectionviewlistcell.md) object that appears as the first item in the section automatically uses a header appearance. When you configure your data source, make sure to account for the fact that the first item in the section (at index `0`) represents the header, and the actual items in the section start at index `1`.

By default, lists that use the [UICollectionLayoutListConfiguration.Appearance.plain](../appearance-swift.enum/plain.md) and [UICollectionLayoutListConfiguration.Appearance.sidebarPlain](../appearance-swift.enum/sidebarplain.md) list appearances use pinned headers. If you want to opt into this default pinning behavior, use the [UICollectionLayoutListConfiguration.HeaderMode.supplementary](supplementary.md) header mode instead.

## See Also

### Header modes

- [UICollectionLayoutListConfiguration.HeaderMode.none](none.md) — No headers are shown.
- [UICollectionLayoutListConfiguration.HeaderMode.supplementary](supplementary.md) — A header mode that uses supplementary views to show headers.
