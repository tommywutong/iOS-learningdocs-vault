---
title: 'recommended(excluding:including:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avexperiencecontroller/experiences/recommended(excluding:including:)'
source_url: 'https://developer.apple.com/documentation/avkit/avexperiencecontroller/experiences/recommended(excluding:including:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avexperiencecontroller/experiences/recommended%28excluding%3Aincluding%3A%29.json'
content_hash: 'sha256:bb485596346b427e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVExperienceController](../../avexperiencecontroller.md) · [Experiences](../experiences.md)

# recommended(excluding:including:)

<sub>Type Method</sub>

Returns the recommended set of experiences.

<sub>visionOS</sub>

```swift
static func recommended<C>(excluding: C = [], including: C = []) -> AVExperienceController.Experiences where C : Collection, C.Element == AVExperienceController.Experience
```

## Parameters

- `excluding` — The experiences to remove. Removal happens before adding.

- `including` — The experiences to add. Redundant items are ignored.

## Discussion

Use this method to return the default recommended set of experiences for each platform and SDK version. Include or exclude experiences specifically desired or not supported by your app.

## See Also

### Defining experiences

- [only(_:)](<only(__).md>) — Returns a set of experiences for the provided list.
