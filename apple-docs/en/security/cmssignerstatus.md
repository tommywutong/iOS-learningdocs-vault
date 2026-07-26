---
title: CMSSignerStatus
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/cmssignerstatus
source_url: 'https://developer.apple.com/documentation/security/cmssignerstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmssignerstatus.json'
content_hash: 'sha256:d3e415995f3527cb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSSignerStatus

<sub>Enumeration</sub>

The constants that indicate the status of the signature and signer information in a signed message.

<sub>Mac Catalyst, macOS</sub>

```swift
enum CMSSignerStatus
```

## Overview

These are obtained using the [CMSDecoderCopySignerStatus](<cmsdecodercopysignerstatus(______________).md>) function.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCMSSignerUnsigned](cmssignerstatus/unsigned.md) — The message was not signed.
- [kCMSSignerValid](cmssignerstatus/valid.md) — The message was signed and both the signature and the signer certificate have been verified.
- [kCMSSignerNeedsDetachedContent](cmssignerstatus/needsdetachedcontent.md) — The message was signed but has detached content. You must call the [CMSDecoderSetDetachedContent](<cmsdecodersetdetachedcontent(____).md>) function before ascertaining the signature status.
- [kCMSSignerInvalidSignature](cmssignerstatus/invalidsignature.md) — The message was signed but the signature is invalid.
- [kCMSSignerInvalidCert](cmssignerstatus/invalidcert.md) — The message was signed but the signer’s certificate could not be verified.
- [kCMSSignerInvalidIndex](cmssignerstatus/invalidindex.md) — The specified value for the signer index (`signerIndex` parameter) is greater than the number of signers of the message minus one (`signerIndex > (numSigners – 1)`).

### Initializers

- [init(rawValue:)](<cmssignerstatus/init(rawvalue_).md>)
