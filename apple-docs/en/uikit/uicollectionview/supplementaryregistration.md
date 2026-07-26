---
title: UICollectionView.SupplementaryRegistration
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/supplementaryregistration
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/supplementaryregistration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/supplementaryregistration.json'
content_hash: 'sha256:1ed19fefafb287f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# UICollectionView.SupplementaryRegistration

<sub>Structure</sub>

A registration for the collection view’s supplementary views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct SupplementaryRegistration<Supplementary> where Supplementary : UICollectionReusableView
```

## Overview

Use a supplementary registration to register supplementary views, like headers and footers, with your collection view and configure each view for display. You create a supplementary registration with your supplementary view type and data item type as the registration’s generic parameters, passing in a registration handler to configure the view. In the registration handler, you specify how to configure the content and appearance of that type of supplementary view.

The following example creates a supplementary registration for a custom header view subclass.

```swift
let headerRegistration = UICollectionView.SupplementaryRegistration
    <HeaderView>(elementKind: "Header") {
    supplementaryView, string, indexPath in
    supplementaryView.label.text = "\(string) for section \(indexPath.section)"
    supplementaryView.backgroundColor = .lightGray
}
```

After you create a supplementary registration, you pass it in to [dequeueConfiguredReusableSupplementary(using:for:)](<dequeueconfiguredreusablesupplementary(using_for_).md>), which you call from your data source’s [supplementaryViewProvider](../uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.property.md).

```swift
dataSource.supplementaryViewProvider = { collectionView, elementKind, indexPath in
    return collectionView.dequeueConfiguredReusableSupplementary(using: headerRegistration,
                                                                 for: indexPath)
}
```

You don’t need to call [- registerClass:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-661io.md>) or [- registerNib:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-9hn73.md>). The registration occurs automatically when you pass the supplementary view registration to [dequeueConfiguredReusableSupplementary(using:for:)](<dequeueconfiguredreusablesupplementary(using_for_).md>).

> [!important] Important
> Don’t create your supplementary view registration inside a [SupplementaryViewProvider](../uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.typealias.md) closure; doing so prevents reuse, and generates an exception in iOS 15 and higher.

## Topics

### Creating a supplementary registration

- [init(elementKind:handler:)](<supplementaryregistration/init(elementkind_handler_).md>) — Creates a supplementary registration for the specified element kind with a registration handler.
- [init(supplementaryNib:elementKind:handler:)](<supplementaryregistration/init(supplementarynib_elementkind_handler_).md>) — Creates a supplementary registration for the specified element kind with a registration handler and nib file.
- [Handler](supplementaryregistration/handler.md) — A closure that handles the supplementary view registration and configuration.

## See Also

### Creating headers and footers

- [dequeueConfiguredReusableSupplementary(using:for:)](<dequeueconfiguredreusablesupplementary(using_for_).md>) — Dequeues a configured reusable supplementary view object.
- [- registerClass:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-661io.md>) — Registers a class for use in creating supplementary views for the collection view.
- [- registerNib:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-9hn73.md>) — Registers a nib file for use in creating supplementary views for the collection view.
- [- dequeueReusableSupplementaryViewOfKind:withReuseIdentifier:forIndexPath:](<dequeuereusablesupplementaryview(ofkind_withreuseidentifier_for_).md>) — Dequeues a reusable supplementary view located by its identifier and kind.
