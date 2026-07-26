---
title: 'didUpdateFocus(in:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifocusenvironment/didupdatefocus(in:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifocusenvironment/didupdatefocus(in:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusenvironment/didupdatefocus%28in%3Awith%3A%29.json'
content_hash: 'sha256:c6c66cf1e691eee2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusEnvironment](../uifocusenvironment.md)

# didUpdateFocus(in:with:)

<sub>Instance Method</sub>

Called immediately after the system updates the focus to a new view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func didUpdateFocus(in context: UIFocusUpdateContext, with coordinator: UIFocusAnimationCoordinator)
```

## Parameters

- `context` — An instance of [UIFocusUpdateContext](../uifocusupdatecontext.md) containing metadata of the focus related update.

- `coordinator` — An instance of [UIFocusAnimationCoordinator](../uifocusanimationcoordinator.md) used for coordinating focus-related animations.

## Discussion

After the focus is updated to a new view, the focus engine calls this method on all focus environments that contain either the previously focused view, the next focused view, or both, in ascending order. You should override this method to update your app’s state in response to changes in focus. Use the provided animation coordinator to animate changes in visual appearance related to the update. For more information on animation coordinators, see [UIFocusAnimationCoordinator](../uifocusanimationcoordinator.md).
