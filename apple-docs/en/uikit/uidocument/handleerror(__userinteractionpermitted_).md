---
title: 'handleError(_:userInteractionPermitted:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/handleerror(_:userinteractionpermitted:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/handleerror(_:userinteractionpermitted:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/handleerror%28_%3Auserinteractionpermitted%3A%29.json'
content_hash: 'sha256:320cb8489a26e8fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# handleError(_:userInteractionPermitted:)

<sub>Instance Method</sub>

Handles an error that occurs during an attempt to read, save, or revert a document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func handleError(_ error: any Error, userInteractionPermitted: Bool)
```

## Parameters

- `error` — An object encapsulating information about an error encountered in an attempt to open, save, or revert a document. The error domain is [NSCocoaErrorDomain](../../foundation/nscocoaerrordomain.md). The error code is one of the `enum` constants declared in `FoundationErrors.h`.

- `userInteractionPermitted` — If [false](../../swift/false.md), no attempt is (or should be) made to present a modal view to the user. This value can be [false](../../swift/false.md) in cases such as when a save operation fails while the application is being suspended. If this parameter is [true](../../swift/true.md), UIKit or your override may present error information to the user in a modal view and (optionally) allow the user to resolve the error.

## Discussion

Typical [UIDocument](../uidocument.md) subclasses don’t need to call or override this method. Instead, they can observe the [UIDocumentStateChangedNotification](statechangednotification.md) notification to be notified of changes in document state. In their notification handler, they can check the value of the [documentState](documentstate.md) property and proceed accordingly. See [Resolve conflicts and handle errors](../uidocument.md#Resolve-conflicts-and-handle-errors) for a discussion of this.

If you’re using managed documents (instances of the [UIManagedDocument](../uimanageddocument.md) subclass), you must subclass this method and, if desired, the [- finishedHandlingError:recovered:](<finishedhandlingerror(__recovered_).md>) method. Subclassing allows your app to observe errors in saving or validation. The [UIDocumentStateChangedNotification](statechangednotification.md) notification doesn’t contain a `userInfo` dictionary and so doesn’t convey specific error information.

If you directly call any of the advanced reading and writing methods that have an error-object parameter (for example, [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<writecontents(__andattributes_safelyto_for_).md>)) and that call returns an [NSError](../../foundation/nserror.md) object by indirection, you should call this method ([- handleError:userInteractionPermitted:](<handleerror(__userinteractionpermitted_).md>)), passing in the error object.

This method is called by the default implementations of [- openWithCompletionHandler:](<open(completionhandler_).md>) and [- saveToURL:forSaveOperation:completionHandler:](<save(to_for_completionhandler_).md>) when [UIDocument](../uidocument.md) encounters a reading or writing error, respectively.

If you override this method and don’t invoke the superclass implementation (`super`), you’re responsible for the following:

- Calling [- finishedHandlingError:recovered:](<finishedhandlingerror(__recovered_).md>) when you’re finished handling the error — for example, when the application doesn’t require any additional user feedback about the error.
- Implementing [- userInteractionNoLongerPermittedForError:](<userinteractionnolongerpermitted(forerror_).md>) to conclude error handling immediately. If `userInteractionPermitted` is [false](../../swift/false.md), you should immediately handle the error and call [- finishedHandlingError:recovered:](<finishedhandlingerror(__recovered_).md>) within the context of the [- handleError:userInteractionPermitted:](<handleerror(__userinteractionpermitted_).md>).

## See Also

### Resolving conflicts and handling errors

- [- finishedHandlingError:recovered:](<finishedhandlingerror(__recovered_).md>) — Tells UIKit that you finished handling the error.
- [- userInteractionNoLongerPermittedForError:](<userinteractionnolongerpermitted(forerror_).md>) — Indicates when it’s no longer safe to proceed without immediately handling the error.
