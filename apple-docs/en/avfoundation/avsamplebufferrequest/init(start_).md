---
title: 'init(start:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebufferrequest/init(start:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/init(start:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrequest/init%28start%3A%29.json'
content_hash: 'sha256:c88a137b4e0e72f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRequest](../avsamplebufferrequest.md)

# init(start:)

<sub>Initializer</sub>

Creates a newly allocated sample buffer request with the specified sample cursor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(start startCursor: AVSampleCursor)
```

## Parameters

- `startCursor` — The starting cursor position.

## Return Value

An initialized `AVSampleBufferRequest` instance.
