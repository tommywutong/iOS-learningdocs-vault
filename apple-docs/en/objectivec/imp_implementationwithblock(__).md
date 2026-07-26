---
title: 'imp_implementationWithBlock(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/imp_implementationwithblock(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/imp_implementationwithblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/imp_implementationwithblock%28_%3A%29.json'
content_hash: 'sha256:443359328d6ca046'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# imp_implementationWithBlock(_:)

<sub>Function</sub>

Creates a pointer to a function that calls the specified block when the method is called.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func imp_implementationWithBlock(_ block: Any) -> IMP
```

## Parameters

- `block` — The block that implements this method. The signature of `block` should be `method_return_type ^(id self, method_args …)`. The selector of the method is not available to `block`. `block` is copied with `Block_copy()`.

## Return Value

The [IMP](imp.md) that calls `block`. You must dispose of the returned [IMP](imp.md) using the function.

## See Also

### Using Objective-C Language Features

- [objc_enumerationMutation](<objc_enumerationmutation(__).md>) — Inserted by the compiler when a mutation is detected during a foreach iteration.
- [objc_setEnumerationMutationHandler](<objc_setenumerationmutationhandler(__).md>) — Sets the current mutation handler.
- [imp_getBlock](<imp_getblock(__).md>) — Returns the block associated with an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>).
- [imp_removeBlock](<imp_removeblock(__).md>) — Disassociates a block from an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>), and releases the copy of the block that was created.
- [objc_loadWeak](<objc_loadweak(__).md>) — Loads the object referenced by a weak pointer and returns it.
- [objc_storeWeak](<objc_storeweak(____).md>) — Stores a new value in a `__weak` variable.
