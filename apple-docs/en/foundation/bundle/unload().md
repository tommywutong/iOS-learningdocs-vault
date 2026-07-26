---
title: unload()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/unload()
source_url: 'https://developer.apple.com/documentation/foundation/bundle/unload()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/unload%28%29.json'
content_hash: 'sha256:501cecebc65ad6c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# unload()

<sub>Instance Method</sub>

Unloads the code associated with the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unload() -> Bool
```

## Return Value

[true](../../swift/true.md) if the bundle was successfully unloaded or was not already loaded; otherwise, [false](../../swift/false.md) if the bundle could not be unloaded.

## Discussion

This method attempts to unload a bundle’s executable code using the underlying dynamic loader (typically `dyld`). You may use this method to unload plug-in and framework bundles when you no longer need the code they contain. You should use this method to unload bundles that were loaded using the methods of the `NSBundle` class only. Do not use this method to unload bundles that were originally loaded using the bundle-manipulation functions in Core Foundation.

It is the responsibility of the caller to ensure that no in-memory objects or data structures refer to the code being unloaded. For example, if you have an object whose class is defined in a bundle, you must release that object prior to unloading the bundle. Similarly, your code should not attempt to access any symbols defined in an unloaded bundle.

### Special Considerations

Prior to OS X version 10.5, code could not be unloaded once loaded, and this method would always return [false](../../swift/false.md). In macOS 10.5 and later, you can unload a bundle’s executable code using this method.

## See Also

### Loading code from a bundle

- [executableArchitectures](executablearchitectures.md) — An array of numbers indicating the architecture types supported by the bundle’s executable.
- [- preflightAndReturnError:](<preflight().md>) — Returns a Boolean value indicating whether the bundle’s executable code could be loaded successfully.
- [- load](<load().md>) — Dynamically loads the bundle’s executable code into a running program, if the code has not already been loaded.
- [- loadAndReturnError:](<loadandreturnerror().md>) — Loads the bundle’s executable code and returns any errors.
- [loaded](isloaded.md) — The load status of a bundle.
- [Mach-O Architecture](../1495005-mach-o-architecture.md) — Constants that describe the CPU types that a bundle’s executable code supports.
