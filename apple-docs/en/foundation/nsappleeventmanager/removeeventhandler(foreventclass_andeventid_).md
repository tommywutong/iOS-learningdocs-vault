---
title: 'removeEventHandler(forEventClass:andEventID:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventmanager/removeeventhandler(foreventclass:andeventid:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventmanager/removeeventhandler(foreventclass:andeventid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventmanager/removeeventhandler%28foreventclass%3Aandeventid%3A%29.json'
content_hash: 'sha256:9c16140bc3ef2314'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventManager](../nsappleeventmanager.md)

# removeEventHandler(forEventClass:andEventID:)

<sub>Instance Method</sub>

If an Apple event handler has been registered for the event specified by `eventClass` and `eventID`, removes it.

<sub>Mac Catalyst, macOS</sub>

```swift
func removeEventHandler(forEventClass eventClass: AEEventClass, andEventID eventID: AEEventID)
```

## Discussion

Otherwise does nothing.

## See Also

### Working with event handlers

- [- setEventHandler:andSelector:forEventClass:andEventID:](<seteventhandler(__andselector_foreventclass_andeventid_).md>) — Registers the Apple event handler specified by `handler` for the event specified by `eventClass` and `eventID`.
