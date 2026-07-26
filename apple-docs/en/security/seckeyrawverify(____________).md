---
title: 'SecKeyRawVerify(_:_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 4.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeyrawverify(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeyrawverify(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyrawverify%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:1ad8942e8c527814'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyRawVerify(_:_:_:_:_:_:)

<sub>Function</sub>

Verifies a digital signature.

> [!warning] Deprecated
> Use SecKeyVerifySignature

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func SecKeyRawVerify(_ key: SecKey, _ padding: SecPadding, _ signedData: UnsafePointer<UInt8>, _ signedDataLen: Int, _ sig: UnsafePointer<UInt8>, _ sigLen: Int) -> OSStatus
```

## Parameters

- `key` — Public key with which to verify the data.

- `padding` — The type of padding used. Possible values are listed in [SecPadding](secpadding.md). Use [kSecPaddingPKCS1SHA1](secpadding/pkcs1sha1.md) if you are verifying a PKCS1-style signature with DER encoding of the digest type and the signed data is a SHA1 digest of the actual data. Specify [kSecPaddingNone](secpadding/ksecpaddingnone.md) if no padding was used.

- `signedData` — The data for which the signature is being verified. Typically, a digest of the actual data is signed.

- `signedDataLen` — Length in bytes of the data in the `signedData` buffer.

- `sig` — The digital signature to be verified.

- `sigLen` — Length of the data in the `sig` buffer.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
