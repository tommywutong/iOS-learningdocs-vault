---
title: 'init(nibName:bundle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewcontroller/init(nibname:bundle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/init(nibname:bundle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcontroller/init%28nibname%3Abundle%3A%29.json'
content_hash: 'sha256:fd5145e5d0583cc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewController](../uicollectionviewcontroller.md)

# init(nibName:bundle:)

<sub>Initializer</sub>

Returns a newly initialized view controller with the nib file in the specified bundle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(nibName nibNameOrNil: String?, bundle nibBundleOrNil: Bundle?)
```

## Parameters

- `nibNameOrNil` — The name of the nib file to associate with the view controller. The nib file name shouldn’t contain any leading path information. If you specify `nil`, the [nibName](../uiviewcontroller/nibname.md) property is set to `nil`.

- `nibBundleOrNil` — The bundle in which to search for the nib file. This method looks for the nib file in the bundle’s language-specific project directories first, followed by the Resources directory.

## Return Value

A newly initialized [UICollectionViewController](../uicollectionviewcontroller.md) object.

## Discussion

For more information on how to initialize a view controller from a nib file, see [- initWithNibName:bundle:](<../uiviewcontroller/init(nibname_bundle_).md>).

## See Also

### Creating a collection view controller

- [- initWithCollectionViewLayout:](<init(collectionviewlayout_).md>) — Initializes a collection view controller and configures the collection view with the provided layout.
- [- initWithCoder:](<init(coder_).md>) — Creates a collection view controller with the nib file in the specified bundle.
