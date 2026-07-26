---
title: 'init(forKeySystem:identifier:options:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeyspecifier/init(forkeysystem:identifier:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyspecifier/init(forkeysystem:identifier:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyspecifier/init%28forkeysystem%3Aidentifier%3Aoptions%3A%29.json'
content_hash: 'sha256:84f3764ae629b0e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySpecifier](../avcontentkeyspecifier.md)

# init(forKeySystem:identifier:options:)

<sub>Initializer</sub>

Creates a content key specifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(forKeySystem keySystem: AVContentKeySystem, identifier contentKeyIdentifier: Any, options: [String : Any] = [:])
```

## Parameters

- `keySystem` — The key system to use to generate content keys.

- `contentKeyIdentifier` — The container and protocol-specific key identifier.

- `options` — Additional information necessary to obtain the key. Pass `nil` to indicate no additional options.
