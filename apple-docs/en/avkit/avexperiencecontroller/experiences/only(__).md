---
title: 'only(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avexperiencecontroller/experiences/only(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/experiences/only(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/experiences/only%28_%3A%29.json'
content_hash: 'sha256:f34980c8badfbf12'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [Experiences](../experiences.md)

# only(_:)

<sub>Type Method</sub>

Returns a set of experiences for the provided list.

<sub>visionOS</sub>

```swift
static func only<C>(_ experiences: C) -> AVExperienceController.Experiences where C : Collection, C.Element == AVExperienceController.Experience
```

## Parameters

- `experiences` — The experiences to include. Order and duplication are not significant.

## Discussion

Use this method when the use case requires a specific set of experiences.

## See Also

### Defining experiences

- [recommended(excluding:including:)](<recommended(excluding_including_).md>) — Returns the recommended set of experiences.
