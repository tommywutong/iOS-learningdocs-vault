---
title: 'contentKeySession(_:didUpdatePersistableContentKey:forContentKeyIdentifier:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:didupdatepersistablecontentkey:forcontentkeyidentifier:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:didupdatepersistablecontentkey:forcontentkeyidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession%28_%3Adidupdatepersistablecontentkey%3Aforcontentkeyidentifier%3A%29.json'
content_hash: 'sha256:1551989eb4211640'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySessionDelegate](../avcontentkeysessiondelegate.md)

# contentKeySession(_:didUpdatePersistableContentKey:forContentKeyIdentifier:)

<sub>Instance Method</sub>

Provides the receiver with an updated persistable content key for a specific key request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func contentKeySession(_ session: AVContentKeySession, didUpdatePersistableContentKey persistableContentKey: Data, forContentKeyIdentifier keyIdentifier: Any)
```

## Parameters

- `session` — The content key session that is providing the updated persistable content key.

- `persistableContentKey` — The updated persistent content key data. This data can be stored offline and used to answer future content key requests with the matching key identifier.

- `keyIdentifier` — A container- and protocol-specific identifier for the updated persistent content key.

## Discussion

If the content key session provides updated persistable content key data, previous key data is no longer valid and cannot be used to answer future loading requests.

## See Also

### Updating and retrying content key requests

- [- contentKeySession:didProvideContentKeyRequests:forInitializationData:](<contentkeysession(__didprovide_forinitializationdata_).md>)
- [- contentKeySession:externalProtectionStatusDidChangeForContentKey:](<contentkeysession(__externalprotectionstatusdidchangefor_).md>) — Tells the delegate when external protection state has changed.
- [- contentKeySession:shouldRetryContentKeyRequest:reason:](<contentkeysession(__shouldretry_reason_).md>) — Provides the receiver with a content key request object to retry.
- [RetryReason](../avcontentkeyrequest/retryreason.md) — The reason for asking the client to retry a content key request.
- [- contentKeySessionContentProtectionSessionIdentifierDidChange:](<contentkeysessioncontentprotectionsessionidentifierdidchange(__).md>) — Tells the receiver the content protection session identifier changed.
- [- contentKeySession:contentKeyRequest:didFailWithError:](<contentkeysession(__contentkeyrequest_didfailwitherror_).md>) — Tells the receiver that the content key request failed.
- [- contentKeySession:contentKeyRequestDidSucceed:](<contentkeysession(__contentkeyrequestdidsucceed_).md>) — Tells the content key session that the response to a content key requeset was successfully processed.
- [- contentKeySessionDidGenerateExpiredSessionReport:](<contentkeysessiondidgenerateexpiredsessionreport(__).md>) — Notifies the sender that an expired session report has been generated.
