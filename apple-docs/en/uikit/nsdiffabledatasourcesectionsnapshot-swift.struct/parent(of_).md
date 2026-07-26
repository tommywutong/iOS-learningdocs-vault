---
title: 'parent(of:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/parent(of:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/parent(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/parent%28of%3A%29.json'
content_hash: 'sha256:643998a46b7a2140'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionSnapshot](../nsdiffabledatasourcesectionsnapshot-swift.struct.md)

# parent(of:)

<sub>Instance Method</sub>

Finds the parent item of the specified item in the section snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func parent(of child: ItemIdentifierType) -> ItemIdentifierType?
```

## See Also

### Getting item metrics

- [index(of:)](<index(of_).md>) — Finds the index of the specified item in the section snapshot.
- [level(of:)](<level(of_).md>) — Finds the hierarchical level of the specified item in the section snapshot.
- [contains(_:)](<contains(__).md>) — Indicates whether the section snapshot contains the specified item.
- [isVisible(_:)](<isvisible(__).md>) — Indicates whether the specified item is currently visible onscreen.
