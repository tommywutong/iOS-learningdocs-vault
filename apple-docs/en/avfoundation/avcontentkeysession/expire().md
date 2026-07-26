---
title: expire()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeysession/expire()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/expire()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/expire%28%29.json'
content_hash: 'sha256:3f3ca37812210f76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# expire()

<sub>Instance Method</sub>

Tells the delegate that the session expired as the result of normal, intentional processes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func expire()
```

## See Also

### Managing expiration

- [- makeSecureTokenForExpirationDateOfPersistableContentKey:completionHandler:](<makesecuretokenforexpirationdate(ofpersistablecontentkey_completionhandler_).md>) — Creates a secure server playback context that the client sends to the key server to get an expiration date for the given persistable content key data.
- [- renewExpiringResponseDataForContentKeyRequest:](<renewexpiringresponsedata(for_).md>) — Tells the delegate that previously provided response data for a content key request is about to expire.
- [contentProtectionSessionIdentifier](contentprotectionsessionidentifier.md) — The identifier for the current content protection session.
