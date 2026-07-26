---
title: 'CFBooleanGetValue(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbooleangetvalue(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbooleangetvalue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbooleangetvalue%28_%3A%29.json'
content_hash: 'sha256:2845284e55324d1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBooleanGetValue(_:)

<sub>Function</sub>

Returns the value of a CFBoolean object as a standard C type `Boolean`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBooleanGetValue(_ boolean: CFBoolean!) -> Bool
```

## Parameters

- `boolean` — The boolean to examine.

## Return Value

The value of `boolean`.

## See Also

### CFBoolean Miscellaneous Functions

- [CFBooleanGetTypeID](<cfbooleangettypeid().md>) — Returns the Core Foundation type identifier for the CFBoolean opaque type.
