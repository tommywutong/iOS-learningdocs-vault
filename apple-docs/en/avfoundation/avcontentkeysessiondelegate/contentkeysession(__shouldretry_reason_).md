---
title: 'contentKeySession(_:shouldRetry:reason:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:shouldretry:reason:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:shouldretry:reason:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession%28_%3Ashouldretry%3Areason%3A%29.json'
content_hash: 'sha256:d8e584d7e1fc3b18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySessionDelegate](../avcontentkeysessiondelegate.md)

# contentKeySession(_:shouldRetry:reason:)

<sub>Instance Method</sub>

Provides the receiver with a content key request object to retry.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func contentKeySession(_ session: AVContentKeySession, shouldRetry keyRequest: AVContentKeyRequest, reason retryReason: AVContentKeyRequest.RetryReason) -> Bool
```

## Parameters

- `session` — The content key session that is providing the content key request.

- `keyRequest` — The key request to be retried.

- `retryReason` — The reason for the retry request.

## See Also

### Updating and retrying content key requests

- [- contentKeySession:didProvideContentKeyRequests:forInitializationData:](<contentkeysession(__didprovide_forinitializationdata_).md>)
- [- contentKeySession:externalProtectionStatusDidChangeForContentKey:](<contentkeysession(__externalprotectionstatusdidchangefor_).md>) — Tells the delegate when external protection state has changed.
- [- contentKeySession:didUpdatePersistableContentKey:forContentKeyIdentifier:](<contentkeysession(__didupdatepersistablecontentkey_forcontentkeyidentifier_).md>) — Provides the receiver with an updated persistable content key for a specific key request.
- [RetryReason](../avcontentkeyrequest/retryreason.md) — The reason for asking the client to retry a content key request.
- [- contentKeySessionContentProtectionSessionIdentifierDidChange:](<contentkeysessioncontentprotectionsessionidentifierdidchange(__).md>) — Tells the receiver the content protection session identifier changed.
- [- contentKeySession:contentKeyRequest:didFailWithError:](<contentkeysession(__contentkeyrequest_didfailwitherror_).md>) — Tells the receiver that the content key request failed.
- [- contentKeySession:contentKeyRequestDidSucceed:](<contentkeysession(__contentkeyrequestdidsucceed_).md>) — Tells the content key session that the response to a content key requeset was successfully processed.
- [- contentKeySessionDidGenerateExpiredSessionReport:](<contentkeysessiondidgenerateexpiredsessionreport(__).md>) — Notifies the sender that an expired session report has been generated.
