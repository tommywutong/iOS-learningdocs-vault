---
title: localIdentifier
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phobject/localidentifier
source_url: 'https://developer.apple.com/documentation/photos/phobject/localidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phobject/localidentifier.json'
content_hash: 'sha256:3985072e37b83515'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHObject](../phobject.md)

# localIdentifier

<sub>Instance Property</sub>

A unique string that persistently identifies the object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var localIdentifier: String { get }
```

## Discussion

Use this string to find the object by using the [+ fetchAssetsWithLocalIdentifiers:options:](<../phasset/fetchassets(withlocalidentifiers_options_).md>), [+ fetchAssetCollectionsWithLocalIdentifiers:options:](<../phassetcollection/fetchassetcollections(withlocalidentifiers_options_).md>), or [+ fetchCollectionListsWithLocalIdentifiers:options:](<../phcollectionlist/fetchcollectionlists(withlocalidentifiers_options_).md>) method.
