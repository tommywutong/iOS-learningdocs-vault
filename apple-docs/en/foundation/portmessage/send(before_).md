---
title: 'send(before:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/portmessage/send(before:)'
source_url: 'https://developer.apple.com/documentation/foundation/portmessage/send(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/portmessage/send%28before%3A%29.json'
content_hash: 'sha256:0d051eef5a252d7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PortMessage](../portmessage.md)

# send(before:)

<sub>Instance Method</sub>

Attempts to send the message before the specified date.

<sub>Mac Catalyst, macOS</sub>

```swift
func send(before date: Date) -> Bool
```

## Parameters

- `date` — The instant before which the message should be sent.

## Return Value

[true](../../swift/true.md) if the operation is successful, otherwise [false](../../swift/false.md) (for example, if the operation times out).

## Discussion

If an error other than a time out occurs, this method could raise an `NSInvalidSendPortException`, `NSInvalidReceivePortException`, or an `NSPortSendException`, depending on the type of send port and the type of error.

If the message cannot be sent immediately, the sending thread blocks until either the message is sent or `aDate` is reached. Sent messages are queued to minimize blocking, but failure can occur if multiple messages are sent to a port faster than the port’s owner can receive them, causing the queue to fill up. Therefore, select a value for `aDate` that provides enough time for the message to be processed before the next message is sent. See the [Port](../port.md) class specification for information on receiving a port message.
