---
title: 'checkResourceIsReachableAndReturnError(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/checkresourceisreachableandreturnerror(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/checkresourceisreachableandreturnerror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/checkresourceisreachableandreturnerror%28_%3A%29.json'
content_hash: 'sha256:0cccb39b82dc6a1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# checkResourceIsReachableAndReturnError(_:)

<sub>Instance Method</sub>

Returns whether the resource pointed to by a file URL can be reached.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func checkResourceIsReachableAndReturnError(_ error: NSErrorPointer) -> Bool
```

## Parameters

- `error` — The error that occurred when the resource could not be reached.

## Return Value

[true](../../swift/true.md) if the resource is reachable; otherwise, [false](../../swift/false.md).

## Discussion

This method synchronously checks if the file at the provided URL is reachable. Checking reachability is appropriate when making decisions that do not require other immediate operations on the resource, such as periodic maintenance of user interface state that depends on the existence of a specific document. For example, you might remove an item from a download list if the user deletes the file.

If your app must perform operations on the file, such as opening it or copying resource properties, it is more efficient to attempt the operation and handle any failure that may occur.

If this method returns [false](../../swift/false.md), the object pointer referenced by `error` is populated with additional information.

## See Also

### Querying an NSURL

- [- isFileReferenceURL](<isfilereferenceurl().md>) — Returns whether the URL is a file reference URL.
- [fileURL](isfileurl.md) — A boolean value that determines whether the receiver is a file URL.
