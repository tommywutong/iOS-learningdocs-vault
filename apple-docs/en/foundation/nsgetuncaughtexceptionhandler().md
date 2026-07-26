---
title: NSGetUncaughtExceptionHandler()
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsgetuncaughtexceptionhandler()
source_url: 'https://developer.apple.com/documentation/foundation/nsgetuncaughtexceptionhandler()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgetuncaughtexceptionhandler%28%29.json'
content_hash: 'sha256:bf1c44633fbcbbba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSGetUncaughtExceptionHandler()

<sub>Function</sub>

Returns the top-level error handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSGetUncaughtExceptionHandler() -> ((NSException) -> Void)?
```

## Return Value

A pointer to the top-level error-handling function where you can perform last-minute logging before the program terminates.

## See Also

### Related Documentation

- [NSSetUncaughtExceptionHandler](<nssetuncaughtexceptionhandler(__).md>) — Changes the top-level error handler.

### Functions

- [NSSetUncaughtExceptionHandler](<nssetuncaughtexceptionhandler(__).md>) — Changes the top-level error handler.
