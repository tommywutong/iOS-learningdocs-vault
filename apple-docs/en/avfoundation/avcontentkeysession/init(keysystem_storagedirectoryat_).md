---
title: 'init(keySystem:storageDirectoryAt:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysession/init(keysystem:storagedirectoryat:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/init(keysystem:storagedirectoryat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/init%28keysystem%3Astoragedirectoryat%3A%29.json'
content_hash: 'sha256:35cf47f68b34fb39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# init(keySystem:storageDirectoryAt:)

<sub>Initializer</sub>

Creates a content key session to manage a collection of content decryption keys; points to a directory that stores abnormal session termination reports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(keySystem: AVContentKeySystem, storageDirectoryAt storageURL: URL)
```

## Parameters

- `keySystem` — A valid key system used to retrieve keys.

- `storageURL` — A URL that points to a writable directory. The session uses the directory to facilitate expired session reports after an abnormal session termination.

## Return Value

Returns a new AVContentKeySession instance.

## Discussion

The `AVContentKeySession` instance returned is capable of managing a collection of content decryption keys that correspond to the input key system. An [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) is raised when the value of `keySystem` is unsupported.

## See Also

### Creating a session

- [+ contentKeySessionWithKeySystem:](<init(keysystem_).md>) — Creates a content key session to manage a collection of content decryption keys.
