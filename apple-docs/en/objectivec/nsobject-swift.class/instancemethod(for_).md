---
title: 'instanceMethod(for:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/instancemethod(for:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/instancemethod(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/instancemethod%28for%3A%29.json'
content_hash: 'sha256:ca4bb10643b08de2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# instanceMethod(for:)

<sub>Type Method</sub>

Locates and returns the address of the implementation of the instance method identified by a given selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func instanceMethod(for aSelector: Selector!) -> IMP!
```

## Parameters

- `aSelector` — A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method for which to return the implementation address. The selector must be non-`NULL` and valid for the receiver. If in doubt, use the [- respondsToSelector:](<../nsobjectprotocol/responds(to_).md>) method to check before passing the selector to [- methodForSelector:](<method(for_).md>).

## Return Value

The address of the implementation of the `aSelector` instance method.

## Discussion

An error is generated if instances of the receiver can’t respond to `aSelector` messages.

Use this method to ask the class object for the implementation of instance methods only. To ask the class for the implementation of a class method, send the [- methodForSelector:](<method(for_).md>) instance method to the class instead.

## See Also

### Obtaining Information About Methods

- [- methodForSelector:](<method(for_).md>) — Locates and returns the address of the receiver’s implementation of a method so it can be called as a function.
