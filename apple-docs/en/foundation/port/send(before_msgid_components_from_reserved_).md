---
title: 'send(before:msgid:components:from:reserved:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/port/send(before:msgid:components:from:reserved:)'
source_url: 'https://developer.apple.com/documentation/foundation/port/send(before:msgid:components:from:reserved:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/port/send%28before%3Amsgid%3Acomponents%3Afrom%3Areserved%3A%29.json'
content_hash: 'sha256:ad9ca3eea7b73486'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Port](../port.md)

# send(before:msgid:components:from:reserved:)

<sub>Instance Method</sub>

This method is provided for subclasses that have custom types of `NSPort`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func send(before limitDate: Date, msgid msgID: Int, components: NSMutableArray?, from receivePort: Port?, reserved headerSpaceReserved: Int) -> Bool
```

## Parameters

- `limitDate` — The last instant that a message may be sent.

- `msgID` — The message ID.

- `components` — The message components.

- `receivePort` — The receive port.

- `headerSpaceReserved` — The number of bytes reserved for the header.

## Discussion

`NSConnection` calls this method at the appropriate times. This method should not be called directly. This method could raise an `NSInvalidSendPortException`, `NSInvalidReceivePortException`, or an `NSPortSendException`, depending on the type of send port and the type of error.

## See Also

### Setting information

- [- sendBeforeDate:components:from:reserved:](<send(before_components_from_reserved_).md>) — This method is provided for subclasses that have custom types of `NSPort`.
- [reservedSpaceLength](reservedspacelength.md) — The number of bytes of space reserved by the receiver for sending data.
