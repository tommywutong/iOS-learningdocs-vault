---
title: userInfo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/userinfo
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/userinfo.json'
content_hash: 'sha256:94b122fbbeacb9df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# userInfo

<sub>Instance Property</sub>

A dictionary containing app-specific state information needed to continue an activity on another device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var userInfo: [AnyHashable : Any]? { get set }
```

## Discussion

Each key and value must be of the following types: [NSArray](../nsarray.md), [NSData](../nsdata.md), [NSDate](../nsdate.md), [NSDictionary](../nsdictionary.md), [NSNull](../nsnull.md), [NSNumber](../nsnumber.md), [NSSet](../nsset.md), [NSString](../nsstring.md), or [NSURL](../nsurl.md). The system may translate file scheme URLs that refer to iCloud documents to valid file URLs on a continuing device.

## See Also

### Specifying activity-related data

- [- addUserInfoEntriesFromDictionary:](<adduserinfoentries(from_).md>) — Adds the contents of the specified dictionary to the user info dictionary.
- [requiredUserInfoKeys](requireduserinfokeys.md) — A set of keys that represent the minimal information about the activity that should be stored for later restoration.
