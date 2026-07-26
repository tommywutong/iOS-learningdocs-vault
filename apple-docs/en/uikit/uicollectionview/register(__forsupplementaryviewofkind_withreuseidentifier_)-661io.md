---
title: 'register(_:forSupplementaryViewOfKind:withReuseIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-661io'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-661io'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/register%28_%3Aforsupplementaryviewofkind%3Awithreuseidentifier%3A%29-661io.json'
content_hash: 'sha256:e8b86c88b2757844'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# register(_:forSupplementaryViewOfKind:withReuseIdentifier:)

<sub>Instance Method</sub>

Registers a class for use in creating supplementary views for the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func register(_ viewClass: AnyClass?, forSupplementaryViewOfKind elementKind: String, withReuseIdentifier identifier: String)
```

## Parameters

- `viewClass` — The class to use for the supplementary view.

- `elementKind` — The kind of supplementary view to create. This value is defined by the layout object. This parameter must not be `nil`.

- `identifier` — The reuse identifier to associate with the specified class. This parameter must not be `nil` and must not be an empty string.

## Discussion

Prior to calling the [- dequeueReusableSupplementaryViewOfKind:withReuseIdentifier:forIndexPath:](<dequeuereusablesupplementaryview(ofkind_withreuseidentifier_for_).md>) method of the collection view, you must use this method or the [- registerNib:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-9hn73.md>) method to tell the collection view how to create a supplementary view of the given type. If a view of the specified type isn’t currently in a reuse queue, the collection view uses the provided information to create a view object automatically.

If you previously registered a class or nib file with the same element kind and reuse identifier, the class you specify in the `viewClass` parameter replaces the old entry. You may specify `nil` for `viewClass` if you want to unregister the class from the specified element kind and reuse identifier.

## See Also

### Creating headers and footers

- [SupplementaryRegistration](supplementaryregistration.md) — A registration for the collection view’s supplementary views.
- [dequeueConfiguredReusableSupplementary(using:for:)](<dequeueconfiguredreusablesupplementary(using_for_).md>) — Dequeues a configured reusable supplementary view object.
- [- registerNib:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-9hn73.md>) — Registers a nib file for use in creating supplementary views for the collection view.
- [- dequeueReusableSupplementaryViewOfKind:withReuseIdentifier:forIndexPath:](<dequeuereusablesupplementaryview(ofkind_withreuseidentifier_for_).md>) — Dequeues a reusable supplementary view located by its identifier and kind.
