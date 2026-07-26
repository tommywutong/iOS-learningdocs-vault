---
title: CrlSign
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_spi_tp_funcs-c.struct/crlsign
source_url: 'https://developer.apple.com/documentation/security/cssm_spi_tp_funcs-c.struct/crlsign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_spi_tp_funcs-c.struct/crlsign.json'
content_hash: 'sha256:5f99d9f5ab297f4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [cssm_spi_tp_funcs](../cssm_spi_tp_funcs-c.struct.md)

# CrlSign

<sub>Instance Property</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(long, long, unsigned long long, const struct cssm_encoded_crl *, const struct cssm_certgroup *, const struct cssm_tp_verify_context *, struct cssm_tp_verify_context_result *, struct cssm_data *) CrlSign;
```
