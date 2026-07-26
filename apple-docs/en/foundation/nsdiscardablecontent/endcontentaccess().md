---
title: endContentAccess()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdiscardablecontent/endcontentaccess()
source_url: 'https://developer.apple.com/documentation/foundation/nsdiscardablecontent/endcontentaccess()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdiscardablecontent/endcontentaccess%28%29.json'
content_hash: 'sha256:02f740a9223ed1f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDiscardableContent](../nsdiscardablecontent.md)

# endContentAccess()

<sub>Instance Method</sub>

Called if the discardable contents are no longer being accessed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func endContentAccess()
```

## Discussion

This method decrements the counter variable of the object, which will usually bring the value of the counter variable back down to 0, which allows the discardable contents of the object to be thrown away if necessary.

## See Also

### Accessing Content

- [- beginContentAccess](<begincontentaccess().md>) — Returns a Boolean value indicating whether the discardable contents are still available and have been successfully accessed.
