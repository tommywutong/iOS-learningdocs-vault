---
title: 'contentKeySpecifierForKeySystem:identifier:options:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeyspecifier/contentkeyspecifierforkeysystem:identifier:options:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyspecifier/contentkeyspecifierforkeysystem:identifier:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyspecifier/contentkeyspecifierforkeysystem%3Aidentifier%3Aoptions%3A.json'
content_hash: 'sha256:8a5a5ad7404f7d82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySpecifier](../avcontentkeyspecifier.md)

# contentKeySpecifierForKeySystem:identifier:options:

<sub>Type Method</sub>

A convenience initializer to create a content key specifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) contentKeySpecifierForKeySystem:(AVContentKeySystem) keySystem identifier:(id) contentKeyIdentifier options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `keySystem` — The key system to use to generate content keys.

- `contentKeyIdentifier` — The container and protocol-specific key identifier.

- `options` — Additional information necessary to obtain the key. Pass `nil` to indicate no additional options.

## See Also

### Creating a specifier

- [- initForKeySystem:identifier:options:](<init(forkeysystem_identifier_options_).md>) — Creates a content key specifier.
