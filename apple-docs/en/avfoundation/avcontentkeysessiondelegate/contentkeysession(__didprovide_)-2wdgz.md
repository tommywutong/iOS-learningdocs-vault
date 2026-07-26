---
title: 'contentKeySession(_:didProvide:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:didprovide:)-2wdgz'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:didprovide:)-2wdgz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession%28_%3Adidprovide%3A%29-2wdgz.json'
content_hash: 'sha256:2398a802b2121f09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySessionDelegate](../avcontentkeysessiondelegate.md)

# contentKeySession(_:didProvide:)

<sub>Instance Method</sub>

Provides the receiver with a new content key request object to process a persistable content key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func contentKeySession(_ session: AVContentKeySession, didProvide keyRequest: AVPersistableContentKeyRequest)
```

## Parameters

- `session` — The content key session that is providing the new persistable content key request.

- `keyRequest` — The request for a new persistable content key.

## See Also

### Providing new content key requests

- [- contentKeySession:didProvideContentKeyRequest:](<contentkeysession(__didprovide_)-3coq5.md>) — Provides the receiver with a new content key request object.
- [- contentKeySession:didProvideRenewingContentKeyRequest:](<contentkeysession(__didproviderenewingcontentkeyrequest_).md>) — Provides the receiver with a new content key request object for the renewal of an existing content key.
