---
title: 'imp_removeBlock(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/imp_removeblock(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/imp_removeblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/imp_removeblock%28_%3A%29.json'
content_hash: 'sha256:da981451d60f6fc6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# imp_removeBlock(_:)

<sub>Function</sub>

Disassociates a block from an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>), and releases the copy of the block that was created.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func imp_removeBlock(_ anImp: IMP) -> Bool
```

## Parameters

- `anImp` — An [IMP](imp.md) that was created using the [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) function.

## Return Value

[YES](yes.md) if the block was released successfully; otherwise, [NO](no.md) (for example, the function returns [NO](no.md) if the block was not used to create `anImp` previously).

## See Also

### Using Objective-C Language Features

- [objc_enumerationMutation](<objc_enumerationmutation(__).md>) — Inserted by the compiler when a mutation is detected during a foreach iteration.
- [objc_setEnumerationMutationHandler](<objc_setenumerationmutationhandler(__).md>) — Sets the current mutation handler.
- [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) — Creates a pointer to a function that calls the specified block when the method is called.
- [imp_getBlock](<imp_getblock(__).md>) — Returns the block associated with an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>).
- [objc_loadWeak](<objc_loadweak(__).md>) — Loads the object referenced by a weak pointer and returns it.
- [objc_storeWeak](<objc_storeweak(____).md>) — Stores a new value in a `__weak` variable.
