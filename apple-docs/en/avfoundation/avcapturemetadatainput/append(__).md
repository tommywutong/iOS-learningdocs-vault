---
title: 'append(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturemetadatainput/append(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput/append(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemetadatainput/append%28_%3A%29.json'
content_hash: 'sha256:a9dac99bb8e78f7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMetadataInput](../avcapturemetadatainput.md)

# append(_:)

<sub>Instance Method</sub>

Provides metadata to the capture session.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func append(_ metadata: AVTimedMetadataGroup) throws
```

## Parameters

- `metadata` — A timed group of metadata. To denote a period of no metadata, pass an empty [AVTimedMetadataGroup](../avtimedmetadatagroup.md).
