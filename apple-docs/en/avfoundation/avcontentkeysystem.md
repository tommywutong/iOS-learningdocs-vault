---
title: AVContentKeySystem
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeysystem
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysystem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysystem.json'
content_hash: 'sha256:1467556569a99b81'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVContentKeySystem

<sub>Structure</sub>

A key-delivery method for a content key session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVContentKeySystem
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Key-delivery methods

- [AVContentKeySystemFairPlayStreaming](avcontentkeysystem/fairplaystreaming.md) — A method of key delivery that uses FairPlay Streaming.
- [AVContentKeySystemClearKey](avcontentkeysystem/clearkey.md) — A method of key delivery that uses a clear key system.
- [AVContentKeySystemAuthorizationToken](avcontentkeysystem/authorizationtoken.md) — A method of key delivery that uses a token to authorize playback.

### Initializers

- [init(rawValue:)](<avcontentkeysystem/init(rawvalue_).md>) — Creates a content key system with a string value.

## See Also

### Inspecting the session

- [keySystem](avcontentkeysession/keysystem.md) — The type of key system used to retrieve keys.
- [storageURL](avcontentkeysession/storageurl.md) — A URL that points to a writable storage directory.
