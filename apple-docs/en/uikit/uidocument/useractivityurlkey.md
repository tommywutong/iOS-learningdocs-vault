---
title: userActivityURLKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/useractivityurlkey
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/useractivityurlkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/useractivityurlkey.json'
content_hash: 'sha256:9c60820c8b067a2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# userActivityURLKey

<sub>Type Property</sub>

The key that identifies the document associated with a user activity.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class let userActivityURLKey: String
```

## Discussion

You use this key in the [userInfo](../../foundation/nsuseractivity/userinfo.md) dictionary of an [NSUserActivity](../../foundation/nsuseractivity.md) object. Its value is the URL of the document associated with the user activity.

When the `NSUbiquitousDocumentUserActivityType` key is present in a [CFBundleDocumentTypes](../../bundleresources/information-property-list/cfbundledocumenttypes.md) entry, AppKit automatically creates an [NSUserActivity](../../foundation/nsuseractivity.md) object for documents in iCloud, using the given activity type.

## See Also

### Constants

- [ChangeKind](changekind.md) — Constants that specify the kind of change to a document.
- [SaveOperation](saveoperation.md) — Constants that specify the type of save operation.
- [State](state.md) — Constants that specify the document state.
