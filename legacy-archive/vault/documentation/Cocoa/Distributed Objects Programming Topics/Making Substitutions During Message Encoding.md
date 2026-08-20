---
title: Distributed Objects Programming Topics
apple_id: 10000102i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2017-06-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Tasks/substitutions.html
archived_at: '2026-07-15T07:15:04.104338Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Distributed Objects Programming Topics](Introduction%20to%20Distributed%20Objects.md)


[Next](Using%20NSInvocation.md)[Previous](Authenticating%20Connections.md)

For interprocess communication, you should use XPC instead; see _[XPC Services API Reference](https://developer.apple.com/documentation/xpc)_ for more information.

# Making Substitutions During Message Encoding

Like its abstract superclass, `NSCoder`, `NSPortCoder` makes use of substitution methods that allow an object to encode itself as an instance of another class or to replace another object for itself. An object may need to offer a different replacement when being encoded specifically by an `NSPortCoder` object, however, so instead of the generic `classForCoder` and `replacementObjectForCoder:` methods, `NSPortCoder` invokes `classForPortCoder` and `replacementObjectForPortCoder:`. Their default implementations in `NSObject` fall back to the generic methods, providing reasonable default behavior. (`NSPortCoder` does not use a special substitution method for decoding; it simply uses `awakeAfterUsingCoder:` as `NSCoder` does.)

The generic `classForCoder` method is most useful for mapping private subclass hierarchies through a public superclass, which (for example) aids the stability of archives when subclasses are private or subject to change. Since processes communicating at run time typically use the same version of a class library, this mapping is often not needed in distributed objects communication. `classForPortCoder` allows an object to bypass or override the generic `classForCoder` behavior, sending its real class (or simply a different one from the generic case) to the communicating process or thread. If you implement a group of classes that use the generic `classForCoder` method, you should also consider using `classForPortCoder` to handle the special case of encoding with the distributed objects system.

The generic `replacementObjectForCoder:` method offers a standard way to substitute a different instance at encoding time. `replacementObjectForPortCoder:` specifically allows for the substitution of proxies over a distributed objects connection. The receiver of a `replacementObjectForPortCoder:` message can ask the `NSPortCoder` instance whether it should be encoded `bycopy` or not, and return itself or a proxy as appropriate. `NSObject`'s implementation always returns a proxy, so subclasses that allow `bycopy` encoding should override `replacementObjectForPortCoder:` to perform at least as this sample does:

```objc
- (id)replacementObjectForPortCoder:(NSPortCoder *)encoder
{
    if ([encoder isBycopy]) return self;
    return [super replacementObjectForPortCoder:encoder];
}
```

If the `NSPortCoder` object returns `YES` when sent an `isBycopy` message, this example method returns _self_, which results in the receiver being sent an `encodeWithCoder:` message. If the `NSPortCoder` object returns `NO`, this method invokes the superclass’s implementation, which typically returns an instance of `NSDistantObject`.

[Next](Using%20NSInvocation.md)[Previous](Authenticating%20Connections.md)

