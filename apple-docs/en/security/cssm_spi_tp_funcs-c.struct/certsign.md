---
title: CertSign
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_spi_tp_funcs-c.struct/certsign
source_url: 'https://developer.apple.com/documentation/security/cssm_spi_tp_funcs-c.struct/certsign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_spi_tp_funcs-c.struct/certsign.json'
content_hash: 'sha256:f8b1a3491fed811f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [cssm_spi_tp_funcs](../cssm_spi_tp_funcs-c.struct.md)

# CertSign

<sub>Instance Property</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(long, long, unsigned long long, const struct cssm_data *, const struct cssm_certgroup *, const struct cssm_tp_verify_context *, struct cssm_tp_verify_context_result *, struct cssm_data *) CertSign;
```
