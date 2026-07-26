---
title: try()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdistributedlock/try()
source_url: 'https://developer.apple.com/documentation/foundation/nsdistributedlock/try()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistributedlock/try%28%29.json'
content_hash: 'sha256:b1dfa130b2df2257'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDistributedLock](../nsdistributedlock.md)

# try()

<sub>Instance Method</sub>

Attempts to acquire the receiver and immediately returns a Boolean value that indicates whether the attempt was successful.

<sub>Mac Catalyst, macOS</sub>

```swift
func `try`() -> Bool
```

## Return Value

[true](../../swift/true.md) if the attempt to acquire the receiver was successful, otherwise [false](../../swift/false.md).

## Discussion

Raises `NSGenericException` if a file-system error occurs.

## See Also

### Related Documentation

- [- unlock](<unlock().md>) — Relinquishes the receiver.
