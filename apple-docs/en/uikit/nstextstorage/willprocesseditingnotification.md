---
title: willProcessEditingNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextstorage/willprocesseditingnotification
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorage/willprocesseditingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorage/willprocesseditingnotification.json'
content_hash: 'sha256:8de7b009f2bed444'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorage](../nstextstorage.md)

# willProcessEditingNotification

<sub>Type Property</sub>

A notification that posts before a text storage begins processing edits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class let willProcessEditingNotification: NSNotification.Name
```

## Discussion

The framework posts this notification before a text storage begins processing edits in [- processEditing](<processediting().md>). Observers other than the delegate shouldn’t make further changes to the text storage. The notification object is the text storage object that’s about to process the edits. This notification doesn’t contain a `userInfo` dictionary.

## See Also

### Notifications

- [NSTextStorageDidProcessEditingNotification](didprocesseditingnotification.md) — A notification that posts after a text storage finishes processing edits.
