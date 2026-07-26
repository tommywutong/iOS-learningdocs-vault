---
title: AVContentKeyRecipient
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrecipient
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrecipient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrecipient.json'
content_hash: 'sha256:b0c4e32ce3f0feea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVContentKeyRecipient

<sub>Protocol</sub>

A protocol for requiring decryption keys for media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AVContentKeyRecipient
```

## Relationships

- **Conforming Types**: [AVFragmentedAsset](avfragmentedasset.md), [AVURLAsset](avurlasset.md)

## Topics

### Verifying decryption key requirements

- [mayRequireContentKeysForMediaDataProcessing](avcontentkeyrecipient/mayrequirecontentkeysformediadataprocessing.md) — A Boolean value that indicates whether the recipient requires decryption keys for media data to enable processing.
- [- contentKeySession:didProvideContentKey:](<avcontentkeyrecipient/contentkeysession(__didprovide_).md>) — Tells the recipient that a content key is available.

## See Also

### Managing content key recipients

- [contentKeyRecipients](avcontentkeysession/contentkeyrecipients.md) — An array of content key recipients.
- [- addContentKeyRecipient:](<avcontentkeysession/addcontentkeyrecipient(__).md>) — Tells the delegate that the specified recipient should have access to the decryption keys loaded with the session.
- [- removeContentKeyRecipient:](<avcontentkeysession/removecontentkeyrecipient(__).md>) — Tells the delegate to remove the specified recipient.
