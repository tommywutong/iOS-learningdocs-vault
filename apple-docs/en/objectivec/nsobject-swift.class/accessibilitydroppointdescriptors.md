---
title: accessibilityDropPointDescriptors
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilitydroppointdescriptors
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitydroppointdescriptors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilitydroppointdescriptors.json'
content_hash: 'sha256:c78b0fe0931e7aeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityDropPointDescriptors

<sub>Instance Property</sub>

An array of location descriptor objects that you use to define where drops are possible on this element.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor var accessibilityDropPointDescriptors: [UIAccessibilityLocationDescriptor]? { get set }
```

## Discussion

To restore the default automatic behavior for this property, assign or return the default value of `nil`.

> [!note] Note
> A value of `nil` does not describe the same behavior as the empty array, which specifies that there are no relevant interactions for this element.

## See Also

### Fine-Tuning Drag and Drop

- [accessibilityDragSourceDescriptors](accessibilitydragsourcedescriptors.md) — An array of location descriptor objects that you use to define what drags are possible from this element.
