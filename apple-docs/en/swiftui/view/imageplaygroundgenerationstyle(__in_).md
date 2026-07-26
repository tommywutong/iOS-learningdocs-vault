---
title: 'imagePlaygroundGenerationStyle(_:in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+, macOS 15.4+, visionOS 2.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/imageplaygroundgenerationstyle(_:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/imageplaygroundgenerationstyle(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/imageplaygroundgenerationstyle%28_%3Ain%3A%29.json'
content_hash: 'sha256:8c8426e84535e0a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# imagePlaygroundGenerationStyle(_:in:)

<sub>Instance Method</sub>

Sets the selected and allowed styles to use when displaying the image generation sheet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func imagePlaygroundGenerationStyle(_ style: ImagePlaygroundStyle, in allowedStyles: [ImagePlaygroundStyle] = ImagePlaygroundStyle.all) -> some View

```

## Parameters

- `style` — The style to pre-select in the sheet. This style must also be present in the `allowedStyles` parameter.

- `allowedStyles` — The list of styles that the sheet can display to people. Specify `ImagePlaygroundStyle/all` to make all styles available from the sheet.

## Return Value

An image playground sheet configured with the specified style information.

## Discussion

Configures the sheet with the specified style information. At presentation time, the sheet selects the style from the `style` parameter initially, but the person can change the selected style to any of the values in the `allowedStyles` parameter.

## See Also

### Generating images

- [imagePlaygroundOptions(_:)](<imageplaygroundoptions(__).md>) — Sets the options to use when generating an image.
- [imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onCancellation:)](<imageplaygroundsheet(ispresented_concept_sourceimage_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using the specified string and optional starting image.
- [imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<imageplaygroundsheet(ispresented_concept_sourceimage_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create images from the specified input.
- [imagePlaygroundSheet(isPresented:concept:sourceImageURL:onCompletion:onCancellation:)](<imageplaygroundsheet(ispresented_concept_sourceimageurl_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using the specified string and image URL.
- [imagePlaygroundSheet(isPresented:concept:sourceImageURL:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<imageplaygroundsheet(ispresented_concept_sourceimageurl_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create an image or Genmoji using the specified string and image URL.
- [imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onCancellation:)](<imageplaygroundsheet(ispresented_concepts_sourceimage_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using one or more concepts and an optional starting image.
- [imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<imageplaygroundsheet(ispresented_concepts_sourceimage_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create an image or Genmoji using one or more concepts and an optional starting image.
- [imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onCancellation:)](<imageplaygroundsheet(ispresented_concepts_sourceimageurl_oncompletion_oncancellation_).md>) — Presents the system sheet to create an image using one or more concepts and an image URL.
- [imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onAdaptiveImageGlyphCreation:onCancellation:)](<imageplaygroundsheet(ispresented_concepts_sourceimageurl_oncompletion_onadaptiveimageglyphcreation_oncancellation_).md>) — Presents the system sheet to create an image or Genmoji using one or more concepts and an image URL.
