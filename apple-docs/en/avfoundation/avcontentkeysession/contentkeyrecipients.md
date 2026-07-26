---
title: contentKeyRecipients
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeysession/contentkeyrecipients
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/contentkeyrecipients'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/contentkeyrecipients.json'
content_hash: 'sha256:be6f7d6a6db4e3b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# contentKeyRecipients

<sub>Instance Property</sub>

An array of content key recipients.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var contentKeyRecipients: [any AVContentKeyRecipient] { get }
```

## See Also

### Managing content key recipients

- [AVContentKeyRecipient](../avcontentkeyrecipient.md) — A protocol for requiring decryption keys for media data.
- [- addContentKeyRecipient:](<addcontentkeyrecipient(__).md>) — Tells the delegate that the specified recipient should have access to the decryption keys loaded with the session.
- [- removeContentKeyRecipient:](<removecontentkeyrecipient(__).md>) — Tells the delegate to remove the specified recipient.
