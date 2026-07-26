---
title: 'finishedHandlingError(_:recovered:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/finishedhandlingerror(_:recovered:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/finishedhandlingerror(_:recovered:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/finishedhandlingerror%28_%3Arecovered%3A%29.json'
content_hash: 'sha256:8d92ba673d1c1411'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# finishedHandlingError(_:recovered:)

<sub>Instance Method</sub>

Tells UIKit that you finished handling the error.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func finishedHandlingError(_ error: any Error, recovered: Bool)
```

## Parameters

- `error` — An error object encapsulating information about the error.

- `recovered` — [true](../../swift/true.md) if you recovered from the error, otherwise [false](../../swift/false.md).

## Discussion

This method is called by default when handling of an error (including any user interaction) is complete. Subclasses need to call this method only if they override [- handleError:userInteractionPermitted:](<handleerror(__userinteractionpermitted_).md>) and do not call the superclass implementation (`super`). If you override this method, you must call `super`.

## See Also

### Resolving conflicts and handling errors

- [- handleError:userInteractionPermitted:](<handleerror(__userinteractionpermitted_).md>) — Handles an error that occurs during an attempt to read, save, or revert a document.
- [- userInteractionNoLongerPermittedForError:](<userinteractionnolongerpermitted(forerror_).md>) — Indicates when it’s no longer safe to proceed without immediately handling the error.
