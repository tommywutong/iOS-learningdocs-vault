---
title: 'resolveInstanceMethod(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/resolveinstancemethod(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/resolveinstancemethod(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/resolveinstancemethod%28_%3A%29.json'
content_hash: 'sha256:e2aca049fa024731'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# resolveInstanceMethod(_:)

<sub>Type Method</sub>

Dynamically provides an implementation for a given selector for an instance method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func resolveInstanceMethod(_ sel: Selector!) -> Bool
```

## Parameters

- `sel` — The name of a selector to resolve.

## Return Value

[YES](../yes.md) if the method was found and added to the receiver, otherwise [NO](../no.md).

## Discussion

This method and [+ resolveClassMethod:](<resolveclassmethod(__).md>) allow you to dynamically provide an implementation for a given selector.

An Objective-C method is simply a C function that take at least two arguments—`self` and `_cmd`. Using the [class_addMethod](<../class_addmethod(________).md>) function, you can add a function to a class as a method. Given the following function:

```objc
void dynamicMethodIMP(id self, SEL _cmd)
{
    // implementation ....
}
```

you can use `resolveInstanceMethod:` to dynamically add it to a class as a method (called `resolveThisMethodDynamically`) like this:

```objc
+ (BOOL) resolveInstanceMethod:(SEL)aSEL
{
    if (aSEL == @selector(resolveThisMethodDynamically))
    {
          class_addMethod([self class], aSEL, (IMP) dynamicMethodIMP, "v@:");
          return YES;
    }
    return [super resolveInstanceMethod:aSel];
}
```

### Special Considerations

This method is called before the Objective-C forwarding mechanism is invoked. If [- respondsToSelector:](<../nsobjectprotocol/responds(to_).md>) or [+ instancesRespondToSelector:](<instancesrespond(to_).md>) is invoked, the dynamic method resolver is given the opportunity to provide an `IMP` for the given selector first.

## See Also

### Dynamically Resolving Methods

- [+ resolveClassMethod:](<resolveclassmethod(__).md>) — Dynamically provides an implementation for a given selector for a class method.
