---
title: contentProtectionSessionIdentifier
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeysession/contentprotectionsessionidentifier
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/contentprotectionsessionidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/contentprotectionsessionidentifier.json'
content_hash: 'sha256:f3b59e2484883040'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# contentProtectionSessionIdentifier

<sub>Instance Property</sub>

The identifier for the current content protection session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var contentProtectionSessionIdentifier: Data? { get }
```

## Discussion

The content protection session identifier is a unique string the session generates.

## See Also

### Managing expiration

- [- expire](<expire().md>) — Tells the delegate that the session expired as the result of normal, intentional processes.
- [- makeSecureTokenForExpirationDateOfPersistableContentKey:completionHandler:](<makesecuretokenforexpirationdate(ofpersistablecontentkey_completionhandler_).md>) — Creates a secure server playback context that the client sends to the key server to get an expiration date for the given persistable content key data.
- [- renewExpiringResponseDataForContentKeyRequest:](<renewexpiringresponsedata(for_).md>) — Tells the delegate that previously provided response data for a content key request is about to expire.
