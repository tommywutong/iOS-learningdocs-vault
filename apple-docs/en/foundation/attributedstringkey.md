---
title: AttributedStringKey
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstringkey
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringkey.json'
content_hash: 'sha256:866c860676f3a6d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# AttributedStringKey

<sub>Protocol</sub>

A type that defines an attribute’s name and type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AttributedStringKey : SendableMetatype
```

## Overview

You don’t instantiate types that conform to this protocol. Rather, dynamic member lookup uses this type as the basis for looking up key paths on [AttributedString](attributedstring.md) subtypes when using an [AttributeScope](attributescope.md) type parameter. When it also conforms to [CodableAttributedStringKey](codableattributedstringkey.md), (or [DecodableAttributedStringKey](decodableattributedstringkey.md)/[EncodableAttributedStringKey](encodableattributedstringkey.md) if the type isn’t fully codable), the [AttributedStringKey](attributedstringkey.md) describes which attributes of an [AttributedString](attributedstring.md) support encoding or decoding.

Attribute owners — typically frameworks — declare a key like the following:

```swift
enum OutlineColorAttribute : AttributedStringKey {
    typealias Value = Color
    static let name = "OutlineColor"
}
```

Callers can use these types to get attribute values from attributed strings, but typically you want to reference them by name. Attribute owners enable this by creating one or more structures that conform to [AttributeScope](attributescope.md), in which they provide short names for their attributes that map to the [AttributedStringKey](attributedstringkey.md) type. The following example shows how to do this:

```swift
struct MyTextStyleAttributes : AttributeScope {
    let outlineColor : OutlineColorAttribute // OutlineColorAttribute.Value == Color
    let shadowColor : ShadowColorAttribute // ShadowColorAttribute.Value == Color
    // etc.
}
```

After you extend [AttributeScope](attributescope.md) like this, extend [AttributeDynamicLookup](attributedynamiclookup.md) to allow callers to use dynamic member lookup syntax, like `myAttributedString.outlineColor = .red`.

## Relationships

- **Inherits From**: [SendableMetatype](../swift/sendablemetatype.md)

- **Inherited By**: [DecodableAttributedStringKey](decodableattributedstringkey.md), [EncodableAttributedStringKey](encodableattributedstringkey.md), [MarkdownDecodableAttributedStringKey](markdowndecodableattributedstringkey.md), [ObjectiveCConvertibleAttributedStringKey](objectivecconvertibleattributedstringkey.md)

- **Conforming Types**: [AdjustedPitchAttribute](attributescopes/accessibilityattributes/adjustedpitchattribute.md), [AnnouncementPriorityAttribute](attributescopes/accessibilityattributes/announcementpriorityattribute.md), [HeadingLevelAttribute](attributescopes/accessibilityattributes/headinglevelattribute.md), [IPANotationAttribute](attributescopes/accessibilityattributes/ipanotationattribute.md), [IncludesPunctuationAttribute](attributescopes/accessibilityattributes/includespunctuationattribute.md), [QueueAnnouncementAttribute](attributescopes/accessibilityattributes/queueannouncementattribute.md), [SpellOutAttribute](attributescopes/accessibilityattributes/spelloutattribute.md), [TextCustomAttribute](attributescopes/accessibilityattributes/textcustomattribute.md), [TextualContextAttribute](attributescopes/accessibilityattributes/textualcontextattribute.md), [AdaptiveImageGlyphAttribute](attributescopes/appkitattributes/adaptiveimageglyphattribute.md), [AttachmentAttribute](attributescopes/appkitattributes/attachmentattribute.md), [BackgroundColorAttribute](attributescopes/appkitattributes/backgroundcolorattribute.md), [BaselineOffsetAttribute](attributescopes/appkitattributes/baselineoffsetattribute.md), [CursorAttribute](attributescopes/appkitattributes/cursorattribute.md), [ExpansionAttribute](attributescopes/appkitattributes/expansionattribute.md), [FontAttribute](attributescopes/appkitattributes/fontattribute.md), [ForegroundColorAttribute](attributescopes/appkitattributes/foregroundcolorattribute.md), [GlyphInfoAttribute](attributescopes/appkitattributes/glyphinfoattribute.md), [KernAttribute](attributescopes/appkitattributes/kernattribute.md), [LigatureAttribute](attributescopes/appkitattributes/ligatureattribute.md), [MarkedClauseSegmentAttribute](attributescopes/appkitattributes/markedclausesegmentattribute.md), [ObliquenessAttribute](attributescopes/appkitattributes/obliquenessattribute.md), [ParagraphStyleAttribute](attributescopes/appkitattributes/paragraphstyleattribute.md), [ShadowAttribute](attributescopes/appkitattributes/shadowattribute.md), [StrikethroughColorAttribute](attributescopes/appkitattributes/strikethroughcolorattribute.md), [StrikethroughStyleAttribute](attributescopes/appkitattributes/strikethroughstyleattribute.md), [StrokeColorAttribute](attributescopes/appkitattributes/strokecolorattribute.md), [StrokeWidthAttribute](attributescopes/appkitattributes/strokewidthattribute.md), [SuperscriptAttribute](attributescopes/appkitattributes/superscriptattribute.md), [TextAlternativesAttribute](attributescopes/appkitattributes/textalternativesattribute.md), [TextEffectAttribute](attributescopes/appkitattributes/texteffectattribute.md), [ToolTipAttribute](attributescopes/appkitattributes/tooltipattribute.md), [TrackingAttribute](attributescopes/appkitattributes/trackingattribute.md), [UnderlineColorAttribute](attributescopes/appkitattributes/underlinecolorattribute.md), [UnderlineStyleAttribute](attributescopes/appkitattributes/underlinestyleattribute.md), [LineHeightAttribute](attributescopes/coretextattributes/lineheightattribute.md), [TextAlignmentAttribute](attributescopes/coretextattributes/textalignmentattribute.md), [AgreementArgumentAttribute](attributescopes/foundationattributes/agreementargumentattribute.md), [AgreementConceptAttribute](attributescopes/foundationattributes/agreementconceptattribute.md), [AlternateDescriptionAttribute](attributescopes/foundationattributes/alternatedescriptionattribute.md), [ByteCountAttribute](attributescopes/foundationattributes/bytecountattribute.md), [DateFieldAttribute](attributescopes/foundationattributes/datefieldattribute.md), [DurationFieldAttribute](attributescopes/foundationattributes/durationfieldattribute.md), [ImageURLAttribute](attributescopes/foundationattributes/imageurlattribute.md), [InflectionAlternativeAttribute](attributescopes/foundationattributes/inflectionalternativeattribute.md), [InflectionRuleAttribute](attributescopes/foundationattributes/inflectionruleattribute.md), [InlinePresentationIntentAttribute](attributescopes/foundationattributes/inlinepresentationintentattribute.md), [LanguageIdentifierAttribute](attributescopes/foundationattributes/languageidentifierattribute.md), [LinkAttribute](attributescopes/foundationattributes/linkattribute.md), [ListItemDelimiterAttribute](attributescopes/foundationattributes/listitemdelimiterattribute.md), [LocalizedNumberFormatAttribute](attributescopes/foundationattributes/localizednumberformatattribute.md), [LocalizedDateArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizeddateargumentattribute.md), [LocalizedDateIntervalArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizeddateintervalargumentattribute.md), [LocalizedNumericArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizednumericargumentattribute.md), [LocalizedURLArgumentAttribute](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizedurlargumentattribute.md), [MarkdownSourcePositionAttribute](attributescopes/foundationattributes/markdownsourcepositionattribute.md), [MeasurementAttribute](attributescopes/foundationattributes/measurementattribute.md), [MorphologyAttribute](attributescopes/foundationattributes/morphologyattribute.md), [NumberPartAttribute](attributescopes/foundationattributes/numberformatattributes/numberpartattribute.md), [SymbolAttribute](attributescopes/foundationattributes/numberformatattributes/symbolattribute.md), [PersonNameComponentAttribute](attributescopes/foundationattributes/personnamecomponentattribute.md), [PresentationIntentAttribute](attributescopes/foundationattributes/presentationintentattribute.md), [ReferentConceptAttribute](attributescopes/foundationattributes/referentconceptattribute.md), [ReplacementIndexAttribute](attributescopes/foundationattributes/replacementindexattribute.md), [WritingDirectionAttribute](attributescopes/foundationattributes/writingdirectionattribute.md), [ConfidenceAttribute](attributescopes/speechattributes/confidenceattribute.md), [TimeRangeAttribute](attributescopes/speechattributes/timerangeattribute.md), [AdaptiveImageGlyphAttribute](attributescopes/swiftuiattributes/adaptiveimageglyphattribute.md), [BackgroundColorAttribute](attributescopes/swiftuiattributes/backgroundcolorattribute.md), [BaselineOffsetAttribute](attributescopes/swiftuiattributes/baselineoffsetattribute.md), [FontAttribute](attributescopes/swiftuiattributes/fontattribute.md), [ForegroundColorAttribute](attributescopes/swiftuiattributes/foregroundcolorattribute.md), [KerningAttribute](attributescopes/swiftuiattributes/kerningattribute.md), [StrikethroughStyleAttribute](attributescopes/swiftuiattributes/strikethroughstyleattribute.md), [TrackingAttribute](attributescopes/swiftuiattributes/trackingattribute.md), [UnderlineStyleAttribute](attributescopes/swiftuiattributes/underlinestyleattribute.md), [SkipTranslationAttribute](attributescopes/translationattributes/skiptranslationattribute.md), [AdaptiveImageGlyphAttribute](attributescopes/uikitattributes/adaptiveimageglyphattribute.md), [AttachmentAttribute](attributescopes/uikitattributes/attachmentattribute.md), [BackgroundColorAttribute](attributescopes/uikitattributes/backgroundcolorattribute.md), [BaselineOffsetAttribute](attributescopes/uikitattributes/baselineoffsetattribute.md), [ExpansionAttribute](attributescopes/uikitattributes/expansionattribute.md), [FontAttribute](attributescopes/uikitattributes/fontattribute.md), [ForegroundColorAttribute](attributescopes/uikitattributes/foregroundcolorattribute.md), [KernAttribute](attributescopes/uikitattributes/kernattribute.md), [LigatureAttribute](attributescopes/uikitattributes/ligatureattribute.md), [ObliquenessAttribute](attributescopes/uikitattributes/obliquenessattribute.md), [ParagraphStyleAttribute](attributescopes/uikitattributes/paragraphstyleattribute.md), [ShadowAttribute](attributescopes/uikitattributes/shadowattribute.md), [StrikethroughColorAttribute](attributescopes/uikitattributes/strikethroughcolorattribute.md), [StrikethroughStyleAttribute](attributescopes/uikitattributes/strikethroughstyleattribute.md), [StrokeColorAttribute](attributescopes/uikitattributes/strokecolorattribute.md), [StrokeWidthAttribute](attributescopes/uikitattributes/strokewidthattribute.md), [TextEffectAttribute](attributescopes/uikitattributes/texteffectattribute.md), [TextItemTagAttribute](attributescopes/uikitattributes/textitemtagattribute.md), [TrackingAttribute](attributescopes/uikitattributes/trackingattribute.md), [UnderlineColorAttribute](attributescopes/uikitattributes/underlinecolorattribute.md), [UnderlineStyleAttribute](attributescopes/uikitattributes/underlinestyleattribute.md)

## Topics

### Delcaring Key Properties

- [name](attributedstringkey/name.md) — The name of the key.
- [Value](attributedstringkey/value.md) — The type of the key’s value.

### Describing the Key

- [description](attributedstringkey/description.md)

### Type Properties

- [inheritedByAddedText](attributedstringkey/inheritedbyaddedtext.md)
- [invalidationConditions](attributedstringkey/invalidationconditions.md)
- [runBoundaries](attributedstringkey/runboundaries.md)

## See Also

### Accessing Attributes

- [subscript(_:)](<attributecontainer/subscript(__).md>) — Returns the attribute that corresponds to a specified key.
- [subscript(dynamicMember:)](<attributecontainer/subscript(dynamicmember_)-657oj.md>) — Returns the attribute that corresponds to a specified key path.
- [subscript(dynamicMember:)](<attributecontainer/subscript(dynamicmember_)-3jcvx.md>) — Returns the attribute container that corresponds to a specified key path.
- [subscript(dynamicMember:)](<attributecontainer/subscript(dynamicmember_)-60ps5.md>) — Returns a modified attribute container as part of building a chain of attributes.
- [subscript(dynamicMember:)](<attributecontainer/subscript(dynamicmember_)-swift.type.subscript.md>) — Returns a modified attribute container as part of building a chain of attributes, for use as a static method.
- [Builder](attributecontainer/builder.md) — A type that iteratively builds attribute containers by setting attribute values.
