---
title: 'insert(_:before:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/insert(_:before:)-bsrn'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/insert(_:before:)-bsrn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/insert%28_%3Abefore%3A%29-bsrn.json'
content_hash: 'sha256:6e2c4b76a2d93f62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionSnapshot](../nsdiffabledatasourcesectionsnapshot-swift.struct.md)

# insert(_:before:)

<sub>Instance Method</sub>

Inserts the provided section snapshot immediately before the item with the specified identifier in the section snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
mutating func insert(_ snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, before item: ItemIdentifierType)
```

## See Also

### Inserting items

- [insert(_:after:)](<insert(__after_)-9v9c7.md>) — Inserts the provided items immediately after the item with the specified identifier in the section snapshot.
- [insert(_:after:)](<insert(__after_)-4it9s.md>) — Inserts the provided section snapshot immediately after the item with the specified identifier in the section snapshot.
- [insert(_:before:)](<insert(__before_)-5o91y.md>) — Inserts the provided items immediately before the item with the specified identifier in the section snapshot.
