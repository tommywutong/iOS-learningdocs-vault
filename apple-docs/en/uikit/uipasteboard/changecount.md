---
title: changeCount
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/changecount
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/changecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/changecount.json'
content_hash: 'sha256:2dffa32a67226c38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# changeCount

<sub>Instance Property</sub>

The number of times the pasteboard’s contents change.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var changeCount: Int { get }
```

## Discussion

Whenever the contents of a pasteboard changes—specifically, when pasteboard items are added, modified, or removed—`UIPasteboard` increments the value of this property. After it increments the change count, UIPasteboard posts the notifications named [UIPasteboardChangedNotification](changednotification.md) (for additions and modifications) and [UIPasteboardRemovedNotification](removednotification.md) (for removals). These notifications include (in the `userInfo` dictionary) the types of the pasteboard items added or removed. Because `UIPasteboard` waits until the end of the current event loop before incrementing the change count, notifications can be batched. The class also updates the change count when an app reactivates and another app has changed the pasteboard contents. When users restart a device, the change count is reset to zero.

## See Also

### Getting and setting pasteboard attributes

- [name](name-swift.property.md) — The name of the pasteboard.
