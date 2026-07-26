---
title: 'processContentKeyRequest(withIdentifier:initializationData:options:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysession/processcontentkeyrequest(withidentifier:initializationdata:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/processcontentkeyrequest(withidentifier:initializationdata:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/processcontentkeyrequest%28withidentifier%3Ainitializationdata%3Aoptions%3A%29.json'
content_hash: 'sha256:cdb8cb6b918cdef4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# processContentKeyRequest(withIdentifier:initializationData:options:)

<sub>Instance Method</sub>

Tells the delegate to start loading the content decryption key with the specified identifier and initialization data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func processContentKeyRequest(withIdentifier identifier: (any Sendable)?, initializationData: Data?, options: [String : any Sendable]? = nil)
```

## Parameters

- `identifier` — The container- and protocol-specific identifier used to obtain a key response.

- `initializationData` — The container- and protocol-specific data used to obtain a key response.

- `options` — No options are currently defined. Set this value to `nil`.

## Discussion

Either the `identifier` or `initializationData` parameters must be non-`nil`. If required by the protocol, both parameters can be non-`nil`.
