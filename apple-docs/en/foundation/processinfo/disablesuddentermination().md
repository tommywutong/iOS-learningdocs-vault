---
title: disableSuddenTermination()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.6+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/disablesuddentermination()
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/disablesuddentermination()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/disablesuddentermination%28%29.json'
content_hash: 'sha256:a4bccdf314318694'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# disableSuddenTermination()

<sub>Instance Method</sub>

Disables the application for quickly killing using sudden termination.

<sub>macOS</sub>

```swift
func disableSuddenTermination()
```

## Discussion

This method increments the sudden termination counter. When the termination counter reaches `0` the application allows sudden termination.

By default the sudden termination counter is set to 1. This can be overridden in your application Info.plist. See [Support Sudden Termination](../processinfo.md#Support-Sudden-Termination) for more information and debugging suggestions.

## See Also

### Working with sudden application termination

- [- enableSuddenTermination](<enablesuddentermination().md>) — Enables the application for quick killing using sudden termination.
