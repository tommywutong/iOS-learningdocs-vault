---
title: 'assetWriterInputMetadataAdaptorWithAssetWriterInput:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinputmetadataadaptor/assetwriterinputmetadataadaptorwithassetwriterinput:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/assetwriterinputmetadataadaptorwithassetwriterinput:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputmetadataadaptor/assetwriterinputmetadataadaptorwithassetwriterinput%3A.json'
content_hash: 'sha256:76e38a1881bcac70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputMetadataAdaptor](../avassetwriterinputmetadataadaptor.md)

# assetWriterInputMetadataAdaptorWithAssetWriterInput:

<sub>Type Method</sub>

Returns a new metadata adaptor to append timed metadata groups to write to an output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetWriterInputMetadataAdaptorWithAssetWriterInput:(AVAssetWriterInput *) input;
```

## Parameters

- `input` — The metadata input to which to append groups of timed metadata.

## Return Value

An input metadata adaptor.

## See Also

### Creating an input metadata adaptor

- [- initWithAssetWriterInput:](<init(assetwriterinput_).md>) — Creates a metadata group adaptor to append timed metadata groups to write to an output file. _(deprecated)_
