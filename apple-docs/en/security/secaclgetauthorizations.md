---
title: SecACLGetAuthorizations
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secaclgetauthorizations
source_url: 'https://developer.apple.com/documentation/security/secaclgetauthorizations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaclgetauthorizations.json'
content_hash: 'sha256:abefe187b1f126bc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecACLGetAuthorizations

<sub>Function</sub>

Retrieves the CSSM authorization tags of a given access control list entry.

> [!warning] Deprecated
> Use [SecACLCopyAuthorizations](<secaclcopyauthorizations(__).md>) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecACLGetAuthorizations(SecACLRef acl, CSSM_ACL_AUTHORIZATION_TAG *tags, uint32 *tagCount);
```

## Parameters

- `acl` — An ACL object that identifies the access control list entry from which you wish to retrieve the authorization tags.

- `tags` — A pointer to an array of CSSM authorization tags. You must allocate this array before calling the function. On return, this array contains the authorization tags of the specified ACL entry.

- `tagCount` — On entry, points to the number of elements in the array you passed in the `tags` parameter. On return, points to the number of tags actually returned or, in the case of an overflow, the number of tags required.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

> [!important] Important
> This function is deprecated. Use [SecACLCopyAuthorizations](<secaclcopyauthorizations(__).md>) instead.

An ACL object includes a list of trusted applications (see [SecTrustedApplicationCreateFromPath](<sectrustedapplicationcreatefrompath(____).md>)), the name of the keychain item as it appears in user prompts, the prompt selector flag, and a list of one or more operations to which this ACL object applies. Use this function to retrieve the list of operations for an ACL object. Use the [SecACLCopySimpleContents](secaclcopysimplecontents.md) function to retrieve the other information.

The `SecACLGetAuthorizations` function returns an error if there are more tags to return than the number of elements you allocated in the `tags` array. A 20-element array should suffice for most purposes; however, you can test for the `errSecBufferTooSmall` error and increase the size of the array before calling the function again if necessary. Alternatively, you can call the function with a tag count of `0`, read the value returned in the `tagCount` parameter, and then call the function again using that value.

### Special Considerations

This function is deprecated in macOS 10.7 and later; use [SecACLCopyAuthorizations](<secaclcopyauthorizations(__).md>) instead.
