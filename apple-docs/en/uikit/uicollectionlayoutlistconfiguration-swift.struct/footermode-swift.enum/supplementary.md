---
title: UICollectionLayoutListConfiguration.FooterMode.supplementary
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/footermode-swift.enum/supplementary
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/footermode-swift.enum/supplementary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/footermode-swift.enum/supplementary.json'
content_hash: 'sha256:867559addd6ce1c2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionLayoutListConfiguration](../../uicollectionlayoutlistconfiguration-swift.struct.md) · [FooterMode](../footermode-swift.enum.md)

# UICollectionLayoutListConfiguration.FooterMode.supplementary

<sub>Case</sub>

A footer mode that uses supplementary views to show footers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case supplementary
```

## Discussion

Choose this footer mode to use supplementary views with [UICollectionElementKindSectionFooter](../../uicollectionview/elementkindsectionfooter.md) as the section footer.

By default, lists that use the [UICollectionLayoutListConfiguration.Appearance.plain](../appearance-swift.enum/plain.md) and [UICollectionLayoutListConfiguration.Appearance.sidebarPlain](../appearance-swift.enum/sidebarplain.md) list appearances use pinned footers. You must use this footer mode if you want to opt into this default pinning behavior.

## See Also

### Footer modes

- [UICollectionLayoutListConfiguration.FooterMode.none](none.md) — No footers are shown.
