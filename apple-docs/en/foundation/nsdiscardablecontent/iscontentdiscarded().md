---
title: isContentDiscarded()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdiscardablecontent/iscontentdiscarded()
source_url: 'https://developer.apple.com/documentation/foundation/nsdiscardablecontent/iscontentdiscarded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdiscardablecontent/iscontentdiscarded%28%29.json'
content_hash: 'sha256:288deea698fb8ce6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDiscardableContent](../nsdiscardablecontent.md)

# isContentDiscarded()

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the content has been discarded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isContentDiscarded() -> Bool
```

## Return Value

[true](../../swift/true.md) if the content has been discarded; otherwise, [false](../../swift/false.md).

## See Also

### Discarding Content

- [- discardContentIfPossible](<discardcontentifpossible().md>) — Called to discard the contents of the receiver if the value of the accessed counter is 0.
