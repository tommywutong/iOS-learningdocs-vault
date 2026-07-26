---
title: 'removeContentKeyRecipient(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysession/removecontentkeyrecipient(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/removecontentkeyrecipient(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/removecontentkeyrecipient%28_%3A%29.json'
content_hash: 'sha256:7e316b347a2dab3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# removeContentKeyRecipient(_:)

<sub>Instance Method</sub>

Tells the delegate to remove the specified recipient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeContentKeyRecipient(_ recipient: any AVContentKeyRecipient)
```

## Parameters

- `recipient` — The content key recipient to remove.

## See Also

### Managing content key recipients

- [contentKeyRecipients](contentkeyrecipients.md) — An array of content key recipients.
- [AVContentKeyRecipient](../avcontentkeyrecipient.md) — A protocol for requiring decryption keys for media data.
- [- addContentKeyRecipient:](<addcontentkeyrecipient(__).md>) — Tells the delegate that the specified recipient should have access to the decryption keys loaded with the session.
