---
title: 'methodSignatureForSelector:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsproxy/methodsignatureforselector:'
source_url: 'https://developer.apple.com/documentation/foundation/nsproxy/methodsignatureforselector:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsproxy/methodsignatureforselector%3A.json'
content_hash: 'sha256:96cfbf3ead5c9530'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSProxy](../nsproxy.md)

# methodSignatureForSelector:

<sub>Instance Method</sub>

Raises `NSInvalidArgumentException`. Override this method in your concrete subclass to return a proper `NSMethodSignature` object for the given selector and the class your proxy objects stand in for.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSMethodSignature *) methodSignatureForSelector:(SEL) sel;
```

## Parameters

- `sel` — The selector for which to return a method signature.

## Return Value

Not applicable. The implementation provided by `NSProxy` raises an exception.

## Discussion

Be sure to avoid an infinite loop when necessary by checking that `sel` isn’t the selector for this method itself and by not sending any message that might invoke this method.

For example, if your proxy merely forwards messages to an instance variable named `realObject`, it can implement [methodSignatureForSelector:](methodsignatureforselector_.md) like this:

```objc
– (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector
{
    return [realObject methodSignatureForSelector:aSelector];
}
```

## See Also

### Related Documentation

- [methodSignatureForSelector:](../../objectivec/nsobject-swift.class/methodsignatureforselector_.md) — Returns an `NSMethodSignature` object that contains a description of the method identified by a given selector.

### Handling Unimplemented Methods

- [- forwardInvocation:](<forwardinvocation(__).md>) — Passes a given invocation to the real object the proxy represents.
