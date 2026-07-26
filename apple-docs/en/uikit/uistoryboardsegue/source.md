---
title: source
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uistoryboardsegue/source
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboardsegue/source'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboardsegue/source.json'
content_hash: 'sha256:31b323e601c6797f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStoryboardSegue](../uistoryboardsegue.md)

# source

<sub>Instance Property</sub>

The source view controller for the segue.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var source: UIViewController { get }
```

## Discussion

This property contains the view controller whose contents are displayed at the beginning of the segue.

## See Also

### Accessing the segue attributes

- [destinationViewController](destination.md) — The destination view controller for the segue.
- [identifier](identifier.md) — The identifier for the segue object.
