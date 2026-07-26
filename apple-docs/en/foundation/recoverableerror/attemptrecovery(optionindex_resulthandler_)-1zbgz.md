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
doc_path: '/documentation/foundation/recoverableerror/attemptrecovery(optionindex:resulthandler:)-1zbgz'
source_url: 'https://developer.apple.com/documentation/foundation/recoverableerror/attemptrecovery(optionindex:resulthandler:)-1zbgz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/recoverableerror/attemptrecovery%28optionindex%3Aresulthandler%3A%29-1zbgz.json'
content_hash: 'sha256:47b48e70c942c22f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RecoverableError](../recoverableerror.md)

# attemptRecovery(optionIndex:resultHandler:)

<sub>Instance Method</sub>

Default implementation that uses the application-model recovery mechanism ([attemptRecovery(optionIndex:)](<attemptrecovery(optionindex_).md>)) to implement document-modal recovery.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attemptRecovery(optionIndex recoveryOptionIndex: Int, resultHandler handler: @escaping (Bool) -> Void)
```
