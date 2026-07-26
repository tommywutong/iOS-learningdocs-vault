---
title: 'CFMessagePortInvalidate(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmessageportinvalidate(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportinvalidate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportinvalidate%28_%3A%29.json'
content_hash: 'sha256:a1c603beb7fb13d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortInvalidate(_:)

<sub>Function</sub>

Invalidates a CFMessagePort object, stopping it from receiving or sending any more messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMessagePortInvalidate(_ ms: CFMessagePort!)
```

## Parameters

- `ms` — The message port to invalidate.

## Discussion

Invalidating a message port prevents the port from ever sending or receiving any more messages; the message port is not deallocated, though. If the port has not already been invalidated, the port’s invalidation callback function is invoked, if one has been set with [CFMessagePortSetInvalidationCallBack](<cfmessageportsetinvalidationcallback(____).md>). The [CFMessagePortContext](cfmessageportcontext.md)  `info` information for `ms` is also released, if a release callback was specified in the port’s context structure. Finally, if a run loop source was created for `ms`, the run loop source is also invalidated.

## See Also

### Using a Message Port

- [CFMessagePortSendRequest](<cfmessageportsendrequest(______________).md>) — Sends a message to a remote CFMessagePort object.
- [CFMessagePortSetDispatchQueue](<cfmessageportsetdispatchqueue(____).md>) — Schedules callbacks for the specified message port on the specified dispatch queue.
