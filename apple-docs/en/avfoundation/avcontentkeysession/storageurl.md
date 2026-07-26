---
title: storageURL
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeysession/storageurl
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/storageurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/storageurl.json'
content_hash: 'sha256:f71fcc9b72642322'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# storageURL

<sub>Instance Property</sub>

A URL that points to a writable storage directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var storageURL: URL? { get }
```

## Discussion

The writable directory stores expired session reports.

## See Also

### Inspecting the session

- [keySystem](keysystem.md) — The type of key system used to retrieve keys.
- [AVContentKeySystem](../avcontentkeysystem.md) — A key-delivery method for a content key session.
