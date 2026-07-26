---
title: 'unarchiverDidFinish(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiverdelegate/unarchiverdidfinish(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/unarchiverdidfinish(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiverdelegate/unarchiverdidfinish%28_%3A%29.json'
content_hash: 'sha256:777419d088633a3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiverDelegate](../nskeyedunarchiverdelegate.md)

# unarchiverDidFinish(_:)

<sub>Instance Method</sub>

Notifies the delegate that decoding has finished.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func unarchiverDidFinish(_ unarchiver: NSKeyedUnarchiver)
```

## Parameters

- `unarchiver` — An unarchiver for which the receiver is the delegate.

## See Also

### Finishing Decoding

- [- unarchiverWillFinish:](<unarchiverwillfinish(__).md>) — Notifies the delegate that decoding is about to finish.
