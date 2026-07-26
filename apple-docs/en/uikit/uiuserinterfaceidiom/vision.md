---
title: UIUserInterfaceIdiom.vision
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiuserinterfaceidiom/vision
source_url: 'https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom/vision'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiuserinterfaceidiom/vision.json'
content_hash: 'sha256:0b61fd2a447bca90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUserInterfaceIdiom](../uiuserinterfaceidiom.md)

# UIUserInterfaceIdiom.vision

<sub>Case</sub>

An interface designed for visionOS and Apple Vision Pro.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case vision
```

## Discussion

If your app has existing code that runs in the [UIUserInterfaceIdiomPad](pad.md) idiom, you might want to reuse the same code in the [UIUserInterfaceIdiomVision](vision.md) idiom. The following code shows how to check for these idioms:

```swift
if idiom == .pad || idiom == .vision {
   // Code to run in the iPad or Apple Vision Pro idioms.
} else { 
   // Code to run in other idioms.
}
```

## See Also

### Idioms

- [UIUserInterfaceIdiomUnspecified](unspecified.md) — An unspecified idiom.
- [UIUserInterfaceIdiomPhone](phone.md) — An interface designed for iPhone and iPod touch.
- [UIUserInterfaceIdiomPad](pad.md) — An interface designed for iPad.
- [UIUserInterfaceIdiomTV](tv.md) — An interface designed for tvOS and Apple TV.
- [UIUserInterfaceIdiomCarPlay](carplay.md) — An interface designed for an in-car experience.
- [UIUserInterfaceIdiomMac](mac.md) — An interface designed for the Mac.
