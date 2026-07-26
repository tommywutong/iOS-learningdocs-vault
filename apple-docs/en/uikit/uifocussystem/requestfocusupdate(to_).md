---
title: 'requestFocusUpdate(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifocussystem/requestfocusupdate(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifocussystem/requestfocusupdate(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocussystem/requestfocusupdate%28to%3A%29.json'
content_hash: 'sha256:bc67c4c2334c2c95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusSystem](../uifocussystem.md)

# requestFocusUpdate(to:)

<sub>Instance Method</sub>

Submits a request to update the focus state of the specified object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func requestFocusUpdate(to environment: any UIFocusEnvironment)
```

## Parameters

- `environment` — The view, view controller, window, or other object that you want to update. You can specify any object that adopts the [UIFocusEnvironment](../uifocusenvironment.md) protocol.

## Discussion

Use this method to ask the focus engine to update the focus-related information for the specified object. If the update request is accepted, the focus engine updates the object’s focus-related information during the next run loop cycle. If the specified object does not contain a focused item, calling this method has no effect.

## See Also

### Managing focus updates

- [- updateFocusIfNeeded](<updatefocusifneeded().md>) — Forces the system to act on a pending focus update for the current environment.
