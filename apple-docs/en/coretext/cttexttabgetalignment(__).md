---
title: 'CTTextTabGetAlignment(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/cttexttabgetalignment(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/cttexttabgetalignment(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttexttabgetalignment%28_%3A%29.json'
content_hash: 'sha256:ead7878fc1576d43'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTTextTabGetAlignment(_:)

<sub>Function</sub>

Returns the text alignment of the tab.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTTextTabGetAlignment(_ tab: CTTextTab) -> CTTextAlignment
```

## Parameters

- `tab` — The tab whose text alignment is obtained.

## Return Value

The tab’s text alignment value.

## See Also

### Getting Text Tab Data

- [CTTextTabGetLocation](<cttexttabgetlocation(__).md>) — Returns the tab’s ruler location.
- [CTTextTabGetOptions](<cttexttabgetoptions(__).md>) — Returns the dictionary of attributes associated with the tab.
