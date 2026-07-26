---
title: 'sec_protocol_metadata_challenge_parameters_are_equal(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_metadata_challenge_parameters_are_equal(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_metadata_challenge_parameters_are_equal(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_metadata_challenge_parameters_are_equal%28_%3A_%3A%29.json'
content_hash: 'sha256:0c0c5ddc326a3eb5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_metadata_challenge_parameters_are_equal(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_metadata_challenge_parameters_are_equal(_ metadataA: sec_protocol_metadata_t, _ metadataB: sec_protocol_metadata_t) -> Bool
```

## Parameters

- `metadataA` — A `sec_protocol_metadata_t` instance.

- `metadataB` — A `sec_protocol_metadata_t` instance.

## Return Value

Returns true if both metadata values have the same challenge parameters.

## Discussion

Compare challenge-relevant information for two `sec_protocol_metadata` instances.

```
 This comparison includes all information relevant to a challenge request, including:
 distinguished names, signature algorithms, and supported certificate types.
 See Section 7.4.4 of RFC5246 for more details.
```
