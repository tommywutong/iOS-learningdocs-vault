---
title: NSHTTPCookieManagerAcceptPolicyChanged
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.11 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nshttpcookiemanageracceptpolicychanged
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nshttpcookiemanageracceptpolicychanged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nshttpcookiemanageracceptpolicychanged.json'
content_hash: 'sha256:82755c49a8562487'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSHTTPCookieManagerAcceptPolicyChanged

<sub>Type Property</sub>

A notification posted when the acceptance policy of the cookie storage has changed.

> [!warning] Deprecated
> Notification is never posted

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSHTTPCookieManagerAcceptPolicyChanged: NSNotification.Name
```

## Discussion

In macOS, cookies are shared among applications, meaning this notification can be received as a result of another application’s actions. Cookies are not shared among applications in iOS.

The notification’s [object](../../notification/object.md) is the [HTTPCookieStorage](../../httpcookiestorage.md) instance. This notification does not contain a [userInfo](../../notification/userinfo.md) dictionary.

## See Also

### Tracking cookie storage changes

- [NSHTTPCookieManagerCookiesChangedNotification](nshttpcookiemanagercookieschanged.md) — A notification posted when the cookies stored in the cookie storage have changed.
- [CookiesChangedMessage](../../httpcookiestorage/cookieschangedmessage.md) — A message a cookie storage instance sends when its cookies change.
