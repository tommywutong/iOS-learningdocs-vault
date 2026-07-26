---
title: 'assetReaderSampleReferenceOutputWithTrack:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreadersamplereferenceoutput/assetreadersamplereferenceoutputwithtrack:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreadersamplereferenceoutput/assetreadersamplereferenceoutputwithtrack:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreadersamplereferenceoutput/assetreadersamplereferenceoutputwithtrack%3A.json'
content_hash: 'sha256:2d011a6e04ff5140'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderSampleReferenceOutput](../avassetreadersamplereferenceoutput.md)

# assetReaderSampleReferenceOutputWithTrack:

<sub>Type Method</sub>

Returns a new object that supplies sample references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetReaderSampleReferenceOutputWithTrack:(AVAssetTrack *) track;
```

## Parameters

- `track` — The track for which to provide sample references.

## Return Value

A sample rererence output object.

## See Also

### Creating a sample reference output

- [- initWithTrack:](<init(track_).md>) — Creates an object that supplies sample references.
