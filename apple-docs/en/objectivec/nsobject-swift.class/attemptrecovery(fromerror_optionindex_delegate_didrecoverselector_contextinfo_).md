---
title: 'attemptRecovery(fromError:optionIndex:delegate:didRecoverSelector:contextInfo:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/attemptrecovery(fromerror:optionindex:delegate:didrecoverselector:contextinfo:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/attemptrecovery(fromerror:optionindex:delegate:didrecoverselector:contextinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/attemptrecovery%28fromerror%3Aoptionindex%3Adelegate%3Adidrecoverselector%3Acontextinfo%3A%29.json'
content_hash: 'sha256:69c4e2e8f82499df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# attemptRecovery(fromError:optionIndex:delegate:didRecoverSelector:contextInfo:)

<sub>Instance Method</sub>

Implemented to attempt a recovery from an error noted in a document-modal sheet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attemptRecovery(fromError error: any Error, optionIndex recoveryOptionIndex: Int, delegate: Any?, didRecoverSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

## Parameters

- `error` — An [NSError](../../foundation/nserror.md) object that describes the error, including error recovery options.

- `recoveryOptionIndex` — The index of the user selected recovery option in `error`’s localized recovery array.

- `delegate` — An object that is the modal delegate.

- `didRecoverSelector` — A selector identifying the method implemented by the modal delegate.

- `contextInfo` — Arbitrary data associated with the attempt at error recovery, to be passed to `delegate` in `didRecoverSelector`.

## Discussion

Invoked when an error alert is presented to the user in a document-modal sheet, and the user has selected an error recovery option specified by `error`. After recovery is attempted, your implementation should send `delegate` the message specified in `didRecoverSelector`, passing the provided `contextInfo`.

The `didRecoverSelector` should have the following signature:

```objc
- (void)didPresentErrorWithRecovery:(BOOL)didRecover contextInfo:(void *)contextInfo;
```

where `didRecover` is [YES](../yes.md) if the error recovery attempt was successful; otherwise it is [NO](../no.md).
