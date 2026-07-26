---
title: 'userActivityWillSave(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuseractivitydelegate/useractivitywillsave(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivitydelegate/useractivitywillsave(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivitydelegate/useractivitywillsave%28_%3A%29.json'
content_hash: 'sha256:97777528ab0cee22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivityDelegate](../nsuseractivitydelegate.md)

# userActivityWillSave(_:)

<sub>Instance Method</sub>

Notifies the delegate that the user activity will be saved to be continued or persisted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func userActivityWillSave(_ userActivity: NSUserActivity)
```

## Parameters

- `userActivity` — The user activity to update.

## Discussion

The delegate overrides this method to update the activity with current state.

## See Also

### Managing activity continuation

- [- userActivityWasContinued:](<useractivitywascontinued(__).md>) — Notifies the delegate that the user activity was continued on another device.
