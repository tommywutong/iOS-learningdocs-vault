---
title: 'disableAutomaticTermination(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/processinfo/disableautomatictermination(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/disableautomatictermination(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/disableautomatictermination%28_%3A%29.json'
content_hash: 'sha256:6ca2a4ffae85756b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# disableAutomaticTermination(_:)

<sub>Instance Method</sub>

Disables automatic termination for the application.

<sub>macOS</sub>

```swift
func disableAutomaticTermination(_ reason: String)
```

## Parameters

- `reason` — The reason why automatic termination is being disabled.

## Discussion

This method increments the automatic termination counter. When the counter is greater than `0`, the application is considered active and ineligible for automatic termination. For example, you could disable automatic termination when the user of an instant messaging application signs on, because the application requires a background connection to be maintained even if the application is otherwise inactive.

The reason parameter is used to track why an application is or is not automatically terminable and can be inspected by debugging tools. For example, you could pass the string `@"file transfer in progress"` if you disable automatic termination before transferring a file over the network. When you reenable automatic termination after the transfer is complete using [- enableAutomaticTermination:](<enableautomatictermination(__).md>), you should pass the matching string. A given reason can be used more than once at the same time; for example, if two files were being transferred at the same time, automatic termination could be disabled for each, passing the same reason string.

## See Also

### Controlling automatic termination

- [- enableAutomaticTermination:](<enableautomatictermination(__).md>) — Enables automatic termination for the application.
- [automaticTerminationSupportEnabled](automaticterminationsupportenabled.md) — A Boolean value indicating whether the app supports automatic termination.
