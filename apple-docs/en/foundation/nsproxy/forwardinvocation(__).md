---
title: 'forwardInvocation(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsproxy/forwardinvocation(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsproxy/forwardinvocation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsproxy/forwardinvocation%28_%3A%29.json'
content_hash: 'sha256:6abd0834d773ed75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSProxy](../nsproxy.md)

# forwardInvocation(_:)

<sub>Instance Method</sub>

Passes a given invocation to the real object the proxy represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func forwardInvocation(_ invocation: NSInvocation)
```

## Parameters

- `invocation` — The invocation to forward.

## Discussion

`NSProxy`’s implementation merely raises `NSInvalidArgumentException`. Override this method in your subclass to handle `invocation` appropriately, at the very least by setting its return value.

For example, if your proxy merely forwards messages to an instance variable named `realObject`, it can implement [- forwardInvocation:](<forwardinvocation(__).md>) like this:

```objc
- (void)forwardInvocation:(NSInvocation *)anInvocation
{
    [anInvocation setTarget:realObject];
    [anInvocation invoke];
    return;
}
```
