---
title: identifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uistoryboardsegue/identifier
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboardsegue/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboardsegue/identifier.json'
content_hash: 'sha256:561d9c7c08dfa845'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStoryboardSegue](../uistoryboardsegue.md)

# identifier

<sub>Instance Property</sub>

The identifier for the segue object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var identifier: String? { get }
```

## Discussion

You assign identifiers to your segues in Interface Builder. An identifier is a string that your application uses to distinguish one segue from another. For example, if you have a source view controller that can segue to two or more different destination view controllers, you’d assign different identifiers to each segue so that the source view controller’s [- prepareForSegue:sender:](<../uiviewcontroller/prepare(for_sender_).md>) method could tell them apart and prepare each segue appropriately.

## See Also

### Accessing the segue attributes

- [sourceViewController](source.md) — The source view controller for the segue.
- [destinationViewController](destination.md) — The destination view controller for the segue.
