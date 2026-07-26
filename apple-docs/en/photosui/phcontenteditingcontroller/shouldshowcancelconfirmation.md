---
title: shouldShowCancelConfirmation
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, macOS 10.11+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phcontenteditingcontroller/shouldshowcancelconfirmation
source_url: 'https://developer.apple.com/documentation/photosui/phcontenteditingcontroller/shouldshowcancelconfirmation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phcontenteditingcontroller/shouldshowcancelconfirmation.json'
content_hash: 'sha256:6016ee4556a00baa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHContentEditingController](../phcontenteditingcontroller.md)

# shouldShowCancelConfirmation

<sub>Instance Property</sub>

A Boolean value that determines whether Photos should prompt the user when canceling the editing session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var shouldShowCancelConfirmation: Bool { get }
```

## Discussion

Implement a getter method for this property to customize the Photos app’s behavior when the user chooses to cancel content editing.

If you return `false` (the default), Photos immediately terminates your extension when the user cancels editing. Use this option when your extension’s state can be easily recreated—that is, if the user loses no significant effort by canceling editing. For example, this option is appropriate for extensions that offer a simple choice between several preconfigured image filters.

If you return `true`, Photos shows an alert to confirm the user’s choice to cancel. Use this option when the user has invested significant effort in your extension workflow that would be lost when canceling. This option is appropriate if the user creates new content during the editing process (for example, in an extension that lets a user “paint” on an image).

## See Also

### Canceling an Edit

- [- cancelContentEditing](<cancelcontentediting().md>) — Tells your extension to cancel editing.
