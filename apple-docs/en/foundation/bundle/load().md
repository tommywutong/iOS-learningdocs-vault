---
title: load()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle/load()
source_url: 'https://developer.apple.com/documentation/foundation/bundle/load()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/load%28%29.json'
content_hash: 'sha256:4259f46db9e840e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# load()

<sub>Instance Method</sub>

Dynamically loads the bundle’s executable code into a running program, if the code has not already been loaded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func load() -> Bool
```

## Return Value

[true](../../swift/true.md) if the method successfully loads the bundle’s code or if the code has already been loaded, otherwise [false](../../swift/false.md).

## Discussion

You can use this method to load the code associated with a dynamically loaded bundle, such as a plug-in or framework. Prior to OS X version 10.5, a bundle would attempt to load its code—if it had any—only once. Once loaded, you could not unload that code. In macOS 10.5 and later, you can unload a bundle’s executable code using the [- unload](<unload().md>) method.

You don’t need to load a bundle’s executable code to search the bundle’s resources.

This method initializes the principal class in the bundle. To add code you want executed after loading, override the [initialize()](<../../objectivec/nsobject-swift.class/initialize().md>) class method of the principal class.

### Special Considerations

If an `NSBundle` object calls the [- load](<load().md>) method, it calls the [- unload](<unload().md>) method before being deallocated. Therefore, you should retain any `NSBundle` object for as long as any code from it is used by the app.

## See Also

### Related Documentation

- [principalClass](principalclass.md) — The bundle’s principal class.
- [- classNamed:](<classnamed(__).md>) — Returns the `Class` object for the specified name.

### Loading code from a bundle

- [executableArchitectures](executablearchitectures.md) — An array of numbers indicating the architecture types supported by the bundle’s executable.
- [- preflightAndReturnError:](<preflight().md>) — Returns a Boolean value indicating whether the bundle’s executable code could be loaded successfully.
- [- loadAndReturnError:](<loadandreturnerror().md>) — Loads the bundle’s executable code and returns any errors.
- [- unload](<unload().md>) — Unloads the code associated with the receiver.
- [loaded](isloaded.md) — The load status of a bundle.
- [Mach-O Architecture](../1495005-mach-o-architecture.md) — Constants that describe the CPU types that a bundle’s executable code supports.
