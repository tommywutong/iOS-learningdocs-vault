---
title: CGDataProviderRewindCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataproviderrewindcallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataproviderrewindcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataproviderrewindcallback.json'
content_hash: 'sha256:b9eb9a7a70d4da4d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataProviderRewindCallback

<sub>Type Alias</sub>

A callback function that moves the current position in the data stream back to the beginning.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGDataProviderRewindCallback = (UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [init(version:getBytes:skipForward:rewind:releaseInfo:)](<cgdataprovidersequentialcallbacks/init(version_getbytes_skipforward_rewind_releaseinfo_).md>).

## Discussion

When Core Graphics needs to read from the beginning of the provider’s data stream, your function is called.

For information on how to associate your callback function with a data provider, see [CGDataProvider](cgdataprovider.md) and [CGDataProviderSequentialCallbacks](cgdataprovidersequentialcallbacks.md).

## See Also

### Creating Sequential-Access Data Providers

- [CGDataProviderCreateSequential](<cgdataprovider/init(sequentialinfo_callbacks_).md>) — Creates a sequential-access data provider.
- [CGDataProviderSequentialCallbacks](cgdataprovidersequentialcallbacks.md) — Defines a structure containing pointers to client-defined callback functions that manage the sending of data for a sequential-access data provider.
- [CGDataProviderGetBytesCallback](cgdataprovidergetbytescallback.md) — A callback function that copies from a provider data stream into a Core Graphics buffer.
- [CGDataProviderSkipForwardCallback](cgdataproviderskipforwardcallback.md) — A callback function that advances the current position in the data stream supplied by the provider.
- [CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md) — A callback function that releases any private data or resources associated with the data provider.
