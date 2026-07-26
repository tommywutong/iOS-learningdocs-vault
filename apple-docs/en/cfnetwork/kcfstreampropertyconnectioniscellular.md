---
title: kCFStreamPropertyConnectionIsCellular
framework: CFNetwork
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/cfnetwork/kcfstreampropertyconnectioniscellular
source_url: 'https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyconnectioniscellular'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cfnetwork/kcfstreampropertyconnectioniscellular.json'
content_hash: 'sha256:b58a228f7c75a0e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [CFNetwork](../cfnetwork.md)

# kCFStreamPropertyConnectionIsCellular

<sub>Global Variable</sub>

A boolean value indicating whether the stream is connected over a cellular (WWAN) interface. This is a read-only property, and is `false` until the connection has been established.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let kCFStreamPropertyConnectionIsCellular: CFString
```

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
