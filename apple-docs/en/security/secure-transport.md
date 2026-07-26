---
title: Secure Transport
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secure-transport
source_url: 'https://developer.apple.com/documentation/security/secure-transport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secure-transport.json'
content_hash: 'sha256:3849addb672c471c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# Secure Transport

<sub>API Collection</sub>

Secure network communication using standardized transport layer security mechanisms.

## Overview

The `Security.SecureTransport` API gives you access to Apple’s implementation of Secure Sockets Layer version 3.0 (SSLv3), Transport Layer Security (TLS) versions 1.0 through 1.2, and Datagram Transport Layer Security (DTLS) version 1.0.

This API imposes no transport layer dependencies. You can use it with BSD Sockets and other protocols. To use this API, you provide callback functions to perform I/O on the underlying network connections. You are also responsible for setting up raw network connections. You pass in an opaque reference to the underlying (connected) entity at the start of an SSL session in the form of an [SSLConnectionRef](sslconnectionref.md) object.

> [!important] Important
> This API is considered legacy. Use the [Network](../network.md) framework instead.

## Topics

### First Steps

- [Using the Secure Socket Layer for Network Communication](using-the-secure-socket-layer-for-network-communication.md) — Establish Secure Sockets Layer (SSL) sessions to facilitate secure communication between client and server.

### Session Context

- [SSLCreateContext](<sslcreatecontext(______).md>) — Allocates and returns a new context. _(deprecated)_
- [SSLProtocolSide](sslprotocolside.md) — The flags that indicate whether a context is for the server or client side of a connection.
- [SSLConnectionType](sslconnectiontype.md) — The flags that indicate whether a context is to be used for streaming or datagram-based communication.
- [SSLContext](sslcontext.md) — An opaque type that represents an SSL session context object.
- [SSLContextGetTypeID](<sslcontextgettypeid().md>) — Returns the Core Foundation type ID for context objects. _(deprecated)_

### Context Options

- [SSLSetSessionOption](<sslsetsessionoption(______).md>) — Specifies options for a specific session. _(deprecated)_
- [SSLGetSessionOption](<sslgetsessionoption(______).md>) — Indicates the current setting of Secure Sockets Layer (SSL) session options. _(deprecated)_
- [SSLSessionOption](sslsessionoption.md) — The options that can be set for an SSL session.

### Context Callbacks

- [SSLSetIOFuncs](<sslsetiofuncs(______).md>) — Specifies callback functions that perform the network I/O operations. _(deprecated)_
- [SSLReadFunc](sslreadfunc.md) — A pointer to a customized read function that secure transport calls to read data from the connection.
- [SSLWriteFunc](sslwritefunc.md) — A pointer to a customized write function that secure transport calls to write data to the connection.

### Session Configuration

- [SSLSetSessionConfig](<sslsetsessionconfig(____).md>) — Sets a predefined configuration for the Secure Sockets Layer (SSL) session. _(deprecated)_
- [SSLSetClientSideAuthenticate](<sslsetclientsideauthenticate(____).md>) — Specifies the requirements for client-side authentication. _(deprecated)_
- [SSLConfig](sslconfig.md) — Use these constants to configure Transport Layer Security (TLS) sessions.
- [SSLAuthenticate](sslauthenticate.md) — The flags that represent the requirements for client-side authentication.

### I/O Connections

- [SSLSetConnection](<sslsetconnection(____).md>) — Specifies an I/O connection for a specific session. _(deprecated)_
- [SSLGetConnection](<sslgetconnection(____).md>) — Retrieves an I/O connection—such as a socket or endpoint—for a specific session. _(deprecated)_
- [SSLConnectionRef](sslconnectionref.md) — A pointer to an opaque I/O connection object.

### Session State

- [SSLHandshake](<sslhandshake(__).md>) — Performs the SSL handshake. _(deprecated)_
- [SSLReHandshake](<sslrehandshake(__).md>) — Requests renegotiation of the SSL handshake. Server only. _(deprecated)_
- [SSLClose](<sslclose(__).md>) — Terminates the current SSL session. _(deprecated)_
- [SSLSetPeerID](<sslsetpeerid(______).md>) — Specifies data that is sufficient to uniquely identify the peer of the current session. _(deprecated)_
- [SSLGetPeerID](<sslgetpeerid(______).md>) — Retrieves the current peer ID data. _(deprecated)_
- [SSLGetSessionState](<sslgetsessionstate(____).md>) — Retrieves the state of an SSL session. _(deprecated)_
- [SSLSessionState](sslsessionstate.md) — The flags that represent the state of an SSL session.
- [SSLSetError](<sslseterror(____).md>) — Sets the status of a session context. _(deprecated)_

### Read Operations

- [SSLRead](<sslread(________).md>) — Performs a normal application-level read operation. _(deprecated)_
- [SSLGetBufferedReadSize](<sslgetbufferedreadsize(____).md>) — Determines how much data is available to be read. _(deprecated)_

### Write Operations

- [SSLWrite](<sslwrite(________).md>) — Performs a typical application-level write operation. _(deprecated)_
- [SSLGetDatagramWriteSize](<sslgetdatagramwritesize(____).md>) — Provides the largest packet that the OS guarantees it can send without fragmentation. _(deprecated)_
- [SSLGetMaxDatagramRecordSize](<sslgetmaxdatagramrecordsize(____).md>) — Obtains the maximum datagram record size allowed by the application for a given context. _(deprecated)_
- [SSLSetMaxDatagramRecordSize](<sslsetmaxdatagramrecordsize(____).md>) — Sets the maximum datagram record size allowed by the application for a given context. _(deprecated)_
- [SSLSetDatagramHelloCookie](<sslsetdatagramhellocookie(______).md>) — Sets the cookie value used in the Datagram Transport Layer Security (DTLS) hello message. _(deprecated)_

### The Peer Domain Name

- [SSLSetPeerDomainName](<sslsetpeerdomainname(______).md>) — Specifies the fully qualified domain name of the peer. _(deprecated)_
- [SSLGetPeerDomainNameLength](<sslgetpeerdomainnamelength(____).md>) — Determines the length of a previously set peer domain name. _(deprecated)_
- [SSLGetPeerDomainName](<sslgetpeerdomainname(______).md>) — Retrieves the peer domain name specified previously. _(deprecated)_
- [SSLCopyRequestedPeerName](<sslcopyrequestedpeername(______).md>) — Determines the buffer size needed for the peer domain name. _(deprecated)_
- [SSLCopyRequestedPeerNameLength](<sslcopyrequestedpeernamelength(____).md>) — Obtains the hostname specified by the client in the ServerName extension (SNI). Server only. _(deprecated)_

### Versions

- [SSLSetProtocolVersionMax](<sslsetprotocolversionmax(____).md>) — Sets the maximum protocol version allowed by the application for a given SSL context. _(deprecated)_
- [SSLSetProtocolVersionMin](<sslsetprotocolversionmin(____).md>) — Sets the minimum protocol version allowed by the application for a given SSL context. _(deprecated)_
- [SSLGetProtocolVersionMax](<sslgetprotocolversionmax(____).md>) — Gets the maximum protocol version allowed by the application for a given SSL context. _(deprecated)_
- [SSLGetProtocolVersionMin](<sslgetprotocolversionmin(____).md>) — Gets the minimum protocol version allowed by the application for a given SSL context. _(deprecated)_
- [SSLGetNegotiatedProtocolVersion](<sslgetnegotiatedprotocolversion(____).md>) — Obtains the negotiated protocol version of the active session. _(deprecated)_
- [tls_protocol_version_t](tls_protocol_version_t.md) — The collection of supported TLS and DTLS versions.
- [SSLProtocol](sslprotocol.md) — An enumeration of valid SSL protocol versions.

### Application Layer Protocols

- [SSLCopyALPNProtocols](<sslcopyalpnprotocols(____).md>) — Gets the list of supported application layer protocols. _(deprecated)_
- [SSLSetALPNProtocols](<sslsetalpnprotocols(____).md>) — Sets the list of supported applicaiton layer protocols. _(deprecated)_

### Ciphers

- [SSLGetNumberSupportedCiphers](<sslgetnumbersupportedciphers(____).md>) — Determines the number of cipher suites supported. _(deprecated)_
- [SSLGetSupportedCiphers](<sslgetsupportedciphers(______).md>) — Determines the values of the supported cipher suites. _(deprecated)_
- [SSLSetEnabledCiphers](<sslsetenabledciphers(______).md>) — Specifies a restricted set of SSL cipher suites to be enabled by the current SSL session context. _(deprecated)_
- [SSLGetNumberEnabledCiphers](<sslgetnumberenabledciphers(____).md>) — Determines the number of cipher suites currently enabled. _(deprecated)_
- [SSLGetEnabledCiphers](<sslgetenabledciphers(______).md>) — Determines which SSL cipher suites are currently enabled. _(deprecated)_
- [SSLGetNegotiatedCipher](<sslgetnegotiatedcipher(____).md>) — Retrieves the cipher suite negotiated for this session. _(deprecated)_
- [SSLSetDiffieHellmanParams](<sslsetdiffiehellmanparams(______).md>) — Specifies Diffie-Hellman parameters for a given context. _(deprecated)_
- [SSLGetDiffieHellmanParams](<sslgetdiffiehellmanparams(______).md>) — Retrieves the Diffie-Hellman parameters for a given context. _(deprecated)_
- [tls_ciphersuite_group_t](tls_ciphersuite_group_t.md) — Groups that collect ciphersuites of comparable security properties.
- [tls_ciphersuite_t](tls_ciphersuite_t.md) — The collection of valid ciphersuites.
- [SSLCipherSuite](sslciphersuite.md) — A type for storing cipher suite values.
- [SSLCiphersuiteGroup](sslciphersuitegroup.md) — A mechanism for grouping related cipher suites.
- [SSL Cipher Suite Values](ssl-cipher-suite-values.md) — Recognize the set of valid SSL cipher suite values.

### Root Certificates

- [SSLSetCertificateAuthorities](<sslsetcertificateauthorities(______).md>) — Adds one or more certificates to a server’s list of certification authorities (CAs) acceptable for client authentication. _(deprecated)_
- [SSLCopyCertificateAuthorities](<sslcopycertificateauthorities(____).md>) — Retrieves the current list of certification authorities. _(deprecated)_

### Authentication

- [SSLAddDistinguishedName](<ssladddistinguishedname(______).md>) — Adds a DER-encoded distinguished name to a list of acceptable names to be specified in requests for client certificates. _(deprecated)_
- [SSLCopyDistinguishedNames](<sslcopydistinguishednames(____).md>) — Retrieves the distinguished names of acceptable certification authorities. _(deprecated)_
- [SSLSetCertificate](<sslsetcertificate(____).md>) — Specifies this connection’s certificate or certificates. _(deprecated)_
- [SSLGetClientCertificateState](<sslgetclientcertificatestate(____).md>) — Retrieves the exchange status of the client certificate. _(deprecated)_
- [SSLCopyPeerTrust](<sslcopypeertrust(____).md>) — Retrieves a trust management object for the certificate used by a session. _(deprecated)_
- [SSLClientCertificateState](sslclientcertificatestate.md) — An enumeration of the states of client certificate exchange.
- [SSLSetOCSPResponse](<sslsetocspresponse(____).md>) — Sets the OCSP response for the given SSL session. _(deprecated)_
- [SSLSetSessionTicketsEnabled](<sslsetsessionticketsenabled(____).md>) — Enables or disables session ticket resumption. _(deprecated)_

### Result Codes

- [Secure Transport Result Codes](secure-transport-result-codes.md) — Recognize result codes specific to the secure transport API.

### Legacy Operations

- [SSLSetEncryptionCertificate](<sslsetencryptioncertificate(____).md>) — Specifies the encryption certificates used for this connection. _(deprecated)_
