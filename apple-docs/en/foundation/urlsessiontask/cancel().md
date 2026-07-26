---
title: cancel()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontask/cancel()
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontask/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontask/cancel%28%29.json'
content_hash: 'sha256:56de243f4880885d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTask](../urlsessiontask.md)

# cancel()

<sub>Instance Method</sub>

Cancels the task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

This method returns immediately, marking the task as being canceled. Once a task is marked as being canceled, [- URLSession:task:didCompleteWithError:](<../urlsessiontaskdelegate/urlsession(__task_didcompletewitherror_).md>) will be sent to the task delegate, passing an error in the domain [NSURLErrorDomain](../nsurlerrordomain.md) with the code [NSURLErrorCancelled](../nsurlerrorcancelled-swift.var.md). A task may, under some circumstances, send messages to its delegate before the cancelation is acknowledged.

This method may be called on a task that is suspended.

## See Also

### Related Documentation

- [- cancelByProducingResumeData:](<../urlsessiondownloadtask/cancel(byproducingresumedata_).md>) — Cancels a download and calls a callback with resume data for later use.

### Controlling the task state

- [- resume](<resume().md>) — Resumes the task, if it is suspended.
- [- suspend](<suspend().md>) — Temporarily suspends a task.
- [state](state-swift.property.md) — The current state of the task—active, suspended, in the process of being canceled, or completed.
- [State](state-swift.enum.md) — Constants for determining the current state of a task.
- [priority](priority.md) — The relative priority at which you’d like a host to handle the task, specified as a floating point value between `0.0` (lowest priority) and `1.0` (highest priority).
- [URL session task priority](../url-session-task-priority.md) — Constants for providing task priority hints to a host, used with the [priority](priority.md) property.
