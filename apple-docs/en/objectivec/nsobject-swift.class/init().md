---
title: init()
framework: Objective-C Runtime
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/init()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/init%28%29.json'
content_hash: 'sha256:24ca24f9d648cfde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# init()

<sub>Initializer</sub>

Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Return Value

An initialized object, or `nil` if an object could not be created for some reason that would not result in an exception.

## Discussion

An [- init](<init().md>) message is coupled with an [alloc](alloc.md) (or [allocWithZone:](allocwithzone_.md)) message in the same line of code:

```objc
SomeClass *object = [[SomeClass alloc] init];
```

An object isn’t ready to be used until it has been initialized.

In a custom implementation of this method, you must invoke super’s [Initialization](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21) then initialize and return the new object. If the new object can’t be initialized, the method should return `nil`. For example, a hypothetical `BuiltInCamera` class might return `nil` from its `init` method if run on a device that has no camera.

```objc
- (instancetype)init {
    if (self = [super init]) {
        // Initialize self
    }
    return self;
}
```

In some cases, a custom implementation of the [- init](<init().md>) method might return a substitute object. You must therefore always use the object returned by [- init](<init().md>), and not the one returned by [alloc](alloc.md) or [allocWithZone:](allocwithzone_.md), in subsequent code.

The [- init](<init().md>) method defined in the `NSObject` class does no initialization; it simply returns `self`. In terms of nullability, callers can assume that the `NSObject` implementation of [- init](<init().md>) does not return `nil`.

## See Also

### Creating, Copying, and Deallocating Objects

- [- copy](<copy().md>) — Returns the object returned by `copy(with:)`.
- [- mutableCopy](<mutablecopy().md>) — Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.
