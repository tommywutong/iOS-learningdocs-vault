---
title: 'register(_:forCellWithReuseIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/register(_:forcellwithreuseidentifier:)-3vaho'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/register(_:forcellwithreuseidentifier:)-3vaho'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/register%28_%3Aforcellwithreuseidentifier%3A%29-3vaho.json'
content_hash: 'sha256:a7a418ccae5a14b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# register(_:forCellWithReuseIdentifier:)

<sub>Instance Method</sub>

Registers a class for use in creating new collection view cells.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func register(_ cellClass: AnyClass?, forCellWithReuseIdentifier identifier: String)
```

## Parameters

- `cellClass` — The class of a cell that you want to use in the collection view.

- `identifier` — The reuse identifier to associate with the specified class. This parameter must not be `nil` and must not be an empty string.

## Discussion

Prior to calling the [- dequeueReusableCellWithReuseIdentifier:forIndexPath:](<dequeuereusablecell(withreuseidentifier_for_).md>) method of the collection view, you must use this method or the [- registerNib:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-6z6t4.md>) method to tell the collection view how to create a new cell of the given type. If a cell of the specified type is not currently in a reuse queue, the collection view uses the provided information to create a new cell object automatically.

If you previously registered a class or nib file with the same reuse identifier, the class you specify in the `cellClass` parameter replaces the old entry. You may specify `nil` for `cellClass` if you want to unregister the class from the specified reuse identifier.

## See Also

### Creating cells

- [CellRegistration](cellregistration.md) — A registration for the collection view’s cells.
- [dequeueConfiguredReusableCell(using:for:item:)](<dequeueconfiguredreusablecell(using_for_item_).md>) — Dequeues a configured reusable cell object.
- [- registerNib:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-6z6t4.md>) — Registers a nib file for use in creating new collection view cells.
- [- dequeueReusableCellWithReuseIdentifier:forIndexPath:](<dequeuereusablecell(withreuseidentifier_for_).md>) — Dequeues a reusable cell object located by its identifier.
