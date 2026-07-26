---
title: 'isMember(of:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/ismember(of:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/ismember(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/ismember%28of%3A%29.json'
content_hash: 'sha256:e769037ce13459df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# isMember(of:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver is an instance of a given class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isMember(of aClass: AnyClass) -> Bool
```

## Parameters

- `aClass` — A class object representing the Objective-C class to be tested.

## Return Value

[YES](../yes.md) if the receiver is an instance of `aClass`, otherwise [NO](../no.md).

## Discussion

For example, in this code, [- isMemberOfClass:](<ismember(of_).md>) would return [NO](../no.md):

```objc
NSMutableData *myData = [NSMutableData dataWithCapacity:30];
id anArchiver = [[NSArchiver alloc] initForWritingWithMutableData:myData];
if ([anArchiver isMemberOfClass:[NSCoder class]])
    ...
```

Class objects may be compiler-created objects but they still support the concept of membership. Thus, you can use this method to verify that the receiver is a specific Class object.

## See Also

### Testing Object Inheritance, Behavior, and Conformance

- [- isKindOfClass:](<iskind(of_).md>) — Returns a Boolean value that indicates whether the receiver is an instance of given class or an instance of any class that inherits from that class.
- [- respondsToSelector:](<responds(to_).md>) — Returns a Boolean value that indicates whether the receiver implements or inherits a method that can respond to a specified message.
- [- conformsToProtocol:](<conforms(to_).md>) — Returns a Boolean value that indicates whether the receiver conforms to a given protocol.
