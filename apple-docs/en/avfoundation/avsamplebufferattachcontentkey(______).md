---
title: 'AVSampleBufferAttachContentKey(_:_:_:)'
framework: AVFoundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 14.5+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avsamplebufferattachcontentkey(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferattachcontentkey(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferattachcontentkey%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:09400a24cc2a440c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferAttachContentKey(_:_:_:)

<sub>Function</sub>

Attaches a content key to a sample buffer for the purpose of content decryption.

> [!warning] Deprecated
> Use CMReadySampleBuffer.attach(contentKey:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func AVSampleBufferAttachContentKey(_ sbuf: CMSampleBuffer, _ contentKey: AVContentKey, _ outError: NSErrorPointer) -> Bool
```

## Parameters

- `sbuf` — The sample buffer to which to attach the content key.

- `contentKey` — The content key to attach.

- `outError` — An error pointer. If a failure occurs, the system sets the pointer to an error object that describes the details of the failure.

## Return Value

A Boolean value that indicates whether the attachment is successful.

## See Also

### FairPlay streaming

- [AVContentKeySession](avcontentkeysession.md) — An object that creates and tracks decryption keys for media data.
- [AVContentKeySessionDelegate](avcontentkeysessiondelegate.md) — A protocol that handles content key requests.
- [AVContentKey](avcontentkey.md) — An object that represents the content key decryptor.
- [AVContentKeySpecifier](avcontentkeyspecifier.md) — An object that uniquely identifies a content key.
- [AVContentKeyRequest](avcontentkeyrequest.md) — An object that encapsulates information about a content decryption key request issued from a content key session object.
- [AVPersistableContentKeyRequest](avpersistablecontentkeyrequest.md) — An object that encapsulates information about a persistable content decryption key request issued from a content key session.
- [AVContentKeyResponse](avcontentkeyresponse.md) — An object that encapsulates information about a response to a content decryption key request.
- [AVExternalContentProtectionStatus](avexternalcontentprotectionstatus.md) — Constants that specify whether sufficient protection exists to display the content.
