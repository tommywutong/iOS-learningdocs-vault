---
title: 'SecCodeCopyPath(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccodecopypath(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccodecopypath(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodecopypath%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8c6ac1742ae77dae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCodeCopyPath(_:_:_:)

<sub>Function</sub>

Retrieves the location on disk of signed code, given a code or static code object.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecCodeCopyPath(_ staticCode: SecStaticCode, _ flags: SecCSFlags, _ path: UnsafeMutablePointer<CFURL?>) -> OSStatus
```

## Parameters

- `staticCode` — The code or static code object whose code you wish to locate. If you provide a code object, the function processes it in the same manner as the  [SecCodeCopyStaticCode](<seccodecopystaticcode(______).md>) function.

- `flags` — Optional flags; see [SecCSFlags](seccsflags.md) for possible values. Pass [kSecCSDefaultFlags](seccsflags/kseccsdefaultflags.md) for standard behavior.

- `path` — On return, provides a URL identifying the location on disk of the code or static code object. For single files, the URL points to the file. For bundles, it points to the directory containing the entire bundle. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## See Also

### Related Documentation

- [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) — Retrieves various pieces of information from a code signature.
