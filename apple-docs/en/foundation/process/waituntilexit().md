---
title: waitUntilExit()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/waituntilexit()
source_url: 'https://developer.apple.com/documentation/foundation/process/waituntilexit()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/waituntilexit%28%29.json'
content_hash: 'sha256:69dff7fdadcc30d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# waitUntilExit()

<sub>Instance Method</sub>

Blocks the process until the receiver is finished.

<sub>Mac Catalyst, macOS</sub>

```swift
func waitUntilExit()
```

## Discussion

This method first checks to see if the receiver is still running using [running](isrunning.md). Then it polls the current run loop using `NSDefaultRunLoopMode` until the task completes.

**Swift**

```swift
let task: NSTask = // Create and initialize a task
    task.launch()
task.waitUntilExit()
let status = task.terminationStatus
 
if status == 0 {
    print("Task succeeded.")
} else {
    print("Task failed.")
}
```

**Objective-C**

```objc
NSTask *task = // Create and initialize a task
[task launch];
[task waitUntilExit];
int status = [task terminationStatus];
 
if (status == 0) {
    NSLog(@"Task succeeded.");
} else {
    NSLog(@"Task failed.");
}
```

[- waitUntilExit](<waituntilexit().md>) does not guarantee that the [terminationHandler](terminationhandler.md) block has been fully executed before [- waitUntilExit](<waituntilexit().md>) returns.

## See Also

### Related Documentation

- [- launch](<launch().md>) — Launches the task represented by the receiver. _(deprecated)_

### Running and stopping

- [- launchAndReturnError:](<run().md>) — Runs the process with the current environment.
- [- interrupt](<interrupt().md>) — Sends an interrupt signal to the receiver and all of its subtasks.
- [- resume](<resume().md>) — Resumes execution of a suspended task.
- [- suspend](<suspend().md>) — Suspends execution of the receiver task.
- [- terminate](<terminate().md>) — Sends a terminate signal to the receiver and all of its subtasks.
