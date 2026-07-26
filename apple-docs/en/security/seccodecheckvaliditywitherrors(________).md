---
title: 'SecCodeCheckValidityWithErrors(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccodecheckvaliditywitherrors(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccodecheckvaliditywitherrors(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodecheckvaliditywitherrors%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b2b53220c6a06e50'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCodeCheckValidityWithErrors(_:_:_:_:)

<sub>Function</sub>

Performs dynamic validation of signed code and returns detailed error information in the case of failure.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecCodeCheckValidityWithErrors(_ code: SecCode, _ flags: SecCSFlags, _ requirement: SecRequirement?, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OSStatus
```

## Parameters

- `code` — The code object to be validated.

- `flags` — Optional flags; see [SecCSFlags](seccsflags.md) for possible values. Pass `kSecCSDefaultFlags` for standard behavior.

- `requirement` — A code requirement specifying additional conditions the code must satisfy to be considered valid. Specify `NULL` if you don’t want to impose any additional requirements. Use the [SecRequirementCreateWithString](<secrequirementcreatewithstring(______).md>) or [SecRequirementCreateWithStringAndErrors](<secrequirementcreatewithstringanderrors(________).md>) function to create a code requirement object. See [Code Signing Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005929) for a discussion of code requirements.

- `errors` — On return, if the function call fails and returns a result code other than [errSecSuccess](errsecsuccess.md), points to an error object further describing the nature and circumstances of the failure. Use the [CFErrorCopyUserInfo(_:)](<../corefoundation/cferrorcopyuserinfo(__).md>) function to retrieve the user info dictionary from the error object. See [User Info Dictionary Error Keys](user-info-dictionary-error-keys.md) for possible values. Pass `NULL` if you do not want this information. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Discussion

This function obtains and verifies the signature on the code specified by the code object. It checks the validity of only those sealed components required to establish identity. For guest code, first the function checks the code object’s dynamic validity status as reported by its host, then it ensures that the code object’s host is in turn valid. For all code, it validates the code against a code requirement if one is specified. The call succeeds if all these conditions are satisfactory.

This function is secure against attempts to modify the file system source of the code object.
