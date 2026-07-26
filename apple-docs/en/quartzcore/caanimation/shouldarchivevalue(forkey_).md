---
title: 'shouldArchiveValue(forKey:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/caanimation/shouldarchivevalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimation/shouldarchivevalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimation/shouldarchivevalue%28forkey%3A%29.json'
content_hash: 'sha256:82c3f7862e722f39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAnimation](../caanimation.md)

# shouldArchiveValue(forKey:)

<sub>Instance Method</sub>

Specifies whether the value of the property for a given key is archived.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func shouldArchiveValue(forKey key: String) -> Bool
```

## Parameters

- `key` — The name of one of the receiver’s properties.

## Return Value

[true](../../swift/true.md) if the specified property should be archived, otherwise [false](../../swift/false.md).

## Discussion

Called by the object’s implementation of `encodeWithCoder:`. The object must implement keyed archiving.

The default implementation returns [true](../../swift/true.md).

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
