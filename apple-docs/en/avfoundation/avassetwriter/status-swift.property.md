---
title: status
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/status-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/status-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/status-swift.property.json'
content_hash: 'sha256:9a9695341248be42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# status

<sub>Instance Property</sub>

The status of writing samples to the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var status: AVAssetWriter.Status { get }
```

## Discussion

This property is thread safe.

## See Also

### Inspecting writing status

- [Status](status-swift.enum.md) — Values that indicate the state of an asset writer.
- [error](error.md) — An error object that describes an asset-writing failure.
