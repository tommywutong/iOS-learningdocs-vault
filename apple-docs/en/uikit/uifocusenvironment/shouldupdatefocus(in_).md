---
title: 'shouldUpdateFocus(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifocusenvironment/shouldupdatefocus(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifocusenvironment/shouldupdatefocus(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusenvironment/shouldupdatefocus%28in%3A%29.json'
content_hash: 'sha256:6d1ac76dd3857ebe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusEnvironment](../uifocusenvironment.md)

# shouldUpdateFocus(in:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the focus engine should allow the focus update described by the specified context to occur.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func shouldUpdateFocus(in context: UIFocusUpdateContext) -> Bool
```

## Parameters

- `context` — An instance of [UIFocusUpdateContext](../uifocusupdatecontext.md) class, containing metadata for the focus related update.

## Return Value

[true](../../swift/true.md) to allow the focus update; otherwise, [false](../../swift/false.md).

## Discussion

When a focus update is about to occur, the focus engine calls this method on all focus environments that contain either the previously focused view, the next focused view, or both, in ascending order. If any environment returns [false](../../swift/false.md), the update is cancelled. Override this method to prevent the focus from moving to or from certain areas of the screen.
