---
title: kCTTabColumnTerminatorsAttributeName
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kcttabcolumnterminatorsattributename
source_url: 'https://developer.apple.com/documentation/coretext/kcttabcolumnterminatorsattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kcttabcolumnterminatorsattributename.json'
content_hash: 'sha256:54b59fdc1e60f75c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTTabColumnTerminatorsAttributeName

<sub>Global Variable</sub>

Specifies the terminating character for a tab column.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTTabColumnTerminatorsAttributeName: CFString
```

## Discussion

The value associated with this attribute is a [CFCharacterSet](../corefoundation/cfcharacterset.md) object. The character set is used to determine the terminating character for a tab column. The tab and newline characters are implied even if they don’t exist in the character set. This attribute can be used to implement decimal tabs, for instance. This attribute is optional.

## See Also

### Creating Text Tabs

- [CTTextTabCreate](<cttexttabcreate(______).md>) — Creates and initializes a new text tab object.
