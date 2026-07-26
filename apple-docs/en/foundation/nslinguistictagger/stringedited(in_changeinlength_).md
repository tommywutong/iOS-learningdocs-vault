---
title: 'stringEdited(in:changeInLength:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/stringedited(in:changeinlength:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/stringedited(in:changeinlength:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/stringedited%28in%3Achangeinlength%3A%29.json'
content_hash: 'sha256:81e867653e076de9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# stringEdited(in:changeInLength:)

<sub>Instance Method</sub>

Notifies the linguistic tagger that the string (if mutable) has changed as specified by the parameters.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func stringEdited(in newRange: NSRange, changeInLength delta: Int)
```

## Parameters

- `newRange` — The range in the final string that was edited.

- `delta` — The change in length.
