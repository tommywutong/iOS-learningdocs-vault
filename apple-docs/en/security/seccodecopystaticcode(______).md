---
title: 'SecCodeCopyStaticCode(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccodecopystaticcode(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccodecopystaticcode(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodecopystaticcode%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:54ef5ab0bfeaee88'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCodeCopyStaticCode(_:_:_:)

<sub>Function</sub>

Returns a static code object representing the on-disk version of the given running code.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecCodeCopyStaticCode(_ code: SecCode, _ flags: SecCSFlags, _ staticCode: UnsafeMutablePointer<SecStaticCode?>) -> OSStatus
```

## Parameters

- `code` — A valid code object representing code running on the system.

- `flags` — Optional flags; see [SecCSFlags](seccsflags.md) and [Code Signing Architecture Flags](code-signing-architecture-flags.md) for possible values. Pass [kSecCSDefaultFlags](seccsflags/kseccsdefaultflags.md) for standard behavior.

- `staticCode` — On return, a static code object representing the code in the file system that is the origin of the code specified by the `code` parameter.

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Discussion

Use the [SecCodeCopyPath](<seccodecopypath(______).md>) function to get the URL specifying the location on disk of the code represented by a code or static code object.

Many functions in the Code Signing Services API take either a static code object or a code object as an input parameter. For these functions, if you pass in a code reference, the function first translates it to a static code reference in the same manner as the [SecCodeCopyStaticCode](<seccodecopystaticcode(______).md>) function. In each such case, the parameter description documents this behavior.

### Special Considerations

The link established by this function is generally reliable but is not guaranteed to be secure.

## See Also

### Related Documentation

- [SecCodeCopyGuestWithAttributes](<seccodecopyguestwithattributes(________).md>) — Asks a code host to identify one of its guests given the type and value of specific attributes of the guest code.
- [SecCodeCopyHost](<seccodecopyhost(______).md>) — Retrieves the code object for the host of specified guest code.
- [SecCodeCopySelf](<seccodecopyself(____).md>) — Retrieves the code object for the code making the call.
