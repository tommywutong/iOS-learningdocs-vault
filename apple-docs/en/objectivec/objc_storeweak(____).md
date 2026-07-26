---
title: 'objc_storeWeak(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_storeweak(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_storeweak(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_storeweak%28_%3A_%3A%29.json'
content_hash: 'sha256:2135c0973018fe4e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_storeWeak(_:_:)

<sub>Function</sub>

Stores a new value in a `__weak` variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_storeWeak(_ location: AutoreleasingUnsafeMutablePointer<AnyObject?>, _ obj: Any?) -> Any?
```

## Parameters

- `location` — The address of the weak pointer.

- `obj` — The new object you want the weak pointer to now point to.

## Return Value

The value stored in `location` (that is, `obj`).

## Discussion

This function is typically used anywhere a `__weak` variable is the target of an assignment.

## See Also

### Using Objective-C Language Features

- [objc_enumerationMutation](<objc_enumerationmutation(__).md>) — Inserted by the compiler when a mutation is detected during a foreach iteration.
- [objc_setEnumerationMutationHandler](<objc_setenumerationmutationhandler(__).md>) — Sets the current mutation handler.
- [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) — Creates a pointer to a function that calls the specified block when the method is called.
- [imp_getBlock](<imp_getblock(__).md>) — Returns the block associated with an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>).
- [imp_removeBlock](<imp_removeblock(__).md>) — Disassociates a block from an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>), and releases the copy of the block that was created.
- [objc_loadWeak](<objc_loadweak(__).md>) — Loads the object referenced by a weak pointer and returns it.
