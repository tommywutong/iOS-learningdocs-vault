---
title: 'CMSDecoderCopySignerTimestampWithPolicy(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsdecodercopysignertimestampwithpolicy(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsdecodercopysignertimestampwithpolicy(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsdecodercopysignertimestampwithpolicy%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f0c402c11ea1ec37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSDecoderCopySignerTimestampWithPolicy(_:_:_:_:)

<sub>Function</sub>

Returns the timestamp of a signer of a CMS message using a given policy, if present.

<sub>macOS</sub>

```swift
func CMSDecoderCopySignerTimestampWithPolicy(_ cmsDecoder: CMSDecoder, _ timeStampPolicy: CFTypeRef?, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus
```

## Parameters

- `cmsDecoder` — A CMSDecoder reference returned by the [CMSDecoderCreate](<cmsdecodercreate(__).md>) function.

- `timeStampPolicy` — A timestamp policy. Specify `NULL` (or use the [CMSDecoderCopySignerTimestamp](<cmsdecodercopysignertimestamp(______).md>) function instead) to get the default, which is a policy using [kSecPolicyAppleTimeStamping](ksecpolicyappletimestamping.md). See [Policies](policies.md) in [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) for more about policies.

- `signerIndex` — A number indicating which signer to examine. Signer index numbers start with 0. Use the [CMSDecoderGetNumSigners](<cmsdecodergetnumsigners(____).md>) function to determine the total number of signers for a message.

- `timestamp` — The address of an absolute time value where the result should be stored.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
