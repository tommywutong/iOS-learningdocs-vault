---
title: visualDescription()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/visualdescription()
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/visualdescription()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/visualdescription%28%29.json'
content_hash: 'sha256:0d74be590b4893d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionSnapshotReference](../nsdiffabledatasourcesectionsnapshotreference.md)

# visualDescription()

<sub>Instance Method</sub>

Returns a string with an ASCII representation of the section snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func visualDescription() -> String
```

## Discussion

An asterisk (`*`) represents a visible item, a plus sign (`+`) represents an expanded item, and a minus sign (`-`) represents a collapsed item.
