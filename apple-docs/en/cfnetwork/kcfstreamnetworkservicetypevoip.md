---
title: kCFStreamNetworkServiceTypeVoIP
framework: CFNetwork
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+（9.0 起废弃）, iPadOS 4.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.11 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/cfnetwork/kcfstreamnetworkservicetypevoip
source_url: 'https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypevoip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cfnetwork/kcfstreamnetworkservicetypevoip.json'
content_hash: 'sha256:9b7ec98fa73dca9b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [CFNetwork](../cfnetwork.md)

# kCFStreamNetworkServiceTypeVoIP

<sub>Global Variable</sub>

Specifies that the stream is providing VoIP service.

> [!warning] Deprecated
> use PushKit for VoIP control purposes

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let kCFStreamNetworkServiceTypeVoIP: CFString
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
