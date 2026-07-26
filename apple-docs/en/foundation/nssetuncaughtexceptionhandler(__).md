---
title: 'NSSetUncaughtExceptionHandler(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nssetuncaughtexceptionhandler(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nssetuncaughtexceptionhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssetuncaughtexceptionhandler%28_%3A%29.json'
content_hash: 'sha256:ef478e5bd767fd5b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSetUncaughtExceptionHandler(_:)

<sub>Function</sub>

Changes the top-level error handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSSetUncaughtExceptionHandler(_: ((NSException) -> Void)?)
```

## Discussion

Sets the top-level error-handling function where you can perform last-minute logging before the program terminates.

## See Also

### Related Documentation

- [NSGetUncaughtExceptionHandler](<nsgetuncaughtexceptionhandler().md>) — Returns the top-level error handler.
- [reportException(_:)](<../appkit/nsapplication/reportexception(__).md>) — Logs a given exception by calling `NSLog()`.

### Functions

- [NSGetUncaughtExceptionHandler](<nsgetuncaughtexceptionhandler().md>) — Returns the top-level error handler.
