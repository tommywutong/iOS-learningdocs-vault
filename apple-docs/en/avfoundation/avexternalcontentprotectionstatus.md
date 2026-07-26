---
title: AVExternalContentProtectionStatus
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalcontentprotectionstatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalcontentprotectionstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalcontentprotectionstatus.json'
content_hash: 'sha256:72c9a7def333ba5e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVExternalContentProtectionStatus

<sub>Enumeration</sub>

Constants that specify whether sufficient protection exists to display the content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum AVExternalContentProtectionStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Status values

- [AVExternalContentProtectionStatusPending](avexternalcontentprotectionstatus/pending.md) — A status that indicates content protections are pending.
- [AVExternalContentProtectionStatusSufficient](avexternalcontentprotectionstatus/sufficient.md) — A status that indicates sufficient protections exists for display.
- [AVExternalContentProtectionStatusInsufficient](avexternalcontentprotectionstatus/insufficient.md) — A status that indicates insufficient protections exists for display.

### Initializers

- [init(rawValue:)](<avexternalcontentprotectionstatus/init(rawvalue_).md>)

## See Also

### FairPlay streaming

- [AVContentKeySession](avcontentkeysession.md) — An object that creates and tracks decryption keys for media data.
- [AVContentKeySessionDelegate](avcontentkeysessiondelegate.md) — A protocol that handles content key requests.
- [AVContentKey](avcontentkey.md) — An object that represents the content key decryptor.
- [AVContentKeySpecifier](avcontentkeyspecifier.md) — An object that uniquely identifies a content key.
- [AVContentKeyRequest](avcontentkeyrequest.md) — An object that encapsulates information about a content decryption key request issued from a content key session object.
- [AVPersistableContentKeyRequest](avpersistablecontentkeyrequest.md) — An object that encapsulates information about a persistable content decryption key request issued from a content key session.
- [AVContentKeyResponse](avcontentkeyresponse.md) — An object that encapsulates information about a response to a content decryption key request.
- [AVSampleBufferAttachContentKey](<avsamplebufferattachcontentkey(______).md>) — Attaches a content key to a sample buffer for the purpose of content decryption. _(deprecated)_
