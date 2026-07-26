---
title: 'objc_loadWeak(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_loadweak(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_loadweak(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_loadweak%28_%3A%29.json'
content_hash: 'sha256:bf8b84d2d9e0b204'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_loadWeak(_:)

<sub>Function</sub>

Loads the object referenced by a weak pointer and returns it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_loadWeak(_ location: AutoreleasingUnsafeMutablePointer<AnyObject?>) -> Any?
```

## Parameters

- `location` — The address of the weak pointer.

## Return Value

The object pointed to by `location`, or `nil` if `location` is `nil`.

## Discussion

This function loads the object referenced by a weak pointer and returns it after retaining and autoreleasing the object. As a result, the object stays alive long enough for the caller to use it. This function is typically used anywhere a `__weak` variable is used in an expression.

## See Also

### Using Objective-C Language Features

- [objc_enumerationMutation](<objc_enumerationmutation(__).md>) — Inserted by the compiler when a mutation is detected during a foreach iteration.
- [objc_setEnumerationMutationHandler](<objc_setenumerationmutationhandler(__).md>) — Sets the current mutation handler.
- [imp_implementationWithBlock](<imp_implementationwithblock(__).md>) — Creates a pointer to a function that calls the specified block when the method is called.
- [imp_getBlock](<imp_getblock(__).md>) — Returns the block associated with an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>).
- [imp_removeBlock](<imp_removeblock(__).md>) — Disassociates a block from an `IMP` that was created using [imp_implementationWithBlock](<imp_implementationwithblock(__).md>), and releases the copy of the block that was created.
- [objc_storeWeak](<objc_storeweak(____).md>) — Stores a new value in a `__weak` variable.
