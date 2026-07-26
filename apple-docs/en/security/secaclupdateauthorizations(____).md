---
title: 'SecACLUpdateAuthorizations(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/secaclupdateauthorizations(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secaclupdateauthorizations(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaclupdateauthorizations%28_%3A_%3A%29.json'
content_hash: 'sha256:dd63e235a0eb9973'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecACLUpdateAuthorizations(_:_:)

<sub>Function</sub>

Sets the authorization tags for a given ACL.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecACLUpdateAuthorizations(_ acl: SecACL, _ authorizations: CFArray) -> OSStatus
```

## Parameters

- `acl` — An ACL object that identifies the access control list entry for which you wish to set authorization tags.

- `authorizations` — An array of authorization tags. See `CSSM_ACL_AUTHORIZATION_TAG` for details.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

An ACL entry includes a list of trusted apps, the name of the keychain item as it appears in user prompts, the prompt selector flag, and a list of one or more operations to which this ACL entry applies. Use this method to set a list of operations for an ACL entry, or set the [kSecACLAuthorizationAny](ksecaclauthorizationany.md) tag to allow all operations. Use the [SecACLSetContents](<secaclsetcontents(________).md>) method to set the other information.

Because an ACL entry is always associated with an access instance, when you modify an entry, you are modifying the access instance as well.
