---
title: terminationStatus
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/terminationstatus
source_url: 'https://developer.apple.com/documentation/foundation/process/terminationstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/terminationstatus.json'
content_hash: 'sha256:68e1fcb3e0be9026'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# terminationStatus

<sub>Instance Property</sub>

The exit status the receiver’s executable returns.

<sub>Mac Catalyst, macOS</sub>

```swift
var terminationStatus: Int32 { get }
```

## Return Value

The exit status returned by the receiver’s executable.

## Discussion

Each task defines and documents how your app should interpret the return value. For example, many commands return 0 if they complete successfully or an error code if they don’t. You’ll need to look at the documentation for that task to learn what values it returns under what circumstances.

This method raises an `NSInvalidArgumentException` if the receiver is still running. Verify that the receiver isn’t running before you use it.

**Swift**

```swift
let task: NSTask = // Create and initialize a task
if !task.isRunning {
    let status = task.terminationStatus
    if status == 0 {
        print("Task succeeded.")
    } else {
        print("Task failed.")
    }
}
```

**Objective-C**

```objc
NSTask *task = // Create and initialize a task
if (![task isRunning]) {
    int status = [task terminationStatus];
    if (status == 0) {
        NSLog(@"Task succeeded.");
    } else {
        NSLog(@"Task failed.");
    }
}
```

## See Also

### Related Documentation

- [- waitUntilExit](<waituntilexit().md>) — Blocks the process until the receiver is finished.
- [- terminate](<terminate().md>) — Sends a terminate signal to the receiver and all of its subtasks.

### Querying the process state

- [running](isrunning.md) — A status that indicates whether the receiver is still running.
- [terminationReason](terminationreason-swift.property.md) — The reason the system terminated the task.
