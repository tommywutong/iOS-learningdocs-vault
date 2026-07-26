---
title: 'contentKeySession(_:contentKeyRequestDidSucceed:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:contentkeyrequestdidsucceed:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:contentkeyrequestdidsucceed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession%28_%3Acontentkeyrequestdidsucceed%3A%29.json'
content_hash: 'sha256:7c2f2c4a514d3d31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySessionDelegate](../avcontentkeysessiondelegate.md)

# contentKeySession(_:contentKeyRequestDidSucceed:)

<sub>Instance Method</sub>

Tells the content key session that the response to a content key requeset was successfully processed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func contentKeySession(_ session: AVContentKeySession, contentKeyRequestDidSucceed keyRequest: AVContentKeyRequest)
```

## Parameters

- `session` — The [AVContentKeySession](../avcontentkeysession.md) instance that initiated the content key request.

- `keyRequest` — The [AVContentKeyRequest](../avcontentkeyrequest.md) instance whose response was successfully processed.

## See Also

### Updating and retrying content key requests

- [- contentKeySession:didProvideContentKeyRequests:forInitializationData:](<contentkeysession(__didprovide_forinitializationdata_).md>)
- [- contentKeySession:externalProtectionStatusDidChangeForContentKey:](<contentkeysession(__externalprotectionstatusdidchangefor_).md>) — Tells the delegate when external protection state has changed.
- [- contentKeySession:didUpdatePersistableContentKey:forContentKeyIdentifier:](<contentkeysession(__didupdatepersistablecontentkey_forcontentkeyidentifier_).md>) — Provides the receiver with an updated persistable content key for a specific key request.
- [- contentKeySession:shouldRetryContentKeyRequest:reason:](<contentkeysession(__shouldretry_reason_).md>) — Provides the receiver with a content key request object to retry.
- [RetryReason](../avcontentkeyrequest/retryreason.md) — The reason for asking the client to retry a content key request.
- [- contentKeySessionContentProtectionSessionIdentifierDidChange:](<contentkeysessioncontentprotectionsessionidentifierdidchange(__).md>) — Tells the receiver the content protection session identifier changed.
- [- contentKeySession:contentKeyRequest:didFailWithError:](<contentkeysession(__contentkeyrequest_didfailwitherror_).md>) — Tells the receiver that the content key request failed.
- [- contentKeySessionDidGenerateExpiredSessionReport:](<contentkeysessiondidgenerateexpiredsessionreport(__).md>) — Notifies the sender that an expired session report has been generated.
