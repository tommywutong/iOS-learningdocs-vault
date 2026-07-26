---
title: URLSessionTaskMetrics
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontaskmetrics
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskmetrics.json'
content_hash: 'sha256:baf713c349497d6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLSessionTaskMetrics

<sub>Class</sub>

An object encapsulating the metrics for a session task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class URLSessionTaskMetrics
```

## Overview

Each [URLSessionTaskMetrics](urlsessiontaskmetrics.md) object contains the [taskInterval](urlsessiontaskmetrics/taskinterval.md) and [redirectCount](urlsessiontaskmetrics/redirectcount.md), as well as metrics for each request-and-response transaction made during the execution of the task.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating task metrics

- [- init](<urlsessiontaskmetrics/init().md>) — Creates a task metrics instance. _(deprecated)_

### Accessing task metrics

- [transactionMetrics](urlsessiontaskmetrics/transactionmetrics.md) — An array of metrics for each individual request-response transaction made during the execution of the task.
- [URLSessionTaskTransactionMetrics](urlsessiontasktransactionmetrics.md) — An object that encapsualtes the performance metrics collected by the URL Loading System during the execution of a session task.
- [taskInterval](urlsessiontaskmetrics/taskinterval.md) — The time interval between when a task is instantiated and when the task is completed.
- [redirectCount](urlsessiontaskmetrics/redirectcount.md) — The number of redirects that occurred during the execution of the task.

### Type Methods

- [+ new](<urlsessiontaskmetrics/new().md>) — Creates a task metrics instance. _(deprecated)_

## See Also

### Collecting task metrics

- [- URLSession:task:didFinishCollectingMetrics:](<urlsessiontaskdelegate/urlsession(__task_didfinishcollecting_).md>) — Tells the delegate that the session finished collecting metrics for the task.
