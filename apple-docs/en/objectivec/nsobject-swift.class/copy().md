---
title: copy()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/copy()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/copy()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/copy%28%29.json'
content_hash: 'sha256:adf30273a116de64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# copy()

<sub>Instance Method</sub>

Returns the object returned by `copy(with:)`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copy() -> Any
```

## Return Value

The object returned by the [NSCopying](../../foundation/nscopying.md) protocol method [copy(with:)](<../../foundation/nscopying/copy(with_).md>),.

## Discussion

This is a convenience method for classes that adopt the [NSCopying](../../foundation/nscopying.md) protocol. An exception is raised if there is no implementation for [copy(with:)](<../../foundation/nscopying/copy(with_).md>).

`NSObject` does not itself support the [NSCopying](../../foundation/nscopying.md) protocol. Subclasses must support the protocol and implement the [copy(with:)](<../../foundation/nscopying/copy(with_).md>) method. A subclass version of the [copy(with:)](<../../foundation/nscopying/copy(with_).md>) method should send the message to `super` first, to incorporate its implementation, unless the subclass descends directly from `NSObject`.

## See Also

### Creating, Copying, and Deallocating Objects

- [- init](<init().md>) — Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [- mutableCopy](<mutablecopy().md>) — Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.
