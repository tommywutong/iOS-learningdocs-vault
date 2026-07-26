---
title: SecAccessOwnerType Values
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: [Mac Catalyst 16.0+, macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secaccessownertype-values
source_url: 'https://developer.apple.com/documentation/security/secaccessownertype-values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccessownertype-values.json'
content_hash: 'sha256:8e1f1362df8121f9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Keychain services](keychain-services.md) · [Access Control Lists](access-control-lists.md)

# SecAccessOwnerType Values

<sub>API Collection</sub>

Flags that enable you to configure ACL ownership.

## Topics

### Constants

- [kSecUseOnlyUID](ksecuseonlyuid.md) — The access control list should be owned by the user matching the specified user ID parameter.
- [kSecUseOnlyGID](ksecuseonlygid.md) — The access control list should be owned by users that are members of a group matching the specified group ID parameter.
- [kSecHonorRoot](ksechonorroot.md) — The access control list should treat the root user as a typical user for ownership purposes.
- [kSecMatchBits](ksecmatchbits.md) — The access control list should be owned by users whose ID matches the specified user ID or who are members of a group whose ID matches the specified group ID parameter.
