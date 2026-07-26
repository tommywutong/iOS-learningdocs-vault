---
title: beginContentAccess()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdiscardablecontent/begincontentaccess()
source_url: 'https://developer.apple.com/documentation/foundation/nsdiscardablecontent/begincontentaccess()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdiscardablecontent/begincontentaccess%28%29.json'
content_hash: 'sha256:7a8616f7000d22de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDiscardableContent](../nsdiscardablecontent.md)

# beginContentAccess()

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the discardable contents are still available and have been successfully accessed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func beginContentAccess() -> Bool
```

## Return Value

YES if the discardable contents are still available and have now been successfully accessed; otherwise, [false](../../swift/false.md).

## Discussion

Call this method if the object’s memory is needed or is about to be used. This method increments the counter variable, thus protecting the object’s memory from possibly being discarded. The implementing class may decide that this method will try to recreate the contents if they have been discarded and return YES if the re-creation was successful. Implementors of this protocol should raise exceptions if the `NSDiscardableContent` objects are used when the `beginContentAccess` method has not been called on them.

## See Also

### Accessing Content

- [- endContentAccess](<endcontentaccess().md>) — Called if the discardable contents are no longer being accessed.
