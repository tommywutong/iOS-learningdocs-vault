---
title: 'CFUUIDGetUUIDBytes(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfuuidgetuuidbytes(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfuuidgetuuidbytes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfuuidgetuuidbytes%28_%3A%29.json'
content_hash: 'sha256:653a4f3133bc1a01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUUIDGetUUIDBytes(_:)

<sub>Function</sub>

Returns the value of a UUID object as raw bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFUUIDGetUUIDBytes(_ uuid: CFUUID!) -> CFUUIDBytes
```

## Parameters

- `uuid` — The CFUUID object to examine.

## Return Value

The value of `uuid` represented as raw bytes.

## See Also

### Getting Information About CFUUID Objects

- [CFUUIDCreateString](<cfuuidcreatestring(____).md>) — Returns the string representation of a specified CFUUID object.
- [CFUUIDGetConstantUUIDWithBytes](<cfuuidgetconstantuuidwithbytes(__________________________________).md>) — Returns a CFUUID object from raw UUID bytes.
