---
title: NSURLErrorCancelledReasonInsufficientSystemResources
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlerrorcancelledreasoninsufficientsystemresources
source_url: 'https://developer.apple.com/documentation/foundation/nsurlerrorcancelledreasoninsufficientsystemresources'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlerrorcancelledreasoninsufficientsystemresources.json'
content_hash: 'sha256:cb12ae97e20c284f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLErrorCancelledReasonInsufficientSystemResources

<sub>Global Variable</sub>

A reason that indicates the system canceled the background task because it lacks sufficient resources to perform the task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSURLErrorCancelledReasonInsufficientSystemResources: Int { get }
```

## Discussion

This error results from factors including (but not limited to) battery capacity, thermal condition, network connectivity, and cellular data plan.

## See Also

### Cancellation reasons

- [NSURLErrorCancelledReasonBackgroundUpdatesDisabled](nsurlerrorcancelledreasonbackgroundupdatesdisabled.md) — A reason that indicates the system canceled the background task because background tasks are disabled.
- [NSURLErrorCancelledReasonUserForceQuitApplication](nsurlerrorcancelledreasonuserforcequitapplication.md) — A reason that indicates the system canceled the background task because the user force-quit the application.
