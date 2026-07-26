---
title: 'isSubclass(of:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/issubclass(of:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/issubclass(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/issubclass%28of%3A%29.json'
content_hash: 'sha256:e25046c275d4fad4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isSubclass(of:)

<sub>Type Method</sub>

Returns a Boolean value that indicates whether the receiving class is a subclass of, or identical to, a given class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func isSubclass(of aClass: AnyClass) -> Bool
```

## Parameters

- `aClass` — A class object.

## Return Value

[YES](../yes.md) if the receiving class is a subclass of—or identical to—`aClass`, otherwise [NO](../no.md).

## See Also

### Identifying Classes

- [+ superclass](<superclass().md>) — Returns the class object for the receiver’s superclass.
