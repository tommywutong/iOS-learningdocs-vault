---
title: class
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/class
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/class.json'
content_hash: 'sha256:0569dc89bbd29653'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# class

<sub>Type Method</sub>

Returns the class object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (Class) class;
```

## Return Value

The class object.

## Discussion

Refer to a class only by its name when it is the receiver of a message. In all other cases, the class object must be obtained through this or a similar method. For example, here `SomeClass` is passed as an argument to the [- isKindOfClass:](<../nsobjectprotocol/iskind(of_).md>) method (declared in the `NSObject` protocol):

```objc
BOOL test = [self isKindOfClass:[SomeClass class]];
```

## See Also

### Related Documentation

- [NSStringFromClass(_:)](<../../foundation/nsstringfromclass(__).md>) — Returns the name of a class as a string.
- [class](../nsobject-c.protocol/class.md) — Returns the class object for the receiver’s class.
- [NSClassFromString(_:)](<../../foundation/nsclassfromstring(__).md>) — Obtains a class by name.

### Identifying Classes

- [+ superclass](<superclass().md>) — Returns the class object for the receiver’s superclass.
- [+ isSubclassOfClass:](<issubclass(of_).md>) — Returns a Boolean value that indicates whether the receiving class is a subclass of, or identical to, a given class.
