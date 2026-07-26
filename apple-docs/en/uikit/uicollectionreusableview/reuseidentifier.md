---
title: reuseIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionreusableview/reuseidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionreusableview/reuseidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionreusableview/reuseidentifier.json'
content_hash: 'sha256:31467fe910e7d457'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionReusableView](../uicollectionreusableview.md)

# reuseIdentifier

<sub>Instance Property</sub>

A string that identifies the purpose of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var reuseIdentifier: String? { get }
```

## Discussion

The collection view identifies and queues reusable views using their reuse identifiers. The collection view sets this value when it first creates the view, and the value cannot be changed later. When your data source is prompted to provide a given view, it can use the reuse identifier to dequeue a view of the appropriate type.

## See Also

### Reusing cells

- [- prepareForReuse](<prepareforreuse().md>) — Performs any clean up necessary to prepare the view for use again.
