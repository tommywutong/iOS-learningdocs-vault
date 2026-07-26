---
title: 'responds(to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 1.0+, iPadOS 1.0+, Mac Catalyst 1.0+, macOS 10.0+, tvOS 1.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/responds(to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/responds(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/responds%28to%3A%29.json'
content_hash: 'sha256:bf23290f06079660'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# responds(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver implements or inherits a method that can respond to a specified message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func responds(to aSelector: Selector!) -> Bool
```

## Parameters

- `aSelector` — A selector that identifies a message.

## Return Value

[YES](../yes.md) if the receiver implements or inherits a method that can respond to `aSelector`, otherwise [NO](../no.md).

## Discussion

The application is responsible for determining whether a [NO](../no.md) response should be considered an error.

You cannot test whether an object inherits a method from its superclass by sending [- respondsToSelector:](<responds(to_).md>) to the object using the `super` keyword. This method will still be testing the object as a whole, not just the superclass’s implementation. Therefore, sending [- respondsToSelector:](<responds(to_).md>) to `super` is equivalent to sending it to `self`. Instead, you must invoke the `NSObject` class method [+ instancesRespondToSelector:](<../nsobject-swift.class/instancesrespond(to_).md>) directly on the object’s superclass, as illustrated in the following code fragment.

```objc
if( [MySuperclass instancesRespondToSelector:@selector(aMethod)] ) {
    // invoke the inherited method
    [super aMethod];
}
```

You cannot simply use `[[self superclass] instancesRespondToSelector:@selector(aMethod)]` since this may cause the method to fail if it is invoked by a subclass.

Note that if the receiver is able to forward `aSelector` messages to another object, it will be able to respond to the message, albeit indirectly, even though this method returns [NO](../no.md).

## See Also

### Related Documentation

- [+ instancesRespondToSelector:](<../nsobject-swift.class/instancesrespond(to_).md>) — Returns a Boolean value that indicates whether instances of the receiver are capable of responding to a given selector.

### Testing Object Inheritance, Behavior, and Conformance

- [- isKindOfClass:](<iskind(of_).md>) — Returns a Boolean value that indicates whether the receiver is an instance of given class or an instance of any class that inherits from that class.
- [- isMemberOfClass:](<ismember(of_).md>) — Returns a Boolean value that indicates whether the receiver is an instance of a given class.
- [- conformsToProtocol:](<conforms(to_).md>) — Returns a Boolean value that indicates whether the receiver conforms to a given protocol.
