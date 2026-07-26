---
title: commit()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransaction/commit()
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/commit()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/commit%28%29.json'
content_hash: 'sha256:a02135de7c3c2f2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# commit()

<sub>Type Method</sub>

Commit all changes made during the current transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func commit()
```

## Discussion

Raises an exception if no current transaction exists.

## See Also

### Creating and Committing Transactions

- [+ begin](<begin().md>) — Begin a new transaction for the current thread.
- [+ flush](<flush().md>) — Flushes any extant implicit transaction.
