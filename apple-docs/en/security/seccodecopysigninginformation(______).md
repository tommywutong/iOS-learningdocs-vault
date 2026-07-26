---
title: 'SecCodeCopySigningInformation(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccodecopysigninginformation(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccodecopysigninginformation(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodecopysigninginformation%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:dd90e111c2199b28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCodeCopySigningInformation(_:_:_:)

<sub>Function</sub>

Retrieves various pieces of information from a code signature.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecCodeCopySigningInformation(_ code: SecStaticCode, _ flags: SecCSFlags, _ information: UnsafeMutablePointer<CFDictionary?>) -> OSStatus
```

## Parameters

- `code` — The code or static code object from whose signature you wish to retrieve information. If you provide a code object, the function processes it in the same manner as the [SecCodeCopyStaticCode](<seccodecopystaticcode(______).md>) function—that is, the static code signing information is obtained from the signature on disk. Note that dynamic information ([kSecCSDynamicInformation](kseccsdynamicinformation.md)) can be obtained only for a code object, not for a static code object.

- `flags` — Specify any or all of the flags in [Code Signing Information Flags](code-signing-information-flags.md) to select what information to return. A basic set of values is returned regardless; specify [kSecCSDefaultFlags](seccsflags/kseccsdefaultflags.md) for just those.

- `information` — On return, a dictionary containing information about the code. The contents of the dictionary depend on the flags you pass in the `flags` parameter. Regardless of flags, the [kSecCodeInfoIdentifier](kseccodeinfoidentifier.md) key is always present if the code is signed and always absent if the code is unsigned. See [Signing Information Dictionary Keys](signing-information-dictionary-keys.md) for descriptions of the dictionary keys.  In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Discussion

The amount and detail level of the data returned is controlled by the flags passed to the call.

If the code exists but is not signed, this function call succeeds and returns a dictionary that does not contain the [kSecCodeInfoIdentifier](kseccodeinfoidentifier.md) key. This is the recommended way to check quickly whether code is signed if that is the only information you need. However, note that this function does not validate the signature.

If the signing data for the code is corrupt or invalid, this function may fail or it may return partial data. To ensure that only valid data is returned (and errors are raised for invalid data), you must successfully call the [SecCodeCheckValidity](<seccodecheckvalidity(______).md>) or [SecCodeCheckValidityWithErrors](<seccodecheckvaliditywitherrors(________).md>) function before calling [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>).

### Special Considerations

Some of the objects returned in the information dictionary are (retained) “live” API objects used by the code signing infrastructure. Making changes to these objects is unsupported and may cause subsequent code signing operations on the affected code to behave in undefined ways.

## See Also

### Related Documentation

- [SecCodeCopyDesignatedRequirement](<seccodecopydesignatedrequirement(______).md>) — Retrieves the designated code requirement of signed code.
- [SecCodeCopyPath](<seccodecopypath(______).md>) — Retrieves the location on disk of signed code, given a code or static code object.
