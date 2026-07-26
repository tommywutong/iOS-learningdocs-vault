---
title: 'CTTextTabGetLocation(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/cttexttabgetlocation(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/cttexttabgetlocation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttexttabgetlocation%28_%3A%29.json'
content_hash: 'sha256:04a8602c85e323f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTTextTabGetLocation(_:)

<sub>Function</sub>

Returns the tab’s ruler location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTTextTabGetLocation(_ tab: CTTextTab) -> Double
```

## Parameters

- `tab` — The tab whose location is obtained.

## Return Value

The tab’s ruler location relative to the back margin.

## See Also

### Getting Text Tab Data

- [CTTextTabGetAlignment](<cttexttabgetalignment(__).md>) — Returns the text alignment of the tab.
- [CTTextTabGetOptions](<cttexttabgetoptions(__).md>) — Returns the dictionary of attributes associated with the tab.
