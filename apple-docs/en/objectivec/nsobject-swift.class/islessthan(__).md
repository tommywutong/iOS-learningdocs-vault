---
title: 'isLessThan(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/islessthan(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/islessthan(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/islessthan%28_%3A%29.json'
content_hash: 'sha256:f08936245955a4f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isLessThan(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver is less than another given object.

<sub>Mac Catalyst, macOS</sub>

```swift
func isLessThan(_ object: Any?) -> Bool
```

## Parameters

- `object` — The object with which to compare the receiver.

## Return Value

[YES](../yes.md) if the receiver is less than `object`, otherwise [NO](../no.md).

## Discussion

During the evaluation of an `NSWhoseSpecifier` object that contains a test whose operator is `NSLessThanComparison`, an [- isLessThan:](<islessthan(__).md>) message may be sent to each potentially specified object, if the potentially specified object does not implement a [- scriptingIsLessThan:](<scriptingislessthan(__).md>) method and the object being tested against does not implement a [- scriptingIsGreaterThanOrEqualTo:](<scriptingisgreaterthanorequal(to_).md>) method.

The default implementation for this method provided by `NSObject` method returns [YES](../yes.md) if a `compare:` message sent to the same object would return `NSOrderedAscending`.
