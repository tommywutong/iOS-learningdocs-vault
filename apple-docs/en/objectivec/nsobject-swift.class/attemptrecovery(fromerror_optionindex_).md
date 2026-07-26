---
title: 'attemptRecovery(fromError:optionIndex:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/attemptrecovery(fromerror:optionindex:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/attemptrecovery(fromerror:optionindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/attemptrecovery%28fromerror%3Aoptionindex%3A%29.json'
content_hash: 'sha256:93ee6b43ee00f916'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# attemptRecovery(fromError:optionIndex:)

<sub>Instance Method</sub>

Implemented to attempt a recovery from an error noted in an application-modal dialog.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attemptRecovery(fromError error: any Error, optionIndex recoveryOptionIndex: Int) -> Bool
```

## Parameters

- `error` — An [NSError](../../foundation/nserror.md) object that describes the error, including error recovery options.

- `recoveryOptionIndex` — The index of the user selected recovery option in `error`’s localized recovery array.

## Return Value

[YES](../yes.md) if the error recovery was completed successfully, [NO](../no.md) otherwise.

## Discussion

Invoked when an error alert is been presented to the user in an application-modal dialog, and the user has selected an error recovery option specified by `error`.
