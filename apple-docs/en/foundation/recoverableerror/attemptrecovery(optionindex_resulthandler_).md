---
title: 'attemptRecovery(optionIndex:resultHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/recoverableerror/attemptrecovery(optionindex:resulthandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/recoverableerror/attemptrecovery(optionindex:resulthandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/recoverableerror/attemptrecovery%28optionindex%3Aresulthandler%3A%29.json'
content_hash: 'sha256:7fa612f9c51148f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RecoverableError](../recoverableerror.md)

# attemptRecovery(optionIndex:resultHandler:)

<sub>Instance Method</sub>

Attempt to recover from this error when the user selected the option at the given index. This routine must call handler and indicate whether recovery was successful (or not).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attemptRecovery(optionIndex recoveryOptionIndex: Int, resultHandler handler: @escaping (Bool) -> Void)
```

## Discussion

This entry point is used for recovery of errors handled at a “document” granularity, that do not affect the entire application.

## Default Implementations

### RecoverableError Implementations

- [attemptRecovery(optionIndex:resultHandler:)](<attemptrecovery(optionindex_resulthandler_)-1zbgz.md>) — Default implementation that uses the application-model recovery mechanism ([attemptRecovery(optionIndex:)](<attemptrecovery(optionindex_).md>)) to implement document-modal recovery.
