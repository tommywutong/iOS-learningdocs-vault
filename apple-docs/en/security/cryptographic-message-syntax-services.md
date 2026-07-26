---
title: Cryptographic Message Syntax Services
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/cryptographic-message-syntax-services
source_url: 'https://developer.apple.com/documentation/security/cryptographic-message-syntax-services'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cryptographic-message-syntax-services.json'
content_hash: 'sha256:0c07d5385fa55591'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# Cryptographic Message Syntax Services

<sub>API Collection</sub>

Cryptographically sign and encrypt S/MIME messages.

## Overview

When you want to exchange data securely using the Multipurpose Internet Mail Extensions (MIME) protocol, you use the version of the protocol known as S/MIME defined in [RFC 3851](https://tools.ietf.org/html/rfc3851). This allows you to, among other things, ensure data integrity through digital signatures and data confidentiality through encryption. S/MIME in turn relies on the Cryptographic Message Syntax (CMS) protocol defined in [RFC 3852](https://tools.ietf.org/html/rfc3852) to carry out these operations.

Cryptographic message syntax services provides encoder objects that perform encryption using the CMS protocol’s enveloped-data content type and sign using the signed-data content type. When a message is both signed and encrypted, the enveloped data content contains the signed data content. That is, the message is first signed and then the signed content is encrypted.

## Topics

### The Encoder

- [CMSEncoderCreate](<cmsencodercreate(__).md>) — Creates a CMSEncoder reference.
- [CMSEncoder](cmsencoder.md) — Opaque reference to a CMS encoder object.
- [CMSEncoderGetTypeID](<cmsencodergettypeid().md>) — Returns the type identifier for the CMSEncoder opaque type.

### Message Creation

- [CMSEncoderAddSigners](<cmsencoderaddsigners(____).md>) — Specifies signers of the message.
- [CMSEncoderAddRecipients](<cmsencoderaddrecipients(____).md>) — Specifies a message is to be encrypted and specifies the recipients of the message.
- [CMSEncoderSetHasDetachedContent](<cmsencodersethasdetachedcontent(____).md>) — Specifies whether the signed data is to be separate from the message.
- [CMSEncoderSetEncapsulatedContentTypeOID](<cmsencodersetencapsulatedcontenttypeoid(____).md>) — Specifies an object identifier for the encapsulated data of a signed message.
- [CMSEncoderAddSupportingCerts](<cmsencoderaddsupportingcerts(____).md>) — Adds certificates to a message.
- [CMSEncoderAddSignedAttributes](<cmsencoderaddsignedattributes(____).md>) — Specifies attributes for a signed message.
- [CMSSignedAttributes](cmssignedattributes.md) — Optional attributes you can add to a signed message.
- [CMSEncoderSetCertificateChainMode](<cmsencodersetcertificatechainmode(____).md>) — Specifies which certificates to include in a signed CMS message.
- [CMSCertificateChainMode](cmscertificatechainmode.md) — Constants that can be set to specify what certificates to include in a signed message.
- [CMSEncoderSetSignerAlgorithm](<cmsencodersetsigneralgorithm(____).md>) — Sets the digest algorithm to use for the signer.

### Message Characteristics

- [CMSEncoderCopySigners](<cmsencodercopysigners(____).md>) — Obtains the array of signers specified with the `CMSEncoderAddSigners` function.
- [CMSEncoderCopyRecipients](<cmsencodercopyrecipients(____).md>) — Obtains the array of recipients specified with the `CMSEncoderAddRecipients` function.
- [CMSEncoderGetHasDetachedContent](<cmsencodergethasdetachedcontent(____).md>) — Indicates whether the message is to have detached content.
- [CMSEncoderCopyEncapsulatedContentType](<cmsencodercopyencapsulatedcontenttype(____).md>) — Obtains the object identifier for the encapsulated data of a signed message.
- [CMSEncoderCopySupportingCerts](<cmsencodercopysupportingcerts(____).md>) — Obtains the certificates added to a message with `CMSEncoderAddSupportingCerts`.
- [CMSEncoderGetCertificateChainMode](<cmsencodergetcertificatechainmode(____).md>) — Obtains a constant that indicates which certificates are to be included in a signed CMS message.

### Encoding

- [CMSEncoderUpdateContent](<cmsencoderupdatecontent(______).md>) — Feeds content bytes into the encoder.
- [CMSEncoderCopyEncodedContent](<cmsencodercopyencodedcontent(____).md>) — Finishes encoding the message and obtains the encoded result.
- [CMSEncodeContent](<cmsencodecontent(________________).md>) — Encodes a message and obtains the result in one high-level function call.

### The Decoder

- [CMSDecoderCreate](<cmsdecodercreate(__).md>) — Creates a CMSDecoder reference.
- [CMSDecoder](cmsdecoder.md) — An opaque reference to a CMS decoder object.
- [CMSDecoderGetTypeID](<cmsdecodergettypeid().md>) — Returns the type identifier for the CMSDecoder opaque type.

### Decoding

- [CMSDecoderUpdateMessage](<cmsdecoderupdatemessage(______).md>) — Feeds raw bytes of the message to be decoded into the decoder.
- [CMSDecoderFinalizeMessage](<cmsdecoderfinalizemessage(__).md>) — Indicates that there is no more data to decode.
- [CMSDecoderSetDetachedContent](<cmsdecodersetdetachedcontent(____).md>) — Specifies the message’s detached content, if any.
- [CMSDecoderCopyDetachedContent](<cmsdecodercopydetachedcontent(____).md>) — Obtains the detached content specified with the `CMSDecoderSetDetachedContent` function.

### Signature Verification

- [CMSDecoderSetSearchKeychain](<cmsdecodersetsearchkeychain(____).md>) — Specifies the keychains to search for intermediate certificates to be used in verifying a signed message’s signer certificates. _(deprecated)_
- [CMSDecoderGetNumSigners](<cmsdecodergetnumsigners(____).md>) — Obtains the number of signers of a message.
- [CMSDecoderCopySignerEmailAddress](<cmsdecodercopysigneremailaddress(______).md>) — Obtains the email address of the specified signer of a CMS message.
- [CMSDecoderCopySignerCert](<cmsdecodercopysignercert(______).md>) — Obtains the certificate of the specified signer of a CMS message.
- [CMSDecoderCopySignerStatus](<cmsdecodercopysignerstatus(______________).md>) — Obtains the status of a CMS message’s signature.
- [CMSSignerStatus](cmssignerstatus.md) — The constants that indicate the status of the signature and signer information in a signed message.

### Message Content

- [CMSDecoderIsContentEncrypted](<cmsdecoderiscontentencrypted(____).md>) — Determines whether a CMS message was encrypted.
- [CMSDecoderCopyEncapsulatedContentType](<cmsdecodercopyencapsulatedcontenttype(____).md>) — Obtains the object identifier for the encapsulated data of a signed message.
- [CMSDecoderCopyAllCerts](<cmsdecodercopyallcerts(____).md>) — Obtains an array of all of the certificates in a message.
- [CMSDecoderCopyContent](<cmsdecodercopycontent(____).md>) — Obtains the message content, if any.

### Timestamps

- [CMSDecoderCopySignerSigningTime](<cmsdecodercopysignersigningtime(______).md>) — Obtains the signing time of a CMS message, if present.
- [CMSDecoderCopySignerTimestamp](<cmsdecodercopysignertimestamp(______).md>) — Returns the timestamp of a signer of a CMS message, if present.
- [CMSDecoderCopySignerTimestampCertificates](<cmsdecodercopysignertimestampcertificates(______).md>) — Returns an array containing the certificates from a timestamp response.
- [CMSDecoderCopySignerTimestampWithPolicy](<cmsdecodercopysignertimestampwithpolicy(________).md>) — Returns the timestamp of a signer of a CMS message using a given policy, if present.
- [CMSEncoderCopySignerTimestamp](<cmsencodercopysignertimestamp(______).md>) — Returns the timestamp of a signer of a CMS message, if present.
- [CMSEncoderCopySignerTimestampWithPolicy](<cmsencodercopysignertimestampwithpolicy(________).md>) — Returns the timestamp of a signer of a CMS message using a particular policy, if present.
