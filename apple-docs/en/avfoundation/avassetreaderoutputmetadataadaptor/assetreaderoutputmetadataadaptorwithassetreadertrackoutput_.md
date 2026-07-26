---
title: 'assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreaderoutputmetadataadaptor/assetreaderoutputmetadataadaptorwithassetreadertrackoutput:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor/assetreaderoutputmetadataadaptorwithassetreadertrackoutput:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutputmetadataadaptor/assetreaderoutputmetadataadaptorwithassetreadertrackoutput%3A.json'
content_hash: 'sha256:2408f84801bc68e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutputMetadataAdaptor](../avassetreaderoutputmetadataadaptor.md)

# assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput:

<sub>Type Method</sub>

Returns a new object that reads timed metadata groups from an asset reader output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput:(AVAssetReaderTrackOutput *) trackOutput;
```

## Parameters

- `trackOutput` — A track output that vends sample buffers that contain metadata.

## Return Value

A metadata adaptor object.

## Discussion

You can only create an adaptor with a track output that vends metadata and isn’t associated with another adaptor instance. Likewise, you can only create an adaptor with a track output whose asset reader hasn’t started reading.

> [!important] Important
> Don’t call the [- copyNextSampleBuffer](<../avassetreaderoutput/copynextsamplebuffer().md>) method on the track output after you use it to initialize a timed metadata adaptor. Calling the track output’s [- copyNextSampleBuffer](<../avassetreaderoutput/copynextsamplebuffer().md>) method after this occurs results in the system throwing an exception.

## See Also

### Creating a metadata adaptor

- [- initWithAssetReaderTrackOutput:](<init(assetreadertrackoutput_).md>) — Creates an object that reads timed metadata groups from an asset reader output. _(deprecated)_
