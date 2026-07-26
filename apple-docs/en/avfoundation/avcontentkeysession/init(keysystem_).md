---
title: 'init(keySystem:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysession/init(keysystem:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/init(keysystem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/init%28keysystem%3A%29.json'
content_hash: 'sha256:573b66844e3a0b1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# init(keySystem:)

<sub>Initializer</sub>

Creates a content key session to manage a collection of content decryption keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(keySystem: AVContentKeySystem)
```

## Parameters

- `keySystem` — A valid key system used to retrieve keys.

## Return Value

Returns a new [AVContentKeySession](../avcontentkeysession.md) instance.

## Discussion

The `AVContentKeySession` instance returned is capable of managing a collection of content decryption keys that correspond to the input key system. An [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) is raised when the value of `keySystem` is unsupported.

## See Also

### Creating a session

- [+ contentKeySessionWithKeySystem:storageDirectoryAtURL:](<init(keysystem_storagedirectoryat_).md>) — Creates a content key session to manage a collection of content decryption keys; points to a directory that stores abnormal session termination reports.
