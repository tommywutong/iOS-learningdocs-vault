---
title: 'storeIfNil(_:)'
framework: Synchronization
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/synchronization/atomiclazyreference/storeifnil(_:)'
source_url: 'https://developer.apple.com/documentation/synchronization/atomiclazyreference/storeifnil(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomiclazyreference/storeifnil%28_%3A%29.json'
content_hash: 'sha256:96315d06cccf3c10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Synchronization](../../synchronization.md) · [AtomicLazyReference](../atomiclazyreference.md)

# storeIfNil(_:)

<sub>Instance Method</sub>

Atomically initializes this reference if its current value is nil, then returns the initialized value. If this reference is already initialized, then `storeIfNil(_:)` discards its supplied argument and returns the current value without updating it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func storeIfNil(_ desired: consuming Instance) -> Instance
```

## Parameters

- `desired` — A value of `Instance` that we will attempt to store if the lazy reference is currently nil.

## Return Value

The value of `Instance` that was successfully stored within the lazy reference. This may or may not be the same value of `Instance` that was passed to this function.

## Discussion

The following example demonstrates how this can be used to implement a thread-safe lazily initialized reference:

```swift
class Image {
  let _histogram = AtomicLazyReference<Histogram>()

  // This is safe to call concurrently from multiple threads.
  var atomicLazyHistogram: Histogram {
    if let histogram = _histogram.load() { return histogram }
    // Note that code here may run concurrently on
    // multiple threads, but only one of them will get to
    // succeed setting the reference.
    let histogram = ...
    return _histogram.storeIfNil(histogram)
  }
}
```

> [!note] Note
> This operation uses acquiring-and-releasing memory ordering.
