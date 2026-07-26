---
title: 'init(dataInfo:data:size:releaseData:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgdataprovider/init(datainfo:data:size:releasedata:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataprovider/init(datainfo:data:size:releasedata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataprovider/init%28datainfo%3Adata%3Asize%3Areleasedata%3A%29.json'
content_hash: 'sha256:5ecace7430c63582'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataProvider](../cgdataprovider.md)

# init(dataInfo:data:size:releaseData:)

<sub>Initializer</sub>

Creates a direct-access data provider that uses data your program supplies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(dataInfo info: UnsafeMutableRawPointer?, data: UnsafeRawPointer, size: Int, releaseData: CGDataProviderReleaseDataCallback)
```

## Parameters

- `info` — A pointer to data of any type, or `NULL`. When Core Graphics calls the function specified in the `releaseData` parameter, it sends this pointer as its first argument.

- `data` — A pointer to the array of data that the provider contains.

- `size` — A value that specifies the number of bytes that the data provider contains.

- `releaseData` — A pointer to a release callback for the data provider, or `NULL`. Your release function is called when Core Graphics frees the data provider. For more information, see [CGDataProviderReleaseDataCallback](../cgdataproviderreleasedatacallback.md).

## Return Value

A new data provider. In Objective-C, you’re responsible for releasing this object using [CGDataProviderRelease](../cgdataproviderrelease.md).

## Discussion

You use this function to create a direct-access data provider that uses callback functions to read data from your program an entire block at one time.

## See Also

### Creating Direct-Access Data Providers

- [CGDataProviderCreateDirect](<init(directinfo_size_callbacks_).md>) — Creates a direct-access data provider.
- [CGDataProviderCreateWithCFData](<init(data_).md>) — Creates a data provider that reads from a CFData object.
- [CGDataProviderCreateWithURL](<init(url_).md>) — Creates a direct-access data provider that uses a URL to supply data.
- [CGDataProviderCreateWithFilename](<init(filename_).md>) — Creates a direct-access data provider that uses a file to supply data.
- [CGDataProviderDirectCallbacks](../cgdataproviderdirectcallbacks.md) — Defines pointers to client-defined callback functions that manage the sending of data for a direct-access data provider.
- [CGDataProviderGetBytePointerCallback](../cgdataprovidergetbytepointercallback.md) — A callback function that returns a generic pointer to the provider data.
- [CGDataProviderGetBytesAtPositionCallback](../cgdataprovidergetbytesatpositioncallback.md) — A callback function that copies data from the provider into a Core Graphics buffer.
- [CGDataProviderReleaseBytePointerCallback](../cgdataproviderreleasebytepointercallback.md) — A callback function that releases the pointer Core Graphics obtained by calling [CGDataProviderGetBytePointerCallback](../cgdataprovidergetbytepointercallback.md).
- [CGDataProviderReleaseInfoCallback](../cgdataproviderreleaseinfocallback.md) — A callback function that releases any private data or resources associated with the data provider.
- [CGDataProviderReleaseDataCallback](../cgdataproviderreleasedatacallback.md) — A callback function that releases data you supply to the function [CGDataProviderCreateWithData](<init(datainfo_data_size_releasedata_).md>).
