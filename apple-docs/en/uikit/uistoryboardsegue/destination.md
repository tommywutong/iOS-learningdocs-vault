---
title: destination
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uistoryboardsegue/destination
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboardsegue/destination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboardsegue/destination.json'
content_hash: 'sha256:2e7720b376b3fcd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStoryboardSegue](../uistoryboardsegue.md)

# destination

<sub>Instance Property</sub>

The destination view controller for the segue.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var destination: UIViewController { get }
```

## Discussion

This property contains the view controller whose contents should be displayed at the end of the segue.

## See Also

### Accessing the segue attributes

- [sourceViewController](source.md) — The source view controller for the segue.
- [identifier](identifier.md) — The identifier for the segue object.
