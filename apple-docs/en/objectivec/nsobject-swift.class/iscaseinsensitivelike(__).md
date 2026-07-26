---
title: 'isCaseInsensitiveLike(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/iscaseinsensitivelike(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/iscaseinsensitivelike(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/iscaseinsensitivelike%28_%3A%29.json'
content_hash: 'sha256:ec00c2d8b0a34d5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isCaseInsensitiveLike(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether receiver is considered to be “like” a given string when the case of characters in the receiver is ignored.

<sub>Mac Catalyst, macOS</sub>

```swift
func isCaseInsensitiveLike(_ object: String) -> Bool
```

## Parameters

- `object` — The string with which to compare the receiver.

## Return Value

[YES](../yes.md) if the receiver is considered to be “like” `aString` when the case of characters in the receiver is ignored, otherwise [NO](../no.md).

## Discussion

Currently, [- isCaseInsensitiveLike:](<iscaseinsensitivelike(__).md>) messages are never sent to any object from within Cocoa itself.

The default implementation for this method provided by `NSObject` returns [NO](../no.md). `NSString` also provides an implementation of this method, which returns [YES](../yes.md) if the receiver matches a pattern described by `aString`, ignoring the case of the characters in the receiver.
