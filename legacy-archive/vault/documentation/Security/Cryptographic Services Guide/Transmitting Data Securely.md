---
title: Cryptographic Services Guide
apple_id: TP40011172
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Security
technology: Security
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/SecureNetworkCommunicationAPIs/SecureNetworkCommunicationAPIs.html
archived_at: '2026-07-18T02:06:48.549135Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cryptographic Services Guide](About%20Cryptographic%20Services.md)


[Next](CDSA%20Overview.md)[Previous](Generating%20Random%20Numbers.md)

# Transmitting Data Securely

One important aspect of computer security is the secure communication of data over a network. Although you can devise your own security protocols and use low-level APIs to implement them, it’s best to use standard protocols as much as possible, and the highest level API that supports them.

The Secure Sockets Layer (SSL) protocol and its successor, the Transport Layer Security (TLS) protocol, provide support for secure communication over a network. They are commonly used over TCP/IP connections such as the Internet. They use certificate-based authentication to ensure that you are communicating with a valid server, they validate data to prevent tampering, and they can use public-key cryptography to guard against eavesdropping or message forgery.

SSL and TLS are built into all major browsers and web servers. Whenever you use a secure website—for example, to send your credit card number to a vendor over the Internet—and see a protocol identifier of `https` rather than `http` at the beginning of the URL, you are using SSL or TLS for communication.

There are several ways to take advantage of SSL and TLS:

- At a high level, you can use an `https` URL with the URL Loading System (the _NSURL_ class, CFURL functions, and related classes).
- At a lower level, you can use the CFNetwork API to negotiate an SSL or TLS connection.
- For maximum control, you can use the Secure Transport API in macOS or in iOS 5.0 and later.

In addition to these APIs, a number of open source tools use OpenSSL for secure networking. If you use OpenSSL in your publicly shipping apps, you _must_ provide your own copy of the OpenSSL libraries, preferably as part of your app bundle; the OpenSSL libraries that macOS provides are deprecated.

The URL Loading System is a very high-level API that you can use to access the contents of `HTTP://`, `HTTPS://`, and `FTP://` URLs. Because URL Loading System works with secure `https://` URLs, it can be used for secure transport of data.

You should use the URL loading system when you need to download a resource from a remote server. Unlike CFNetwork, this API does not maintain a continuous data stream. This makes it a better choice for mobile use when it meets your needs (particularly with cellular networks, where your IP number may change as you switch from tower to tower).

CFNetwork is an API for creating, sending, and receiving serialized messages over a network. It provides a higher-level interface than Secure Transport that can be used by apps to set up and maintain a secure SSL or TLS networking session and to add authentication information to a message.

CFNetwork includes the following security-related components:

- CFHTTPMessage, which you can use to create, serialize, deserialize, and manage HTTP protocol messages. You should use the CFHTTPMessage API instead of other CFHTTP APIs if you need to add authentication information to a message.
- CFHTTPAuthentication, which applies authentication credentials to challenged HTTP messages. You use this API in conjunction with CHTTPMessage.
- CFStream Socket Additions, which allocates read and write streams and provides constants used with the CFReadStream and CFWriteStream APIs to set security protocols. You should use CFStream objects if you need to set up a streaming data connection (as opposed to an HTTP request).
- CFFTPStream, which you can use to perform FTP file transfers using the file transfer protocol (FTP). This component lets you send passwords to FTP servers.

In addition to the CFNetwork API, you use the CFReadStream and CFWriteStream APIs in the Core Foundation framework to create and manage the read and write streams that CFNetwork depends on. You can specify an SSL or TLS protocol version to encrypt and decrypt the data stream. Note that CFReadStream and CFWriteStream are “toll-free bridged” with their Cocoa Foundation counterparts, the classes `NSInputStream` and `NSOutputStream`. This means that each Core Foundation type is interchangeable in function or method calls with the corresponding bridged Foundation object, so you can use either C or Objective C interfaces, whichever is most convenient for you.

_Secure Transport_ is a low-level API for working with SSL and TLS. With Secure Transport, your code must set up the network connection and provide callback functions that Secure Transport calls to perform I/O operations over the network.

The CFNetwork and URL Loading System APIs are built on top of Secure Transport.

You can use the Secure Transport API to set parameters for a secure session, open and maintain a session, and close a session. However, because Secure Transport is a fairly complex API, you should generally use Secure Transport directly only if you need more control than you can get with CFNetwork.

The Secure Transport API lets you:

- Choose which protocols (SSL/TLS versions) and cipher suites should be allowed, and (after connecting) determine which protocol and cipher suite were actually negotiated.
- Specify Diffie-Hellman parameters for key exchange
- Specify whether client-side authentication should be required, and obtain that identification.
- Manage certificates and trust policies—specify certificates to use for client or server identification, specify the domain name to use when determining whether the other host’s certificate is valid, provide trust policies for expired certificates and unknown or expired root certificates, add additional trusted root certificates, and so on.

Secure Transport has no transport-layer dependencies; it can be used with BSD sockets, Open Transport, or any other transport-layer protocol available.

macOS includes a low-level command-line interface to the OpenSSL open-source cryptography toolkit; this interface is not available in iOS.

Although OpenSSL is commonly used in the open source community, it doesn’t provide a stable API from version to version. For this reason, the programmatic interface to OpenSSL is deprecated in macOS and is not provided in iOS. Use of the Apple-provided OpenSSL libraries by apps is strongly discouraged.

To ensure compatibility, if your app depends on OpenSSL, you should compile it yourself and statically link a known version of OpenSSL into your app. Such use works on both iOS and macOS.

In general, however, you should use the CFNetwork API for secure networking and the Certificate, Key, and Trust Services API for cryptographic services. Alternatively, in macOS, you can use the Secure Transport API.

To learn about other security issues related to network communication, read [Using Networking Securely](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/SecureNetworking/SecureNetworking.html#//apple_ref/doc/uid/TP40010220-CH1) in _[Networking Overview](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_.

For more information on the TLS standard, see [IETF's TLS Working Group site](http://datatracker.ietf.org/wg/tls/charter/).

To learn more about CFNetwork, read _[CFNetwork Programming Guide](../../Networking/CFNetwork%20Programming%20Guide/Introduction%20to%20CFNetwork%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzs)_.

To get started with Secure Transport, see _[Secure Transport Reference](https://developer.apple.com/documentation/security/secure_transport)_.

[Next](CDSA%20Overview.md)[Previous](Generating%20Random%20Numbers.md)

