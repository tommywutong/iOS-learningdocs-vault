---
title: UICollectionLayoutListConfiguration.HeaderMode.supplementary
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/supplementary
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/supplementary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/supplementary.json'
content_hash: 'sha256:74a52d3da8b74ef0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollectionLayoutListConfiguration](../../uicollectionlayoutlistconfiguration-swift.struct.md) · [HeaderMode](../headermode-swift.enum.md)

# UICollectionLayoutListConfiguration.HeaderMode.supplementary

<sub>Case</sub>

A header mode that uses supplementary views to show headers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case supplementary
```

## Discussion

Choose this header mode to use supplementary views with [UICollectionElementKindSectionHeader](../../uicollectionview/elementkindsectionheader.md) as the section header.

By default, lists that use the [UICollectionLayoutListConfiguration.Appearance.plain](../appearance-swift.enum/plain.md) and [UICollectionLayoutListConfiguration.Appearance.sidebarPlain](../appearance-swift.enum/sidebarplain.md) list appearances use pinned headers. You must use this header mode if you want to opt into this default pinning behavior.

## See Also

### Header modes

- [UICollectionLayoutListConfiguration.HeaderMode.none](none.md) — No headers are shown.
- [UICollectionLayoutListConfiguration.HeaderMode.firstItemInSection](firstiteminsection.md) — A header mode that styles the first item in a section as a header.
