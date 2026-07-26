---
title: DispatchSourceUserDataAdd
framework: Dispatch
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourceuserdataadd
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceuserdataadd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceuserdataadd.json'
content_hash: 'sha256:56146f5098358f73'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSourceUserDataAdd

<sub>Protocol</sub>

A dispatch source that coalesces data you provide using an AND operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DispatchSourceUserDataAdd : DispatchSourceProtocol, Sendable
```

## Overview

You do not adopt this protocol in your objects. Instead, use the [makeUserDataAddSource(queue:)](<dispatchsource/makeuserdataaddsource(queue_).md>) method to create an object that adopts this protocol.

To add custom data to the dispatch source, call the [add(data:)](<dispatchsourceuserdataadd/add(data_).md>) method.

## Relationships

- **Inherits From**: [DispatchSourceProtocol](dispatchsourceprotocol.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DispatchSource](dispatchsource.md)

## Topics

### Getting the Event Data

- [add(data:)](<dispatchsourceuserdataadd/add(data_).md>) — Adds the value to the current pending data.

## See Also

### Creating a Custom Source

- [makeUserDataAddSource(queue:)](<dispatchsource/makeuserdataaddsource(queue_).md>) — Creates a new dispatch source object that you use to coalesce custom app data using an AND operator.
- [makeUserDataOrSource(queue:)](<dispatchsource/makeuserdataorsource(queue_).md>) — Creates a new dispatch source object that you use to coalesce custom app data using an OR operator.
- [makeUserDataReplaceSource(queue:)](<dispatchsource/makeuserdatareplacesource(queue_).md>) — Creates a new dispatch source object that you use to track custom app data.
- [DispatchSourceUserDataOr](dispatchsourceuserdataor.md) — A dispatch source that coalesces data you provide using an OR operation.
- [DispatchSourceUserDataReplace](dispatchsourceuserdatareplace.md) — A dispatch source that replaces any pending data with the new value you provide.
