---
title: didTerminateNotification
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/didterminatenotification
source_url: 'https://developer.apple.com/documentation/foundation/process/didterminatenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/didterminatenotification.json'
content_hash: 'sha256:ee92c4203a00dedb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# didTerminateNotification

<sub>Type Property</sub>

Posted when the task has stopped execution.

<sub>Mac Catalyst, macOS</sub>

```swift
class let didTerminateNotification: NSNotification.Name
```

## Discussion

The notification object is the `NSTask` object that the system terminated. This notification doesn’t contain a `userInfo` dictionary.

The system posts this notification from the thread in which the `NSTask` object called [- launch](<launch().md>). When launching a task from a secondary thread or background queue, you can use the [terminationHandler](terminationhandler.md) property instead for greater control over the execution context of any operations to be performed after the task finishes.

This notification can be posted either when the task has exited normally or as a result of [- terminate](<terminate().md>) being sent to the `NSTask` object. If the `NSTask` object gets released, however, this notification won’t get sent, as the port the message would have been sent on was released as part of the task release. The observer method can use [terminationStatus](terminationstatus.md) to determine why the task died.
