---
title: 'methodSignatureForSelector:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/methodsignatureforselector:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/methodsignatureforselector:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/methodsignatureforselector%3A.json'
content_hash: 'sha256:a67811a18c39f1be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# methodSignatureForSelector:

<sub>Instance Method</sub>

Returns an `NSMethodSignature` object that contains a description of the method identified by a given selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSMethodSignature *) methodSignatureForSelector:(SEL) aSelector;
```

## Parameters

- `aSelector` — A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method for which to return the implementation address. When the receiver is an instance, `aSelector` should identify an instance method; when the receiver is a class, it should identify a class method.

## Return Value

An `NSMethodSignature` object that contains a description of the method identified by `aSelector`, or `nil` if the method can’t be found.

## Discussion

This method is used in the implementation of protocols. This method is also used in situations where an `NSInvocation` object must be created, such as during message forwarding. If your object maintains a delegate or is capable of handling messages that it does not directly implement, you should override this method to return an appropriate method signature.

## See Also

### Related Documentation

- [forwardInvocation:](forwardinvocation_.md) — Overridden by subclasses to forward messages to other objects.

### Obtaining Information About Methods

- [- methodForSelector:](<method(for_).md>) — Locates and returns the address of the receiver’s implementation of a method so it can be called as a function.
- [+ instanceMethodForSelector:](<instancemethod(for_).md>) — Locates and returns the address of the implementation of the instance method identified by a given selector.
- [instanceMethodSignatureForSelector:](instancemethodsignatureforselector_.md) — Returns an `NSMethodSignature` object that contains a description of the instance method identified by a given selector.
