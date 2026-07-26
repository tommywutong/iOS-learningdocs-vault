---
title: 'numberOfItems(inSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesnapshotreference/numberofitems(insection:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/numberofitems(insection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesnapshotreference/numberofitems%28insection%3A%29.json'
content_hash: 'sha256:e041fae2a01570da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSnapshotReference](../nsdiffabledatasourcesnapshotreference.md)

# numberOfItems(inSection:)

<sub>Instance Method</sub>

Returns the number of items in the specified section of the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func numberOfItems(inSection sectionIdentifier: Any) -> Int
```

## Parameters

- `sectionIdentifier` — The identifier of the section of the snapshot.

## Return Value

The number of items in the specified section. This method returns `0` if the section is empty.

## Discussion

If you call this method with the identifier of a section that doesn’t exist in the snapshot, the app throws an error.

## See Also

### Getting item and section metrics

- [numberOfItems](numberofitems.md) — The number of items in the snapshot.
- [numberOfSections](numberofsections.md) — The number of sections in the snapshot.
