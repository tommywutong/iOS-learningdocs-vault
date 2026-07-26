---
title: 'makeSecureTokenForExpirationDate(ofPersistableContentKey:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysession/makesecuretokenforexpirationdate(ofpersistablecontentkey:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/makesecuretokenforexpirationdate(ofpersistablecontentkey:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/makesecuretokenforexpirationdate%28ofpersistablecontentkey%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:0be404b13063cad2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# makeSecureTokenForExpirationDate(ofPersistableContentKey:completionHandler:)

<sub>Instance Method</sub>

Creates a secure server playback context that the client sends to the key server to get an expiration date for the given persistable content key data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeSecureTokenForExpirationDate(ofPersistableContentKey persistableContentKeyData: Data, completionHandler handler: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeSecureTokenForExpirationDate(ofPersistableContentKey persistableContentKeyData: Data) async throws -> Data
```

## Parameters

- `persistableContentKeyData` — The previously created persistable content key data.

- `handler` — A block called after the secure token is ready. - **secureTokenData** — The new secure token. - **error** — A parameter that holds the error object that explains the error. If no error occurred, the value of this parameter is `nil`.

## See Also

### Managing expiration

- [- expire](<expire().md>) — Tells the delegate that the session expired as the result of normal, intentional processes.
- [- renewExpiringResponseDataForContentKeyRequest:](<renewexpiringresponsedata(for_).md>) — Tells the delegate that previously provided response data for a content key request is about to expire.
- [contentProtectionSessionIdentifier](contentprotectionsessionidentifier.md) — The identifier for the current content protection session.
