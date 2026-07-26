---
title: options
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyspecifier/options
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyspecifier/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyspecifier/options.json'
content_hash: 'sha256:30a92d14a8da5c4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySpecifier](../avcontentkeyspecifier.md)

# options

<sub>Instance Property</sub>

A dictionary of options with which you initialized the specifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var options: [String : any Sendable] { get }
```

## See Also

### Inspecting a specifier

- [identifier](identifier.md) — The container and protocol-specific key identifier.
- [keySystem](keysystem.md) — The key system that generates content keys.
