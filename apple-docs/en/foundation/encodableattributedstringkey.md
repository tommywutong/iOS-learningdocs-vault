---
title: EncodableAttributedStringKey
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/encodableattributedstringkey
source_url: 'https://developer.apple.com/documentation/foundation/encodableattributedstringkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/encodableattributedstringkey.json'
content_hash: 'sha256:12fa1735ef07892e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# EncodableAttributedStringKey

<sub>Protocol</sub>

A protocol that defines how an attribute key encodes its value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol EncodableAttributedStringKey : AttributedStringKey
```

## Overview

Implement this protocol to make an attribute encodable. Encoding an [AttributedString](attributedstring.md) or [AttributeContainer](attributecontainer.md) drops any attributes whose types don’t conform to this protocol.

## Relationships

- **Inherits From**: [AttributedStringKey](attributedstringkey.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [AdjustedPitchAttribute](attributescopes/accessibilityattributes/adjustedpitchattribute.md), [AnnouncementPriorityAttribute](attributescopes/accessibilityattributes/announcementpriorityattribute.md), [HeadingLevelAttribute](attributescopes/accessibilityattributes/headinglevelattribute.md), [IPANotationAttribute](attributescopes/accessibilityattributes/ipanotationattribute.md), [IncludesPunctuationAttribute](attributescopes/accessibilityattributes/includespunctuationattribute.md), [QueueAnnouncementAttribute](attributescopes/accessibilityattributes/queueannouncementattribute.md), [SpellOutAttribute](attributescopes/accessibilityattributes/spelloutattribute.md), [TextCustomAttribute](attributescopes/accessibilityattributes/textcustomattribute.md), [TextualContextAttribute](attributescopes/accessibilityattributes/textualcontextattribute.md), [AdaptiveImageGlyphAttribute](attributescopes/appkitattributes/adaptiveimageglyphattribute.md), [AttachmentAttribute](attributescopes/appkitattributes/attachmentattribute.md), [BackgroundColorAttribute](attributescopes/appkitattributes/backgroundcolorattribute.md), [BaselineOffsetAttribute](attributescopes/appkitattributes/baselineoffsetattribute.md), [ExpansionAttribute](attributescopes/appkitattributes/expansionattribute.md), [FontAttribute](attributescopes/appkitattributes/fontattribute.md), [ForegroundColorAttribute](attributescopes/appkitattributes/foregroundcolorattribute.md), [GlyphInfoAttribute](attributescopes/appkitattributes/glyphinfoattribute.md), [KernAttribute](attributescopes/appkitattributes/kernattribute.md), [LigatureAttribute](attributescopes/appkitattributes/ligatureattribute.md), [MarkedClauseSegmentAttribute](attributescopes/appkitattributes/markedclausesegmentattribute.md), [ObliquenessAttribute](attributescopes/appkitattributes/obliquenessattribute.md), [ParagraphStyleAttribute](attributescopes/appkitattributes/paragraphstyleattribute.md), [ShadowAttribute](attributescopes/appkitattributes/shadowattribute.md), [StrikethroughColorAttribute](attributescopes/appkitattributes/strikethroughcolorattribute.md), [StrikethroughStyleAttribute](attributescopes/appkitattributes/strikethroughstyleattribute.md), [StrokeColorAttribute](attributescopes/appkitattributes/strokecolorattribute.md), [StrokeWidthAttribute](attributescopes/appkitattributes/strokewidthattribute.md), [SuperscriptAttribute](attributescopes/appkitattributes/superscriptattribute.md), [TextAlternativesAttribute](attributescopes/appkitattributes/textalternativesattribute.md), [TextEffectAttribute](attributescopes/appkitattributes/texteffectattribute.md), [ToolTipAttribute](attributescopes/appkitattributes/tooltipattribute.md), [TrackingAttribute](attributescopes/appkitattributes/trackingattribute.md), [UnderlineColorAttribute](attributescopes/appkitattributes/underlinecolorattribute.md), [UnderlineStyleAttribute](attributescopes/appkitattributes/underlinestyleattribute.md), [TextAlignmentAttribute](attributescopes/coretextattributes/textalignmentattribute.md), [AgreementArgumentAttribute](attributescopes/foundationattributes/agreementargumentattribute.md), [AgreementConceptAttribute](attributescopes/foundationattributes/agreementconceptattribute.md), [AlternateDescriptionAttribute](attributescopes/foundationattributes/alternatedescriptionattribute.md), [ByteCountAttribute](attributescopes/foundationattributes/bytecountattribute.md), [DateFieldAttribute](attributescopes/foundationattributes/datefieldattribute.md), [DurationFieldAttribute](attributescopes/foundationattributes/durationfieldattribute.md), [ImageURLAttribute](attributescopes/foundationattributes/imageurlattribute.md), [InflectionAlternativeAttribute](attributescopes/foundationattributes/inflectionalternativeattribute.md), [InflectionRuleAttribute](attributescopes/foundationattributes/inflectionruleattribute.md), [InlinePresentationIntentAttribute](attributescopes/foundationattributes/inlinepresentationintentattribute.md), [LanguageIdentifierAttribute](attributescopes/foundationattributes/languageidentifierattribute.md), [LinkAttribute](attributescopes/foundationattributes/linkattribute.md), [ListItemDelimiterAttribute](attributescopes/foundationattributes/listitemdelimiterattribute.md), [LocalizedNumberFormatAttribute](attributescopes/foundationattributes/localizednumberformatattribute.md), [LocalizedDateArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizeddateargumentattribute.md), [LocalizedDateIntervalArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizeddateintervalargumentattribute.md), [LocalizedNumericArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizednumericargumentattribute.md), [LocalizedURLArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizedurlargumentattribute.md), [MarkdownSourcePositionAttribute](attributescopes/foundationattributes/markdownsourcepositionattribute.md), [MeasurementAttribute](attributescopes/foundationattributes/measurementattribute.md), [MorphologyAttribute](attributescopes/foundationattributes/morphologyattribute.md), [NumberPartAttribute](attributescopes/foundationattributes/numberformatattributes/numberpartattribute.md), [SymbolAttribute](attributescopes/foundationattributes/numberformatattributes/symbolattribute.md), [PersonNameComponentAttribute](attributescopes/foundationattributes/personnamecomponentattribute.md), [PresentationIntentAttribute](attributescopes/foundationattributes/presentationintentattribute.md), [ReferentConceptAttribute](attributescopes/foundationattributes/referentconceptattribute.md), [ReplacementIndexAttribute](attributescopes/foundationattributes/replacementindexattribute.md), [WritingDirectionAttribute](attributescopes/foundationattributes/writingdirectionattribute.md), [ConfidenceAttribute](attributescopes/speechattributes/confidenceattribute.md), [TimeRangeAttribute](attributescopes/speechattributes/timerangeattribute.md), [AdaptiveImageGlyphAttribute](attributescopes/swiftuiattributes/adaptiveimageglyphattribute.md), [BackgroundColorAttribute](attributescopes/swiftuiattributes/backgroundcolorattribute.md), [BaselineOffsetAttribute](attributescopes/swiftuiattributes/baselineoffsetattribute.md), [FontAttribute](attributescopes/swiftuiattributes/fontattribute.md), [ForegroundColorAttribute](attributescopes/swiftuiattributes/foregroundcolorattribute.md), [KerningAttribute](attributescopes/swiftuiattributes/kerningattribute.md), [StrikethroughStyleAttribute](attributescopes/swiftuiattributes/strikethroughstyleattribute.md), [TrackingAttribute](attributescopes/swiftuiattributes/trackingattribute.md), [UnderlineStyleAttribute](attributescopes/swiftuiattributes/underlinestyleattribute.md), [AdaptiveImageGlyphAttribute](attributescopes/uikitattributes/adaptiveimageglyphattribute.md), [AttachmentAttribute](attributescopes/uikitattributes/attachmentattribute.md), [BackgroundColorAttribute](attributescopes/uikitattributes/backgroundcolorattribute.md), [BaselineOffsetAttribute](attributescopes/uikitattributes/baselineoffsetattribute.md), [ExpansionAttribute](attributescopes/uikitattributes/expansionattribute.md), [FontAttribute](attributescopes/uikitattributes/fontattribute.md), [ForegroundColorAttribute](attributescopes/uikitattributes/foregroundcolorattribute.md), [KernAttribute](attributescopes/uikitattributes/kernattribute.md), [LigatureAttribute](attributescopes/uikitattributes/ligatureattribute.md), [ObliquenessAttribute](attributescopes/uikitattributes/obliquenessattribute.md), [ParagraphStyleAttribute](attributescopes/uikitattributes/paragraphstyleattribute.md), [ShadowAttribute](attributescopes/uikitattributes/shadowattribute.md), [StrikethroughColorAttribute](attributescopes/uikitattributes/strikethroughcolorattribute.md), [StrikethroughStyleAttribute](attributescopes/uikitattributes/strikethroughstyleattribute.md), [StrokeColorAttribute](attributescopes/uikitattributes/strokecolorattribute.md), [StrokeWidthAttribute](attributescopes/uikitattributes/strokewidthattribute.md), [TextEffectAttribute](attributescopes/uikitattributes/texteffectattribute.md), [TextItemTagAttribute](attributescopes/uikitattributes/textitemtagattribute.md), [TrackingAttribute](attributescopes/uikitattributes/trackingattribute.md), [UnderlineColorAttribute](attributescopes/uikitattributes/underlinecolorattribute.md), [UnderlineStyleAttribute](attributescopes/uikitattributes/underlinestyleattribute.md)

## Topics

### Encoding Values

- [encode(_:to:)](<encodableattributedstringkey/encode(__to_).md>) — Encodes a value to the provided encoder.

## See Also

### Encoding and Decoding Keys

- [DecodableAttributedStringKey](decodableattributedstringkey.md) — A protocol that defines how an attribute key decodes its value.
- [CodableAttributedStringKey](codableattributedstringkey.md) — A type alias used by attribute keys that are both encodable and decodable.
