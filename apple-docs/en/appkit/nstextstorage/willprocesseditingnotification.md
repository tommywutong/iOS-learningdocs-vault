---
title: willProcessEditingNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstextstorage/willprocesseditingnotification
source_url: 'https://developer.apple.com/documentation/appkit/nstextstorage/willprocesseditingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextstorage/willprocesseditingnotification.json'
content_hash: 'sha256:0d102df2cc2cec40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextStorage](../nstextstorage.md)

# willProcessEditingNotification

<sub>Type Property</sub>

A notification that posts before a text storage begins processing edits.

<sub>macOS</sub>

```swift
class let willProcessEditingNotification: NSNotification.Name
```

## Discussion

The framework posts this notification before a text storage begins processing edits in [- processEditing](<processediting().md>). Observers other than the delegate shouldn’t make further changes to the text storage. The notification object is the text storage object that’s about to process the edits. This notification doesn’t contain a `userInfo` dictionary.

## See Also

### Notifications

- [NSTextStorageDidProcessEditingNotification](didprocesseditingnotification.md) — A notification that posts after a text storage finishes processing edits.
