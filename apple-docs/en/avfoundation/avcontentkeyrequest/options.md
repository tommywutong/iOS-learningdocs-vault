---
title: options
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 13.1+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequest/options
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/options.json'
content_hash: 'sha256:a9b9303cfd2f2f1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# options

<sub>Instance Property</sub>

A dictionary of options used to initialize key loading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var options: [String : any Sendable] { get }
```

## See Also

### Inspecting a request

- [contentKey](contentkey.md) — The generated content key.
- [contentKeySpecifier](contentkeyspecifier.md) — The requested content key specifier.
- [RetryReason](retryreason.md) — The reason for asking the client to retry a content key request.
