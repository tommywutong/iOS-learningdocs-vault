---
title: 'CFPropertyListIsValid(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpropertylistisvalid(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpropertylistisvalid(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpropertylistisvalid%28_%3A_%3A%29.json'
content_hash: 'sha256:be331025aa718165'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPropertyListIsValid(_:_:)

<sub>Function</sub>

Determines if a property list is valid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPropertyListIsValid(_ plist: CFPropertyList!, _ format: CFPropertyListFormat) -> Bool
```

## Parameters

- `plist` — The property list to validate.

- `format` — A constant that specifies the allowable format of `plist`. See [CFPropertyListFormat](cfpropertylistformat.md) for possible values.

## Return Value

`true` if the object graph rooted at `plist` is a valid property list graph—that is, the property list contains no cycles, only contains property list objects, and all dictionary keys are strings; otherwise `false`.

## Discussion

The debugging library version of this function prints out some useful messages.
