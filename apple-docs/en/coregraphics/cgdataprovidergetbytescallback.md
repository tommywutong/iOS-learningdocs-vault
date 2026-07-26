---
title: CGDataProviderGetBytesCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataprovidergetbytescallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataprovidergetbytescallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataprovidergetbytescallback.json'
content_hash: 'sha256:f10315a2e88e51cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataProviderGetBytesCallback

<sub>Type Alias</sub>

A callback function that copies from a provider data stream into a Core Graphics buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGDataProviderGetBytesCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Int
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [init(version:getBytes:skipForward:rewind:releaseInfo:)](<cgdataprovidersequentialcallbacks/init(version_getbytes_skipforward_rewind_releaseinfo_).md>).

- `buffer` — The Core Graphics buffer into which you copy the specified number of bytes.

- `count` — The number of bytes to copy.

## Return Value

The number of bytes copied. If no more data can be written to the buffer, you should return `0`.

## Discussion

When Core Graphics is ready to receive data from the provider data stream, your function is called. It should copy the specified number of bytes into `buffer`.

For information on how to associate your callback function with a data provider, see [CGDataProvider](cgdataprovider.md) and [CGDataProviderSequentialCallbacks](cgdataprovidersequentialcallbacks.md).

## See Also

### Creating Sequential-Access Data Providers

- [CGDataProviderCreateSequential](<cgdataprovider/init(sequentialinfo_callbacks_).md>) — Creates a sequential-access data provider.
- [CGDataProviderSequentialCallbacks](cgdataprovidersequentialcallbacks.md) — Defines a structure containing pointers to client-defined callback functions that manage the sending of data for a sequential-access data provider.
- [CGDataProviderRewindCallback](cgdataproviderrewindcallback.md) — A callback function that moves the current position in the data stream back to the beginning.
- [CGDataProviderSkipForwardCallback](cgdataproviderskipforwardcallback.md) — A callback function that advances the current position in the data stream supplied by the provider.
- [CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md) — A callback function that releases any private data or resources associated with the data provider.
