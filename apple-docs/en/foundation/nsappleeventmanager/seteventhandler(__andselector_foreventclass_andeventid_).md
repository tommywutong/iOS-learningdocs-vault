---
title: 'setEventHandler(_:andSelector:forEventClass:andEventID:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventmanager/seteventhandler(_:andselector:foreventclass:andeventid:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventmanager/seteventhandler(_:andselector:foreventclass:andeventid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventmanager/seteventhandler%28_%3Aandselector%3Aforeventclass%3Aandeventid%3A%29.json'
content_hash: 'sha256:3ac3e8dd1a800c25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventManager](../nsappleeventmanager.md)

# setEventHandler(_:andSelector:forEventClass:andEventID:)

<sub>Instance Method</sub>

Registers the Apple event handler specified by `handler` for the event specified by `eventClass` and `eventID`.

<sub>Mac Catalyst, macOS</sub>

```swift
func setEventHandler(_ handler: Any, andSelector handleEventSelector: Selector, forEventClass eventClass: AEEventClass, andEventID eventID: AEEventID)
```

## Discussion

If an event handler is already registered for the specified event class and event ID, removes it. The signature for `handler` should match the following:

```objc
- (void)handleAppleEvent:(NSAppleEventDescriptor *)event withReplyEvent: (NSAppleEventDescriptor *)replyEvent;
```

## See Also

### Working with event handlers

- [- removeEventHandlerForEventClass:andEventID:](<removeeventhandler(foreventclass_andeventid_).md>) — If an Apple event handler has been registered for the event specified by `eventClass` and `eventID`, removes it.
