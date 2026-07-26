---
title: CMSSignerStatus.invalidIndex
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/cmssignerstatus/invalidindex
source_url: 'https://developer.apple.com/documentation/security/cmssignerstatus/invalidindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmssignerstatus/invalidindex.json'
content_hash: 'sha256:8375f7c19b31ed52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [CMSSignerStatus](../cmssignerstatus.md)

# CMSSignerStatus.invalidIndex

<sub>Case</sub>

The specified value for the signer index (`signerIndex` parameter) is greater than the number of signers of the message minus one (`signerIndex > (numSigners – 1)`).

<sub>Mac Catalyst, macOS</sub>

```swift
case invalidIndex
```
