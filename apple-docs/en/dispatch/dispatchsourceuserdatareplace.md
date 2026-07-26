---
title: DispatchSourceUserDataReplace
framework: Dispatch
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourceuserdatareplace
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceuserdatareplace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceuserdatareplace.json'
content_hash: 'sha256:44d21f617789d473'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchSourceUserDataReplace

<sub>Protocol</sub>

A dispatch source that replaces any pending data with the new value you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DispatchSourceUserDataReplace : DispatchSourceProtocol, Sendable
```

## Overview

You do not adopt this protocol in your objects. Instead, use the [makeUserDataReplaceSource(queue:)](<dispatchsource/makeuserdatareplacesource(queue_).md>) method to create an object that adopts this protocol.

To replace the pending data in the dispatch source, call the [replace(data:)](<dispatchsourceuserdatareplace/replace(data_).md>) method.

## Relationships

- **Inherits From**: [DispatchSourceProtocol](dispatchsourceprotocol.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [DispatchSource](dispatchsource.md)

## Topics

### Getting the Event Data

- [replace(data:)](<dispatchsourceuserdatareplace/replace(data_).md>) — Replaces the current pending data with the new value you provide.

## See Also

### Creating a Custom Source

- [makeUserDataAddSource(queue:)](<dispatchsource/makeuserdataaddsource(queue_).md>) — Creates a new dispatch source object that you use to coalesce custom app data using an AND operator.
- [makeUserDataOrSource(queue:)](<dispatchsource/makeuserdataorsource(queue_).md>) — Creates a new dispatch source object that you use to coalesce custom app data using an OR operator.
- [makeUserDataReplaceSource(queue:)](<dispatchsource/makeuserdatareplacesource(queue_).md>) — Creates a new dispatch source object that you use to track custom app data.
- [DispatchSourceUserDataAdd](dispatchsourceuserdataadd.md) — A dispatch source that coalesces data you provide using an AND operation.
- [DispatchSourceUserDataOr](dispatchsourceuserdataor.md) — A dispatch source that coalesces data you provide using an OR operation.
