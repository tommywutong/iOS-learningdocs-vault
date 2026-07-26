---
title: 'isLike(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/islike(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/islike(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/islike%28_%3A%29.json'
content_hash: 'sha256:8ea81933793e423b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isLike(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver is “like” another given object.

<sub>Mac Catalyst, macOS</sub>

```swift
func isLike(_ object: String) -> Bool
```

## Parameters

- `object` — The object with which to compare the receiver.

## Return Value

[YES](../yes.md) if the receiver is considered to be “like” `object`, otherwise [NO](../no.md).

## Discussion

Currently, [- isLike:](<islike(__).md>) messages are never sent to any object from within Cocoa itself.

The default implementation for this method provided by `NSObject` method returns [NO](../no.md). `NSString` also provides an implementation of this method, which returns [YES](../yes.md) if the receiver matches a pattern described by `object`.
