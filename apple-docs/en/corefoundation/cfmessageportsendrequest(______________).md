---
title: 'CFMessagePortSendRequest(_:_:_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmessageportsendrequest(_:_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportsendrequest(_:_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportsendrequest%28_%3A_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:352956286bec92b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortSendRequest(_:_:_:_:_:_:_:)

<sub>Function</sub>

Sends a message to a remote CFMessagePort object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMessagePortSendRequest(_ remote: CFMessagePort!, _ msgid: Int32, _ data: CFData!, _ sendTimeout: CFTimeInterval, _ rcvTimeout: CFTimeInterval, _ replyMode: CFString!, _ returnData: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> Int32
```

## Parameters

- `remote` — The message port to which `data` should be sent.

- `msgid` — An arbitrary integer value that you can send with the message.

- `data` — The data to send to `remote`.

- `sendTimeout` — The time to wait for `data` to be sent.

- `rcvTimeout` — The time to wait for a reply to be returned.

- `replyMode` — The run loop mode in which the function should wait for a reply. If the message is a `oneway` (so no response is expected), then `replyMode` should be `NULL`. If `replyMode` is non-`NULL`, the function runs the run loop waiting for a reply, in that mode. `replyMode` can be any string name of a run loop mode, but it should be one with input sources installed. You should use the `kCFRunLoopDefaultMode` constant unless you have a specific reason to use a different mode.

- `returnData` — Upon return, contains a CFData object containing the reply data. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Return Value

Error code indicating success or failure. See [CFMessagePortSendRequest Error Codes](1561514-cfmessageportsendrequest-error-c.md) for the possible return values.

## See Also

### Using a Message Port

- [CFMessagePortInvalidate](<cfmessageportinvalidate(__).md>) — Invalidates a CFMessagePort object, stopping it from receiving or sending any more messages.
- [CFMessagePortSetDispatchQueue](<cfmessageportsetdispatchqueue(____).md>) — Schedules callbacks for the specified message port on the specified dispatch queue.
