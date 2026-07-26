---
title: 'userActivityWasContinued(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuseractivitydelegate/useractivitywascontinued(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivitydelegate/useractivitywascontinued(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivitydelegate/useractivitywascontinued%28_%3A%29.json'
content_hash: 'sha256:d35826b8ebd83815'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivityDelegate](../nsuseractivitydelegate.md)

# userActivityWasContinued(_:)

<sub>Instance Method</sub>

Notifies the delegate that the user activity was continued on another device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func userActivityWasContinued(_ userActivity: NSUserActivity)
```

## Parameters

- `userActivity` — The user activity that was continued.

## See Also

### Managing activity continuation

- [- userActivityWillSave:](<useractivitywillsave(__).md>) — Notifies the delegate that the user activity will be saved to be continued or persisted.
