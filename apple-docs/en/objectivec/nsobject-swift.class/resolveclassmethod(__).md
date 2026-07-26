---
title: 'resolveClassMethod(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/resolveclassmethod(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/resolveclassmethod(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/resolveclassmethod%28_%3A%29.json'
content_hash: 'sha256:3c6f7cec39a2eea1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# resolveClassMethod(_:)

<sub>Type Method</sub>

Dynamically provides an implementation for a given selector for a class method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func resolveClassMethod(_ sel: Selector!) -> Bool
```

## Parameters

- `sel` — The name of a selector to resolve.

## Return Value

[YES](../yes.md) if the method was found and added to the receiver, otherwise [NO](../no.md).

## Discussion

This method allows you to dynamically provide an implementation for a given selector. See [+ resolveInstanceMethod:](<resolveinstancemethod(__).md>) for further discussion.

## See Also

### Dynamically Resolving Methods

- [+ resolveInstanceMethod:](<resolveinstancemethod(__).md>) — Dynamically provides an implementation for a given selector for an instance method.
