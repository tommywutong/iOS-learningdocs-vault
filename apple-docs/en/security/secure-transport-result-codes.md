---
title: Secure Transport Result Codes
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secure-transport-result-codes
source_url: 'https://developer.apple.com/documentation/security/secure-transport-result-codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secure-transport-result-codes.json'
content_hash: 'sha256:d1774b5dc74e1f7e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Secure Transport](secure-transport.md)

# Secure Transport Result Codes

<sub>API Collection</sub>

Recognize result codes specific to the secure transport API.

## Discussion

Use the [SecCopyErrorMessageString](<seccopyerrormessagestring(____).md>) function to obtain a human readable string corresponding to these status codes.

The functions of the [Secure Transport](secure-transport.md) API may also return the general codes listed in [Security Framework Result Codes](security-framework-result-codes.md).

Errors in the range of –9819 through –9840 are fatal errors that are detected by the peer.

## Topics

### App Transport Security result codes

- [errSSLATSViolation](errsslatsviolation.md) — An App Transport Security violation occurred.
- [errSSLATSMinimumVersionViolation](errsslatsminimumversionviolation.md) — The minimum protocol version isn’t App Transport Security compliant.
- [errSSLATSCiphersuiteViolation](errsslatsciphersuiteviolation.md) — The selected ciphersuite isn’t App Transport Security compliant.
- [errSSLATSMinimumKeySizeViolation](errsslatsminimumkeysizeviolation.md) — The peer key size isn’t App Transport Security compliant.
- [errSSLATSLeafCertificateHashAlgorithmViolation](errsslatsleafcertificatehashalgorithmviolation.md) — The peer leaf certificate hash algorithm isn’t App Transport Security compliant.
- [errSSLATSCertificateHashAlgorithmViolation](errsslatscertificatehashalgorithmviolation.md) — The peer certificate hash algorithm isn’t App Transport Security compliant.
- [errSSLATSCertificateTrustViolation](errsslatscertificatetrustviolation.md) — The peer certificate wasn’t issued by a trusted peer.

### Certificate issue result codes

- [errSSLBadCert](errsslbadcert.md) — Bad certificate format.
- [errSSLBadCertificateStatusResponse](errsslbadcertificatestatusresponse.md) — Bad OCSP response.
- [errSSLCertExpired](errsslcertexpired.md) — The certificate chain had an expired certificate.
- [errSSLCertNotYetValid](errsslcertnotyetvalid.md) — The certificate chain had a certificatethat is not yet valid.
- [errSSLCertificateRequired](errsslcertificaterequired.md) — Certificate required.
- [errSSLClientCertRequested](errsslclientcertrequested.md) — The server has requested a client certificate.
- [errSSLHostNameMismatch](errsslhostnamemismatch.md) — The host name you connected with does not match any of the host names allowed by the certificate.
- [errSSLNoRootCert](errsslnorootcert.md) — No root certificate for the certificate chain.
- [errSSLPeerBadCert](errsslpeerbadcert.md) — A bad certificate was encountered.
- [errSSLPeerCertExpired](errsslpeercertexpired.md) — The certificate expired.
- [errSSLPeerCertRevoked](errsslpeercertrevoked.md) — The certificate was revoked.
- [errSSLPeerCertUnknown](errsslpeercertunknown.md) — The certificate is unknown.
- [errSSLPeerUnsupportedCert](errsslpeerunsupportedcert.md) — An unsupported certificate format was encountered.
- [errSSLUnknownRootCert](errsslunknownrootcert.md) — Certificate chain is valid, but root is nottrusted.
- [errSSLXCertChainInvalid](errsslxcertchaininvalid.md) — Invalid certificate chain.
- [errSSLPeerUnknownCA](errsslpeerunknownca.md) — An unknown certificate authority was encountered.

### Connection status result codes

- [errSSLClientHelloReceived](errsslclienthelloreceived.md) — A non-fatal result for providing a server name indication.
- [errSSLClosedAbort](errsslclosedabort.md) — The connection closed due to an error.
- [errSSLClosedGraceful](errsslclosedgraceful.md) — The connection closed gracefully.
- [errSSLClosedNoNotify](errsslclosednonotify.md) — The server closed the session with no notification.
- [errSSLConnectionRefused](errsslconnectionrefused.md) — The peer dropped the connection before responding.
- [errSSLPeerAuthCompleted](errsslpeerauthcompleted.md) — A non-fatal result indicating the peer certificate is valid, or was ignored if verification is disabled.
- [errSSLWouldBlock](errsslwouldblock.md) — Function is blocked; waiting for I/O. This is not fatal.

### Cryptography result codes

- [errSSLCrypto](errsslcrypto.md) — An underlying cryptographic error was encountered.
- [errSSLDecryptionFail](errssldecryptionfail.md) — Decryption failed.
- [errSSLPeerDecryptError](errsslpeerdecrypterror.md) — A decryption error occurred.
- [errSSLPeerDecryptionFail](errsslpeerdecryptionfail.md) — Decryption failed.
- [errSSLWeakPeerEphemeralDHKey](errsslweakpeerephemeraldhkey.md) — Indicates a weak ephemeral dh key.

### Other result codes

- [errSSLBadCipherSuite](errsslbadciphersuite.md) — A bad SSL cipher suite was encountered.
- [errSSLBadConfiguration](errsslbadconfiguration.md) — A configuration error occurred.
- [errSSLBadRecordMac](errsslbadrecordmac.md) — A record with a bad message authentication code (MAC) was encountered.
- [errSSLBufferOverflow](errsslbufferoverflow.md) — An insufficient buffer was provided.
- [errSSLConfigurationFailed](errsslconfigurationfailed.md) — TLS configuration failed.
- [errSSLDecodeError](errssldecodeerror.md) — Decode failed.
- [errSSLDecompressFail](errssldecompressfail.md) — Decompression failed.
- [errSSLFatalAlert](errsslfatalalert.md) — A fatal alert was encountered.
- [errSSLHandshakeFail](errsslhandshakefail.md) — Handshake failed.
- [errSSLIllegalParam](errsslillegalparam.md) — An illegal parameter was encountered.
- [errSSLInappropriateFallback](errsslinappropriatefallback.md) — Inappropriate fallback.
- [errSSLInternal](errsslinternal.md) — Internal error.
- [errSSLMissingExtension](errsslmissingextension.md) — Missing extension.
- [errSSLModuleAttach](errsslmoduleattach.md) — Module attach failure.
- [errSSLNegotiation](errsslnegotiation.md) — The cipher suite negotiation failed.
- [errSSLNetworkTimeout](errsslnetworktimeout.md) — Network timeout triggered.
- [errSSLPeerAccessDenied](errsslpeeraccessdenied.md) — Access was denied.
- [errSSLPeerBadRecordMac](errsslpeerbadrecordmac.md) — A record with a bad message authentication code (MAC) was encountered.
- [errSSLPeerDecodeError](errsslpeerdecodeerror.md) — A decoding error occurred.
- [errSSLPeerDecompressFail](errsslpeerdecompressfail.md) — Decompression failed.
- [errSSLPeerExportRestriction](errsslpeerexportrestriction.md) — An export restriction occurred.
- [errSSLPeerHandshakeFail](errsslpeerhandshakefail.md) — The handshake failed.
- [errSSLPeerInsufficientSecurity](errsslpeerinsufficientsecurity.md) — There is insufficient security for this operation.
- [errSSLPeerInternalError](errsslpeerinternalerror.md) — An internal error occurred.
- [errSSLPeerNoRenegotiation](errsslpeernorenegotiation.md) — No renegotiation is allowed.
- [errSSLPeerProtocolVersion](errsslpeerprotocolversion.md) — A bad protocol version was encountered.
- [errSSLPeerRecordOverflow](errsslpeerrecordoverflow.md) — A record overflow occurred.
- [errSSLPeerUnexpectedMsg](errsslpeerunexpectedmsg.md) — An unexpected message was received.
- [errSSLPeerUserCancelled](errsslpeerusercancelled.md) — The user canceled the operation.
- [errSSLProtocol](errsslprotocol.md) — SSL protocol error.
- [errSSLRecordOverflow](errsslrecordoverflow.md) — A record overflow occurred.
- [errSSLSessionNotFound](errsslsessionnotfound.md) — An attempt to restore an unknown session failed.
- [errSSLTransportReset](errssltransportreset.md) — Transport (socket) shutdown, for example, TCP RST or FIN.
- [errSSLUnexpectedMessage](errsslunexpectedmessage.md) — Peer rejected unexpected message.
- [errSSLUnexpectedRecord](errsslunexpectedrecord.md)
- [errSSLUnknownPSKIdentity](errsslunknownpskidentity.md) — Unknown PSK identity.
- [errSSLUnrecognizedName](errsslunrecognizedname.md) — Unknown or unrecognized name.
- [errSSLUnsupportedExtension](errsslunsupportedextension.md) — Unsupported TLS extension.
