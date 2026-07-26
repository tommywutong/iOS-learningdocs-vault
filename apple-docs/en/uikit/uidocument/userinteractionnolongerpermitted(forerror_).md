---
title: 'userInteractionNoLongerPermitted(forError:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/userinteractionnolongerpermitted(forerror:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/userinteractionnolongerpermitted(forerror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/userinteractionnolongerpermitted%28forerror%3A%29.json'
content_hash: 'sha256:0afa571f0d9f9cf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# userInteractionNoLongerPermitted(forError:)

<sub>Instance Method</sub>

Indicates when it’s no longer safe to proceed without immediately handling the error.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func userInteractionNoLongerPermitted(forError error: any Error)
```

## Parameters

- `error` — An error object encapsulating information about the error.

## Discussion

UIKit calls this method when it’s no longer safe to proceed without immediately handling the error, such as when the application is being suspended. Subclasses that override this method must immediately end error handling (including dismissing any interactive user interface) and call [- finishedHandlingError:recovered:](<finishedhandlingerror(__recovered_).md>) before returning. It’s only necessary to override this method if you override [- handleError:userInteractionPermitted:](<handleerror(__userinteractionpermitted_).md>) without invoking the superclass implementation (`super`).

## See Also

### Resolving conflicts and handling errors

- [- handleError:userInteractionPermitted:](<handleerror(__userinteractionpermitted_).md>) — Handles an error that occurs during an attempt to read, save, or revert a document.
- [- finishedHandlingError:recovered:](<finishedhandlingerror(__recovered_).md>) — Tells UIKit that you finished handling the error.
