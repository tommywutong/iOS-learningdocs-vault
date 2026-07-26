---
title: invalidate()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsbackgroundactivityscheduler/invalidate()
source_url: 'https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/invalidate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbackgroundactivityscheduler/invalidate%28%29.json'
content_hash: 'sha256:5752286c20c1c8ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBackgroundActivityScheduler](../nsbackgroundactivityscheduler.md)

# invalidate()

<sub>Instance Method</sub>

Prevents the background activity from being scheduled again.

<sub>macOS</sub>

```swift
func invalidate()
```

## Discussion

When `invalidate` is used to stop an activity that is currently executing, the activity will still finish executing.

See [Stop Activity](../nsbackgroundactivityscheduler.md#Stop-Activity).
