---
title: UIActivityItemProvider
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemprovider
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemprovider.json'
content_hash: 'sha256:2582f1b6f5af07a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIActivityItemProvider

<sub>Class</sub>

A proxy for data that passes to an activity view controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class UIActivityItemProvider
```

## Overview

You can use a provider object in situations where you want to make data available for use by an activity but you want to delay providing that data until it’s actually needed. For example, you might use a provider object to represent a large video file that needs to be processed before it can be shared to a user’s social media account.

When you initialize a [UIActivityViewController](uiactivityviewcontroller.md) object, you can pass a provider object in addition to any other data objects. When the user selects an activity, the activity view controller adds your provider object (which is also an operation object) to an operation queue so that it can begin to gather or process the needed data.

### Subclassing notes

You must subclass `UIActivityItemProvider` and implement its [item](uiactivityitemprovider/item.md) method, which is called to generate the item data. You implement this method instead of the normal [main()](<../foundation/operation/main().md>) method you’d implement for an operation object. (The [main()](<../foundation/operation/main().md>) method calls the [item](uiactivityitemprovider/item.md) method when the operation object is executed.) Your implementation of the [item](uiactivityitemprovider/item.md) method should do whatever work is necessary to create and return the data.

## Relationships

- **Inherits From**: [Operation](../foundation/operation.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemSource](uiactivityitemsource.md)

## Topics

### Initializing the provider

- [- initWithPlaceholderItem:](<uiactivityitemprovider/init(placeholderitem_).md>) — Initializes and returns a provider object with the specified placeholder data.

### Accessing the provider attributes

- [item](uiactivityitemprovider/item.md) — Generates and returns the actual data-bearing object.
- [placeholderItem](uiactivityitemprovider/placeholderitem.md) — The placeholder object you specified at initialization time.
- [activityType](uiactivityitemprovider/activitytype.md) — The type of the activity object that is expecting the data.

## See Also

### Services

- [UIActivity](uiactivity.md) — An abstract class that you subclass to implement app-specific services.
- [UIActivityViewController](uiactivityviewcontroller.md) — A view controller that you use to offer standard services from your app.
- [UIActivityItemSource](uiactivityitemsource.md) — A set of methods that an activity view controller uses to retrieve the data items to act on.
