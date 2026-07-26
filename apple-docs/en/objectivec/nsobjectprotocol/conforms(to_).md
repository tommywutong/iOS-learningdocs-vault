---
title: 'conforms(to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/conforms(to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/conforms(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/conforms%28to%3A%29.json'
content_hash: 'sha256:1e73b58ac38d978c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# conforms(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver conforms to a given protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func conforms(to aProtocol: Protocol) -> Bool
```

## Parameters

- `aProtocol` — A protocol object that represents a particular protocol.

## Return Value

[YES](../yes.md) if the receiver conforms to `aProtocol`, otherwise [NO](../no.md).

## Discussion

This method works identically to the [+ conformsToProtocol:](<../nsobject-swift.class/conforms(to_).md>) class method declared in [NSObject](../nsobject-swift.class.md). It’s provided as a convenience so that you don’t need to get the class object to find out whether an instance can respond to a given set of messages.

## See Also

### Testing Object Inheritance, Behavior, and Conformance

- [- isKindOfClass:](<iskind(of_).md>) — Returns a Boolean value that indicates whether the receiver is an instance of given class or an instance of any class that inherits from that class.
- [- isMemberOfClass:](<ismember(of_).md>) — Returns a Boolean value that indicates whether the receiver is an instance of a given class.
- [- respondsToSelector:](<responds(to_).md>) — Returns a Boolean value that indicates whether the receiver implements or inherits a method that can respond to a specified message.
