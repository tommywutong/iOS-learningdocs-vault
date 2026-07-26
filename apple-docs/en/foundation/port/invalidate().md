---
title: invalidate()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/port/invalidate()
source_url: 'https://developer.apple.com/documentation/foundation/port/invalidate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/port/invalidate%28%29.json'
content_hash: 'sha256:83dee48c89674fba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Port](../port.md)

# invalidate()

<sub>Instance Method</sub>

Marks the receiver as invalid and posts an [NSPortDidBecomeInvalidNotification](didbecomeinvalidnotification.md) to the default notification center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func invalidate()
```

## Discussion

You must call this method before releasing a port object (or removing strong references to it if your application is garbage collected).

## See Also

### Validation

- [valid](isvalid.md) — A Boolean value that indicates whether the receiver is valid.
