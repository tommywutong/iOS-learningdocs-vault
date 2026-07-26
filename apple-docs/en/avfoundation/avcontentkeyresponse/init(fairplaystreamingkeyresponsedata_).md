---
title: 'init(fairPlayStreamingKeyResponseData:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeyresponse/init(fairplaystreamingkeyresponsedata:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyresponse/init(fairplaystreamingkeyresponsedata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyresponse/init%28fairplaystreamingkeyresponsedata%3A%29.json'
content_hash: 'sha256:91f14b3ae12376f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyResponse](../avcontentkeyresponse.md)

# init(fairPlayStreamingKeyResponseData:)

<sub>Initializer</sub>

Creates a content key response with an encrypted key response data blob when FairPlay Streaming is the key delivery method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(fairPlayStreamingKeyResponseData keyResponseData: Data)
```

## Parameters

- `keyResponseData` — The key data from the FairPlay Streaming key server.

## Return Value

Returns a new [AVContentKeyResponse](../avcontentkeyresponse.md) object to decrypt content.

## Discussion

Use the results of this initializer when the content key session creates a key request using the [AVContentKeySystemFairPlayStreaming](../avcontentkeysystem/fairplaystreaming.md) parameter. The results are then passed to the [- processContentKeyResponse:](<../avcontentkeyrequest/processcontentkeyresponse(__).md>) method to supply the decrypter with key data.

## See Also

### Creating new content key responses

- [+ contentKeyResponseWithClearKeyData:initializationVector:](<init(clearkeydata_initializationvector_).md>) — Creates a new key response object for key data and initialization vector sent in the clear.
- [+ contentKeyResponseWithAuthorizationTokenData:](<init(authorizationtokendata_).md>) — Creates a content key response with an authorization token.
