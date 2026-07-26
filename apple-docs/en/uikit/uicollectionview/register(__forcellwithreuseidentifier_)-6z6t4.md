---
title: 'register(_:forCellWithReuseIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicollectionview/register(_:forcellwithreuseidentifier:)-6z6t4'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/register(_:forcellwithreuseidentifier:)-6z6t4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/register%28_%3Aforcellwithreuseidentifier%3A%29-6z6t4.json'
content_hash: 'sha256:0870f467e8fadd31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# register(_:forCellWithReuseIdentifier:)

<sub>Instance Method</sub>

Registers a nib file for use in creating new collection view cells.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func register(_ nib: UINib?, forCellWithReuseIdentifier identifier: String)
```

## Parameters

- `nib` — The nib object containing the cell object. The nib file must contain only one top-level object and that object must be of the type [UICollectionViewCell](../uicollectionviewcell.md).

- `identifier` — The reuse identifier to associate with the specified nib file. This parameter must not be `nil` and must not be an empty string.

## Discussion

Prior to calling the [- dequeueReusableCellWithReuseIdentifier:forIndexPath:](<dequeuereusablecell(withreuseidentifier_for_).md>) method of the collection view, you must use this method or the [- registerClass:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-3vaho.md>) method to tell the collection view how to create a new cell of the given type. If a cell of the specified type is not currently in a reuse queue, the collection view uses the provided information to create a new cell object automatically.

If you previously registered a class or nib file with the same reuse identifier, the object you specify in the `nib` parameter replaces the old entry. You may specify `nil` for `nib` if you want to unregister the nib file from the specified reuse identifier.

## See Also

### Creating cells

- [CellRegistration](cellregistration.md) — A registration for the collection view’s cells.
- [dequeueConfiguredReusableCell(using:for:item:)](<dequeueconfiguredreusablecell(using_for_item_).md>) — Dequeues a configured reusable cell object.
- [- registerClass:forCellWithReuseIdentifier:](<register(__forcellwithreuseidentifier_)-3vaho.md>) — Registers a class for use in creating new collection view cells.
- [- dequeueReusableCellWithReuseIdentifier:forIndexPath:](<dequeuereusablecell(withreuseidentifier_for_).md>) — Dequeues a reusable cell object located by its identifier.
