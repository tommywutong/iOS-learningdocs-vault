---
title: checkPromisedItemIsReachable()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/checkpromiseditemisreachable()
source_url: 'https://developer.apple.com/documentation/foundation/url/checkpromiseditemisreachable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/checkpromiseditemisreachable%28%29.json'
content_hash: 'sha256:7a5162f28aedd3f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# checkPromisedItemIsReachable()

<sub>Instance Method</sub>

Returns whether the promised item URL’s resource exists and is reachable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func checkPromisedItemIsReachable() throws -> Bool
```

## Discussion

This method synchronously checks if the resource’s backing store is reachable. Checking reachability is appropriate when making decisions that do not require other immediate operations on the resource, e.g. periodic maintenance of UI state that depends on the existence of a specific document. When performing operations such as opening a file or copying resource properties, it is more efficient to simply try the operation and handle failures. This method is currently applicable only to URLs for file system resources. For other URL types, `false` is returned.

## See Also

### Working with promised items

- [promisedItemResourceValues(forKeys:)](<promiseditemresourcevalues(forkeys_).md>) — Gets resource values from URLs of ‘promised’ items.
