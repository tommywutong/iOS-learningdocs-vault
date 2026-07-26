---
title: 'CTTextTabCreate(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/cttexttabcreate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/cttexttabcreate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttexttabcreate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:6f9a04cce16bff54'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTTextTabCreate(_:_:_:)

<sub>Function</sub>

Creates and initializes a new text tab object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTTextTabCreate(_ alignment: CTTextAlignment, _ location: Double, _ options: CFDictionary?) -> CTTextTab
```

## Parameters

- `alignment` — The tab’s alignment. This is used to determine the position of text inside the tab column. This parameter must be set to a valid [CTTextAlignment](cttextalignment.md) value or this function returns `NULL`.

- `location` — The tab’s ruler location, relative to the back margin.

- `options` — Options to pass in when the tab is created. Currently, the only option available is [kCTTabColumnTerminatorsAttributeName](kcttabcolumnterminatorsattributename.md). This parameter is optional and can be set to `NULL` if not needed.

## Return Value

A reference to a CTTextTab object if the call was successful; otherwise, `NULL`.

## See Also

### Creating Text Tabs

- [kCTTabColumnTerminatorsAttributeName](kcttabcolumnterminatorsattributename.md) — Specifies the terminating character for a tab column.
