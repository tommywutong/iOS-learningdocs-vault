---
title: 'isNotEqual(to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/isnotequal(to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isnotequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/isnotequal%28to%3A%29.json'
content_hash: 'sha256:125f6bbb61921388'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isNotEqual(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver is not equal to another given object.

<sub>Mac Catalyst, macOS</sub>

```swift
func isNotEqual(to object: Any?) -> Bool
```

## Parameters

- `object` — The object with which to compare the receiver.

## Return Value

[YES](../yes.md) if the receiver is not equal to `object`, otherwise [NO](../no.md).

## Discussion

Currently, [- isNotEqualTo:](<isnotequal(to_).md>) messages are never sent to any object from within Cocoa itself.

The default implementation for this method provided by `NSObject` method returns [YES](../yes.md) if an `isEqual:` message sent to the same object would return [NO](../no.md).
