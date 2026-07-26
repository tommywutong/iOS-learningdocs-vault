---
title: 'dispatchRawAppleEvent(_:withRawReply:handlerRefCon:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventmanager/dispatchrawappleevent(_:withrawreply:handlerrefcon:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventmanager/dispatchrawappleevent(_:withrawreply:handlerrefcon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventmanager/dispatchrawappleevent%28_%3Awithrawreply%3Ahandlerrefcon%3A%29.json'
content_hash: 'sha256:b66de4b238973d03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventManager](../nsappleeventmanager.md)

# dispatchRawAppleEvent(_:withRawReply:handlerRefCon:)

<sub>Instance Method</sub>

Causes the Apple event specified by `theAppleEvent` to be dispatched to the appropriate Apple event handler, if one has been registered by calling [- setEventHandler:andSelector:forEventClass:andEventID:](<seteventhandler(__andselector_foreventclass_andeventid_).md>).

<sub>Mac Catalyst, macOS</sub>

```swift
func dispatchRawAppleEvent(_ theAppleEvent: UnsafePointer<AppleEvent>, withRawReply theReply: UnsafeMutablePointer<AppleEvent>, handlerRefCon: SRefCon) -> OSErr
```

## Discussion

The `theReply` parameter always specifies a reply Apple event, never `nil`. However, the handler should not fill out the reply if the descriptor type for the reply event is `typeNull`, indicating the sender does not want a reply.

The `handlerRefcon` parameter provides 4 bytes of data to the handler; a common use for this parameter is to pass a pointer to additional data.

This method is primarily intended for Cocoa’s internal use. Note that _dispatching_ an event means routing an event to an appropriate handler in the current application. You cannot use this method to _send_ an event to other applications.
