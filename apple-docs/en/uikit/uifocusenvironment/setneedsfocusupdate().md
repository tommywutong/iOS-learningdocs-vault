---
title: setNeedsFocusUpdate()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusenvironment/setneedsfocusupdate()
source_url: 'https://developer.apple.com/documentation/uikit/uifocusenvironment/setneedsfocusupdate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusenvironment/setneedsfocusupdate%28%29.json'
content_hash: 'sha256:1a5ee94e2a30a43a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusEnvironment](../uifocusenvironment.md)

# setNeedsFocusUpdate()

<sub>Instance Method</sub>

Submits a request to the focus engine for a focus update in this environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNeedsFocusUpdate()
```

## Discussion

If this environment does not currently contain the focused view, calling this method has no effect. Otherwise, and if the focus update is accepted by the focus engine, focus is reset to the preferred focused view on the run loop cycle. If a parent of this environment is also requesting focus, the parent’s request takes priority.

## See Also

### Requesting focus update

- [- updateFocusIfNeeded](<updatefocusifneeded().md>) — Tells the focus engine to force a focus update immediately.
