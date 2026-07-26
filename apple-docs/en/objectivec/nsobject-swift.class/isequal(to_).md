---
title: 'isEqual(to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/isequal%28to%3A%29.json'
content_hash: 'sha256:a4ec26dfc6ddcfc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isEqual(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver is equal to another given object.

<sub>Mac Catalyst, macOS</sub>

```swift
func isEqual(to object: Any?) -> Bool
```

## Parameters

- `object` — The object with which to compare the receiver.

## Return Value

[YES](../yes.md) if the receiver is equal to `object`, otherwise [NO](../no.md). In effect returns [NO](../no.md) if receiver is `nil`.

## Discussion

During the evaluation of an `NSWhoseSpecifier` object that contains a test whose operator is `NSEqualToComparison`, an [- isEqualTo:](<isequal(to_).md>) message may be sent to each potentially specified object, if neither the potentially specified object nor the object being tested against implements a [- scriptingIsEqualTo:](<scriptingisequal(to_).md>) method.

The default implementation for this method provided by `NSObject` returns [YES](../yes.md) if an `isEqualTo:` message sent to the same object would return [YES](../yes.md).
