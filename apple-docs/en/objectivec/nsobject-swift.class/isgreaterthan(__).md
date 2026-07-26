---
title: 'isGreaterThan(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/isgreaterthan(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isgreaterthan(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/isgreaterthan%28_%3A%29.json'
content_hash: 'sha256:346be6c1be0c37c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isGreaterThan(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver is greater than another given object.

<sub>Mac Catalyst, macOS</sub>

```swift
func isGreaterThan(_ object: Any?) -> Bool
```

## Parameters

- `object` — The object with which to compare the receiver.

## Return Value

[YES](../yes.md) if the receiver is greater than `object`, otherwise [NO](../no.md).

## Discussion

During the evaluation of an `NSWhoseSpecifier` object that contains a test whose operator is `NSGreaterThanComparison`, an [- isGreaterThan:](<isgreaterthan(__).md>) message may be sent to each potentially specified object, if the potentially specified object does not implement a [- scriptingIsGreaterThan:](<scriptingisgreaterthan(__).md>) method and the object being tested against does not implement a [- scriptingIsLessThanOrEqualTo:](<scriptingislessthanorequal(to_).md>) method.

The default implementation for this method provided by `NSObject` returns [YES](../yes.md) if a `compare:` message sent to the same object would return `NSOrderedDescending`.
