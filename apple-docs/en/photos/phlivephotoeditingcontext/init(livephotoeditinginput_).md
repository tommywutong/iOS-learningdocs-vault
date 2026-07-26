---
title: 'init(livePhotoEditingInput:)'
framework: Photos
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phlivephotoeditingcontext/init(livephotoeditinginput:)'
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/init(livephotoeditinginput:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoeditingcontext/init%28livephotoeditinginput%3A%29.json'
content_hash: 'sha256:8820c1652178ac10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoEditingContext](../phlivephotoeditingcontext.md)

# init(livePhotoEditingInput:)

<sub>Initializer</sub>

Creates a Live Photo editing context for the specified editing input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(livePhotoEditingInput livePhotoInput: PHContentEditingInput)
```

## Parameters

- `livePhotoInput` — A content editing input object representing the Live Photo for which to perform editing.

## Return Value

A new Live Photo editing context, or `nil` if the provided content editing input does not represent a Live Photo.

## Discussion

In an app using the Photos framework, you obtain a [PHContentEditingInput](../phcontenteditinginput.md) object by calling [- requestContentEditingInputWithOptions:completionHandler:](<../phasset/requestcontenteditinginput(with_completionhandler_).md>) method of a [PHAsset](../phasset.md) object that you’ve previously fetched.

In a photo editing extension that runs within the Photos app, your extension’s main view controller (which adopts the [PHContentEditingController](../../photosui/phcontenteditingcontroller.md) protocol) receives a [PHContentEditingInput](../phcontenteditinginput.md) object when the user chooses to edit a Live Photo with your extension.

You can create a Live Photo editing context only from [PHContentEditingInput](../phcontenteditinginput.md) object that represents a Live Photo. Use the [livePhoto](../phcontenteditinginput/livephoto.md) property of the editing input to verify that it has live Photo content.
