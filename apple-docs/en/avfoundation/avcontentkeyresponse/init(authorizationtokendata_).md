---
title: 'init(authorizationTokenData:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeyresponse/init(authorizationtokendata:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyresponse/init(authorizationtokendata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyresponse/init%28authorizationtokendata%3A%29.json'
content_hash: 'sha256:ccd1b4feadd01a9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyResponse](../avcontentkeyresponse.md)

# init(authorizationTokenData:)

<sub>Initializer</sub>

Creates a content key response with an authorization token.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(authorizationTokenData: Data)
```

## Parameters

- `authorizationTokenData` — A data value that contains the authorization token.

## See Also

### Creating new content key responses

- [+ contentKeyResponseWithClearKeyData:initializationVector:](<init(clearkeydata_initializationvector_).md>) — Creates a new key response object for key data and initialization vector sent in the clear.
- [+ contentKeyResponseWithFairPlayStreamingKeyResponseData:](<init(fairplaystreamingkeyresponsedata_).md>) — Creates a content key response with an encrypted key response data blob when FairPlay Streaming is the key delivery method.
