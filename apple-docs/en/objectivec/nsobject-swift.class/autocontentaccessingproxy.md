---
title: autoContentAccessingProxy
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/autocontentaccessingproxy
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/autocontentaccessingproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/autocontentaccessingproxy.json'
content_hash: 'sha256:13861320fdf8ecd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# autoContentAccessingProxy

<sub>Instance Property</sub>

A proxy for the receiving object

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var autoContentAccessingProxy: Any { get }
```

## Discussion

This property returns a proxy for the receiving object if the receiver adopts the [NSDiscardableContent](../../foundation/nsdiscardablecontent.md) protocol and still has content that has not been discarded.

The proxy calls [beginContentAccess()](<../../foundation/nsdiscardablecontent/begincontentaccess().md>) on the receiver to keep the content available as long as the proxy lives, and calls [endContentAccess()](<../../foundation/nsdiscardablecontent/endcontentaccess().md>) when the proxy is deallocated.

The wrapper object is otherwise a subclass of [NSProxy](../../foundation/nsproxy.md) and forwards messages to the original receiver object as an [NSProxy](../../foundation/nsproxy.md) does.

This method can be used to hide an [NSDiscardableContent](../../foundation/nsdiscardablecontent.md) object’s content volatility by creating an object that responds to the same messages but holds the contents of the original receiver available as long as the created proxy lives. Thus hidden, the [NSDiscardableContent](../../foundation/nsdiscardablecontent.md) object (by way of the proxy) can be given out to unsuspecting recipients of the object who would otherwise not know they might have to call [beginContentAccess()](<../../foundation/nsdiscardablecontent/begincontentaccess().md>) and [endContentAccess()](<../../foundation/nsdiscardablecontent/endcontentaccess().md>) around particular usages (specific to each [NSDiscardableContent](../../foundation/nsdiscardablecontent.md) object) of the [NSDiscardableContent](../../foundation/nsdiscardablecontent.md) object.
