---
title: UIPickerViewDataSource
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipickerviewdatasource
source_url: 'https://developer.apple.com/documentation/uikit/uipickerviewdatasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerviewdatasource.json'
content_hash: 'sha256:b3c73986d4eff804'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPickerViewDataSource

<sub>Protocol</sub>

The interface for a picker view’s data source.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIPickerViewDataSource : NSObjectProtocol
```

## Overview

The data source of a [UIPickerView](uipickerview.md) object must adopt this protocol to mediate between the picker view object and your app’s data model for that picker view. The data source provides the picker view with the number of components, and the number of rows in each component, for displaying the picker view data. Both methods in this protocol are required.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing counts for the picker view

- [- numberOfComponentsInPickerView:](<uipickerviewdatasource/numberofcomponents(in_).md>) — Asks the data source for the number of components in the picker view.
- [- pickerView:numberOfRowsInComponent:](<uipickerviewdatasource/pickerview(__numberofrowsincomponent_).md>) — Asks the data source for the number of rows for a specified component.

## See Also

### Providing the picker data

- [dataSource](uipickerview/datasource.md) — The data source for the picker view.
