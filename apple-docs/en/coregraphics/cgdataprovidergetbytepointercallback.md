---
title: CGDataProviderGetBytePointerCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataprovidergetbytepointercallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataprovidergetbytepointercallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataprovidergetbytepointercallback.json'
content_hash: 'sha256:9923279dee226a71'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataProviderGetBytePointerCallback

<sub>Type Alias</sub>

A callback function that returns a generic pointer to the provider data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGDataProviderGetBytePointerCallback = (UnsafeMutableRawPointer?) -> UnsafeRawPointer?
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to `CGDataProviderCreateDirectAccess`.

## Return Value

A generic pointer to your provider data. By suppling this pointer, you are giving Core Graphics read-only access to both the pointer and the underlying provider data. You must not move or modify the provider data until Core Graphics calls your [CGDataProviderReleaseBytePointerCallback](cgdataproviderreleasebytepointercallback.md) function.

## Discussion

When Core Graphics needs direct access to your provider data, this function is called.

For information on how to associate your function with a direct-access data provider, see `CGDataProviderCreateDirectAccess` and `CGDataProviderDirectAccessCallbacks`.

## See Also

### Creating Direct-Access Data Providers

- [CGDataProviderCreateDirect](<cgdataprovider/init(directinfo_size_callbacks_).md>) — Creates a direct-access data provider.
- [CGDataProviderCreateWithCFData](<cgdataprovider/init(data_).md>) — Creates a data provider that reads from a CFData object.
- [CGDataProviderCreateWithURL](<cgdataprovider/init(url_).md>) — Creates a direct-access data provider that uses a URL to supply data.
- [CGDataProviderCreateWithData](<cgdataprovider/init(datainfo_data_size_releasedata_).md>) — Creates a direct-access data provider that uses data your program supplies.
- [CGDataProviderCreateWithFilename](<cgdataprovider/init(filename_).md>) — Creates a direct-access data provider that uses a file to supply data.
- [CGDataProviderDirectCallbacks](cgdataproviderdirectcallbacks.md) — Defines pointers to client-defined callback functions that manage the sending of data for a direct-access data provider.
- [CGDataProviderGetBytesAtPositionCallback](cgdataprovidergetbytesatpositioncallback.md) — A callback function that copies data from the provider into a Core Graphics buffer.
- [CGDataProviderReleaseBytePointerCallback](cgdataproviderreleasebytepointercallback.md) — A callback function that releases the pointer Core Graphics obtained by calling [CGDataProviderGetBytePointerCallback](cgdataprovidergetbytepointercallback.md).
- [CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md) — A callback function that releases any private data or resources associated with the data provider.
- [CGDataProviderReleaseDataCallback](cgdataproviderreleasedatacallback.md) — A callback function that releases data you supply to the function [CGDataProviderCreateWithData](<cgdataprovider/init(datainfo_data_size_releasedata_).md>).
