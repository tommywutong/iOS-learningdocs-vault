---
title: 'doesContain(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/doescontain(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/doescontain(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/doescontain%28_%3A%29.json'
content_hash: 'sha256:806f0de3aaf54b80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# doesContain(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver contains a given object.

<sub>Mac Catalyst, macOS</sub>

```swift
func doesContain(_ object: Any) -> Bool
```

## Parameters

- `object` — The object to search for in the receiver.

## Return Value

[YES](../yes.md) if the receiver contains `object`, otherwise [NO](../no.md).

## Discussion

Currently, [- doesContain:](<doescontain(__).md>) messages are never sent to any object from within Cocoa itself.

The default implementation for this method provided by `NSObject` returns [YES](../yes.md) if the receiver is actually an `NSArray` object and an [indexOfObjectIdentical(to:)](<../../foundation/nsarray/indexofobjectidentical(to_).md>) message sent to the same object would return something other than `NSNotFound`.
