---
title: 'dequeueReusableSupplementaryView(ofKind:withReuseIdentifier:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/dequeuereusablesupplementaryview(ofkind:withreuseidentifier:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/dequeuereusablesupplementaryview(ofkind:withreuseidentifier:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/dequeuereusablesupplementaryview%28ofkind%3Awithreuseidentifier%3Afor%3A%29.json'
content_hash: 'sha256:54165b489417f2e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# dequeueReusableSupplementaryView(ofKind:withReuseIdentifier:for:)

<sub>Instance Method</sub>

Dequeues a reusable supplementary view located by its identifier and kind.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func dequeueReusableSupplementaryView(ofKind elementKind: String, withReuseIdentifier identifier: String, for indexPath: IndexPath) -> UICollectionReusableView
```

## Parameters

- `elementKind` — The kind of supplementary view to retrieve. This value is defined by the layout object. This parameter must not be `nil`.

- `identifier` — The reuse identifier for the specified view. This parameter must not be `nil`.

- `indexPath` — The index path specifying the location of the supplementary view in the collection view. The data source receives this information when it’s asked for the view and should just pass it along. This method uses the information to perform additional configuration based on the view’s position in the collection view.

## Return Value

A valid [UICollectionReusableView](../uicollectionreusableview.md) object.

## Discussion

Call this method from your data source object when asked to provide a new supplementary view for the collection view. This method dequeues an existing view if one is available or creates a new one based on the class or nib file you previously registered.

> [!important] Important
> You must register a class or nib file using the [- registerClass:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-661io.md>) or [- registerNib:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-9hn73.md>) method before calling this method. You can also register a set of default supplementary views with the layout object using the [- registerClass:forDecorationViewOfKind:](<../uicollectionviewlayout/register(__fordecorationviewofkind_)-361k6.md>) or [- registerNib:forDecorationViewOfKind:](<../uicollectionviewlayout/register(__fordecorationviewofkind_)-35jf9.md>) method.

If you registered a class for the specified `identifier` and a new cell must be created, this method initializes the cell by calling its [- initWithFrame:](<../uiview/init(frame_).md>) method. For nib-based cells, this method loads the cell object from the provided nib file. If an existing cell was available for reuse, this method calls the cell’s [- prepareForReuse](<../uicollectionreusableview/prepareforreuse().md>) method instead.

## See Also

### Creating headers and footers

- [SupplementaryRegistration](supplementaryregistration.md) — A registration for the collection view’s supplementary views.
- [dequeueConfiguredReusableSupplementary(using:for:)](<dequeueconfiguredreusablesupplementary(using_for_).md>) — Dequeues a configured reusable supplementary view object.
- [- registerClass:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-661io.md>) — Registers a class for use in creating supplementary views for the collection view.
- [- registerNib:forSupplementaryViewOfKind:withReuseIdentifier:](<register(__forsupplementaryviewofkind_withreuseidentifier_)-9hn73.md>) — Registers a nib file for use in creating supplementary views for the collection view.
