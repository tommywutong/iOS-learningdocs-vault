---
title: 'init(identifiers:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemmetadataoutput/init(identifiers:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/init(identifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemmetadataoutput/init%28identifiers%3A%29.json'
content_hash: 'sha256:fb8197b95fa81b96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemMetadataOutput](../avplayeritemmetadataoutput.md)

# init(identifiers:)

<sub>Initializer</sub>

Creates an instance of AVPlayerItemMetadataOutput.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(identifiers: [String]?)
```

## Parameters

- `identifiers` — A array of metadata identifiers indicating the metadata items that the output should provide.

## Return Value

An AVPlayerItemMetadataOutput instance.

## Discussion

Pass `nil` to receive all of the timed metadata from all enabled `AVPlayerItemTracks` that carry timed metadata.
