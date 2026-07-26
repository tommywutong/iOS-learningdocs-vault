---
title: unwindAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistoryboardunwindseguesource/unwindaction
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource/unwindaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboardunwindseguesource/unwindaction.json'
content_hash: 'sha256:c0d1629106a60a8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStoryboardUnwindSegueSource](../uistoryboardunwindseguesource.md)

# unwindAction

<sub>Instance Property</sub>

The action method associated with the unwind segue.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var unwindAction: Selector { get }
```

## Discussion

Each unwind segue has an associated action method. The view controller that’s the destination of the unwind segue must implement this action method.

## See Also

### Getting the unwind segue attributes

- [sourceViewController](source.md) — The view controller being dismissed by the unwind segue.
- [sender](sender.md) — The object that performed the unwind action.
