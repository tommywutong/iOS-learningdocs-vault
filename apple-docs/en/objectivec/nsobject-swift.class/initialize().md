---
title: initialize()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/initialize()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/initialize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/initialize%28%29.json'
content_hash: 'sha256:cc2fe1a4747a387c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# initialize()

<sub>Type Method</sub>

Initializes the class before it receives its first message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func initialize()
```

## Discussion

The runtime sends [+ initialize](<initialize().md>) to each class in a program just before the class, or any class that inherits from it, is sent its first message from within the program. Superclasses receive this message before their subclasses.

The runtime sends the [+ initialize](<initialize().md>) message to classes in a thread-safe manner. That is, [+ initialize](<initialize().md>) is run by the first thread to send a message to a class, and any other thread that tries to send a message to that class will block until [+ initialize](<initialize().md>) completes.

The superclass implementation may be called multiple times if subclasses do not implement [+ initialize](<initialize().md>)—the runtime will call the inherited implementation—or if subclasses explicitly call `[super initialize]`. If you want to protect yourself from being run multiple times, you can structure your implementation along these lines:

```objc
+ (void)initialize {
  if (self == [ClassName self]) {
    // ... do the initialization ...
  }
}
```

Because [+ initialize](<initialize().md>) is called in a blocking manner, it’s important to limit method implementations to the minimum amount of work necessary possible. Specifically, any code that takes locks that might be required by other classes in their [+ initialize](<initialize().md>) methods is liable to lead to deadlocks. Therefore, you should not rely on [+ initialize](<initialize().md>) for complex initialization, and should instead limit it to straightforward, class local initialization.

### Special Considerations

[+ initialize](<initialize().md>) is invoked only once per class. If you want to perform independent initialization for the class and for categories of the class, you should implement [+ load](<load().md>) methods.

## See Also

### Related Documentation

- [- init](<init().md>) — Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.

### Initializing a Class

- [+ load](<load().md>) — Invoked whenever a class or category is added to the Objective-C runtime; implement this method to perform class-specific behavior upon loading.
