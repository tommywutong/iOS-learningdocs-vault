---
title: 'appendSections(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/appendsections(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/appendsections(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/appendsections%28_%3A%29.json'
content_hash: 'sha256:37efd911a78a43b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshot](../nsdiffabledatasourcesnapshot-swift.struct.md)

# appendSections(_:)

<sub>Instance Method</sub>

Adds the sections with the specified identifiers to the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
mutating func appendSections(_ identifiers: [SectionIdentifierType])
```

## Parameters

- `identifiers` — An array of identifiers specifying the sections to add to the snapshot.

## See Also

### Creating a snapshot

- [init()](<init().md>) — Creates an empty snapshot.
- [appendItems(_:toSection:)](<appenditems(__tosection_).md>) — Adds the items with the specified identifiers to the specified section of the snapshot.
