---
title: didProcessEditingNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstextstorage/didprocesseditingnotification
source_url: 'https://developer.apple.com/documentation/appkit/nstextstorage/didprocesseditingnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextstorage/didprocesseditingnotification.json'
content_hash: 'sha256:ed86ece8f3f53ba2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextStorage](../nstextstorage.md)

# didProcessEditingNotification

<sub>Type Property</sub>

A notification that posts after a text storage finishes processing edits.

<sub>macOS</sub>

```swift
class let didProcessEditingNotification: NSNotification.Name
```

## Discussion

The framework posts this notification after a text storage finishes processing edits in [- processEditing](<processediting().md>). Observers other than the delegate shouldn’t make further changes to the text storage. The notification object is the text storage object that processed the edits. This notification doesn’t contain a `userInfo` dictionary.

## See Also

### Notifications

- [NSTextStorageWillProcessEditingNotification](willprocesseditingnotification.md) — A notification that posts before a text storage begins processing edits.
