---
title: 'sec_protocol_options_are_equal(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_protocol_options_are_equal(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_are_equal(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_are_equal%28_%3A_%3A%29.json'
content_hash: 'sha256:5bc6b9d0c0b4a526'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_are_equal(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_protocol_options_are_equal(_ optionsA: sec_protocol_options_t, _ optionsB: sec_protocol_options_t) -> Bool
```

## Parameters

- `optionsA` — A `sec_protocol_options_t` instance.

- `optionsB` — A `sec_protocol_options_t` instance.

## Return Value

True if equal, and false otherwise.

## Discussion

Compare two `sec_protocol_options_t` instances.
