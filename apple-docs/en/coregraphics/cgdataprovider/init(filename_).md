---
title: 'init(filename:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgdataprovider/init(filename:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataprovider/init(filename:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataprovider/init%28filename%3A%29.json'
content_hash: 'sha256:ecc8e0dfe1d24b6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataProvider](../cgdataprovider.md)

# init(filename:)

<sub>Initializer</sub>

Creates a direct-access data provider that uses a file to supply data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(filename: UnsafePointer<CChar>)
```

## Parameters

- `filename` — The full or relative pathname to use for the data provider. When you supply Core Graphics data via the provider, it reads the data from the specified file.

## Return Value

A new data provider or `NULL` if the file could not be opened. In Objective-C, you’re responsible for releasing this object using [CGDataProviderRelease](../cgdataproviderrelease.md).

## Discussion

You use this function to create a direct-access data provider that supplies data from a file. When you supply Core Graphics with a direct-access data provider, Core Graphics obtains data from your program in a single block.

## See Also

### Creating Direct-Access Data Providers

- [CGDataProviderCreateDirect](<init(directinfo_size_callbacks_).md>) — Creates a direct-access data provider.
- [CGDataProviderCreateWithCFData](<init(data_).md>) — Creates a data provider that reads from a CFData object.
- [CGDataProviderCreateWithURL](<init(url_).md>) — Creates a direct-access data provider that uses a URL to supply data.
- [CGDataProviderCreateWithData](<init(datainfo_data_size_releasedata_).md>) — Creates a direct-access data provider that uses data your program supplies.
- [CGDataProviderDirectCallbacks](../cgdataproviderdirectcallbacks.md) — Defines pointers to client-defined callback functions that manage the sending of data for a direct-access data provider.
- [CGDataProviderGetBytePointerCallback](../cgdataprovidergetbytepointercallback.md) — A callback function that returns a generic pointer to the provider data.
- [CGDataProviderGetBytesAtPositionCallback](../cgdataprovidergetbytesatpositioncallback.md) — A callback function that copies data from the provider into a Core Graphics buffer.
- [CGDataProviderReleaseBytePointerCallback](../cgdataproviderreleasebytepointercallback.md) — A callback function that releases the pointer Core Graphics obtained by calling [CGDataProviderGetBytePointerCallback](../cgdataprovidergetbytepointercallback.md).
- [CGDataProviderReleaseInfoCallback](../cgdataproviderreleaseinfocallback.md) — A callback function that releases any private data or resources associated with the data provider.
- [CGDataProviderReleaseDataCallback](../cgdataproviderreleasedatacallback.md) — A callback function that releases data you supply to the function [CGDataProviderCreateWithData](<init(datainfo_data_size_releasedata_).md>).
