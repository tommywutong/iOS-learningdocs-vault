---
title: didProcessEditingNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextstorage/didprocesseditingnotification
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorage/didprocesseditingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorage/didprocesseditingnotification.json'
content_hash: 'sha256:6f6ceda819fecc8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorage](../nstextstorage.md)

# didProcessEditingNotification

<sub>Type Property</sub>

A notification that posts after a text storage finishes processing edits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class let didProcessEditingNotification: NSNotification.Name
```

## Discussion

The framework posts this notification after a text storage finishes processing edits in [- processEditing](<processediting().md>). Observers other than the delegate shouldn’t make further changes to the text storage. The notification object is the text storage object that processed the edits. This notification doesn’t contain a `userInfo` dictionary.

## See Also

### Notifications

- [NSTextStorageWillProcessEditingNotification](willprocesseditingnotification.md) — A notification that posts before a text storage begins processing edits.
