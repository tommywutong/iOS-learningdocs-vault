---
title: sec_protocol_options_set_peer_authentication_optional
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/sec_protocol_options_set_peer_authentication_optional
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_options_set_peer_authentication_optional'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_options_set_peer_authentication_optional.json'
content_hash: 'sha256:8f8242208bb719c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_options_set_peer_authentication_optional

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
void sec_protocol_options_set_peer_authentication_optional(sec_protocol_options_t options, bool peer_authentication_optional);
```

## Parameters

- `options` — A `sec_protocol_options_t` instance.

- `peer_authentication_optional` — Flag to enable or disable requested peer authentication.

## Discussion

When this is enabled, the endpoint requests the peer certificate, but if none is provided, the endpoint still proceeds with the connection. Default false for servers; always false for clients (clients ignore this option). If peer_authentication_required is set to true via sec_protocol_options_set_peer_authentication_required(), peer_authentication_optional will be disregarded and the peer certificate will be required.
