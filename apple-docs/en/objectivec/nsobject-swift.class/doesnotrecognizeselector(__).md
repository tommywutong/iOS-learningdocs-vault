---
title: 'doesNotRecognizeSelector(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/doesnotrecognizeselector(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/doesnotrecognizeselector(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/doesnotrecognizeselector%28_%3A%29.json'
content_hash: 'sha256:a0b1b13ad150561c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# doesNotRecognizeSelector(_:)

<sub>Instance Method</sub>

Handles messages the receiver doesn’t recognize.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func doesNotRecognizeSelector(_ aSelector: Selector!)
```

## Parameters

- `aSelector` — A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies a method not implemented or recognized by the receiver.

## Discussion

The runtime system invokes this method whenever an object receives an `aSelector` message it can’t respond to or forward. This method, in turn, raises an `NSInvalidArgumentException`, and generates an error message.

Any [- doesNotRecognizeSelector:](<doesnotrecognizeselector(__).md>) messages are generally sent only by the runtime system. However, they can be used in program code to prevent a method from being inherited. For example, an `NSObject` subclass might renounce the [- copy](<copy().md>) or [- init](<init().md>) method by re-implementing it to include a [- doesNotRecognizeSelector:](<doesnotrecognizeselector(__).md>) message as follows:

```objc
- (id)copy
{
    [self doesNotRecognizeSelector:_cmd];
}
```

The `_cmd` variable is a hidden argument passed to every method that is the current selector; in this example, it identifies the selector for the `copy` method. This code prevents instances of the subclass from responding to `copy` messages or superclasses from forwarding `copy` messages—although [- respondsToSelector:](<../nsobjectprotocol/responds(to_).md>) will still report that the receiver has access to a `copy` method.

If you override this method, you must call `super` or raise an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) exception at the end of your implementation. In other words, this method must not return normally; it must always result in an exception being thrown.
