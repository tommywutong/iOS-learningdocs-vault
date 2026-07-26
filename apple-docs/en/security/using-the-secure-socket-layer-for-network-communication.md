---
title: Using the Secure Socket Layer for Network Communication
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/using-the-secure-socket-layer-for-network-communication
source_url: 'https://developer.apple.com/documentation/security/using-the-secure-socket-layer-for-network-communication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/using-the-secure-socket-layer-for-network-communication.json'
content_hash: 'sha256:bf45f35d49736809'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Secure Transport](secure-transport.md)

# Using the Secure Socket Layer for Network Communication

<sub>Article</sub>

Establish Secure Sockets Layer (SSL) sessions to facilitate secure communication between client and server.

## Overview

The following terms are used in this discussion:

- **Client** — The initiator of an SSL session. The canonical example of a client is a web browser communicating with an HTTPS URL.
- **Server** — An entity that accepts requests for SSL sessions made by clients. An example is a secure web server.
- **SSLSession** — An entity whose existence is bounded by calls to the functions [SSLHandshake](<sslhandshake(__).md>) and [SSLClose](<sslclose(__).md>). An active session is in some state between these two calls, inclusive.
- **SSLSessionContext** — The state associated with one session. A session context cannot be reused for multiple sessions.

Most applications need only a few of the functions in this API, which are normally called in the following sequence:

- Prepare for a session
- Call [SSLCreateContext](<sslcreatecontext(______).md>) to create a new SSL session context.
- Write the [SSLWriteFunc](sslwritefunc.md) and [SSLReadFunc](sslreadfunc.md) I/O functions and register them with Secure Transport by calling the [SSLSetIOFuncs](<sslsetiofuncs(______).md>) function.
- Establish a connection using [CFNetwork](../cfnetwork.md), BSD Sockets, or Open Transport. Then call [SSLSetConnection](<sslsetconnection(____).md>) to specify the connection to which the SSL session context applies.
- Call [SSLSetPeerDomainName](<sslsetpeerdomainname(______).md>) to specify the fully-qualified domain name of the peer to which you want to connect (optional but highly recommended).
- Call [SSLSetCertificate](<sslsetcertificate(____).md>) to specify the certificate to be used in authentication (required for server side, optional for client).
- Start a session
- Call [SSLHandshake](<sslhandshake(__).md>) to perform the SSL handshake and establish a secure session.
- Maintain a session
- To transfer data over the secure session, Secure Transport calls your [SSLWrite](<sslwrite(________).md>) and [SSLRead](<sslread(________).md>) functions as needed.
- End a session
- Call [SSLClose](<sslclose(__).md>) to close the secure session.
- Close the connection and dispose of the connection reference.
- Release the SSL session context by calling [CFRelease](../corefoundation/cfrelease.md).
- If you called `SSLGetPeerCertificates` to obtain any certificates, call [CFRelease](../corefoundation/cfrelease.md) to release the certificate reference objects.

In many cases, it is easier to use the CFNetwork API than Secure Transport to implement a simple connection to a secure (HTTPS) URL. See [CFNetwork Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001132) for documentation of the CFNetwork API and the CFNetworkHTTPDownload sample code for an example of code that downloads data from a URL. If you specify an HTTPS URL, this routine automatically uses Secure Transport to encrypt the data stream.

For functions to manage and evaluate certificates, see [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md).
