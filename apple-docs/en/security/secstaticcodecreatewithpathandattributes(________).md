---
title: 'SecStaticCodeCreateWithPathAndAttributes(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secstaticcodecreatewithpathandattributes(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secstaticcodecreatewithpathandattributes(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secstaticcodecreatewithpathandattributes%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4fd08fc8968c1ae9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecStaticCodeCreateWithPathAndAttributes(_:_:_:_:)

<sub>Function</sub>

Creates a static code object representing the code at a specified file system path using an attributes dictionary.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecStaticCodeCreateWithPathAndAttributes(_ path: CFURL, _ flags: SecCSFlags, _ attributes: CFDictionary, _ staticCode: UnsafeMutablePointer<SecStaticCode?>) -> OSStatus
```

## Parameters

- `path` — A URL identifying the location on disk of the code for which you want a static code object. For bundles, pass a URL to the root directory of the bundle. For single files, pass a URL to the file. If you pass a URL to the main executable of a bundle, the bundle as a whole is generally recognized. Only absolute paths should be used.

- `flags` — Optional flags; see [SecCSFlags](seccsflags.md) for possible values. Pass [kSecCSDefaultFlags](seccsflags/kseccsdefaultflags.md) for standard behavior.

- `attributes` — A [CFDictionary](../corefoundation/cfdictionary.md) containing additional attributes of the requested code. Possible values are defined in [Code Attributes](code-attributes.md).

- `staticCode` — On return, the static code object representing the code you specified in the `path` parameter.

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Discussion

A static code object is not inherently linked to running code in the system.

It is possible to create a static code object from unsigned code. Although most uses of such an object cause the function to fail and return the result code [errSecCSUnsigned](errseccsunsigned.md) error, you can call the [SecCodeCopyPath](<seccodecopypath(______).md>) and [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) functions for such objects.

## See Also

### Related Documentation

- [SecCodeCopyPath](<seccodecopypath(______).md>) — Retrieves the location on disk of signed code, given a code or static code object.
- [SecCodeCopyStaticCode](<seccodecopystaticcode(______).md>) — Returns a static code object representing the on-disk version of the given running code.
