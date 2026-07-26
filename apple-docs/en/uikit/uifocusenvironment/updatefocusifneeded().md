---
title: updateFocusIfNeeded()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusenvironment/updatefocusifneeded()
source_url: 'https://developer.apple.com/documentation/uikit/uifocusenvironment/updatefocusifneeded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusenvironment/updatefocusifneeded%28%29.json'
content_hash: 'sha256:66671d98c3dc49f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusEnvironment](../uifocusenvironment.md)

# updateFocusIfNeeded()

<sub>Instance Method</sub>

Tells the focus engine to force a focus update immediately.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateFocusIfNeeded()
```

## Discussion

If any focus environment is currently pending an update (after calling [- setNeedsFocusUpdate](<setneedsfocusupdate().md>)), then calling this method forces the focus engine to immediately update focus. Unlike [- setNeedsFocusUpdate](<setneedsfocusupdate().md>), it does not matter if this environment currently contains focus, or if this environment is the one pending an update.

## See Also

### Requesting focus update

- [- setNeedsFocusUpdate](<setneedsfocusupdate().md>) — Submits a request to the focus engine for a focus update in this environment.
