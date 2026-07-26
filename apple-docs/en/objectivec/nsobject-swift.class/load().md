---
title: load()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/load()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/load()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/load%28%29.json'
content_hash: 'sha256:4be60cbf76ea49ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# load()

<sub>Type Method</sub>

Invoked whenever a class or category is added to the Objective-C runtime; implement this method to perform class-specific behavior upon loading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func load()
```

## Discussion

The [+ load](<load().md>) message is sent to classes and categories that are both dynamically loaded and statically linked, but only if the newly loaded class or category implements a method that can respond.

The order of initialization is as follows:

1. All initializers in any framework you link to.
2. All `+load` methods in your image.
3. All C++ static initializers and C/C++ `__attribute__(constructor)` functions in your image.
4. All initializers in frameworks that link to you.

In addition:

- A class’s `+load` method is called after all of its superclasses’ `+load` methods.
- A category `+load` method is called after the class’s own `+load` method.

In a custom implementation of [+ load](<load().md>) you can therefore safely message other unrelated classes from the same image, but any [+ load](<load().md>) methods implemented by those classes may not have run yet.

> [!important] Important
> Custom implementations of the `load` method for Swift classes bridged to Objective-C are not called automatically.

## See Also

### Initializing a Class

- [+ initialize](<initialize().md>) — Initializes the class before it receives its first message.
