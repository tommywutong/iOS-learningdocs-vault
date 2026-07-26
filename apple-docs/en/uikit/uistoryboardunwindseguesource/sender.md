---
title: sender
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistoryboardunwindseguesource/sender
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboardunwindseguesource/sender'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboardunwindseguesource/sender.json'
content_hash: 'sha256:c76a6c3c618c9d3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStoryboardUnwindSegueSource](../uistoryboardunwindseguesource.md)

# sender

<sub>Instance Property</sub>

The object that performed the unwind action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sender: Any? { get }
```

## Discussion

Use this property to determine which object in your interface triggered the unwind segue.

## See Also

### Getting the unwind segue attributes

- [sourceViewController](source.md) — The view controller being dismissed by the unwind segue.
- [unwindAction](unwindaction.md) — The action method associated with the unwind segue.
