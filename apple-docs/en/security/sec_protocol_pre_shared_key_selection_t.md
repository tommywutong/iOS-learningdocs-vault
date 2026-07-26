---
title: sec_protocol_pre_shared_key_selection_t
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sec_protocol_pre_shared_key_selection_t
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_pre_shared_key_selection_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_pre_shared_key_selection_t.json'
content_hash: 'sha256:279c54601e97697f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_pre_shared_key_selection_t

<sub>Type Alias</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias sec_protocol_pre_shared_key_selection_t = (sec_protocol_metadata_t, dispatch_data_t?, @escaping sec_protocol_pre_shared_key_selection_complete_t) -> Void
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

- `psk_identity_hint` — A `dispatch_data_t` object carrying the peer’s (optional) PSK identity hint.

- `complete` — A `sec_protocol_pre_shared_key_selection_complete_t` block to be invoked when PSK selection is complete.

## Discussion

Block to be invoked when the client must choose a PSK identity given a hint from its peer.
