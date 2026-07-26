---
title: 'sec_protocol_metadata_access_supported_signature_algorithms(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_metadata_access_supported_signature_algorithms(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_access_supported_signature_algorithms(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_access_supported_signature_algorithms%28_%3A_%3A%29.json'
content_hash: 'sha256:dec95ee10e23ecc4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_access_supported_signature_algorithms(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_metadata_access_supported_signature_algorithms(_ metadata: sec_protocol_metadata_t, _ handler: @escaping (UInt16) -> Void) -> Bool
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

- `handler` — A block to invoke one or more times, once per signature algorithm advertised by the peer. Each `signature_algorithm` is a TLS SignatureScheme codepoint (the on-the-wire 2-byte value) from the IANA “TLS SignatureScheme” registry — see RFC 8446 §4.2.3.

## Return Value

Returns true if the supported signature list was accessible, false otherwise.

## Discussion

Get the signature algorithms supported by the peer. Clients may call this in response to a challenge block.
