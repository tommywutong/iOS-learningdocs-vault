---
title: 'renewExpiringResponseData(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysession/renewexpiringresponsedata(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/renewexpiringresponsedata(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/renewexpiringresponsedata%28for%3A%29.json'
content_hash: 'sha256:9202818e325b56d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# renewExpiringResponseData(for:)

<sub>Instance Method</sub>

Tells the delegate that previously provided response data for a content key request is about to expire.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func renewExpiringResponseData(for contentKeyRequest: AVContentKeyRequest)
```

## Parameters

- `contentKeyRequest` — The content key request that’s about to expire.

## See Also

### Managing expiration

- [- expire](<expire().md>) — Tells the delegate that the session expired as the result of normal, intentional processes.
- [- makeSecureTokenForExpirationDateOfPersistableContentKey:completionHandler:](<makesecuretokenforexpirationdate(ofpersistablecontentkey_completionhandler_).md>) — Creates a secure server playback context that the client sends to the key server to get an expiration date for the given persistable content key data.
- [contentProtectionSessionIdentifier](contentprotectionsessionidentifier.md) — The identifier for the current content protection session.
