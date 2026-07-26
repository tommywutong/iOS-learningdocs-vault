---
title: 'init(assetReaderTrackOutput:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetreaderoutputmetadataadaptor/init(assetreadertrackoutput:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor/init(assetreadertrackoutput:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutputmetadataadaptor/init%28assetreadertrackoutput%3A%29.json'
content_hash: 'sha256:36accf90d6f45996'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutputMetadataAdaptor](../avassetreaderoutputmetadataadaptor.md)

# init(assetReaderTrackOutput:)

<sub>Initializer</sub>

Creates an object that reads timed metadata groups from an asset reader output.

> [!warning] Deprecated
> Use AVAssetReader.outputMetadataProvider(for:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput)
```

## Parameters

- `trackOutput` — A track output that vends sample buffers that contain metadata.

## Discussion

You can only create an adaptor with a track output that vends metadata, and that isn’t associated with another adaptor instance. Likewise, you can only create an adaptor with a track output whose asset reader hasn’t started reading.

> [!important] Important
> Don’t call the [- copyNextSampleBuffer](<../avassetreaderoutput/copynextsamplebuffer().md>) method on the track output after you use it to initialize a timed metadata adaptor. Calling the track output’s [- copyNextSampleBuffer](<../avassetreaderoutput/copynextsamplebuffer().md>) method after this occurs results in the system throwing an exception.
