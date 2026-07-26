---
title: 'contentKeySession(_:didProvide:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeyrecipient/contentkeysession(_:didprovide:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrecipient/contentkeysession(_:didprovide:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrecipient/contentkeysession%28_%3Adidprovide%3A%29.json'
content_hash: 'sha256:ec37c2dc68932e52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRecipient](../avcontentkeyrecipient.md)

# contentKeySession(_:didProvide:)

<sub>Instance Method</sub>

Tells the recipient that a content key is available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func contentKeySession(_ contentKeySession: AVContentKeySession, didProvide contentKey: AVContentKey)
```

## Parameters

- `contentKeySession` — The current content key session.

- `contentKey` — A content key to use with objects that support manual attachment of keys, such as [CMSampleBuffer](../../coremedia/cmsamplebuffer.md).

## See Also

### Verifying decryption key requirements

- [mayRequireContentKeysForMediaDataProcessing](mayrequirecontentkeysformediadataprocessing.md) — A Boolean value that indicates whether the recipient requires decryption keys for media data to enable processing.
