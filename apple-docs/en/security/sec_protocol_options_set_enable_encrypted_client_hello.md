---
title: sec_protocol_options_set_enable_encrypted_client_hello
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/sec_protocol_options_set_enable_encrypted_client_hello
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_set_enable_encrypted_client_hello'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_set_enable_encrypted_client_hello.json'
content_hash: 'sha256:e7aa5e70b30f261e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_set_enable_encrypted_client_hello

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
void sec_protocol_options_set_enable_encrypted_client_hello(sec_protocol_options_t options, bool enable_encrypted_client_hello);
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

## Discussion

For experimental use only. When this is enabled, the Encrypted Client Hello extension will be sent on the Client Hello if TLS 1.3 is among the supported TLS versions. Default false.
