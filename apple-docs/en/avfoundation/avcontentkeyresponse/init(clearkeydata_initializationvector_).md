---
title: 'init(clearKeyData:initializationVector:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeyresponse/init(clearkeydata:initializationvector:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyresponse/init(clearkeydata:initializationvector:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyresponse/init%28clearkeydata%3Ainitializationvector%3A%29.json'
content_hash: 'sha256:281f5578ed23d22a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyResponse](../avcontentkeyresponse.md)

# init(clearKeyData:initializationVector:)

<sub>Initializer</sub>

Creates a new key response object for key data and initialization vector sent in the clear.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(clearKeyData keyData: Data, initializationVector: Data?)
```

## Parameters

- `keyData` — The key used for decrypting content.

- `initializationVector` — The initialization vector used for decrypting content. This value is `nil` when the initialization vector is contained in the media to be decrypted.

## Return Value

Returns a new [AVContentKeyResponse](../avcontentkeyresponse.md) object to decrypt content.

## Discussion

Use the results of this initializer when the content key session creates a key request using the [AVContentKeySystemClearKey](../avcontentkeysystem/clearkey.md) parameter. The results are then passed to the [- processContentKeyResponse:](<../avcontentkeyrequest/processcontentkeyresponse(__).md>) method to supply the decrypter with key data.

## See Also

### Creating new content key responses

- [+ contentKeyResponseWithFairPlayStreamingKeyResponseData:](<init(fairplaystreamingkeyresponsedata_).md>) — Creates a content key response with an encrypted key response data blob when FairPlay Streaming is the key delivery method.
- [+ contentKeyResponseWithAuthorizationTokenData:](<init(authorizationtokendata_).md>) — Creates a content key response with an authorization token.
