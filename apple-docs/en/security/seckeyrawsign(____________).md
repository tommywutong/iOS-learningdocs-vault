---
title: 'SecKeyRawSign(_:_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 4.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeyrawsign(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeyrawsign(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyrawsign%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:aec1d6959a7d8c17'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyRawSign(_:_:_:_:_:_:)

<sub>Function</sub>

Generates a digital signature for a block of data.

> [!warning] Deprecated
> Use SecKeyCreateSignature

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyRawSign(_ key: SecKey, _ padding: SecPadding, _ dataToSign: UnsafePointer<UInt8>, _ dataToSignLen: Int, _ sig: UnsafeMutablePointer<UInt8>, _ sigLen: UnsafeMutablePointer<Int>) -> OSStatus
```

## Parameters

- `key` — Private key with which to sign the data.

- `padding` — The type of padding to use. Possible values are listed in [SecPadding](secpadding.md). Use [kSecPaddingPKCS1SHA1](secpadding/pkcs1sha1.md) if the data to be signed is a SHA1 digest of the actual data. If you specify [kSecPaddingNone](secpadding/ksecpaddingnone.md), the data is signed as-is.

- `dataToSign` — The data to be signed. Typically, a digest of the actual data is signed.

- `dataToSignLen` — Length in bytes of the data in the `dataToSign` buffer. When PKCS1 padding is performed, the maximum length of data that can be signed is 11 bytes less than the value returned by the [SecKeyGetBlockSize](<seckeygetblocksize(__).md>) function (`secKeyGetBlockSize() - 11`).

- `sig` — On return, the digital signature.

- `sigLen` — On entry, the size of the buffer provided in the `sig` parameter. On return, the amount of data actually placed in the buffer.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The behavior this function with [kSecPaddingNone](secpadding/ksecpaddingnone.md) is undefined if the first byte of the data to sign is `0`; there is no way to verify leading zeroes, as they are discarded during the calculation.
