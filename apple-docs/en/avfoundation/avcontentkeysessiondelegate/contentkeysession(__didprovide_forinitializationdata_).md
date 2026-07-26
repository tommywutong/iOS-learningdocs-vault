---
title: 'contentKeySession(_:didProvide:forInitializationData:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+, watchOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:didprovide:forinitializationdata:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:didprovide:forinitializationdata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession%28_%3Adidprovide%3Aforinitializationdata%3A%29.json'
content_hash: 'sha256:a8d79f4ad4968da3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySessionDelegate](../avcontentkeysessiondelegate.md)

# contentKeySession(_:didProvide:forInitializationData:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func contentKeySession(_ session: AVContentKeySession, didProvide keyRequests: [AVContentKeyRequest], forInitializationData initializationData: Data?)
```

## See Also

### Updating and retrying content key requests

- [- contentKeySession:externalProtectionStatusDidChangeForContentKey:](<contentkeysession(__externalprotectionstatusdidchangefor_).md>) — Tells the delegate when external protection state has changed.
- [- contentKeySession:didUpdatePersistableContentKey:forContentKeyIdentifier:](<contentkeysession(__didupdatepersistablecontentkey_forcontentkeyidentifier_).md>) — Provides the receiver with an updated persistable content key for a specific key request.
- [- contentKeySession:shouldRetryContentKeyRequest:reason:](<contentkeysession(__shouldretry_reason_).md>) — Provides the receiver with a content key request object to retry.
- [RetryReason](../avcontentkeyrequest/retryreason.md) — The reason for asking the client to retry a content key request.
- [- contentKeySessionContentProtectionSessionIdentifierDidChange:](<contentkeysessioncontentprotectionsessionidentifierdidchange(__).md>) — Tells the receiver the content protection session identifier changed.
- [- contentKeySession:contentKeyRequest:didFailWithError:](<contentkeysession(__contentkeyrequest_didfailwitherror_).md>) — Tells the receiver that the content key request failed.
- [- contentKeySession:contentKeyRequestDidSucceed:](<contentkeysession(__contentkeyrequestdidsucceed_).md>) — Tells the content key session that the response to a content key requeset was successfully processed.
- [- contentKeySessionDidGenerateExpiredSessionReport:](<contentkeysessiondidgenerateexpiredsessionreport(__).md>) — Notifies the sender that an expired session report has been generated.
