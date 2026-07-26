---
title: canBeFulfilledWithAdvisoryKey
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequest/canbefulfilledwithadvisorykey
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/canbefulfilledwithadvisorykey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/canbefulfilledwithadvisorykey.json'
content_hash: 'sha256:c70c71fbf5cb4410'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# canBeFulfilledWithAdvisoryKey

<sub>Instance Property</sub>

Indicates whether this key request was initiated for an advisory key.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var canBeFulfilledWithAdvisoryKey: Bool { get }
```

## Discussion

This property is set to true when: 1. Advisory key loading is enabled on the parent AVContentKeySession 2. The key was previously loaded as an advisory key and cached by FairPlay 3. A subsequent request for the same key is made

When `canBeFulfilledWithAdvisoryKey` is true and `makeStreamingContentKeyRequestData` returns nil for the key request data, this indicates FairPlay has already cached the key. No request to the key server for a key response is necessary, and the application should simply return from the completion handler.

This property should be checked in the completion handler of `makeStreamingContentKeyRequestData(forApp:contentIdentifier:options:completionHandler:)` whenever the key request data is nil to distinguish advisory keys from actual errors.
