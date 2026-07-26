---
title: sec_protocol_options_set_quic_use_legacy_codepoint
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/sec_protocol_options_set_quic_use_legacy_codepoint
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_set_quic_use_legacy_codepoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_set_quic_use_legacy_codepoint.json'
content_hash: 'sha256:406e1239f8a81b1d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_set_quic_use_legacy_codepoint

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
void sec_protocol_options_set_quic_use_legacy_codepoint(sec_protocol_options_t options, bool quic_use_legacy_codepoint);
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `quic_use_legacy_codepoint` — A boolean to enable/disable the legacy codepoint.

## Discussion

Set QUIC to use the legacy codepoint. Defaults to true.
