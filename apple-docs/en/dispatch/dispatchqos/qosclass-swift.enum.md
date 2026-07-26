---
title: DispatchQoS.QoSClass
framework: Dispatch
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqos/qosclass-swift.enum
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqos/qosclass-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqos/qosclass-swift.enum.json'
content_hash: 'sha256:a366d2b017502903'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQoS](../dispatchqos.md)

# DispatchQoS.QoSClass

<sub>Enumeration</sub>

Quality-of-service classes that specify the priorities for executing tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum QoSClass
```

## Overview

Use quality-of-service classes to communicate the intent behind the work that your app performs. The system uses those intentions to determine the best way to execute your tasks given the available resources. For example, the system gives higher priority to threads that contain user-interactive tasks to ensure that those tasks are executed quickly. Conversely, it gives lower priority to background tasks, and may attempt to save power by executing them on more power-efficient CPU cores. The system determines how to execute your tasks dynamically based on system conditions and the tasks you schedule.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the Quality-of-Service Class

- [DispatchQoS.QoSClass.userInteractive](qosclass-swift.enum/userinteractive.md) — The quality-of-service class for user-interactive tasks, such as animations, event handling, or updating your app’s user interface.
- [DispatchQoS.QoSClass.userInitiated](qosclass-swift.enum/userinitiated.md) — The quality-of-service class for tasks that prevent the user from actively using your app.
- [DispatchQoS.QoSClass.default](qosclass-swift.enum/default.md) — The default quality-of-service class.
- [DispatchQoS.QoSClass.utility](qosclass-swift.enum/utility.md) — The quality-of-service class for tasks that the user does not track actively.
- [DispatchQoS.QoSClass.background](qosclass-swift.enum/background.md) — The quality-of-service class for maintenance or cleanup tasks that you create.
- [DispatchQoS.QoSClass.unspecified](qosclass-swift.enum/unspecified.md) — The absence of a quality-of-service class.

### Initializing the Type

- [init(rawValue:)](<qosclass-swift.enum/init(rawvalue_).md>) — Initializes the type with a raw value.
- [rawValue](qosclass-swift.enum/rawvalue.md) — The value of the raw type.

## See Also

### Creating a QoS Structure

- [init(qosClass:relativePriority:)](<init(qosclass_relativepriority_).md>) — Creates a new `DispatchQoS` object with the specified QoS class and relative priority.
