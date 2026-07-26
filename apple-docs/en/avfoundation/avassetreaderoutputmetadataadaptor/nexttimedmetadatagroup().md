---
title: nextTimedMetadataGroup()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetreaderoutputmetadataadaptor/nexttimedmetadatagroup()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor/nexttimedmetadatagroup()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutputmetadataadaptor/nexttimedmetadatagroup%28%29.json'
content_hash: 'sha256:745f905d2c5200cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutputMetadataAdaptor](../avassetreaderoutputmetadataadaptor.md)

# nextTimedMetadataGroup()

<sub>Instance Method</sub>

Returns the next timed metadata group for the asset reader output.

> [!warning] Deprecated
> Use AVAssetReader.outputMetadataProvider(for:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func nextTimedMetadataGroup() -> AVTimedMetadataGroup?
```

## Return Value

A timed metadata group that represents the next logical segment of metadata from the source asset reader output.

## Discussion

This method returns `nil` after the adaptor reads all timed metadata groups from the output, or if an error occurs. When the return value is `nil`, check the asset reader’s [status](../avassetreader/status-swift.property.md) property to determine why it couldn’t read more samples.
