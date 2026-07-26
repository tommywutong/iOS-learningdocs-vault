---
title: error
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/error
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/error.json'
content_hash: 'sha256:1805d2c5b1bfed2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# error

<sub>Instance Property</sub>

An error object that describes an asset-writing failure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var error: (any Error)? { get }
```

## See Also

### Inspecting writing status

- [status](status-swift.property.md) — The status of writing samples to the output file.
- [Status](status-swift.enum.md) — Values that indicate the state of an asset writer.
