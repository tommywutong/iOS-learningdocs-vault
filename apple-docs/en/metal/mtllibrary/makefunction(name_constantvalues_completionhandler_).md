---
title: 'makeFunction(name:constantValues:completionHandler:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtllibrary/makefunction(name:constantvalues:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/metal/mtllibrary/makefunction(name:constantvalues:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibrary/makefunction%28name%3Aconstantvalues%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:64978cde4e2fb70e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibrary](../mtllibrary.md)

# makeFunction(name:constantValues:completionHandler:)

<sub>Instance Method</sub>

Asynchronously creates a specialized shader function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeFunction(name: String, constantValues: MTLFunctionConstantValues, completionHandler: @escaping @Sendable ((any MTLFunction)?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeFunction(name: String, constantValues: MTLFunctionConstantValues) async throws -> any MTLFunction
```

## Parameters

- `name` — The name of the specialized function.

- `constantValues` — The set of constant values assigned to the function constants. Compilation fails if you don’t provide valid constant values for all required function constants.

- `completionHandler` — A block of code that Metal calls after it creates the specialized function. - **function** — A specialized function, or `nil` if an error occurred. - **error** — An error object that describes compilation problems, if any. This object contains compiler errors if the specialized function is `nil`, and compiler warnings if Metal created the specialized function with warnings. If Metal created the function without errors or warnings, this error object is `nil`.

## Discussion

Function constant values are first looked up by their index, then by their name. Metal ignores any values that don’t correspond to a function constant in the named function without generating errors or warnings.

## See Also

### Creating shader function instances

- [- newFunctionWithName:](<makefunction(name_).md>) — Creates an instance that represents a shader function in the library.
- [- newFunctionWithName:constantValues:error:](<makefunction(name_constantvalues_).md>) — Synchronously creates a specialized shader function.
- [- newFunctionWithDescriptor:completionHandler:](<makefunction(descriptor_completionhandler_).md>) — Asynchronously creates an object representing a shader function, using the specified descriptor.
- [- newFunctionWithDescriptor:error:](<makefunction(descriptor_).md>) — Synchronously creates an object representing a shader function, using the specified descriptor.
