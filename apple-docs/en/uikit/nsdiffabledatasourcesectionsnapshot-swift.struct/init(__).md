---
title: 'init(_:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/init(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/init%28_%3A%29.json'
content_hash: 'sha256:57a05184ff0f6e4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionSnapshot](../nsdiffabledatasourcesectionsnapshot-swift.struct.md)

# init(_:)

<sub>Initializer</sub>

Creates a copy of the provided section snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(_ snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)
```

## See Also

### Creating a section snapshot

- [init()](<init().md>) — Creates an empty section snapshot.
- [snapshot(of:includingParent:)](<snapshot(of_includingparent_).md>) — Creates a section snapshot that contains the child items of the specified parent item, optionally including the parent item.
- [append(_:to:)](<append(__to_).md>) — Adds the specified items as child items of the specified parent item in the section snapshot.
