---
title: 'init(delegate:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarselectionsingledate/init(delegate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarselectionsingledate/init(delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarselectionsingledate/init%28delegate%3A%29.json'
content_hash: 'sha256:0a88ae61b6d534d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICalendarSelectionSingleDate](../uicalendarselectionsingledate.md)

# init(delegate:)

<sub>Initializer</sub>

Creates an object that tracks a date a user selects from a calendar view, with an optional delegate to manage selectable dates and selection changes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(delegate: (any UICalendarSelectionSingleDateDelegate)?)
```

## Parameters

- `delegate` — A delegate object that a calendar view asks about selectable dates, and informs of changes to the selection of a single date.
