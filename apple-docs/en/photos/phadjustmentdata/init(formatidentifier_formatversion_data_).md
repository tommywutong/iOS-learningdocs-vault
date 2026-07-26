---
title: 'init(formatIdentifier:formatVersion:data:)'
framework: Photos
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phadjustmentdata/init(formatidentifier:formatversion:data:)'
source_url: 'https://developer.apple.com/documentation/photos/phadjustmentdata/init(formatidentifier:formatversion:data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phadjustmentdata/init%28formatidentifier%3Aformatversion%3Adata%3A%29.json'
content_hash: 'sha256:ad74377ded525361'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAdjustmentData](../phadjustmentdata.md)

# init(formatIdentifier:formatVersion:data:)

<sub>Initializer</sub>

Initializes an adjustment object with the specified format and data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(formatIdentifier: String, formatVersion: String, data: Data)
```

## Parameters

- `formatIdentifier` — A string that uniquely identifies the format of the adjustment data.

- `formatVersion` — A version number for the adjustment data format.

- `data` — A serialized form of whatever information is needed to reconstruct the adjustment.

## Return Value

An initialized adjustment object.

## Discussion

To uniquely identify the adjustments your app makes, use the `formatIdentifier` and `formatVersion` parameters. These parameters help you determine whether and how to interpret the adjustment data when working with an edited asset later. For best results, use reverse-DNS-style identifiers and monotonically increasing version numbers.

For example, in the first version of your app, you might save adjustment data using the identifier `com.example.myApp` and version `1.0`. If a later version of your app adds incompatible information to the adjustment data, you can use the same identifier and increase the version number to `2.0`.

Use the `data` parameter to store whatever information is useful to your app for reconstructing an edit. For example, if your app applies Core Image filters to photos, you can use this parameter to store a serialized property list that describes the filters and their parameters.

> [!note] Note
> Because Photos limits the size of adjustment data, you should keep your edit information short and descriptive. Don’t use image data to describe an edit—instead, save only the minimal information that is needed to recreate the edit.

Your app must provide a non-empty [NSData](../../foundation/nsdata.md) object for the `data` parameter. If you cannot provide relevant data to describe an edit, you may pass data that encodes an [NSUUID](../../foundation/nsuuid.md) object.
