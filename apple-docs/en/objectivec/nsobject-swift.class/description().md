---
title: description()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/description()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/description()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/description%28%29.json'
content_hash: 'sha256:d79532bbf97fac45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# description()

<sub>Type Method</sub>

Returns a string that represents the contents of the receiving class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func description() -> String
```

## Return Value

A string that represents the contents of the receiving class.

## Discussion

The debugger’s print-object command invokes this method to produce a textual description of an object.

`NSObject`’s implementation of this method simply prints the name of the class.

## See Also

### Related Documentation

- [description](../nsobjectprotocol/description.md) — A textual representation of the receiver.
