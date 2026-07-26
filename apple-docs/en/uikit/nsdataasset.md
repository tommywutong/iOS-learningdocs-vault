---
title: NSDataAsset
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdataasset
source_url: 'https://developer.apple.com/documentation/uikit/nsdataasset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdataasset.json'
content_hash: 'sha256:7d55b6f6b345704b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDataAsset

<sub>Class</sub>

An object from a data set type stored in an asset catalog.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class NSDataAsset
```

## Overview

The object’s content is stored as a set of one or more files with associated device attributes. These sets can also be tagged for use as on-demand resources.

### Initialize data assets

Data assets are initialized from a named data set in an asset catalog. You create data sets during app development. Each data set contains one or more data files. Each file has associated attributes for features of the device, including the minimum amount of memory and the version of Metal. When you initialize the data asset, the system selects the data file that best matches the current device.

For more information on the data set type in an asset catalog, see [Data Set Type](https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/DataSetType.html#//apple_ref/doc/uid/TP40015170-CH23) in [Asset Catalog Format Reference](https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/index.html#//apple_ref/doc/uid/TP40015170). For information on asset catalogs, see [Managing assets with asset catalogs](../xcode/managing-assets-with-asset-catalogs.md).

### Access the data

You access the data file by using the [data](nsdataasset/data.md) property. Because the property is of type [NSData](../foundation/nsdata.md) it provides methods for accessing the raw data only as bytes and ranges of bytes.

To access structured data, convert the bytes into the appropriate format. The system can convert some data types for you. One example is XML data using the [init(data:)](<../foundation/xmlparser/init(data_).md>) method of [XMLParser](../foundation/xmlparser.md). Other data types require code for parsing and converting the raw data. You may need to convert larger data files incrementally.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing the data asset

- [- initWithName:](<nsdataasset/init(name_).md>) — Initializes and returns an object with a reference to the named data asset in an asset catalog.
- [- initWithName:bundle:](<nsdataasset/init(name_bundle_).md>) — Initializes and returns an object with a reference to the named data asset that’s in an asset catalog in the specified bundle.

### Accessing data

- [data](nsdataasset/data.md) — The raw data values in the data asset.

### Getting data asset information

- [name](nsdataasset/name.md) — The name of the data set in the asset catalog.
- [NSDataAssetName](nsdataassetname.md) — The name of a data asset.
- [typeIdentifier](nsdataasset/typeidentifier.md) — The uniform type identifier for the data asset.

## See Also

### Assets

- [UIImageAsset](uiimageasset.md) — A container for a collection of images that represent multiple ways of describing a single piece of artwork.
