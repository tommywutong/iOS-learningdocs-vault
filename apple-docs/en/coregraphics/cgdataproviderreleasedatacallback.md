---
title: CGDataProviderReleaseDataCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataproviderreleasedatacallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataproviderreleasedatacallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataproviderreleasedatacallback.json'
content_hash: 'sha256:077f1d6152ec4c6b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataProviderReleaseDataCallback

<sub>Type Alias</sub>

A callback function that releases data you supply to the function [CGDataProviderCreateWithData](<cgdataprovider/init(datainfo_data_size_releasedata_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGDataProviderReleaseDataCallback = (UnsafeMutableRawPointer?, UnsafeRawPointer, Int) -> Void
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [CGDataProviderCreateWithData](<cgdataprovider/init(datainfo_data_size_releasedata_).md>).

- `data` — A pointer to your provider data.

- `size` — The size of the data.

## Discussion

When Core Graphics no longer needs direct access to your provider data, your function is called. You may safely modify, move, or release your provider data at this time.

## See Also

### Creating Direct-Access Data Providers

- [CGDataProviderCreateDirect](<cgdataprovider/init(directinfo_size_callbacks_).md>) — Creates a direct-access data provider.
- [CGDataProviderCreateWithCFData](<cgdataprovider/init(data_).md>) — Creates a data provider that reads from a CFData object.
- [CGDataProviderCreateWithURL](<cgdataprovider/init(url_).md>) — Creates a direct-access data provider that uses a URL to supply data.
- [CGDataProviderCreateWithData](<cgdataprovider/init(datainfo_data_size_releasedata_).md>) — Creates a direct-access data provider that uses data your program supplies.
- [CGDataProviderCreateWithFilename](<cgdataprovider/init(filename_).md>) — Creates a direct-access data provider that uses a file to supply data.
- [CGDataProviderDirectCallbacks](cgdataproviderdirectcallbacks.md) — Defines pointers to client-defined callback functions that manage the sending of data for a direct-access data provider.
- [CGDataProviderGetBytePointerCallback](cgdataprovidergetbytepointercallback.md) — A callback function that returns a generic pointer to the provider data.
- [CGDataProviderGetBytesAtPositionCallback](cgdataprovidergetbytesatpositioncallback.md) — A callback function that copies data from the provider into a Core Graphics buffer.
- [CGDataProviderReleaseBytePointerCallback](cgdataproviderreleasebytepointercallback.md) — A callback function that releases the pointer Core Graphics obtained by calling [CGDataProviderGetBytePointerCallback](cgdataprovidergetbytepointercallback.md).
- [CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md) — A callback function that releases any private data or resources associated with the data provider.
