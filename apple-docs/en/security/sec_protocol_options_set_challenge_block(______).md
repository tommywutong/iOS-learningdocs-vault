---
title: 'sec_protocol_options_set_challenge_block(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_options_set_challenge_block(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_set_challenge_block(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_set_challenge_block%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c2e3d224bcf9f552'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_set_challenge_block(_:_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_set_challenge_block(_ options: sec_protocol_options_t, _ challenge_block: @escaping sec_protocol_challenge_t, _ challenge_queue: dispatch_queue_t)
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

## Discussion

Set the challenge block.

```
 A `sec_protocol_challenge_t` block.
```

```
 A `dispatch_queue_t` on which the challenge block should be called.
```
