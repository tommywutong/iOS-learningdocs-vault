---
title: 'init(url:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgdataprovider/init(url:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataprovider/init(url:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataprovider/init%28url%3A%29.json'
content_hash: 'sha256:7c0dc9d909569855'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataProvider](../cgdataprovider.md)

# init(url:)

<sub>Initializer</sub>

Creates a direct-access data provider that uses a URL to supply data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(url: CFURL)
```

## Parameters

- `url` — A CFURL object for the URL that you want to read the data from.

## Return Value

A new data provider or `NULL` if the data from the URL could not be accessed. In Objective-C, you’re responsible for releasing this object using [CGDataProviderRelease](../cgdataproviderrelease.md).

## Discussion

You use this function to create a direct-access data provider that supplies data from a URL. When you supply Core Graphics with a direct-access data provider, Core Graphics obtains data from your program in a single entire block.

## See Also

### Creating Direct-Access Data Providers

- [CGDataProviderCreateDirect](<init(directinfo_size_callbacks_).md>) — Creates a direct-access data provider.
- [CGDataProviderCreateWithCFData](<init(data_).md>) — Creates a data provider that reads from a CFData object.
- [CGDataProviderCreateWithData](<init(datainfo_data_size_releasedata_).md>) — Creates a direct-access data provider that uses data your program supplies.
- [CGDataProviderCreateWithFilename](<init(filename_).md>) — Creates a direct-access data provider that uses a file to supply data.
- [CGDataProviderDirectCallbacks](../cgdataproviderdirectcallbacks.md) — Defines pointers to client-defined callback functions that manage the sending of data for a direct-access data provider.
- [CGDataProviderGetBytePointerCallback](../cgdataprovidergetbytepointercallback.md) — A callback function that returns a generic pointer to the provider data.
- [CGDataProviderGetBytesAtPositionCallback](../cgdataprovidergetbytesatpositioncallback.md) — A callback function that copies data from the provider into a Core Graphics buffer.
- [CGDataProviderReleaseBytePointerCallback](../cgdataproviderreleasebytepointercallback.md) — A callback function that releases the pointer Core Graphics obtained by calling [CGDataProviderGetBytePointerCallback](../cgdataprovidergetbytepointercallback.md).
- [CGDataProviderReleaseInfoCallback](../cgdataproviderreleaseinfocallback.md) — A callback function that releases any private data or resources associated with the data provider.
- [CGDataProviderReleaseDataCallback](../cgdataproviderreleasedatacallback.md) — A callback function that releases data you supply to the function [CGDataProviderCreateWithData](<init(datainfo_data_size_releasedata_).md>).
