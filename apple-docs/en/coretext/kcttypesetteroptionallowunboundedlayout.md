---
title: kCTTypesetterOptionAllowUnboundedLayout
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kcttypesetteroptionallowunboundedlayout
source_url: 'https://developer.apple.com/documentation/coretext/kcttypesetteroptionallowunboundedlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kcttypesetteroptionallowunboundedlayout.json'
content_hash: 'sha256:6ec6c72ec6c2b83e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTTypesetterOptionAllowUnboundedLayout

<sub>Global Variable</sub>

A key that specifies whether the text system lays out text that requires unreasonable effort.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTTypesetterOptionAllowUnboundedLayout: CFString
```

## Discussion

Proper Unicode layout of some text requires unreasonable effort. By default, the text system avoids expending this effort. To create a typesetter that always typesets the text, regardless of the amount of work needed, call [CTTypesetterCreateWithAttributedStringAndOptions](<cttypesettercreatewithattributedstringandoptions(____).md>) and set this option to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md).

The value for this key must be a `CFBooleanRef`. The default value is [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md).

## See Also

### Constants

- [kCTTypesetterOptionForcedEmbeddingLevel](kcttypesetteroptionforcedembeddinglevel.md) — A key that specifies the embedding level of the typesetter’s text.
- [kCTTypesetterOptionDisableBidiProcessing](kcttypesetteroptiondisablebidiprocessing.md) _(deprecated)_
