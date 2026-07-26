---
title: 'addContentKeyRecipient(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysession/addcontentkeyrecipient(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/addcontentkeyrecipient(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/addcontentkeyrecipient%28_%3A%29.json'
content_hash: 'sha256:cac634ed2a69c68b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# addContentKeyRecipient(_:)

<sub>Instance Method</sub>

Tells the delegate that the specified recipient should have access to the decryption keys loaded with the session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addContentKeyRecipient(_ recipient: any AVContentKeyRecipient)
```

## Parameters

- `recipient` — The content key recipient to use for the session.

## Discussion

Don’t add a recipient to a session that has expired or had already begun to process media data.

## See Also

### Managing content key recipients

- [contentKeyRecipients](contentkeyrecipients.md) — An array of content key recipients.
- [AVContentKeyRecipient](../avcontentkeyrecipient.md) — A protocol for requiring decryption keys for media data.
- [- removeContentKeyRecipient:](<removecontentkeyrecipient(__).md>) — Tells the delegate to remove the specified recipient.
