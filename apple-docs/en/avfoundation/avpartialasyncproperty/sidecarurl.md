---
title: sidecarURL
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/sidecarurl
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/sidecarurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/sidecarurl.json'
content_hash: 'sha256:5b3bc1fe378bb419'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# sidecarURL

<sub>Type Property</sub>

The sidecar URL used by the MediaExtension. The sidecar URL is returned only if the MediaExtension format reader supports sidecar files, and implements this property [MEFileInfo setSidecarFilename:]. Will return nil otherwise.

<sub>macOS</sub>

```swift
static var sidecarURL: AVAsyncProperty<Root, URL?> { get }
```

## See Also

### Describing a property

- [description](description.md) — A description of the object.
