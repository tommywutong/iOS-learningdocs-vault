---
title: 'CFMessagePortSetDispatchQueue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmessageportsetdispatchqueue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportsetdispatchqueue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportsetdispatchqueue%28_%3A_%3A%29.json'
content_hash: 'sha256:05705ce0106779cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortSetDispatchQueue(_:_:)

<sub>Function</sub>

Schedules callbacks for the specified message port on the specified dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMessagePortSetDispatchQueue(_ ms: CFMessagePort!, _ queue: dispatch_queue_t!)
```

## Parameters

- `ms` — The message port to schedule.

- `queue` — The libdispatch queue.

## See Also

### Using a Message Port

- [CFMessagePortInvalidate](<cfmessageportinvalidate(__).md>) — Invalidates a CFMessagePort object, stopping it from receiving or sending any more messages.
- [CFMessagePortSendRequest](<cfmessageportsendrequest(______________).md>) — Sends a message to a remote CFMessagePort object.
