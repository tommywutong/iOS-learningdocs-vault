---
title: DispatchQoS
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqos
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqos.json'
content_hash: 'sha256:5b840256a0818af6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchQoS

<sub>Structure</sub>

The quality of service, or the execution priority, to apply to tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DispatchQoS
```

## Overview

A quality-of-service (QoS) class categorizes work to perform on a [DispatchQueue](dispatchqueue.md). By specifying the quality of a task, you indicate its importance to your app. When scheduling tasks, the system prioritizes those that have higher service classes.

Because higher priority work is performed more quickly and with more resources than lower priority work, it typically requires more energy than lower priority work. Accurately specifying appropriate QoS classes for the work your app performs ensures that your app is responsive and energy efficient.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the Predefined QoS Objects

- [userInteractive](dispatchqos/userinteractive.md) — The quality-of-service class for user-interactive tasks, such as animations, event handling, or updates to your app’s user interface.
- [userInitiated](dispatchqos/userinitiated.md) — The quality-of-service class for tasks that prevent the user from actively using your app.
- [default](dispatchqos/default.md) — The default quality-of-service class.
- [utility](dispatchqos/utility.md) — The quality-of-service class for tasks that the user does not track actively.
- [background](dispatchqos/background.md) — The quality-of-service class for maintenance or cleanup tasks that you create.
- [unspecified](dispatchqos/unspecified.md) — The absence of a quality-of-service class.

### Creating a QoS Structure

- [init(qosClass:relativePriority:)](<dispatchqos/init(qosclass_relativepriority_).md>) — Creates a new `DispatchQoS` object with the specified QoS class and relative priority.
- [QoSClass](dispatchqos/qosclass-swift.enum.md) — Quality-of-service classes that specify the priorities for executing tasks.

### Getting the QoS Attributes

- [qosClass](dispatchqos/qosclass-swift.property.md) — The quality-of-service class.
- [relativePriority](dispatchqos/relativepriority.md) — The priority of a quality of service relative to others with the same class.
