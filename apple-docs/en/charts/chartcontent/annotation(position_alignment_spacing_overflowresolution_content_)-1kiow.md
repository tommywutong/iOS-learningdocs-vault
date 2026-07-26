---
title: 'annotation(position:alignment:spacing:overflowResolution:content:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/annotation(position:alignment:spacing:overflowresolution:content:)-1kiow'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/annotation(position:alignment:spacing:overflowresolution:content:)-1kiow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/annotation%28position%3Aalignment%3Aspacing%3Aoverflowresolution%3Acontent%3A%29-1kiow.json'
content_hash: 'sha256:f3a5436e824dce7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# annotation(position:alignment:spacing:overflowResolution:content:)

<sub>Instance Method</sub>

Annotates this mark or collection of marks with a view positioned relative to its bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func annotation<C>(position: AnnotationPosition = .automatic, alignment: Alignment = .center, spacing: CGFloat? = nil, overflowResolution: AnnotationOverflowResolution, @ViewBuilder content: () -> C) -> some ChartContent where C : View

```

## Parameters

- `position` — The location relative to the item being annotated at which the annotation will be placed.

- `alignment` — The guide for aligning the annotation in the specified position.

- `spacing` — Distance between the annotation and the annotated content, or `nil` if you want to use the default distance.

- `overflowResolution` — How to resolve the annotation exceeding the boundary of the plot.

- `content` — A view builder that creates the annotation. The builder takes one input which provides information regarding the item being annotated such as its size.

## See Also

### Annotating marks

- [annotation(position:alignment:spacing:content:)](<annotation(position_alignment_spacing_content_)-65emh.md>) — Annotates this mark or collection of marks with a view positioned relative to its bounds.
- [annotation(position:alignment:spacing:content:)](<annotation(position_alignment_spacing_content_)-26b2f.md>) — Annotates this mark or collection of marks with a view positioned relative to its bounds.
- [annotation(position:alignment:spacing:overflowResolution:content:)](<annotation(position_alignment_spacing_overflowresolution_content_)-6w4p3.md>) — Annotates this mark or collection of marks with a view positioned relative to its bounds.
