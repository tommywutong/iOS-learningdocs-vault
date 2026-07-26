---
title: 'init(directInfo:size:callbacks:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgdataprovider/init(directinfo:size:callbacks:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataprovider/init(directinfo:size:callbacks:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataprovider/init%28directinfo%3Asize%3Acallbacks%3A%29.json'
content_hash: 'sha256:a9f74ade766755fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataProvider](../cgdataprovider.md)

# init(directInfo:size:callbacks:)

<sub>Initializer</sub>

Creates a direct-access data provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(directInfo info: UnsafeMutableRawPointer?, size: off_t, callbacks: UnsafePointer<CGDataProviderDirectCallbacks>)
```

## Parameters

- `info` — A pointer to data of any type or `NULL`. When Core Graphics calls the functions specified in the `callbacks` parameter, it sends each of the functions this pointer.

- `size` — The number of bytes of data to provide.

- `callbacks` — A pointer to a [CGDataProviderDirectCallbacks](../cgdataproviderdirectcallbacks.md) structure that specifies the callback functions you implement to handle the data provider’s basic memory management.

## Return Value

A new data provider. In Objective-C, you’re responsible for releasing this object using [CGDataProviderRelease](../cgdataproviderrelease.md).

## Discussion

You use this function to create a direct-access data provider that uses callback functions to read data from your program in a single block.

## See Also

### Creating Direct-Access Data Providers

- [CGDataProviderCreateWithCFData](<init(data_).md>) — Creates a data provider that reads from a CFData object.
- [CGDataProviderCreateWithURL](<init(url_).md>) — Creates a direct-access data provider that uses a URL to supply data.
- [CGDataProviderCreateWithData](<init(datainfo_data_size_releasedata_).md>) — Creates a direct-access data provider that uses data your program supplies.
- [CGDataProviderCreateWithFilename](<init(filename_).md>) — Creates a direct-access data provider that uses a file to supply data.
- [CGDataProviderDirectCallbacks](../cgdataproviderdirectcallbacks.md) — Defines pointers to client-defined callback functions that manage the sending of data for a direct-access data provider.
- [CGDataProviderGetBytePointerCallback](../cgdataprovidergetbytepointercallback.md) — A callback function that returns a generic pointer to the provider data.
- [CGDataProviderGetBytesAtPositionCallback](../cgdataprovidergetbytesatpositioncallback.md) — A callback function that copies data from the provider into a Core Graphics buffer.
- [CGDataProviderReleaseBytePointerCallback](../cgdataproviderreleasebytepointercallback.md) — A callback function that releases the pointer Core Graphics obtained by calling [CGDataProviderGetBytePointerCallback](../cgdataprovidergetbytepointercallback.md).
- [CGDataProviderReleaseInfoCallback](../cgdataproviderreleaseinfocallback.md) — A callback function that releases any private data or resources associated with the data provider.
- [CGDataProviderReleaseDataCallback](../cgdataproviderreleasedatacallback.md) — A callback function that releases data you supply to the function [CGDataProviderCreateWithData](<init(datainfo_data_size_releasedata_).md>).
