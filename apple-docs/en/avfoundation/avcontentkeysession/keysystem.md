---
title: keySystem
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeysession/keysystem
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/keysystem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/keysystem.json'
content_hash: 'sha256:29d877311be13608'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# keySystem

<sub>Instance Property</sub>

The type of key system used to retrieve keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var keySystem: AVContentKeySystem { get }
```

## Discussion

Valid values for keySystem are [AVContentKeySystemFairPlayStreaming](../avcontentkeysystem/fairplaystreaming.md) and [AVContentKeySystemClearKey](../avcontentkeysystem/clearkey.md).

## See Also

### Inspecting the session

- [AVContentKeySystem](../avcontentkeysystem.md) — A key-delivery method for a content key session.
- [storageURL](storageurl.md) — A URL that points to a writable storage directory.
