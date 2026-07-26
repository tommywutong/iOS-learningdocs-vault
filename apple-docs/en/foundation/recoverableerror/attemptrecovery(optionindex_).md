---
title: 'attemptRecovery(optionIndex:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/recoverableerror/attemptrecovery(optionindex:)'
source_url: 'https://developer.apple.com/documentation/foundation/recoverableerror/attemptrecovery(optionindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/recoverableerror/attemptrecovery%28optionindex%3A%29.json'
content_hash: 'sha256:b9d17cc9179d54bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RecoverableError](../recoverableerror.md)

# attemptRecovery(optionIndex:)

<sub>Instance Method</sub>

Attempt to recover from this error when the user selected the option at the given index. Returns true to indicate successful recovery, and false otherwise.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attemptRecovery(optionIndex recoveryOptionIndex: Int) -> Bool
```

## Discussion

This entry point is used for recovery of errors handled at the “application” granularity, where nothing else in the application can proceed until the attempted error recovery completes.
