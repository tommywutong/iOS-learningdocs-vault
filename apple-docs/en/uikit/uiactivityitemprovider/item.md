---
title: item
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityitemprovider/item
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemprovider/item'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemprovider/item.json'
content_hash: 'sha256:110188b5feed1d7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemProvider](../uiactivityitemprovider.md)

# item

<sub>Instance Property</sub>

Generates and returns the actual data-bearing object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var item: Any { get }
```

## Discussion

When the actual data-bearing object is required, this method is called by the provider object’s infrastructure. Subclasses must override this method and use it to perform whatever work is required to create the object and return it. You implement this method instead of the normal [main()](<../../foundation/operation/main().md>) method you would implement for operation objects. This method is called on a secondary thread of your app.

The system provides no built-in progress indicator, so if generating the item may take a long time you should plan on providing feedback in your app yourself.

## See Also

### Accessing the provider attributes

- [placeholderItem](placeholderitem.md) — The placeholder object you specified at initialization time.
- [activityType](activitytype.md) — The type of the activity object that is expecting the data.
