---
title: 'SecKeyDecrypt(_:_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 4.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeydecrypt(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeydecrypt(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeydecrypt%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:72fa96310329a966'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyDecrypt(_:_:_:_:_:_:)

<sub>Function</sub>

Decrypts a block of ciphertext.

> [!warning] Deprecated
> Use SecKeyCreateDecryptedData

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyDecrypt(_ key: SecKey, _ padding: SecPadding, _ cipherText: UnsafePointer<UInt8>, _ cipherTextLen: Int, _ plainText: UnsafeMutablePointer<UInt8>, _ plainTextLen: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `key` — Private key with which to decrypt the data.

- `padding` — The type of padding used. Possible values are listed in [SecPadding](secpadding.md). Typically, [kSecPaddingPKCS1](secpadding/pkcs1.md) is used, which removes PKCS1 padding after decryption. If you specify [kSecPaddingNone](secpadding/ksecpaddingnone.md), the decrypted data is returned as-is.

- `cipherText` — The data to decrypt.

- `cipherTextLen` — Length in bytes of the data in the `cipherText` buffer. This must be less than or equal to the value returned by the [SecKeyGetBlockSize](<seckeygetblocksize(__).md>) function.

- `plainText` — On return, the decrypted text.

- `plainTextLen` — On entry, the size of the buffer provided in the `plainText` parameter. On return, the amount of data actually placed in the buffer.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The input buffer (`cipherText`) can be the same as the output buffer (`plainText`) to reduce the amount of memory used by the function.
