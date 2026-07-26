---
title: 'perform(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 1.0+, iPadOS 1.0+, Mac Catalyst 1.0+, macOS 10.0+, tvOS 1.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/perform(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/perform(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/perform%28_%3A%29.json'
content_hash: 'sha256:2c8aa6b935d15e54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# perform(_:)

<sub>Instance Method</sub>

Sends a specified message to the receiver and returns the result of the message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ aSelector: Selector!) -> Unmanaged<AnyObject>!
```

## Parameters

- `aSelector` — A selector identifying the message to send. The message should take no arguments. If `aSelector` is `NULL`, an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) is raised.

## Return Value

An object that is the result of the message.

## Discussion

Calling the [- performSelector:](<perform(__).md>) method is equivalent to sending the `aSelector` message directly to the receiver. For example, the following both do the same thing if `anObject` is an instance of `MyObject`:

**Swift**

```swift
let aClone = anObject.copy()
let aClone = anObject.perform(#selector(MyObject.copy)).takeRetainedValue()
```

**Objective-C**

```objc
id aClone = [anObject copy];
id aClone = [anObject performSelector:@selector(copy)];
id aClone = [anObject performSelector:sel_getUid("copy")];
```

The [- performSelector:](<perform(__).md>) method allows you to send messages that aren’t determined until run-time. This means that you can pass a variable selector as the argument:

**Swift**

```swift
let aSelector = findTheAppropriateSelectorForTheCurrentSituation()
let returnedObject = anObject.perform(aSelector).takeUnretainedValue()
```

**Objective-C**

```objc
SEL aSelector = findTheAppropriateSelectorForTheCurrentSituation();
id returnedObject = [anObject performSelector:aSelector];
```

Use caution when doing this. This method returns an implicitly unwrapped optional unmanaged pointer to an `AnyObject` instance ([Unmanaged](../../swift/unmanaged.md)`<`[AnyObject](../../swift/anyobject.md)`>!`).  It’s up to you to decide how to bring the instance into Swift’s memory management scheme.  Different messages require different memory management strategies for their returned objects, and it might not be obvious which to use.

Usually, a caller isn’t responsible for the memory of a returned instance, in which case you use [takeUnretainedValue()](<../../swift/unmanaged/takeunretainedvalue().md>), as shown above. However, for any of the creation methods, such as [- copy](<../nsobject-swift.class/copy().md>), the caller is responsible, and you use [takeRetainedValue()](<../../swift/unmanaged/takeretainedvalue().md>) instead. See [Memory Management Policy](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmRules.html#//apple_ref/doc/uid/20000994) in [Advanced Memory Management Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i) for a description of ownership expectations.

Due to this uncertainty, the compiler generates a warning if you supply a variable selector while using ARC to manage memory. Because it can’t determine ownership of the returned object at compile-time, ARC makes the assumption that the caller does _not_ need to take ownership, but this may not be true. The compiler warning alerts you to the potential for a memory leak.

To avoid the warning, if you know that `aSelector` has no return value, you might be able to use [- performSelectorOnMainThread:withObject:waitUntilDone:](<../nsobject-swift.class/performselector(onmainthread_with_waituntildone_).md>) or one of the related methods available in [NSObject](../nsobject-swift.class.md).

For a more general solution, use [NSInvocation](../../foundation/nsinvocation.md) to construct a message that you can invoke with an arbitrary argument list and return value.

Alternatively, consider restructuring your code to use blocks as a means of passing chunks of functionality through an API. See [Blocks Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40007502) for details.

> [!important] Important
> Because of the inherent lack of type safety, this API isn’t recommended for use in Swift unless your code specifically relies on the dynamic method resolution provided by the Objective-C run-time.
>
> For more information about using selectors in Swift and alternatives to the [- performSelector:](<perform(__).md>) function, read [Using Objective-C Runtime Features in Swift](../../swift/using-objective-c-runtime-features-in-swift.md).

## See Also

### Sending Messages

- [- performSelector:withObject:](<perform(__with_).md>) — Sends a message to the receiver with an object as the argument.
- [- performSelector:withObject:withObject:](<perform(__with_with_).md>) — Sends a message to the receiver with two objects as arguments.
