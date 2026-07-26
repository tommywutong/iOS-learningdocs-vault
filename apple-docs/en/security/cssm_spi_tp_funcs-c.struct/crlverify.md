---
title: CrlVerify
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_spi_tp_funcs-c.struct/crlverify
source_url: 'https://developer.apple.com/documentation/security/cssm_spi_tp_funcs-c.struct/crlverify'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_spi_tp_funcs-c.struct/crlverify.json'
content_hash: 'sha256:47b092c7ad470948'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [cssm_spi_tp_funcs](../cssm_spi_tp_funcs-c.struct.md)

# CrlVerify

<sub>Instance Property</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(long, long, long, const struct cssm_encoded_crl *, const struct cssm_certgroup *, const struct cssm_tp_verify_context *, struct cssm_tp_verify_context_result *) CrlVerify;
```
