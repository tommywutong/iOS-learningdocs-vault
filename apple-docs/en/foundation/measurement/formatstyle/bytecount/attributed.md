---
title: attributed
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/formatstyle/bytecount/attributed
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/bytecount/attributed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/bytecount/attributed.json'
content_hash: 'sha256:78dbf4453dd44bcf'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Measurement](../../../measurement.md) · [FormatStyle](../../formatstyle.md) · [ByteCount](../bytecount.md)

# attributed

<sub>Instance Property</sub>

An attributed format style based on the byte count format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var attributed: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount { get }
```

## Discussion

Use this modifier to create a [Attributed](../../../bytecountformatstyle/attributed-swift.struct.md) instance, which formats values as [AttributedString](../../../attributedstring.md) instances. These attributed strings contain attributes from the [NumberFormatAttributes](../../../attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

## See Also

### Creating attributed strings

- [ByteCount](../../attributedstyle/bytecount.md) — A format style that converts byte counts into attributed strings.
