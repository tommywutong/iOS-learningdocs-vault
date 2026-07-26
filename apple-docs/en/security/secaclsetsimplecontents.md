---
title: SecACLSetSimpleContents
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secaclsetsimplecontents
source_url: 'https://developer.apple.com/documentation/security/secaclsetsimplecontents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaclsetsimplecontents.json'
content_hash: 'sha256:d3d458ecbab3f902'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecACLSetSimpleContents

<sub>Function</sub>

Sets the application list, description, and prompt selector for a given access control list entry.

> [!warning] Deprecated
> Use [SecACLSetContents](<secaclsetcontents(________).md>) instead.

<sub>macOS</sub>

```objc
OSStatus SecACLSetSimpleContents(SecACLRef acl, CFArrayRef applicationList, CFStringRef description, const CSSM_ACL_KEYCHAIN_PROMPT_SELECTOR *promptSelector);
```

## Parameters

- `acl` — An ACL object that identifies the access control list entry.

- `applicationList` — An array of trusted application objects (that is, [SecTrustedApplication](sectrustedapplication.md) instances) identifying applications that are allowed access to the keychain item without user confirmation. Use the [SecTrustedApplicationCreateFromPath](<sectrustedapplicationcreatefrompath(____).md>) function to create trusted application objects. If you set this parameter to `NULL`, then any application can use this item. If you pass an empty array, then all applications are treated as untrusted.

- `description` — The name of the keychain item that appears in the dialog box when the user is prompted for permission to use the item. Note that this name is not necessarily the same as the one displayed for the item by the Keychain Access application.

- `promptSelector` — The prompt selector flag for the given access control list entry. Set the `CSSM_ACL_KEYCHAIN_PROMPT_REQUIRE_PASSPHRASE` bit to have the user prompted for the keychain password each time a non-trusted application attempts to access this item, even if the keychain is already unlocked.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

> [!important] Important
> This function is deprecated. Use [SecACLSetContents](<secaclsetcontents(________).md>) instead.

Because an ACL object is always associated with an access object, when you modify an ACL entry, you are modifying the access object as well. There is no need for a separate function to write a modified ACL object back into the access object.

Use the [SecACLGetAuthorizations](secaclgetauthorizations.md) function to get the list of operations for an ACL object.

### Special Considerations

This function is deprecated in macOS 10.7 and later; use [SecACLSetContents](<secaclsetcontents(________).md>) instead.
