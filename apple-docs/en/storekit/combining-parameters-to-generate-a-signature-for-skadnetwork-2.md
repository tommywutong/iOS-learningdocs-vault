---
title: Combining parameters to generate a signature for SKAdNetwork 2
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/combining-parameters-to-generate-a-signature-for-skadnetwork-2
source_url: 'https://developer.apple.com/documentation/storekit/combining-parameters-to-generate-a-signature-for-skadnetwork-2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/combining-parameters-to-generate-a-signature-for-skadnetwork-2.json'
content_hash: 'sha256:555bb6c32e96edca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [Ad network attribution](ad-network-attribution.md) · [SKAdNetwork](skadnetwork.md) · [Generating the signature to validate StoreKit-rendered ads](generating-the-signature-to-validate-storekit-rendered-ads.md)

# Combining parameters to generate a signature for SKAdNetwork 2

<sub>Article</sub>

Generate signatures to sign your ad with version 2.

## Overview

To generate the signature, first combine the values of [Ad network install-validation keys](ad-network-install-validation-keys.md) for the version 2.

> [!important] Important
> Lowercase the string representation of the nonce: [SKStoreProductParameterAdNetworkNonce](skstoreproductparameteradnetworknonce.md). Failing to do so results in an invalid signature. Only ads with valid signatures can get ad attributions.

Strings for version 2 and earlier don’t include a `fidelity-type` parameter. For version 2, combine the values into a UTF-8 string with an invisible separator (`‘\u2063’`) between them, in the exact order shown:

Listing 1. Parameter values combined, in order, for version 2.

```javascript
version + '\u2063' + ad-network-id + '\u2063' + campaign-id + '\u2063' + itunes-item-id + '\u2063' + nonce + '\u2063' + source-app-id + '\u2063' + timestamp

```

## See Also

### Signatures for SKAdNetwork 1, 2, and 2.2–3

- [Combining parameters to generate signatures for SKAdNetwork 2.2 and 3](combining-parameters-to-generate-signatures-for-skadnetwork-2-2-and-3.md) — Generate signatures to sign your ad with versions 2.2 and 3.
- [Combining parameters to generate a signature for SKAdNetwork 1](combining-parameters-to-generate-a-signature-for-skadnetwork-1.md) — Generate signatures for apps compiled with earlier SDKs.
