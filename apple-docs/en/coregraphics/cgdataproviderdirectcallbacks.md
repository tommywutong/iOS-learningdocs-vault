---
title: CGDataProviderDirectCallbacks
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataproviderdirectcallbacks
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataproviderdirectcallbacks.json'
content_hash: 'sha256:e4ae67ae76d3e881'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataProviderDirectCallbacks

<sub>Structure</sub>

Defines pointers to client-defined callback functions that manage the sending of data for a direct-access data provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CGDataProviderDirectCallbacks
```

## Overview

You supply a [CGDataProviderDirectCallbacks](cgdataproviderdirectcallbacks.md) structure to the function [CGDataProviderCreateDirect](<cgdataprovider/init(directinfo_size_callbacks_).md>) to create a data provider for direct access. The functions specified by the [CGDataProviderDirectCallbacks](cgdataproviderdirectcallbacks.md) structure are responsible for copying data a block at a time to a memory buffer for Core Graphics to use. The functions are also responsible for handling the data provider’s basic memory management. For the callback to work, one of the `getBytePointer` and `getBytesAtPosition` parameters must be non-`NULL`. If both are non-`NULL`, then `getBytePointer` is used to access the data.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cgdataproviderdirectcallbacks/init().md>)
- [init(version:getBytePointer:releaseBytePointer:getBytesAtPosition:releaseInfo:)](<cgdataproviderdirectcallbacks/init(version_getbytepointer_releasebytepointer_getbytesatposition_releaseinfo_).md>)

### Instance Properties

- [getBytePointer](cgdataproviderdirectcallbacks/getbytepointer.md) — A pointer to a function that returns a pointer to the provider’s data. For more information, see [CGDataProviderGetBytePointerCallback](cgdataprovidergetbytepointercallback.md).
- [getBytesAtPosition](cgdataproviderdirectcallbacks/getbytesatposition.md) — A pointer to a function that copies data from the provider.
- [releaseBytePointer](cgdataproviderdirectcallbacks/releasebytepointer.md) — A pointer to a function that Core Graphics calls to release a pointer to the provider’s data. For more information, see [CGDataProviderReleaseBytePointerCallback](cgdataproviderreleasebytepointercallback.md).
- [releaseInfo](cgdataproviderdirectcallbacks/releaseinfo.md) — A pointer to a function that handles clean-up for the data provider, or `NULL`. For more information, see [CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md).
- [version](cgdataproviderdirectcallbacks/version.md) — The version of this structure. It should be set to 0.

## See Also

### Creating Direct-Access Data Providers

- [CGDataProviderCreateDirect](<cgdataprovider/init(directinfo_size_callbacks_).md>) — Creates a direct-access data provider.
- [CGDataProviderCreateWithCFData](<cgdataprovider/init(data_).md>) — Creates a data provider that reads from a CFData object.
- [CGDataProviderCreateWithURL](<cgdataprovider/init(url_).md>) — Creates a direct-access data provider that uses a URL to supply data.
- [CGDataProviderCreateWithData](<cgdataprovider/init(datainfo_data_size_releasedata_).md>) — Creates a direct-access data provider that uses data your program supplies.
- [CGDataProviderCreateWithFilename](<cgdataprovider/init(filename_).md>) — Creates a direct-access data provider that uses a file to supply data.
- [CGDataProviderGetBytePointerCallback](cgdataprovidergetbytepointercallback.md) — A callback function that returns a generic pointer to the provider data.
- [CGDataProviderGetBytesAtPositionCallback](cgdataprovidergetbytesatpositioncallback.md) — A callback function that copies data from the provider into a Core Graphics buffer.
- [CGDataProviderReleaseBytePointerCallback](cgdataproviderreleasebytepointercallback.md) — A callback function that releases the pointer Core Graphics obtained by calling [CGDataProviderGetBytePointerCallback](cgdataprovidergetbytepointercallback.md).
- [CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md) — A callback function that releases any private data or resources associated with the data provider.
- [CGDataProviderReleaseDataCallback](cgdataproviderreleasedatacallback.md) — A callback function that releases data you supply to the function [CGDataProviderCreateWithData](<cgdataprovider/init(datainfo_data_size_releasedata_).md>).
