---
title: begin()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransaction/begin()
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/begin()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/begin%28%29.json'
content_hash: 'sha256:bca3289bc217e2e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# begin()

<sub>Type Method</sub>

Begin a new transaction for the current thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func begin()
```

## Discussion

The transaction is nested within the thread’s current transaction, if there is one.

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)

### Creating and Committing Transactions

- [+ commit](<commit().md>) — Commit all changes made during the current transaction.
- [+ flush](<flush().md>) — Flushes any extant implicit transaction.
