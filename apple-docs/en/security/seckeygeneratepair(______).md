---
title: 'SecKeyGeneratePair(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.7+（12.0 起废弃）, tvOS 4.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeygeneratepair(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeygeneratepair(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeygeneratepair%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:edb64c4c2b8e5c38'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyGeneratePair(_:_:_:)

<sub>Function</sub>

Creates an asymmetric key pair.

> [!warning] Deprecated
> Use SecKeyCreateRandomKey

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyGeneratePair(_ parameters: CFDictionary, _ publicKey: UnsafeMutablePointer<SecKey?>?, _ privateKey: UnsafeMutablePointer<SecKey?>?) -> OSStatus
```

## Parameters

- `parameters` — A dictionary of key-value pairs that specify the type of keys to be generated.

- `publicKey` — On return, points to the keychain item object of the new public key. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

- `privateKey` — On return, points to the keychain item object of the new private key. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

In order to generate a key pair, the dictionary passed in the `parameters` parameter must contain at least the following key-value pairs:

- A [kSecAttrKeyType](ksecattrkeytype.md) key with a value of any key type defined in `SecItem.h` (see [Keychain services](keychain-services.md)), for example, [kSecAttrKeyTypeRSA](ksecattrkeytypersa.md).
- A [kSecAttrKeySizeInBits](ksecattrkeysizeinbits.md) key with a value specifying the requested key size in bits. This can be specified as either a `CFNumberRef` or `CFStringRef` value. For example, RSA keys may have key size values of 512, 768, 1024, or 2048.

In addition, you can specify a number of other optional attributes for the public and private keys. The way you do this depends on whether you are writing code for macOS or iOS:

- In macOS, add the key-value pairs to the `parameters` dictionary directly. The specified attributes are applied to both the public and private keys.
- In iOS, add dictionaries for the keys [kSecPublicKeyAttrs](ksecpublickeyattrs.md) and [kSecPrivateKeyAttrs](ksecprivatekeyattrs.md) to the `parameters` dictionary, and provide the attributes in those dictionaries. The attributes specified in these dictionaries are added to either the public or private key, respectively, allowing you to apply separate attributes to each key.

The possible attributes are as follows; for details on each attribute, see [Keychain services](keychain-services.md):

- [kSecAttrLabel](ksecattrlabel.md)—Default `NULL`.
- [kSecAttrIsPermanent](ksecattrispermanent.md)—If this key is present and has a Boolean value of `true`, the key or key pair is added to the default       keychain.
- [kSecAttrApplicationTag](ksecattrapplicationtag.md)—Default `NULL`.
- [kSecAttrEffectiveKeySize](ksecattreffectivekeysize.md)—Default (`NULL`) sets the effective key size to the same as the total key size (`kSecAttrKeySizeInBits`).
- [kSecAttrCanEncrypt](ksecattrcanencrypt.md)—Default `false` for private keys, `true` for public keys.
- [kSecAttrCanDecrypt](ksecattrcandecrypt.md)—Default `true` for private keys, `false` for public keys.
- [kSecAttrCanDerive](ksecattrcanderive.md)—Default `true`.
- [kSecAttrCanSign](ksecattrcansign.md)—Default `true` for private keys, `false` for public keys.
- [kSecAttrCanVerify](ksecattrcanverify.md)—Default `false` for private keys, `true` for public keys.
- [kSecAttrCanUnwrap](ksecattrcanunwrap.md)—Default `true` for private keys, `false` for public keys.
