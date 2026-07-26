---
title: 'isGreaterThanOrEqual(to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/isgreaterthanorequal(to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isgreaterthanorequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/isgreaterthanorequal%28to%3A%29.json'
content_hash: 'sha256:3cb4deb9de790c7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isGreaterThanOrEqual(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver is greater than or equal to another given object.

<sub>Mac Catalyst, macOS</sub>

```swift
func isGreaterThanOrEqual(to object: Any?) -> Bool
```

## Parameters

- `object` — The object with which to compare the receiver.

## Return Value

[YES](../yes.md) if the receiver is greater than or equal to `object`, otherwise [NO](../no.md).

## Discussion

During the evaluation of an `NSWhoseSpecifier` object that contains a test whose operator is `NSGreaterThanOrEqualToComparison`, an[- isGreaterThanOrEqualTo:](<isgreaterthanorequal(to_).md>) message may be sent to each potentially specified object, if the potentially specified object does not implement a [- scriptingIsGreaterThanOrEqualTo:](<scriptingisgreaterthanorequal(to_).md>) method and the object being tested against does not implement a [- scriptingIsLessThan:](<scriptingislessthan(__).md>) method.

The default implementation for this method provided by `NSObject` returns [YES](../yes.md) if a `compare:` message sent to the same object would return `NSOrderedSame` or `NSOrderedDescending`.
