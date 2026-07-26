---
title: 'CMSDecoderSetSearchKeychain(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（10.13 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/cmsdecodersetsearchkeychain(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecodersetsearchkeychain(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecodersetsearchkeychain%28_%3A_%3A%29.json'
content_hash: 'sha256:da7ffa46bfeaf960'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderSetSearchKeychain(_:_:)

<sub>Function</sub>

Specifies the keychains to search for intermediate certificates to be used in verifying a signed message’s signer certificates.

<sub>macOS</sub>

```swift
func CMSDecoderSetSearchKeychain(_ cmsDecoder: CMSDecoder, _ keychainOrArray: CFTypeRef) -> OSStatus
```

## Parameters

- `cmsDecoder` — The CMSDecoder reference returned by the `CMSDecoderCreate` function.

- `keychainOrArray` — Either a single keychain to search, specified as a keychain object (type `SecKeychainRef`), or a set of keychains specified as a `CFArray` of keychain objects. If you specify an empty `CFArrayRef`, no keychains are searched for intermediate certificates.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

If you don’t call this function, the decoder uses the default keychain search list to search for intermediate certificates.

If you do call this function, you must call it before you call the `CMSDecoderCopySignerStatus` function.

## See Also

### Related Documentation

- [CMSDecoderCreate](<cmsdecodercreate(__).md>) — Creates a CMSDecoder reference.
