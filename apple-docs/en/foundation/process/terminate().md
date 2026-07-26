---
title: terminate()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/terminate()
source_url: 'https://developer.apple.com/documentation/foundation/process/terminate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/terminate%28%29.json'
content_hash: 'sha256:d057bfb3665c28f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# terminate()

<sub>Instance Method</sub>

Sends a terminate signal to the receiver and all of its subtasks.

<sub>Mac Catalyst, macOS</sub>

```swift
func terminate()
```

## Discussion

If the task terminates as a result, which is the default behavior, an [NSTaskDidTerminateNotification](didterminatenotification.md) gets sent to the default notification center. This method has no effect if the receiver was already launched and has already finished executing. If the receiver hasn’t been launched yet, this method raises an `NSInvalidArgumentException`.

It’s not always possible to terminate the receiver because it might be ignoring the terminate signal. The [- terminate](<terminate().md>) method sends `SIGTERM`.

## See Also

### Related Documentation

- [- launch](<launch().md>) — Launches the task represented by the receiver. _(deprecated)_
- [+ launchedTaskWithLaunchPath:arguments:](<launchedprocess(launchpath_arguments_).md>) — Creates and launches a task with a specified executable and arguments. _(deprecated)_
- [terminationStatus](terminationstatus.md) — The exit status the receiver’s executable returns.

### Running and stopping

- [- launchAndReturnError:](<run().md>) — Runs the process with the current environment.
- [- interrupt](<interrupt().md>) — Sends an interrupt signal to the receiver and all of its subtasks.
- [- resume](<resume().md>) — Resumes execution of a suspended task.
- [- suspend](<suspend().md>) — Suspends execution of the receiver task.
- [- waitUntilExit](<waituntilexit().md>) — Blocks the process until the receiver is finished.
