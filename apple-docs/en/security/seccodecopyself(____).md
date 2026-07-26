---
title: 'SecCodeCopySelf(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccodecopyself(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccodecopyself(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodecopyself%28_%3A_%3A%29.json'
content_hash: 'sha256:dab67b4d02860526'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCodeCopySelf(_:_:)

<sub>Function</sub>

Retrieves the code object for the code making the call.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecCodeCopySelf(_ flags: SecCSFlags, _ self: UnsafeMutablePointer<SecCode?>) -> OSStatus
```

## Parameters

- `flags` — Optional flags; see [SecCSFlags](seccsflags.md) for possible values. Pass [kSecCSDefaultFlags](seccsflags/kseccsdefaultflags.md) for standard behavior.

- `self` — On return, a code object representing the caller.

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Discussion

A code object (that is, an object of type [SecCode](seccode.md)) represents code that is running on the system. The code can be a UNIX process, a script, an applet, a widget, or any other separately-identifiable code. You can use the code object returned by this function as input to other functions in the Code Signing Services API. This function returns a code object for the code that calls it regardless of whether the code is signed. Call the [SecCodeCheckValidity](<seccodecheckvalidity(______).md>) or [SecCodeCheckValidityWithErrors](<seccodecheckvaliditywitherrors(________).md>) function to determine whether the code has a valid signature.

If the code calling this function is either a dedicated host or has called the [SecHostSelectGuest](sechostselectguest.md) function, then the host is considered to be acting as a proxy for its dedicated or selected guest and the [SecCodeCopySelf](<seccodecopyself(____).md>) function returns a code object for that guest.  See [kSecCSDedicatedHost](kseccsdedicatedhost.md) for a discussion of dedicated hosts.

## See Also

### Related Documentation

- [SecCodeCopyGuestWithAttributes](<seccodecopyguestwithattributes(________).md>) — Asks a code host to identify one of its guests given the type and value of specific attributes of the guest code.
- [SecCodeCopyHost](<seccodecopyhost(______).md>) — Retrieves the code object for the host of specified guest code.
- [SecCodeCopyStaticCode](<seccodecopystaticcode(______).md>) — Returns a static code object representing the on-disk version of the given running code.
