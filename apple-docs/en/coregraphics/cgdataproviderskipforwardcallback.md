---
title: CGDataProviderSkipForwardCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataproviderskipforwardcallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataproviderskipforwardcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataproviderskipforwardcallback.json'
content_hash: 'sha256:68a5ea3e2e425f5e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataProviderSkipForwardCallback

<sub>Type Alias</sub>

A callback function that advances the current position in the data stream supplied by the provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGDataProviderSkipForwardCallback = (UnsafeMutableRawPointer?, off_t) -> off_t
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [init(version:getBytes:skipForward:rewind:releaseInfo:)](<cgdataprovidersequentialcallbacks/init(version_getbytes_skipforward_rewind_releaseinfo_).md>).

- `count` — The number of bytes to skip.

## Return Value

The number of bytes that were actually skipped.

## Discussion

When Core Graphics needs to advance forward in the provider’s data stream, your function is called.

## See Also

### Creating Sequential-Access Data Providers

- [CGDataProviderCreateSequential](<cgdataprovider/init(sequentialinfo_callbacks_).md>) — Creates a sequential-access data provider.
- [CGDataProviderSequentialCallbacks](cgdataprovidersequentialcallbacks.md) — Defines a structure containing pointers to client-defined callback functions that manage the sending of data for a sequential-access data provider.
- [CGDataProviderRewindCallback](cgdataproviderrewindcallback.md) — A callback function that moves the current position in the data stream back to the beginning.
- [CGDataProviderGetBytesCallback](cgdataprovidergetbytescallback.md) — A callback function that copies from a provider data stream into a Core Graphics buffer.
- [CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md) — A callback function that releases any private data or resources associated with the data provider.
