---
title: 'CTFontCopyFeatures(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopyfeatures(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopyfeatures(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopyfeatures%28_%3A%29.json'
content_hash: 'sha256:f4326a1b781b9ab9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopyFeatures(_:)

<sub>Function</sub>

Returns an array of font features.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopyFeatures(_ font: CTFont) -> CFArray?
```

## Parameters

- `font` — The font reference.

## Return Value

An array of font feature dictionaries for the font reference.

## See Also

### Getting Font Features

- [CTFontCopyFeatureSettings](<ctfontcopyfeaturesettings(__).md>) — Returns an array of font feature-setting tuples.
