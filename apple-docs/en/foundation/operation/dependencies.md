---
title: dependencies
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operation/dependencies
source_url: 'https://developer.apple.com/documentation/foundation/operation/dependencies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation/dependencies.json'
content_hash: 'sha256:05fb9187745dbe24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Operation](../operation.md)

# dependencies

<sub>Instance Property</sub>

An array of the operation objects that must finish executing before the current object can begin executing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dependencies: [Operation] { get }
```

## Discussion

This property contains an array of `NSOperation` objects. To add an object to this array, use the [- addDependency:](<adddependency(__).md>) method.

An operation object must not execute until all of its dependent operations finish executing. Operations are not removed from this dependency list as they finish executing. You can use this list to track all dependent operations, including those that have already finished executing. The only way to remove an operation from this list is to use the [- removeDependency:](<removedependency(__).md>) method.

## See Also

### Managing Dependencies

- [- addDependency:](<adddependency(__).md>) — Makes the receiver dependent on the completion of the specified operation.
- [- removeDependency:](<removedependency(__).md>) — Removes the receiver’s dependence on the specified operation.
