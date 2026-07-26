---
title: 'instanceMethodSignatureForSelector:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/instancemethodsignatureforselector:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/instancemethodsignatureforselector:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/instancemethodsignatureforselector%3A.json'
content_hash: 'sha256:9d40fdd7479d157b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# instanceMethodSignatureForSelector:

<sub>Type Method</sub>

Returns an `NSMethodSignature` object that contains a description of the instance method identified by a given selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSMethodSignature *) instanceMethodSignatureForSelector:(SEL) aSelector;
```

## Parameters

- `aSelector` — A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method for which to return the implementation address.

## Return Value

An `NSMethodSignature` object that contains a description of the instance method identified by `aSelector`, or `nil` if the method can’t be found.

## See Also

### Obtaining Information About Methods

- [- methodForSelector:](<method(for_).md>) — Locates and returns the address of the receiver’s implementation of a method so it can be called as a function.
- [+ instanceMethodForSelector:](<instancemethod(for_).md>) — Locates and returns the address of the implementation of the instance method identified by a given selector.
- [methodSignatureForSelector:](methodsignatureforselector_.md) — Returns an `NSMethodSignature` object that contains a description of the method identified by a given selector.
