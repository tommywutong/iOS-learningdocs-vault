---
title: 'bonjour(_:domain:includeTxtRecord:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/browserprovider/bonjour(_:domain:includetxtrecord:)'
source_url: 'https://developer.apple.com/documentation/network/browserprovider/bonjour(_:domain:includetxtrecord:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/browserprovider/bonjour%28_%3Adomain%3Aincludetxtrecord%3A%29.json'
content_hash: 'sha256:8632ca6c23169374'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [BrowserProvider](../browserprovider.md)

# bonjour(_:domain:includeTxtRecord:)

<sub>Type Method</sub>

Create a Bonjour browser provider used to browse for Bonjour services.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func bonjour(_ type: String, domain: String? = nil, includeTxtRecord: Bool = false) -> Bonjour
```

## Parameters

- `type` — The Bonjour type to browse for.

- `domain` — Optional Bonjour domain to browse in. If not specified, uses the Bonjour default browse domain, `nil`, which is recommended in most cases.

- `includeTxtRecord` — Boolean specifying whether to query for TXT records.
