---
title: Transform Attributes
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/transform-attributes
source_url: 'https://developer.apple.com/documentation/security/transform-attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/transform-attributes.json'
content_hash: 'sha256:755f0fc4d184b12d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Security Transforms](security-transforms.md)

# Transform Attributes

<sub>API Collection</sub>

Specify the attributes of a transform.

## Overview

Use these keys and values when accessing transform attributes by name, such as with the [SecTransformSetAttribute](<sectransformsetattribute(________).md>) and [SecTransformGetAttribute](<sectransformgetattribute(____).md>) functions. You can also use some of the values directly in certain function calls, such as when you create a encode transform with the [SecEncodeTransformCreate](<secencodetransformcreate(____).md>) function and give it an `encodeType` parameter to seed the [kSecEncodeTypeAttribute](ksecencodetypeattribute.md) attribute.

## Topics

### Encode and Decode Keys

- [kSecEncodeLineLengthAttribute](ksecencodelinelengthattribute.md) — The length of encoded Base32 or Base64 lines. _(deprecated)_
- [kSecEncodeTypeAttribute](ksecencodetypeattribute.md) — The encoding used by an encode transform. _(deprecated)_
- [kSecDecodeTypeAttribute](ksecdecodetypeattribute.md) — The encoding used by a decode transform.
- [kSecCompressionRatio](kseccompressionratio.md) — The compression ratio. _(deprecated)_

### Digest and Encryption Keys

- [kSecDigestTypeAttribute](ksecdigesttypeattribute.md) — The digest algorithm. _(deprecated)_
- [kSecDigestLengthAttribute](ksecdigestlengthattribute.md) — The digest length. _(deprecated)_
- [kSecDigestHMACKeyAttribute](ksecdigesthmackeyattribute.md) — The key for HMAC operation. _(deprecated)_
- [kSecInputIsAttributeName](ksecinputisattributename.md) — The type of input to the transform. _(deprecated)_
- [kSecEncryptionMode](ksecencryptionmode.md) — The encryption mode. _(deprecated)_
- [kSecEncryptKey](ksecencryptkey.md) — The encryption key for the transform. _(deprecated)_
- [kSecIVKey](ksecivkey.md) — The setting for an initialization vector. _(deprecated)_
- [kSecPaddingKey](ksecpaddingkey.md) — The kind of padding to use. _(deprecated)_
- [kSecOAEPEncodingParametersAttributeName](ksecoaepencodingparametersattributename.md) — The OAEP encoding parameters. _(deprecated)_
- [kSecOAEPMGF1DigestAlgorithmAttributeName](ksecoaepmgf1digestalgorithmattributename.md) — The OAEP MGF1 digest algorithm. _(deprecated)_
- [kSecOAEPMessageLengthAttributeName](ksecoaepmessagelengthattributename.md) — The OAEP message length. _(deprecated)_

### Transform Keys

- [kSecTransformInputAttributeName](ksectransforminputattributename.md) — The input to a transform. _(deprecated)_
- [kSecTransformOutputAttributeName](ksectransformoutputattributename.md) — The output of a transform. _(deprecated)_
- [kSecTransformDebugAttributeName](ksectransformdebugattributename.md) — A write stream that should receive debug data. _(deprecated)_
- [kSecKeyAttributeName](kseckeyattributename.md) — The cryptographic key associated with a transform.
- [kSecSignatureAttributeName](ksecsignatureattributename.md) — The cryptographic signature associated with a transform.
- [kSecTransformAbortAttributeName](ksectransformabortattributename.md) — The reason for an abort. _(deprecated)_
- [kSecTransformTransformName](ksectransformtransformname.md) — The name of a transform. _(deprecated)_

### Encode Types

- [kSecBase32Encoding](ksecbase32encoding.md) — A base 32 encoding. _(deprecated)_
- [kSecBase64Encoding](ksecbase64encoding.md) — A base 64 encoding. _(deprecated)_
- [kSecZLibEncoding](kseczlibencoding.md) — A compressed encoding. _(deprecated)_

### Digest Types

- [kSecDigestMD2](ksecdigestmd2.md) — An MD2 digest. _(deprecated)_
- [kSecDigestMD4](ksecdigestmd4.md) — An MD4 digest. _(deprecated)_
- [kSecDigestMD5](ksecdigestmd5.md) — An MD5 digest. _(deprecated)_
- [kSecDigestSHA1](ksecdigestsha1.md) — An SHA1 digest. _(deprecated)_
- [kSecDigestSHA2](ksecdigestsha2.md) — An SHA2 digest. _(deprecated)_
- [kSecDigestHMACMD5](ksecdigesthmacmd5.md) — An HMAC using the MD5 digest algorithm. _(deprecated)_
- [kSecDigestHMACSHA1](ksecdigesthmacsha1.md) — An HMAC using the SHA1 digest algorithm. _(deprecated)_
- [kSecDigestHMACSHA2](ksecdigesthmacsha2.md) — An HMAC using one of the SHA2 digest algorithms. _(deprecated)_

### Line Lengths

- [kSecLineLength64](kseclinelength64.md) — A line length of 64 bytes. _(deprecated)_
- [kSecLineLength76](kseclinelength76.md) — A line length of 76 bytes. _(deprecated)_

### Input Types

- [kSecInputIsDigest](ksecinputisdigest.md) — The input is a digest of the original data.
- [kSecInputIsPlainText](ksecinputisplaintext.md) — The input is plain text.
- [kSecInputIsRaw](ksecinputisraw.md) — The input is raw. _(deprecated)_

### Padding Types

- [kSecPaddingNoneKey](ksecpaddingnonekey.md) — No padding will be used when encrypting or decrypting. _(deprecated)_
- [kSecPaddingOAEPKey](ksecpaddingoaepkey.md) — PKCS7 padding will be used when encrypting or decrypting. _(deprecated)_
- [kSecPaddingPKCS1Key](ksecpaddingpkcs1key.md) — PKCS1 padding will be used when encrypting or decrypting. _(deprecated)_
- [kSecPaddingPKCS5Key](ksecpaddingpkcs5key.md) — PKCS5 padding will be used when encrypting or decrypting. _(deprecated)_
- [kSecPaddingPKCS7Key](ksecpaddingpkcs7key.md) — PKCS7 padding will be used when encrypting or decrypting. _(deprecated)_

### Encryption Modes

- [kSecModeNoneKey](ksecmodenonekey.md) — No mode will be used when encrypting or decrypting. _(deprecated)_
- [kSecModeCBCKey](ksecmodecbckey.md) — CBC mode will be used when encrypting or decrypting. _(deprecated)_
- [kSecModeCFBKey](ksecmodecfbkey.md) — CFB mode will be used when encrypting or decrypting. _(deprecated)_
- [kSecModeECBKey](ksecmodeecbkey.md) — ECB mode will be used when encrypting or decrypting. _(deprecated)_
- [kSecModeOFBKey](ksecmodeofbkey.md) — OFB mode will be used when encrypting or decrypting. _(deprecated)_
