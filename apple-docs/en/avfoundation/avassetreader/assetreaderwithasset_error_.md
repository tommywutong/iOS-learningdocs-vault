---
title: 'assetReaderWithAsset:error:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetreader/assetreaderwithasset:error:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreader/assetreaderwithasset:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreader/assetreaderwithasset%3Aerror%3A.json'
content_hash: 'sha256:400756643eadadc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReader](../avassetreader.md)

# assetReaderWithAsset:error:

<sub>Type Method</sub>

Returns a new object to read media data from an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetReaderWithAsset:(AVAsset *) asset error:(NSError **) outError;
```

## Parameters

- `asset` — The asset from which to read media data.

- `outError` — On return, if the initialization fails, a pointer to an error object provides the details of the failure.

## Return Value

A new asset reader object.

## See Also

### Creating an asset reader

- [- initWithAsset:error:](<init(asset_).md>) — Creates an object to read media data from an asset.
