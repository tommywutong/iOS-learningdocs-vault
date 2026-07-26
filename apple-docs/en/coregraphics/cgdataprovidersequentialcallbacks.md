---
title: CGDataProviderSequentialCallbacks
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataprovidersequentialcallbacks
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataprovidersequentialcallbacks.json'
content_hash: 'sha256:e713b36b8d315960'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataProviderSequentialCallbacks

<sub>Structure</sub>

Defines a structure containing pointers to client-defined callback functions that manage the sending of data for a sequential-access data provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CGDataProviderSequentialCallbacks
```

## Overview

The functions specified by the `CGDataProviderSequentialCallbacks` structure are responsible for sequentially copying data to a memory buffer for Core Graphics to use. The functions are also responsible for handling the data provider’s basic memory management. You supply a `CGDataProviderSequentialCallbacks` structure to the function [CGDataProviderCreateSequential](<cgdataprovider/init(sequentialinfo_callbacks_).md>) to create a sequential-access data provider.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cgdataprovidersequentialcallbacks/init().md>)
- [init(version:getBytes:skipForward:rewind:releaseInfo:)](<cgdataprovidersequentialcallbacks/init(version_getbytes_skipforward_rewind_releaseinfo_).md>)

### Instance Properties

- [getBytes](cgdataprovidersequentialcallbacks/getbytes.md) — A pointer to a function that copies data from the provider. For more information, see [CGDataProviderGetBytesCallback](cgdataprovidergetbytescallback.md).
- [releaseInfo](cgdataprovidersequentialcallbacks/releaseinfo.md) — A pointer to a function that handles clean-up for the data provider, or `NULL`. For more information, see [CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md).
- [rewind](cgdataprovidersequentialcallbacks/rewind.md) — A pointer to a function Core Graphics calls to return the provider to the beginning of the data stream. For more information, see [CGDataProviderRewindCallback](cgdataproviderrewindcallback.md).
- [skipForward](cgdataprovidersequentialcallbacks/skipforward.md) — A pointer to a function that Core Graphics calls to advance the stream of data supplied by the provider.
- [version](cgdataprovidersequentialcallbacks/version.md) — The version of this structure. It should be set to 0.

## See Also

### Creating Sequential-Access Data Providers

- [CGDataProviderCreateSequential](<cgdataprovider/init(sequentialinfo_callbacks_).md>) — Creates a sequential-access data provider.
- [CGDataProviderRewindCallback](cgdataproviderrewindcallback.md) — A callback function that moves the current position in the data stream back to the beginning.
- [CGDataProviderGetBytesCallback](cgdataprovidergetbytescallback.md) — A callback function that copies from a provider data stream into a Core Graphics buffer.
- [CGDataProviderSkipForwardCallback](cgdataproviderskipforwardcallback.md) — A callback function that advances the current position in the data stream supplied by the provider.
- [CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md) — A callback function that releases any private data or resources associated with the data provider.
