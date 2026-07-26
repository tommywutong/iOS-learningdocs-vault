---
title: 'sec_protocol_options_set_pre_shared_key_selection_block(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_options_set_pre_shared_key_selection_block(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_set_pre_shared_key_selection_block(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_set_pre_shared_key_selection_block%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:bea98e9311e7501e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_set_pre_shared_key_selection_block(_:_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_set_pre_shared_key_selection_block(_ options: sec_protocol_options_t, _ psk_selection_block: @escaping sec_protocol_pre_shared_key_selection_t, _ psk_selection_queue: dispatch_queue_t)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `psk_selection_block` — A `sec_protocol_pre_shared_key_selection_t` block.

## Discussion

Set the PSK selection block.

```
 A `dispatch_queue_t` on which the PSK selection block should be called.
```
