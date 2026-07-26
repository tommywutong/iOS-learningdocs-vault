---
title: 'assetReaderOutputCaptionAdaptorWithAssetReaderTrackOutput:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreaderoutputcaptionadaptor/assetreaderoutputcaptionadaptorwithassetreadertrackoutput:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor/assetreaderoutputcaptionadaptorwithassetreadertrackoutput:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutputcaptionadaptor/assetreaderoutputcaptionadaptorwithassetreadertrackoutput%3A.json'
content_hash: 'sha256:dc2c8ae9710e2bc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutputCaptionAdaptor](../avassetreaderoutputcaptionadaptor.md)

# assetReaderOutputCaptionAdaptorWithAssetReaderTrackOutput:

<sub>Type Method</sub>

A class method that creates a caption adaptor that reads from a track output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetReaderOutputCaptionAdaptorWithAssetReaderTrackOutput:(AVAssetReaderTrackOutput *) trackOutput;
```

## Parameters

- `trackOutput` — The track output from which to read captions.

## Return Value

A new instance of [AVAssetReaderOutputCaptionAdaptor](../avassetreaderoutputcaptionadaptor.md).

## See Also

### Creating a caption adaptor

- [- initWithAssetReaderTrackOutput:](<init(assetreadertrackoutput_).md>) — Creates a caption adaptor that reads from a track output. _(deprecated)_
