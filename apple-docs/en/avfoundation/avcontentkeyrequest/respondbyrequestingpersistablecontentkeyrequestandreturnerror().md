---
title: respondByRequestingPersistableContentKeyRequestAndReturnError()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.2+, iPadOS 11.2+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequestandreturnerror()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequestandreturnerror()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequestandreturnerror%28%29.json'
content_hash: 'sha256:0dbfa6cc64a4daa0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# respondByRequestingPersistableContentKeyRequestAndReturnError()

<sub>Instance Method</sub>

Tells the receiver that the app requires a persistable content key request object for processing.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func respondByRequestingPersistableContentKeyRequestAndReturnError() throws
```

<sub>macOS, tvOS, visionOS, watchOS</sub>

```swift
func respondByRequestingPersistableContentKeyRequest() throws
```

## Discussion

To create a key that persists across multiple playback sessions, use this method to request an [AVPersistableContentKeyRequest](../avpersistablecontentkeyrequest.md) object. If the underlying protocol supports persistable content keys, the delegate receives a persistable content key request via the [- contentKeySession:didProvidePersistableContentKeyRequest:](<../avcontentkeysessiondelegate/contentkeysession(__didprovide_)-2wdgz.md>) method. An [internalInconsistencyException](../../foundation/nsexceptionname/internalinconsistencyexception.md) is returned if your delegate does not respond to [- contentKeySession:didProvidePersistableContentKeyRequest:](<../avcontentkeysessiondelegate/contentkeysession(__didprovide_)-2wdgz.md>).
