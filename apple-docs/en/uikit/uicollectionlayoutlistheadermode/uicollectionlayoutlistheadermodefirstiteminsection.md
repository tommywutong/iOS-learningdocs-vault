---
title: UICollectionLayoutListHeaderModeFirstItemInSection
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistheadermode/uicollectionlayoutlistheadermodefirstiteminsection
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistheadermode/uicollectionlayoutlistheadermodefirstiteminsection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistheadermode/uicollectionlayoutlistheadermodefirstiteminsection.json'
content_hash: 'sha256:8d6d995d3adbcc03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutListHeaderMode](../uicollectionlayoutlistheadermode.md)

# UICollectionLayoutListHeaderModeFirstItemInSection

<sub>Enumeration Case</sub>

A header mode that styles the first item in a section as a header.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
UICollectionLayoutListHeaderModeFirstItemInSection
```

## Discussion

Choose this header mode when you’re using hierarchical data sources if you want to be able to expand and collapse the header.

When you use this header mode, a [UICollectionViewListCell](../uicollectionviewlistcell.md) object that appears as the first item in the section automatically uses a header appearance. When you configure your data source, make sure to account for the fact that the first item in the section (at index `0`) represents the header, and the actual items in the section start at index `1`.

By default, lists that use the [UICollectionLayoutListAppearancePlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceplain.md) and [UICollectionLayoutListAppearanceSidebarPlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md) list appearances use pinned headers. If you want to opt into this default pinning behavior, use the [UICollectionLayoutListHeaderModeSupplementary](uicollectionlayoutlistheadermodesupplementary.md) header mode instead.

## See Also

### Header modes

- [UICollectionLayoutListHeaderModeNone](uicollectionlayoutlistheadermodenone.md) — No headers are shown.
- [UICollectionLayoutListHeaderModeSupplementary](uicollectionlayoutlistheadermodesupplementary.md) — A header mode that uses supplementary views to show headers.
