---
title: interrupt()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/process/interrupt()
source_url: 'https://developer.apple.com/documentation/foundation/process/interrupt()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/process/interrupt%28%29.json'
content_hash: 'sha256:91227d5bc58b34b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Process](../process.md)

# interrupt()

<sub>Instance Method</sub>

Sends an interrupt signal to the receiver and all of its subtasks.

<sub>Mac Catalyst, macOS</sub>

```swift
func interrupt()
```

## Discussion

If the task terminates as a result, which is the default behavior, an [NSTaskDidTerminateNotification](didterminatenotification.md) gets sent to the default notification center. This method has no effect if the receiver was already launched and has already finished executing. If the system hasn’t launched the receiver, this method raises an `NSInvalidArgumentException`.

It isn’t always possible to interrupt the receiver because it might be ignoring the interrupt signal. The [- interrupt](<interrupt().md>) method sends `SIGINT`.

## See Also

### Running and stopping

- [- launchAndReturnError:](<run().md>) — Runs the process with the current environment.
- [- resume](<resume().md>) — Resumes execution of a suspended task.
- [- suspend](<suspend().md>) — Suspends execution of the receiver task.
- [- terminate](<terminate().md>) — Sends a terminate signal to the receiver and all of its subtasks.
- [- waitUntilExit](<waituntilexit().md>) — Blocks the process until the receiver is finished.
