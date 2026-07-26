---
title: UICollectionLayoutListFooterModeSupplementary
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistfootermode/uicollectionlayoutlistfootermodesupplementary
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistfootermode/uicollectionlayoutlistfootermodesupplementary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistfootermode/uicollectionlayoutlistfootermodesupplementary.json'
content_hash: 'sha256:0bfc7a4880bf1ef0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutListFooterMode](../uicollectionlayoutlistfootermode.md)

# UICollectionLayoutListFooterModeSupplementary

<sub>Enumeration Case</sub>

A footer mode that uses supplementary views to show footers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
UICollectionLayoutListFooterModeSupplementary
```

## Discussion

Choose this footer mode to use supplementary views with [UICollectionElementKindSectionFooter](../uicollectionview/elementkindsectionfooter.md) as the section footer.

By default, lists that use the [UICollectionLayoutListAppearancePlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceplain.md) and [UICollectionLayoutListAppearanceSidebarPlain](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md) list appearances use pinned footers. You must use this footer mode if you want to opt into this default pinning behavior.

## See Also

### Footer modes

- [UICollectionLayoutListFooterModeNone](uicollectionlayoutlistfootermodenone.md) — No footers are shown.
