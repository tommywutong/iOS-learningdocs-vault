---
title: NSBackgroundActivityScheduler.Result.deferred
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsbackgroundactivityscheduler/result/deferred
source_url: 'https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/result/deferred'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbackgroundactivityscheduler/result/deferred.json'
content_hash: 'sha256:6a130be24fdc7d0e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSBackgroundActivityScheduler](../../nsbackgroundactivityscheduler.md) · [Result](../result.md)

# NSBackgroundActivityScheduler.Result.deferred

<sub>Case</sub>

System conditions have changed since the time the activity began executing, and deferral of additional work is recommended.

<sub>macOS</sub>

```swift
case deferred
```

## See Also

### Constants

- [NSBackgroundActivityResultFinished](finished.md) — The activity has finished executing. If the activity repeats, the next invocation is scheduled by the system.
