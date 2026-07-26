---
title: functionConstantsDictionary
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunction/functionconstantsdictionary
source_url: 'https://developer.apple.com/documentation/metal/mtlfunction/functionconstantsdictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunction/functionconstantsdictionary.json'
content_hash: 'sha256:63734d8fa710b0a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunction](../mtlfunction.md)

# functionConstantsDictionary

<sub>Instance Property</sub>

A dictionary of function constants for a specialized function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var functionConstantsDictionary: [String : MTLFunctionConstant] { get }
```

## Discussion

This property returns a dictionary of the function constants that you need to provide to specialize this function. This property returns an empty dictionary if this function is already specialized or doesn’t declare any function constants.

To create the specialized function, set these constant values in a new [MTLFunctionConstantValues](../mtlfunctionconstantvalues.md) object and call the [- newFunctionWithName:constantValues:completionHandler:](<../mtllibrary/makefunction(name_constantvalues_completionhandler_).md>) method.
