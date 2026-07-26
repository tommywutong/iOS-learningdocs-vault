---
title: ASN.1
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/asn-1
source_url: 'https://developer.apple.com/documentation/security/asn-1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/asn-1.json'
content_hash: 'sha256:b30b8fe56159db2e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# ASN.1

<sub>API Collection</sub>

Encode and decode Distinguished Encoding Rules (DER) and Basic Encoding Rules (BER) data streams.

## Overview

You use an ASN.1 coder to encode and decode both DER and BER data streams based on templates that you supply, which in turn are based upon ASN.1 specifications. You must import this API explicitly:

**Swift**

```swift
import Security.SecAsn1Coder
import Security.SecAsn1Templates
```

**Objective-C**

```objc
#import <Security/SecAsn1Coder.h>
#import <Security/SecAsn1Templates.h>
```

## Topics

### Encoding

- [SecAsn1Item](secasn1item.md) — A structure holding DER encoded data. _(deprecated)_
- [SecAsn1Template_struct](secasn1template_struct.md) — A structure that defines one element of a BER or DER encoding. _(deprecated)_
- [SecAsn1Template_struct](secasn1template_struct.md) — A structure that defines one element of a BER or DER encoding. _(deprecated)_
- [SecAsn1TemplateChooser](secasn1templatechooser.md) — Dynamically provides the sub-template to use during encode or decode. _(deprecated)_
- [SecAsn1TemplateChooserPtr](secasn1templatechooserptr.md) — A pointer to the template chooser function. _(deprecated)_
- [Type Tags](type-tags.md) — Recognize BER and DER values for ASN.1 identifier octets.

### OID Comparison

- [SecAsn1Oid](secasn1oid.md) — An object identifier. _(deprecated)_

### Public Key Info

- [SecAsn1AlgId](secasn1algid.md) — A structure identifying an ASN.1 algorithm by its OID, and its corresponding parameters. _(deprecated)_
- [SecAsn1PubKeyInfo](secasn1pubkeyinfo.md) — A structure containing a public key and its associated algorithm. _(deprecated)_
