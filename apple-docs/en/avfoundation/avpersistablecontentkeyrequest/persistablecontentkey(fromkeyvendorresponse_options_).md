---
title: 'persistableContentKey(fromKeyVendorResponse:options:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avpersistablecontentkeyrequest/persistablecontentkey(fromkeyvendorresponse:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avpersistablecontentkeyrequest/persistablecontentkey(fromkeyvendorresponse:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpersistablecontentkeyrequest/persistablecontentkey%28fromkeyvendorresponse%3Aoptions%3A%29.json'
content_hash: 'sha256:65d855bf734d1d13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPersistableContentKeyRequest](../avpersistablecontentkeyrequest.md)

# persistableContentKey(fromKeyVendorResponse:options:)

<sub>Instance Method</sub>

Creates a persistable content key from the content key context data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func persistableContentKey(fromKeyVendorResponse keyVendorResponse: Data, options: [String : Any]? = nil) throws -> Data
```

## Parameters

- `keyVendorResponse` — The response returned from the key vendor.

- `options` — Additional information required to obtain the persistable content key. The value of this parameter is `nil` when no additional information is required.

## Return Value

Returns a data object that contains the persistable content key.
