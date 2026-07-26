---
title: NSFTPPropertyUserPasswordKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.2+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsftppropertyuserpasswordkey
source_url: 'https://developer.apple.com/documentation/foundation/nsftppropertyuserpasswordkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsftppropertyuserpasswordkey.json'
content_hash: 'sha256:bfe32c113cc5c769'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFTPPropertyUserPasswordKey

<sub>Global Variable</sub>

Key for the user password, returned as an `NSString` object.

> [!warning] Deprecated
> Apple discourages the use of this symbol.

<sub>Mac Catalyst, macOS</sub>

```objc
extern NSString * const NSFTPPropertyUserPasswordKey;
```

## Discussion

The default value for this key is “`NSURLHandle@apple.com`”.

## See Also

### Resource Property Keys

- [NSFTPPropertyActiveTransferModeKey](nsftppropertyactivetransfermodekey.md) — Key for retrieving whether in active transfer mode, returned as a boolean wrapped in an `NSNumber` object. _(deprecated)_
- [NSFTPPropertyFTPProxy](nsftppropertyftpproxy.md) — `NSDictionary` containing proxy information to use in place of proxy identified in `SystemConfiguration.framework`. _(deprecated)_
- [NSFTPPropertyFileOffsetKey](nsftppropertyfileoffsetkey.md) — Key for retrieving the file offset, returned as an `NSNumber` object. The default value for this key is zero. _(deprecated)_
- [NSFTPPropertyUserLoginKey](nsftppropertyuserloginkey.md) — Key for the user login, returned as an `NSString` object. _(deprecated)_
- [NSHTTPPropertyErrorPageDataKey](nshttppropertyerrorpagedatakey.md) — Key for retrieving an error page as an `NSData` object. _(deprecated)_
- [NSHTTPPropertyHTTPProxy](nshttppropertyhttpproxy.md) — Key for retrieving the `NSDictionary` object containing proxy information to use in place of proxy identified in `SystemConfiguration.framework`. _(deprecated)_
- [NSHTTPPropertyRedirectionHeadersKey](nshttppropertyredirectionheaderskey.md) — Key for retrieving the redirection headers as an `NSDictionary` object with each header value keyed to the header name. _(deprecated)_
- [NSHTTPPropertyServerHTTPVersionKey](nshttppropertyserverhttpversionkey.md) — Key for retrieving the HTTP version as an `NSString` object containing the initial server status line up to the first space. _(deprecated)_
- [NSHTTPPropertyStatusCodeKey](nshttppropertystatuscodekey.md) — Key for the status code, returned as an integer wrapped in an `NSNumber` object. _(deprecated)_
- [NSHTTPPropertyStatusReasonKey](nshttppropertystatusreasonkey.md) — Key for the remainder of the HTTP status line following the status code, returned as an `NSString` object. _(deprecated)_
