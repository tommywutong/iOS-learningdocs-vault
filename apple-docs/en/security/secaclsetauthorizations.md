---
title: SecACLSetAuthorizations
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secaclsetauthorizations
source_url: 'https://developer.apple.com/documentation/security/secaclsetauthorizations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaclsetauthorizations.json'
content_hash: 'sha256:d2d4b221aba90369'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecACLSetAuthorizations

<sub>Function</sub>

Sets the CSSM authorization tags for a given access control list entry.

> [!warning] Deprecated
> Use [SecACLUpdateAuthorizations](<secaclupdateauthorizations(____).md>) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecACLSetAuthorizations(SecACLRef acl, CSSM_ACL_AUTHORIZATION_TAG *tags, uint32 tagCount);
```

## Parameters

- `acl` — An ACL object that identifies the access control list entry for which you wish to set authorization tags.

- `tags` — An array of CSSM authorization tags.

- `tagCount` — The number of tags in the CSSM authorization tag array.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

> [!important] Important
> This function is deprecated. Use [SecACLUpdateAuthorizations](<secaclupdateauthorizations(____).md>) instead.

An ACL object includes a list of trusted applications (see [SecTrustedApplicationCreateFromPath](<sectrustedapplicationcreatefrompath(____).md>)), the name of the keychain item as it appears in user prompts, the prompt selector flag, and a list of one or more operations to which this ACL object applies. Use this function to set a list of operations for an ACL object, or set the `CSSM_ACL_AUTHORIZATION_ANY` tag to allow all operations. Use the [SecACLSetSimpleContents](secaclsetsimplecontents.md) function to set the other information.

Because an ACL object is always associated with an access object, when you modify an ACL entry, you are modifying the access object as well. There is no need for a separate function to write a modified ACL object back into the access object.

### Special Considerations

This function is deprecated in macOS 10.7 and later; use [SecACLUpdateAuthorizations](<secaclupdateauthorizations(____).md>) instead.
