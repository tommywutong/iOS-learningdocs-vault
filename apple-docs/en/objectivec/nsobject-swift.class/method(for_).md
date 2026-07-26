---
title: 'method(for:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/method(for:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/method(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/method%28for%3A%29.json'
content_hash: 'sha256:36277790a58e0ddc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# method(for:)

<sub>Instance Method</sub>

Locates and returns the address of the receiver’s implementation of a method so it can be called as a function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func method(for aSelector: Selector!) -> IMP!
```

## Parameters

- `aSelector` — A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method for which to return the implementation address. The selector must be a valid and non-`NULL`. If in doubt, use the [- respondsToSelector:](<../nsobjectprotocol/responds(to_).md>) method to check before passing the selector to [- methodForSelector:](<method(for_).md>).

## Return Value

The address of the receiver’s implementation of the `aSelector`.

## Discussion

If the receiver is an instance, `aSelector` should refer to an instance method; if the receiver is a class, it should refer to a class method.

## See Also

### Obtaining Information About Methods

- [+ instanceMethodForSelector:](<instancemethod(for_).md>) — Locates and returns the address of the implementation of the instance method identified by a given selector.
