---
title: 'isKind(of:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/iskind(of:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/iskind(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/iskind%28of%3A%29.json'
content_hash: 'sha256:8cecdb5c76ea963e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# isKind(of:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver is an instance of given class or an instance of any class that inherits from that class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isKind(of aClass: AnyClass) -> Bool
```

## Parameters

- `aClass` — A class object representing the Objective-C class to be tested.

## Return Value

[YES](../yes.md) if the receiver is an instance of `aClass` or an instance of any class that inherits from `aClass`, otherwise [NO](../no.md).

## Discussion

For example, in this code, [- isKindOfClass:](<iskind(of_).md>) would return [YES](../yes.md) because, in Foundation, the [NSArchiver](../../foundation/nsarchiver.md) class inherits from [NSCoder](../../foundation/nscoder.md):

```objc
NSMutableData *myData = [NSMutableData dataWithCapacity:30];
id anArchiver = [[NSArchiver alloc] initForWritingWithMutableData:myData];
if ( [anArchiver isKindOfClass:[NSCoder class]] )
    ...
```

Be careful when using this method on objects represented by a class cluster. Because of the nature of class clusters, the object you get back may not always be the type you expected. If you call a method that returns a class cluster, the exact type returned by the method is the best indicator of what you can do with that object. For example, if a method returns a pointer to an [NSArray](../../foundation/nsarray.md) object, you should not use this method to see if the array is mutable, as shown in the following code:

```objc
// DO NOT DO THIS!
if ([myArray isKindOfClass:[NSMutableArray class]])
{
    // Modify the object
}
```

If you use such constructs in your code, you might think it is alright to modify an object that in reality should not be modified. Doing so might then create problems for other code that expected the object to remain unchanged.

If the receiver is a class object, this method returns [YES](../yes.md) if `aClass` is a Class object of the same type, [NO](../no.md) otherwise.

## See Also

### Testing Object Inheritance, Behavior, and Conformance

- [- isMemberOfClass:](<ismember(of_).md>) — Returns a Boolean value that indicates whether the receiver is an instance of a given class.
- [- respondsToSelector:](<responds(to_).md>) — Returns a Boolean value that indicates whether the receiver implements or inherits a method that can respond to a specified message.
- [- conformsToProtocol:](<conforms(to_).md>) — Returns a Boolean value that indicates whether the receiver conforms to a given protocol.
