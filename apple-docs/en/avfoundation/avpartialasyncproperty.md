---
title: AVPartialAsyncProperty
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty.json'
content_hash: 'sha256:1650aaaee46e8606'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPartialAsyncProperty

<sub>Class</sub>

An asynchronous property that constrains its type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPartialAsyncProperty<Root>
```

## Overview

This class defines the [AVAsyncProperty](avasyncproperty.md) constants for various AVFoundation types, including [AVAsset](avasset.md), [AVAssetTrack](avassettrack.md), and [AVMetadataItem](avmetadataitem.md).

## Relationships

- **Inherits From**: [AVAnyAsyncProperty](avanyasyncproperty.md)

- **Inherited By**: [AVAsyncProperty](avasyncproperty.md)

- **Conforms To**: [CustomStringConvertible](../swift/customstringconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Loading properties

- [AVAsset](avasset-async-properties.md) — Asynchronous properties for assets.
- [AVAssetTrack](avassettrack-async-properties.md) — Asynchronous properties for asset tracks.
- [AVURLAsset](avurlasset-async-properties.md) — Asynchronous properties for URL assets.
- [AVFragmentedAsset](avfragmentedasset-async-properties.md) — Asynchronous properties for fragmented assets.
- [AVMetadataItem](avmetadataitem-async-properties.md) — Asynchronous properties for metadata items.
- [AVComposition](avcomposition-async-properties.md) — Asynchronous properties for compositions.
- [AVMutableComposition](avmutablecomposition-async-properties.md) — Asynchronous properties for mutable compositions.
- [AVMovie](avmovie-async-properties.md) — Asynchronous properties for movies.
- [AVMutableMovie](avmutablemovie-async-properties.md) — Asynchronous properties for mutable movies.
- [AVFragmentedMovie](avfragmentedmovie-async-properties.md) — Asynchronous properties for fragmented movies.

### Describing a property

- [description](avpartialasyncproperty/description.md) — A description of the object.
- [sidecarURL](avpartialasyncproperty/sidecarurl.md) — The sidecar URL used by the MediaExtension. The sidecar URL is returned only if the MediaExtension format reader supports sidecar files, and implements this property [MEFileInfo setSidecarFilename:]. Will return nil otherwise.

### Type Properties

- [constituentFileURLs](avpartialasyncproperty/constituentfileurls.md) — The list of file URLs used by the MediaExtension that constitute the asset. The list of file URLs that constitute the asset are returned only for QuickTime reference movies, or if the MediaExtension format reader implements this property [MEFileInfo setConstituentFileNames:]. _(beta)_

## See Also

### Property loading

- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md) — A protocol that defines the interface to load media data asynchronously.
- [AVAsyncProperty](avasyncproperty.md) — An asynchronous property that constrains its type and value.
- [AVAnyAsyncProperty](avanyasyncproperty.md) — A base class for asynchronous properties.
