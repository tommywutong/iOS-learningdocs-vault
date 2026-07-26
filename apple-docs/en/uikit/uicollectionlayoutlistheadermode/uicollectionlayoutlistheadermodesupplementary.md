---
title: UICollectionLayoutListHeaderModeSupplementary
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistheadermode/uicollectionlayoutlistheadermodesupplementary
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistheadermode/uicollectionlayoutlistheadermodesupplementary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistheadermode/uicollectionlayoutlistheadermodesupplementary.json'
content_hash: 'sha256:7102458149f99443'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutListHeaderMode](../uicollectionlayoutlistheadermode.md)

# UICollectionLayoutListHeaderModeSupplementary

<sub>Enumeration Case</sub>

A header mode that uses supplementary views to show headers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
UICollectionLayoutListHeaderModeSupplementary
```

## Discussion

Choose this header mode to use supplementary views with [UICollectionElementKindSectionHeader](../uicollectionview/elementkindsectionheader.md) as the section header.

By default, lists that use the [UICollectionLayoutListAppearancePlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceplain.md) and [UICollectionLayoutListAppearanceSidebarPlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md) list appearances use pinned headers. You must use this header mode if you want to opt into this default pinning behavior.

## See Also

### Header modes

- [UICollectionLayoutListHeaderModeNone](uicollectionlayoutlistheadermodenone.md) — No headers are shown.
- [UICollectionLayoutListHeaderModeFirstItemInSection](uicollectionlayoutlistheadermodefirstiteminsection.md) — A header mode that styles the first item in a section as a header.
