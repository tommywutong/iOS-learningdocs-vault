---
title: 'imp_getBlock(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/imp_getblock(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/imp_getblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/imp_getblock%28_%3A%29.json'
content_hash: 'sha256:7bb099e55a54a357'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# imp_getBlock(_:)

<sub>Function</sub>

Returns the block associated with an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func imp_getBlock(_ anImp: IMP) -> Any?
```

## Parameters

- `anImp` — The [IMP](imp.md) that calls this block.

## Return Value

The block called by `anImp`.

## See Also

### Using Objective-C Language Features

- [objc_enumerationMutation](<objc_enumerationmutation(__).md>) — Inserted by the compiler when a mutation is detected during a foreach iteration.
- [objc_setEnumerationMutationHandler](<objc_setenumerationmutationhandler(__).md>) — Sets the current mutation handler.
- [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) — Creates a pointer to a function that calls the specified block when the method is called.
- [imp_removeBlock](<imp_removeblock(__).md>) — Disassociates a block from an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>), and releases the copy of the block that was created.
- [objc_loadWeak](<objc_loadweak(__).md>) — Loads the object referenced by a weak pointer and returns it.
- [objc_storeWeak](<objc_storeweak(____).md>) — Stores a new value in a `__weak` variable.
