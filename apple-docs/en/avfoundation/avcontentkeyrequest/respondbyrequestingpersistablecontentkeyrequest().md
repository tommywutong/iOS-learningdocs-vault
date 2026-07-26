---
title: respondByRequestingPersistableContentKeyRequest()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+（11.2 起废弃）, iPadOS 10.3+（11.2 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequest()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequest()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequest%28%29.json'
content_hash: 'sha256:358c74fd01a9016f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# respondByRequestingPersistableContentKeyRequest()

<sub>Instance Method</sub>

Tells the receiver that the app requires a persistable content key request object for processing.

> [!warning] Deprecated
> Use [- respondByRequestingPersistableContentKeyRequestAndReturnError:](<respondbyrequestingpersistablecontentkeyrequestandreturnerror().md>).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func respondByRequestingPersistableContentKeyRequest()
```

## Discussion

To create a key that persists across multiple playback sessions, use this method to request an [AVPersistableContentKeyRequest](../avpersistablecontentkeyrequest.md) object. If the underlying protocol supports persistable content keys, the delegate receives a persistable content key request via the [- contentKeySession:didProvidePersistableContentKeyRequest:](<../avcontentkeysessiondelegate/contentkeysession(__didprovide_)-2wdgz.md>) method. An [internalInconsistencyException](../../foundation/nsexceptionname/internalinconsistencyexception.md) is returned if your delegate does not respond to [- contentKeySession:didProvidePersistableContentKeyRequest:](<../avcontentkeysessiondelegate/contentkeysession(__didprovide_)-2wdgz.md>).

## See Also

### Responding to the content key request

- [- processContentKeyResponse:](<processcontentkeyresponse(__).md>) — Sends the specified content key response to the receiver for processing.
- [- processContentKeyResponseError:](<processcontentkeyresponseerror(__).md>) — Tells the receiver that the app was unable to obtain a content key response.
