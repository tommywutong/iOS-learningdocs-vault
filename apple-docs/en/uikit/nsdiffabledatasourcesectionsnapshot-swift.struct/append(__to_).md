---
title: 'append(_:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/append(_:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/append(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/append%28_%3Ato%3A%29.json'
content_hash: 'sha256:a14f7ab1f520bf6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionSnapshot](../nsdiffabledatasourcesectionsnapshot-swift.struct.md)

# append(_:to:)

<sub>Instance Method</sub>

Adds the specified items as child items of the specified parent item in the section snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
mutating func append(_ items: [ItemIdentifierType], to parent: ItemIdentifierType? = nil)
```

## Parameters

- `items` — The identifiers of the items to append to the parent item in the section snapshot.

- `parent` — The parent item to append the items to. If you don’t specify a parent, the section snapshot appends the items to its root level.

## See Also

### Creating a section snapshot

- [init()](<init().md>) — Creates an empty section snapshot.
- [init(_:)](<init(__).md>) — Creates a copy of the provided section snapshot.
- [snapshot(of:includingParent:)](<snapshot(of_includingparent_).md>) — Creates a section snapshot that contains the child items of the specified parent item, optionally including the parent item.
