---
title: 'imagePlaygroundOptions(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, visionOS 26.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/imageplaygroundoptions(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/imageplaygroundoptions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/imageplaygroundoptions%28_%3A%29.json'
content_hash: 'sha256:2456c618ce44e3d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# imagePlaygroundOptions(_:)

<sub>Instance Method</sub>

Sets the options to use when generating an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func imagePlaygroundOptions(_ options: ImagePlaygroundOptions = ImagePlaygroundOptions()) -> some View

```

## Parameters

- `options` — The options to apply when generating an image.

## Return Value

An image playground sheet that generates images using the specified `options`.

## Discussion

If you don’t provide any custom options, the sheet applies the default options to image generation.

## See Also

### Generating images

- [imagePlaygroundGenerationStyle(_:in:)](<imageplaygroundgenerationstyle(__in_).md>) — Sets the selected and allowed styles to use when displaying the image generation sheet.
- [imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onCancellation:)](<imageplaygroundsheet(ispresented_concept_sourceimage_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using the specified string and optional starting image.
- [imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<imageplaygroundsheet(ispresented_concept_sourceimage_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create images from the specified input.
- [imagePlaygroundSheet(isPresented:concept:sourceImageURL:onCompletion:onCancellation:)](<imageplaygroundsheet(ispresented_concept_sourceimageurl_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using the specified string and image URL.
- [imagePlaygroundSheet(isPresented:concept:sourceImageURL:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<imageplaygroundsheet(ispresented_concept_sourceimageurl_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create an image or Genmoji using the specified string and image URL.
- [imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onCancellation:)](<imageplaygroundsheet(ispresented_concepts_sourceimage_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using one or more concepts and an optional starting image.
- [imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<imageplaygroundsheet(ispresented_concepts_sourceimage_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create an image or Genmoji using one or more concepts and an optional starting image.
- [imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onCancellation:)](<imageplaygroundsheet(ispresented_concepts_sourceimageurl_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using one or more concepts and an image URL.
- [imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<imageplaygroundsheet(ispresented_concepts_sourceimageurl_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create an image or Genmoji using one or more concepts and an image URL.
