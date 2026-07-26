---
title: 'SecKeyEncrypt(_:_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 4.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeyencrypt(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeyencrypt(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyencrypt%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8128c1ec9ef1d5c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyEncrypt(_:_:_:_:_:_:)

<sub>Function</sub>

Encrypts a block of plaintext.

> [!warning] Deprecated
> Use SecKeyCreateEncryptedData

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyEncrypt(_ key: SecKey, _ padding: SecPadding, _ plainText: UnsafePointer<UInt8>, _ plainTextLen: Int, _ cipherText: UnsafeMutablePointer<UInt8>, _ cipherTextLen: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `key` — Public key with which to encrypt the data.

- `padding` — The type of padding to use. Possible values are listed in [SecPadding](secpadding.md). Typically, [kSecPaddingPKCS1](secpadding/pkcs1.md) is used, which adds PKCS1 padding before encryption. If you specify [kSecPaddingNone](secpadding/ksecpaddingnone.md), the data is encrypted as-is.

- `plainText` — The data to encrypt.

- `plainTextLen` — Length in bytes of the data in the `plainText` buffer. This must be less than or equal to the value returned by the [SecKeyGetBlockSize](<seckeygetblocksize(__).md>) function. When PKCS1 padding is performed, the maximum length of data that can be encrypted is 11 bytes less than the value returned by the [SecKeyGetBlockSize](<seckeygetblocksize(__).md>) function (`secKeyGetBlockSize() - 11`).

- `cipherText` — On return, the encrypted text.

- `cipherTextLen` — On entry, the size of the buffer provided in the `cipherText` parameter. On return, the amount of data actually placed in the buffer.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The input buffer (`plainText`) can be the same as the output buffer (`cipherText`) to reduce the amount of memory used by the function.
