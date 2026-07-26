---
title: main()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operation/main()
source_url: 'https://developer.apple.com/documentation/foundation/operation/main()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation/main%28%29.json'
content_hash: 'sha256:7333a05443857baa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Operation](../operation.md)

# main()

<sub>Instance Method</sub>

Performs the receiver’s non-concurrent task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func main()
```

## Discussion

The default implementation of this method does nothing. You should override this method to perform the desired task. In your implementation, do not invoke `super`. This method will automatically execute within an autorelease pool provided by `NSOperation`, so you do not need to create your own autorelease pool block in your implementation.

If you are implementing a concurrent operation, you are not required to override this method but may do so if you plan to call it from your custom [- start](<start().md>) method.

## See Also

### Executing the Operation

- [- start](<start().md>) — Begins the execution of the operation.
- [completionBlock](completionblock.md) — The block to execute after the operation’s main task is completed.
