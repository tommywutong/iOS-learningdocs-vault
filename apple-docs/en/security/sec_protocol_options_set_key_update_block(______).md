---
title: 'sec_protocol_options_set_key_update_block(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_options_set_key_update_block(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_set_key_update_block(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_set_key_update_block%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a4dcfaba23e7eaf5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_set_key_update_block(_:_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_set_key_update_block(_ options: sec_protocol_options_t, _ key_update_block: @escaping sec_protocol_key_update_t, _ key_update_queue: dispatch_queue_t)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `key_update_block` — A `sec_protocol_key_update_t` block.

## Discussion

Set the key update block.

```
 A `dispatch_queue_t` on which the key update block should be called.
```
