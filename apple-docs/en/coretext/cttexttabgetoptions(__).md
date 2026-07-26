---
title: 'CTTextTabGetOptions(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/cttexttabgetoptions(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/cttexttabgetoptions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttexttabgetoptions%28_%3A%29.json'
content_hash: 'sha256:5bbc5ed5191d0dcf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTTextTabGetOptions(_:)

<sub>Function</sub>

Returns the dictionary of attributes associated with the tab.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTTextTabGetOptions(_ tab: CTTextTab) -> CFDictionary?
```

## Parameters

- `tab` — The tab whose attributes are obtained.

## Return Value

The dictionary of attributes associated with the tab, or if no dictionary is present, `NULL`.

## See Also

### Getting Text Tab Data

- [CTTextTabGetAlignment](<cttexttabgetalignment(__).md>) — Returns the text alignment of the tab.
- [CTTextTabGetLocation](<cttexttabgetlocation(__).md>) — Returns the tab’s ruler location.
