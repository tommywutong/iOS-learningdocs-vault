---
title: 'contentKeySessionDidGenerateExpiredSessionReport(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysessiondidgenerateexpiredsessionreport(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysessiondidgenerateexpiredsessionreport(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysessiondidgenerateexpiredsessionreport%28_%3A%29.json'
content_hash: 'sha256:a5b7a241d3ece25b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySessionDelegate](../avcontentkeysessiondelegate.md)

# contentKeySessionDidGenerateExpiredSessionReport(_:)

<sub>Instance Method</sub>

Notifies the sender that an expired session report has been generated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func contentKeySessionDidGenerateExpiredSessionReport(_ session: AVContentKeySession)
```

## Parameters

- `session` — The [AVContentKeySession](../avcontentkeysession.md) object that recorded the generation of an expired session report.

## Discussion

This method is invoked when an expired session report is added to the [storageURL](../avcontentkeysession/storageurl.md) property.

## See Also

### Updating and retrying content key requests

- [- contentKeySession:didProvideContentKeyRequests:forInitializationData:](<contentkeysession(__didprovide_forinitializationdata_).md>)
- [- contentKeySession:externalProtectionStatusDidChangeForContentKey:](<contentkeysession(__externalprotectionstatusdidchangefor_).md>) — Tells the delegate when external protection state has changed.
- [- contentKeySession:didUpdatePersistableContentKey:forContentKeyIdentifier:](<contentkeysession(__didupdatepersistablecontentkey_forcontentkeyidentifier_).md>) — Provides the receiver with an updated persistable content key for a specific key request.
- [- contentKeySession:shouldRetryContentKeyRequest:reason:](<contentkeysession(__shouldretry_reason_).md>) — Provides the receiver with a content key request object to retry.
- [RetryReason](../avcontentkeyrequest/retryreason.md) — The reason for asking the client to retry a content key request.
- [- contentKeySessionContentProtectionSessionIdentifierDidChange:](<contentkeysessioncontentprotectionsessionidentifierdidchange(__).md>) — Tells the receiver the content protection session identifier changed.
- [- contentKeySession:contentKeyRequest:didFailWithError:](<contentkeysession(__contentkeyrequest_didfailwitherror_).md>) — Tells the receiver that the content key request failed.
- [- contentKeySession:contentKeyRequestDidSucceed:](<contentkeysession(__contentkeyrequestdidsucceed_).md>) — Tells the content key session that the response to a content key requeset was successfully processed.
