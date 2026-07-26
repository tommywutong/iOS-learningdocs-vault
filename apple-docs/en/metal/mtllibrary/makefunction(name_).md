---
title: 'makeFunction(name:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtllibrary/makefunction(name:)'
source_url: 'https://developer.apple.com/documentation/metal/mtllibrary/makefunction(name:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibrary/makefunction%28name%3A%29.json'
content_hash: 'sha256:efe6ca1e7846b8eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibrary](../mtllibrary.md)

# makeFunction(name:)

<sub>Instance Method</sub>

Creates an instance that represents a shader function in the library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeFunction(name functionName: String) -> (any MTLFunction)?
```

## Parameters

- `functionName` — The name of the function.

## Return Value

An [MTLFunction](../mtlfunction.md), or `nil` if the named function isn’t found in the library.

## Discussion

If you call this method to retrieve a function that doesn’t use function constants, it returns an [MTLFunction](../mtlfunction.md) instance that you can use to build a render or compute pipeline.

If you call this method to retrieve a function that uses function constants to specialize its behavior, you can only use the returned instance to query the `functionConstants` property for the list of function constants. You can’t use to create a render or compute pipeline. To get a specialized instance that you can use to create a pipeline instance, call the [- newFunctionWithName:constantValues:completionHandler:](<makefunction(name_constantvalues_completionhandler_).md>) method or [- newFunctionWithName:constantValues:error:](<makefunction(name_constantvalues_).md>) to generate a specialized function.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Creating shader function instances

- [- newFunctionWithName:constantValues:completionHandler:](<makefunction(name_constantvalues_completionhandler_).md>) — Asynchronously creates a specialized shader function.
- [- newFunctionWithName:constantValues:error:](<makefunction(name_constantvalues_).md>) — Synchronously creates a specialized shader function.
- [- newFunctionWithDescriptor:completionHandler:](<makefunction(descriptor_completionhandler_).md>) — Asynchronously creates an object representing a shader function, using the specified descriptor.
- [- newFunctionWithDescriptor:error:](<makefunction(descriptor_).md>) — Synchronously creates an object representing a shader function, using the specified descriptor.
