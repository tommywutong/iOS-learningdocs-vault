---
title: 'register(_:forSupplementaryViewOfKind:withReuseIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-9hn73'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-9hn73'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/register%28_%3Aforsupplementaryviewofkind%3Awithreuseidentifier%3A%29-9hn73.json'
content_hash: 'sha256:04842fd6625a345f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# register(_:forSupplementaryViewOfKind:withReuseIdentifier:)

<sub>Instance Method</sub>

Registers a nib file for use in creating supplementary views for the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func register(_ nib: UINib?, forSupplementaryViewOfKind kind: String, withReuseIdentifier identifier: String)
```

## Parameters

- `nib` — The nib object containing the view object. The nib file must contain only one top-level object and that object must be of the type [UICollectionReusableView](../uicollectionreusableview.md).

- `kind` — The kind of supplementary view to create. The layout defines the types of supplementary views it supports. The value of this string may correspond to one of the predefined kind strings or to a custom string that the layout added to support a new type of supplementary view. This parameter must not be `nil`.

- `identifier` — The reuse identifier to associate with the specified nib file. This parameter must not be `nil` and must not be an empty string.

## Discussion

Prior to calling the [- dequeueReusableSupplementaryViewOfKind:withReuseIdentifier:forIndexPath:](<dequeuereusablesupplementaryview(ofkind_withreuseidentifier_for_).md>) method of the collection view, you must use this method or the [- registerClass:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-661io.md>) method to tell the collection view how to create a supplementary view of the given type. If a view of the specified type isn’t currently in a reuse queue, the collection view uses the provided information to create a view object automatically.

If you previously registered a class or nib file with the same element kind and reuse identifier, the class you specify in the `viewClass` parameter replaces the old entry. You may specify `nil` for `nib` if you want to unregister the class from the specified element kind and reuse identifier.

## See Also

### Creating headers and footers

- [SupplementaryRegistration](supplementaryregistration.md) — A registration for the collection view’s supplementary views.
- [dequeueConfiguredReusableSupplementary(using:for:)](<dequeueconfiguredreusablesupplementary(using_for_).md>) — Dequeues a configured reusable supplementary view object.
- [- registerClass:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-661io.md>) — Registers a class for use in creating supplementary views for the collection view.
- [- dequeueReusableSupplementaryViewOfKind:withReuseIdentifier:forIndexPath:](<dequeuereusablesupplementaryview(ofkind_withreuseidentifier_for_).md>) — Dequeues a reusable supplementary view located by its identifier and kind.
