---
title: CGDataProvider
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataprovider
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataprovider.json'
content_hash: 'sha256:43a0a659f63568d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataProvider

<sub>Class</sub>

An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGDataProvider
```

## Overview

Data provider objects abstract the data-access task and eliminate the need for applications to manage data through a raw memory buffer.

For information on how to use CGDataProvider functions, see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) Programming Guide.

See also [CGDataConsumer](cgdataconsumer.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Sequential-Access Data Providers

- [CGDataProviderCreateSequential](<cgdataprovider/init(sequentialinfo_callbacks_).md>) — Creates a sequential-access data provider.
- [CGDataProviderSequentialCallbacks](cgdataprovidersequentialcallbacks.md) — Defines a structure containing pointers to client-defined callback functions that manage the sending of data for a sequential-access data provider.
- [CGDataProviderRewindCallback](cgdataproviderrewindcallback.md) — A callback function that moves the current position in the data stream back to the beginning.
- [CGDataProviderGetBytesCallback](cgdataprovidergetbytescallback.md) — A callback function that copies from a provider data stream into a Core Graphics buffer.
- [CGDataProviderSkipForwardCallback](cgdataproviderskipforwardcallback.md) — A callback function that advances the current position in the data stream supplied by the provider.
- [CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md) — A callback function that releases any private data or resources associated with the data provider.

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
- [CGDataProviderReleaseDataCallback](cgdataproviderreleasedatacallback.md) — A callback function that releases data you supply to the function [CGDataProviderCreateWithData](<cgdataprovider/init(datainfo_data_size_releasedata_).md>).

### Getting Data from a Data Provider

- [CGDataProviderCopyData](cgdataprovider/data.md) — Returns a copy of the provider’s data.

### Working with Core Foundation Types

- [CGDataProviderGetTypeID](cgdataprovider/typeid.md) — Returns the Core Foundation type identifier for data providers.

### Instance Properties

- [CGDataProviderGetInfo](cgdataprovider/info.md)

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)

### Utility and Support Classes

- [CGDataConsumer](cgdataconsumer.md) — An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [CGShading](cgshading.md) — A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [CGGradient](cggradient.md) — A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [CGFunction](cgfunction.md) — A general facility for defining and using callback functions.
- [CGPattern](cgpattern.md) — A 2D pattern to be used for drawing graphics paths.
