---
title: AVAsynchronousKeyValueLoading
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avasynchronouskeyvalueloading
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronouskeyvalueloading.json'
content_hash: 'sha256:dab8f00307e8d333'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAsynchronousKeyValueLoading

<sub>Protocol</sub>

A protocol that defines the interface to load media data asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AVAsynchronousKeyValueLoading
```

## Overview

Loading media data takes an amount of time that depends on factors including the media’s size, location, device capabilities, network conditions, and so on. To optimize performance, [AVAsset](avasset.md) defers loading its media data until you query its properties or perform an operation that requires it. This means that performing these actions from a synchronous context would block the calling thread for an unknown amount of time, which would result in a poor user experience, and may even cause your app to crash. For this reason, you must load media data asynchronously.

Call the asynchronous [load(_:isolation:)](<avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the values of media properties, or determine the loaded status of a property by calling the [status(of:)](<avasynchronouskeyvalueloading/status(of_).md>) method. See [Loading media data asynchronously](loading-media-data-asynchronously.md) for more information.

## Relationships

- **Conforming Types**: [AVAsset](avasset.md), [AVAssetTrack](avassettrack.md), [AVComposition](avcomposition.md), [AVCompositionTrack](avcompositiontrack.md), [AVFragmentedAsset](avfragmentedasset.md), [AVFragmentedAssetTrack](avfragmentedassettrack.md), [AVFragmentedMovie](avfragmentedmovie.md), [AVFragmentedMovieTrack](avfragmentedmovietrack.md), [AVMetadataItem](avmetadataitem.md), [AVMovie](avmovie.md), [AVMovieTrack](avmovietrack.md), [AVMutableComposition](avmutablecomposition.md), [AVMutableCompositionTrack](avmutablecompositiontrack.md), [AVMutableMetadataItem](avmutablemetadataitem.md), [AVMutableMovie](avmutablemovie.md), [AVMutableMovieTrack](avmutablemovietrack.md), [AVURLAsset](avurlasset.md)

## Topics

### Loading property values

- [load(_:isolation:)](<avasynchronouskeyvalueloading/load(__isolation_).md>) — Loads a property asynchronously and returns the value.
- [load(_:_:_:isolation:)](<avasynchronouskeyvalueloading/load(______isolation_).md>) — Loads two or more properties asynchronously and returns the values.

### Determining the loaded status

- [status(of:)](<avasynchronouskeyvalueloading/status(of_).md>) — Returns a value that indicates the loaded status of a property.

### Deprecated

- [Deprecated symbols](avasynchronouskeyvalueloading-deprecated-symbols.md) — Review unsupported symbols and their replacements.
- [- loadValuesAsynchronouslyForKeys:completionHandler:](<avasynchronouskeyvalueloading/loadvaluesasynchronously(forkeys_completionhandler_).md>) — Tells the asset to load the values of all of the specified keys that aren’t already loaded. _(deprecated)_
- [- statusOfValueForKey:error:](<avasynchronouskeyvalueloading/statusofvalue(forkey_error_).md>) — Returns a status that indicates whether a property value is immediately available without blocking the calling thread. _(deprecated)_
- [AVKeyValueStatus](avkeyvaluestatus.md) — Values that indicate the loaded status of a property. _(deprecated)_

## See Also

### Property loading

- [AVAsyncProperty](avasyncproperty.md) — An asynchronous property that constrains its type and value.
- [AVPartialAsyncProperty](avpartialasyncproperty.md) — An asynchronous property that constrains its type.
- [AVAnyAsyncProperty](avanyasyncproperty.md) — A base class for asynchronous properties.
