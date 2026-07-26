---
title: 'imagePlaygroundSheet(isPresented:concept:sourceImageURL:onCompletion:onCancellation:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.1+, iPadOS 18.1+, Mac Catalyst 18.1+, macOS 15.1+, visionOS 2.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/imageplaygroundsheet(ispresented:concept:sourceimageurl:oncompletion:oncancellation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/imageplaygroundsheet(ispresented:concept:sourceimageurl:oncompletion:oncancellation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/imageplaygroundsheet%28ispresented%3Aconcept%3Asourceimageurl%3Aoncompletion%3Aoncancellation%3A%29.json'
content_hash: 'sha256:4a477885dae21e3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# imagePlaygroundSheet(isPresented:concept:sourceImageURL:onCompletion:onCancellation:)

<sub>Instance Method</sub>

Presents the system sheet to create an image using the specified string and image URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func imagePlaygroundSheet(isPresented: Binding<Bool>, concept: String, sourceImageURL: URL, onCompletion: @escaping (URL) -> Void, onCancellation: (() -> Void)? = nil) -> some View

```

## Parameters

- `isPresented` — A binding to a variable with a Boolean value. Set the Boolean value to `true` to display the sheet, and set it to `false` to dismiss the sheet.

- `concept` — A natural language string that describes the expected contents of the image. Inside the creation UI, the person can replace this value with a different description for the image.

- `sourceImageURL` — A file URL that refers to the image to use as source input for the new image. The person viewing the sheet can override the image you provide, and choose different images and concepts inside the creation UI. If you don’t provide a starting image, the system creates the new image using only the contents of the `concepts` parameter.

- `onCompletion` — The block to receive the created image. The block has no return value and receives the following parameter: - **url** — A URL with the path to the image. The system saves the file at a temporary location inside your app container. Move the file to a new location if you intend to keep it after the dismissal of the sheet, or remove it if you don’t.

- `onCancellation` — The block to execute when the person exits. the creation UI without choosing an image. After executing this block, the system automatically dismisses the sheet.

## Discussion

Use this modifier to display the image-creation sheet from one of your SwiftUI views. The sheet presents a system-provided UI to generate an image from the specified string and an optional image. The sheet gives the person controls to modify the image before returning it to your app. When the person dismisses the sheet, the system runs one of the blocks you provided. Use the completion block to integrate the generated image into your app’s content.

This modifier works only on devices that support the creation of new images. Check the `ImagePlayground/SwiftUICore/EnvironmentValues/supportsImagePlayground` environment variable to determine the availability of the feature. The following code creates a button to display the sheet only when the feature is available:

```swift
@State private var showSheet = false
@State private var createdImageURL: URL? = nil
@Environment(\.supportsImagePlayground) private var supportsImagePlayground
// ....

if supportsImagePlayground {
  Button("Show Generation Sheet") {
    showSheet = true
  }.imagePlaygroundSheet(
    isPresented: $showSheet,
    concept: "Dog on a surfboard",
    sourceImageURL: sourceImageURL) { url in
    createdImageURL = url
  }
}
```

## See Also

### Generating images

- [imagePlaygroundGenerationStyle(_:in:)](<imageplaygroundgenerationstyle(__in_).md>) — Sets the selected and allowed styles to use when displaying the image generation sheet.
- [imagePlaygroundOptions(_:)](<imageplaygroundoptions(__).md>) — Sets the options to use when generating an image.
- [imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onCancellation:)](<imageplaygroundsheet(ispresented_concept_sourceimage_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using the specified string and optional starting image.
- [imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<imageplaygroundsheet(ispresented_concept_sourceimage_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create images from the specified input.
- [imagePlaygroundSheet(isPresented:concept:sourceImageURL:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<imageplaygroundsheet(ispresented_concept_sourceimageurl_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create an image or Genmoji using the specified string and image URL.
- [imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onCancellation:)](<imageplaygroundsheet(ispresented_concepts_sourceimage_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using one or more concepts and an optional starting image.
- [imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<imageplaygroundsheet(ispresented_concepts_sourceimage_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create an image or Genmoji using one or more concepts and an optional starting image.
- [imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onCancellation:)](<imageplaygroundsheet(ispresented_concepts_sourceimageurl_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using one or more concepts and an image URL.
- [imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<imageplaygroundsheet(ispresented_concepts_sourceimageurl_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create an image or Genmoji using one or more concepts and an image URL.
