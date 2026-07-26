---
title: 'instancesRespond(to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/instancesrespond(to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/instancesrespond(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/instancesrespond%28to%3A%29.json'
content_hash: 'sha256:700452b88cc03305'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# instancesRespond(to:)

<sub>Type Method</sub>

Returns a Boolean value that indicates whether instances of the receiver are capable of responding to a given selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func instancesRespond(to aSelector: Selector!) -> Bool
```

## Parameters

- `aSelector` — A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48).

## Return Value

[YES](../yes.md) if instances of the receiver are capable of responding to `aSelector` messages, otherwise [NO](../no.md).

## Discussion

If `aSelector` messages are forwarded to other objects, instances of the class are able to receive those messages without error even though this method returns [NO](../no.md).

To ask the class whether it, rather than its instances, can respond to a particular message, send to the class instead the  `NSObject` protocol instance method [- respondsToSelector:](<../nsobjectprotocol/responds(to_).md>).
