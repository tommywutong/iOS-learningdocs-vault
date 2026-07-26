---
title: 'setClasses(_:for:argumentIndex:ofReply:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpcinterface/setclasses(_:for:argumentindex:ofreply:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcinterface/setclasses(_:for:argumentindex:ofreply:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcinterface/setclasses%28_%3Afor%3Aargumentindex%3Aofreply%3A%29.json'
content_hash: 'sha256:24a990c997e7cbd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCInterface](../nsxpcinterface.md)

# setClasses(_:for:argumentIndex:ofReply:)

<sub>Instance Method</sub>

Sets the classes that can appear within the (numerically) specified collection object argument to the specified method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setClasses(_ classes: Set<AnyHashable>, for sel: Selector, argumentIndex arg: Int, ofReply: Bool)
```

## Parameters

- `classes` — An `NSSet` containing Class objects—for example, `[MyObject class]`.

- `sel` — Specifies which method in the protocol is being configured.

- `arg` — Specifies the position (starting at index 0) of the parameter for which you are allowing classes. This may be either the position of a parameter in the method itself or the position in its reply block.

- `ofReply` — Pass [true](../../swift/true.md) if `arg` is an index into the parameters of the reply block, or [false](../../swift/false.md) if it is an index into the parameters of the method itself.

## Discussion

If an argument to a method in your protocol is a collection class (for example, NSArray or NSDictionary), then you must explicitly specify the set of expected classes that may appear within that collection.

If the expected classes are all property list types, calling this method is optional; property list types are allowed by default inside collection objects. You may, however, call this method to further restrict the set of allowed classes.
