---
title: 'reflection(functionName:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtllibrary/reflection(functionname:)'
source_url: 'https://developer.apple.com/documentation/metal/mtllibrary/reflection(functionname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibrary/reflection%28functionname%3A%29.json'
content_hash: 'sha256:b5de7e6e19b4c840'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibrary](../mtllibrary.md)

# reflection(functionName:)

<sub>Instance Method</sub>

Retrieves reflection information for a function in the library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func reflection(functionName: String) -> MTLFunctionReflection?
```

## Parameters

- `functionName` — The name of a GPU function in the library. The name needs to match one of the elements in the string array of library’s [functionNames](functionnames.md) property.

## Return Value

An `MTLFunctionReflection` instance when the method succeeds; otherwise `nil`.

## Discussion

The reflection instance contains metadata information about a specific GPU function, which can include:

- Function parameters
- Return types
- Bindings
- Annotations from a developer, if available

> [!note] Note
> The Metal compiler generates the function’s reflection information when you or Xcode build the library.

The method only returns reflection information if all of the following conditions apply:

- The library has a function with a name that matches `functionName`.
- The deployment target is macOS 13.0 or later, or iOS 16.0 or later, or visionOS 2.0 or later.
