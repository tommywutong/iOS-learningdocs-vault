---
title: 'objc_setEnumerationMutationHandler(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_setenumerationmutationhandler(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_setenumerationmutationhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_setenumerationmutationhandler%28_%3A%29.json'
content_hash: 'sha256:56468a1ee8715cfa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_setEnumerationMutationHandler(_:)

<sub>Function</sub>

Sets the current mutation handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_setEnumerationMutationHandler(_ handler: ((Any) -> Void)?)
```

## Parameters

- `handler` — A function pointer to the new mutation handler.

## See Also

### Using Objective-C Language Features

- [objc_enumerationMutation](<objc_enumerationmutation(__).md>) — Inserted by the compiler when a mutation is detected during a foreach iteration.
- [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) — Creates a pointer to a function that calls the specified block when the method is called.
- [imp_getBlock](<imp_getblock(__).md>) — Returns the block associated with an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>).
- [imp_removeBlock](<imp_removeblock(__).md>) — Disassociates a block from an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>), and releases the copy of the block that was created.
- [objc_loadWeak](<objc_loadweak(__).md>) — Loads the object referenced by a weak pointer and returns it.
- [objc_storeWeak](<objc_storeweak(____).md>) — Stores a new value in a `__weak` variable.
