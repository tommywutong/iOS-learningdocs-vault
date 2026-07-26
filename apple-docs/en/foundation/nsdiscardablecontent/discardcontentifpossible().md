---
title: discardContentIfPossible()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdiscardablecontent/discardcontentifpossible()
source_url: 'https://developer.apple.com/documentation/foundation/nsdiscardablecontent/discardcontentifpossible()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdiscardablecontent/discardcontentifpossible%28%29.json'
content_hash: 'sha256:60b10c7caa5e76ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDiscardableContent](../nsdiscardablecontent.md)

# discardContentIfPossible()

<sub>Instance Method</sub>

Called to discard the contents of the receiver if the value of the accessed counter is 0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func discardContentIfPossible()
```

## Discussion

This method should only discard the contents of the object if the value of the accessed counter is 0. Otherwise, it should do nothing.

## See Also

### Discarding Content

- [- isContentDiscarded](<iscontentdiscarded().md>) — Returns a Boolean value indicating whether the content has been discarded.
