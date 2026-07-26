---
title: flush()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransaction/flush()
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/flush()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/flush%28%29.json'
content_hash: 'sha256:27de2631c40bb7d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# flush()

<sub>Type Method</sub>

Flushes any extant implicit transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func flush()
```

## Discussion

Delays the commit until any nested explicit transactions have completed.

Flush is typically called automatically at the end of the current runloop, regardless of the runloop mode. If your application does not have a runloop, you must call this method explicitly.

However, you should attempt to avoid calling `flush` explicitly. By allowing `flush` to execute during the runloop your application will achieve better performance, atomic screen updates will be preserved, and transactions and animations that work from transaction to transaction will continue to function.

## See Also

### Creating and Committing Transactions

- [+ begin](<begin().md>) — Begin a new transaction for the current thread.
- [+ commit](<commit().md>) — Commit all changes made during the current transaction.
