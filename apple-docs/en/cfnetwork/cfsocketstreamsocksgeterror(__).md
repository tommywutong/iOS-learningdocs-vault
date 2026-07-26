---
title: 'CFSocketStreamSOCKSGetError(_:)'
framework: CFNetwork
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/cfnetwork/cfsocketstreamsocksgeterror(_:)'
source_url: 'https://developer.apple.com/documentation/cfnetwork/cfsocketstreamsocksgeterror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cfnetwork/cfsocketstreamsocksgeterror%28_%3A%29.json'
content_hash: 'sha256:6291a5cdcde2acac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [CFNetwork](../cfnetwork.md)

# CFSocketStreamSOCKSGetError(_:)

<sub>Function</sub>

This function gets error codes in the `kCFStreamErrorDomainSOCKS` domain from the `CFStreamError` returned by a stream operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func CFSocketStreamSOCKSGetError(_ error: UnsafePointer<CFStreamError>) -> Int32
```

## Parameters

- `error` — The error value to decode.

## Discussion

Error codes in the `kCFStreamErrorDomainSOCKS` domain can come from multiple parts of the protocol stack, many of which define their own error values as part of outside specifications such as the HTTP specification.

To avoid confusion from conflicting error numbers, error codes in the `kCFStreamErrorDomainSOCKS` domain contain two parts: a subdomain, which tells which part of the protocol stack generated the error, and the error code itself.

Calling [CFSocketStreamSOCKSGetError](<cfsocketstreamsocksgeterror(__).md>) returns the error code itself, which must be interpreted in the context of the result of a call to [CFSocketStreamSOCKSGetErrorSubdomain](<cfsocketstreamsocksgeterrorsubdomain(__).md>). Possible return values (beyond subdomain-specific values such as client versions and HTTP error codes) are listed in [Secure Sockets (SOCKS) Errors](1518266-secure-sockets-socks-errors.md).

## See Also

### Streams

- [CFReadStreamCreateForHTTPRequest](<cfreadstreamcreateforhttprequest(____).md>) — Creates a read stream for a CFHTTP request message. _(deprecated)_
- [CFReadStreamCreateForStreamedHTTPRequest](<cfreadstreamcreateforstreamedhttprequest(______).md>) — Creates a read stream for a CFHTTP request message object whose body is too long to keep in memory. _(deprecated)_
- [kCFStreamPropertyHTTPAttemptPersistentConnection](kcfstreampropertyhttpattemptpersistentconnection.md) _(deprecated)_
- [kCFStreamPropertyHTTPFinalRequest](kcfstreampropertyhttpfinalrequest.md) — HTTP Final Request property. A value of type CFHTTPMessage containing the final message transmitted by the stream after all modifications (including authentication, connection policy, redirects, and so on) have been made. This property cannot be set. _(deprecated)_
- [kCFStreamPropertyHTTPFinalURL](kcfstreampropertyhttpfinalurl.md) — HTTP Final URL property. A value of type CFURL containing the final HTTP URL. This value differs from the URL in the original HTTP request if an autoredirection occurred. This property cannot be set. _(deprecated)_
- [kCFStreamPropertyHTTPProxy](kcfstreampropertyhttpproxy.md) _(deprecated)_
- [kCFStreamPropertyHTTPProxyHost](kcfstreampropertyhttpproxyhost.md) _(deprecated)_
- [kCFStreamPropertyHTTPProxyPort](kcfstreampropertyhttpproxyport.md) _(deprecated)_
- [kCFStreamPropertyHTTPRequestBytesWrittenCount](kcfstreampropertyhttprequestbyteswrittencount.md) _(deprecated)_
- [kCFStreamPropertyHTTPResponseHeader](kcfstreampropertyhttpresponseheader.md) — HTTP Response Header property. When copied by [CFReadStreamCopyProperty(_:_:)](<../corefoundation/cfreadstreamcopyproperty(____).md>), the header of an HTTP response message is returned. _(deprecated)_
- [kCFStreamPropertyHTTPSProxyHost](kcfstreampropertyhttpsproxyhost.md) _(deprecated)_
- [kCFStreamPropertyHTTPSProxyPort](kcfstreampropertyhttpsproxyport.md) _(deprecated)_
- [kCFStreamPropertyHTTPShouldAutoredirect](kcfstreampropertyhttpshouldautoredirect.md) — HTTP Should Auto Redirect property. Set this property to `kCFBooleanTrue` to enable autoredirection; set this property to `kCFBooleanFalse` to disable autoredirection. _(deprecated)_
- [CFWriteStreamCreateWithFTPURL](<cfwritestreamcreatewithftpurl(____).md>) — Creates an FTP write stream. _(deprecated)_
- [CFReadStreamCreateWithFTPURL](<cfreadstreamcreatewithftpurl(____).md>) — Creates an FTP read stream. _(deprecated)_
