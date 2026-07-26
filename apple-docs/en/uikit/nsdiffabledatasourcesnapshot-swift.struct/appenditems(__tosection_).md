---
title: 'appendItems(_:toSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/appenditems(_:tosection:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/appenditems(_:tosection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/appenditems%28_%3Atosection%3A%29.json'
content_hash: 'sha256:048145779efaf99a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# appendItems(_:toSection:)

<sub>Instance Method</sub>

Adds the items with the specified identifiers to the specified section of the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
mutating func appendItems(_ identifiers: [ItemIdentifierType], toSection sectionIdentifier: SectionIdentifierType? = nil)
```

## Parameters

- `identifiers` — An array of identifiers specifying the items to add to the snapshot.

- `sectionIdentifier` — The section to which to add the items. If no value is provided, the items are appended to the last section of the snapshot.

## See Also

### Creating a snapshot

- [init()](<init().md>) — Creates an empty snapshot.
- [appendSections(_:)](<appendsections(__).md>) — Adds the sections with the specified identifiers to the snapshot.
