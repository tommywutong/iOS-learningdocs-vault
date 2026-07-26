---
title: CGDataProviderGetBytesAtPositionCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataprovidergetbytesatpositioncallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataprovidergetbytesatpositioncallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataprovidergetbytesatpositioncallback.json'
content_hash: 'sha256:0b0200908494ce4b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataProviderGetBytesAtPositionCallback

<sub>Type Alias</sub>

A callback function that copies data from the provider into a Core Graphics buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGDataProviderGetBytesAtPositionCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer, off_t, Int) -> Int
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [CGDataProviderCreateDirect](<cgdataprovider/init(directinfo_size_callbacks_).md>).

- `buffer` — The Core Graphics buffer into which you copy the specified number of bytes.

- `position` — Specifies the relative location in the data provider at which to begin copying data.

- `count` — The number of bytes to copy.

## Return Value

The number of bytes copied. If no more data can be written to the buffer, you should return 0.

## Discussion

When Core Graphics is ready to receive data from the provider, your function is called.

## See Also

### Creating Direct-Access Data Providers

- [CGDataProviderCreateDirect](<cgdataprovider/init(directinfo_size_callbacks_).md>) — Creates a direct-access data provider.
- [CGDataProviderCreateWithCFData](<cgdataprovider/init(data_).md>) — Creates a data provider that reads from a CFData object.
- [CGDataProviderCreateWithURL](<cgdataprovider/init(url_).md>) — Creates a direct-access data provider that uses a URL to supply data.
- [CGDataProviderCreateWithData](<cgdataprovider/init(datainfo_data_size_releasedata_).md>) — Creates a direct-access data provider that uses data your program supplies.
- [CGDataProviderCreateWithFilename](<cgdataprovider/init(filename_).md>) — Creates a direct-access data provider that uses a file to supply data.
- [CGDataProviderDirectCallbacks](cgdataproviderdirectcallbacks.md) — Defines pointers to client-defined callback functions that manage the sending of data for a direct-access data provider.
- [CGDataProviderGetBytePointerCallback](cgdataprovidergetbytepointercallback.md) — A callback function that returns a generic pointer to the provider data.
- [CGDataProviderReleaseBytePointerCallback](cgdataproviderreleasebytepointercallback.md) — A callback function that releases the pointer Core Graphics obtained by calling [CGDataProviderGetBytePointerCallback](cgdataprovidergetbytepointercallback.md).
- [CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md) — A callback function that releases any private data or resources associated with the data provider.
- [CGDataProviderReleaseDataCallback](cgdataproviderreleasedatacallback.md) — A callback function that releases data you supply to the function [CGDataProviderCreateWithData](<cgdataprovider/init(datainfo_data_size_releasedata_).md>).
