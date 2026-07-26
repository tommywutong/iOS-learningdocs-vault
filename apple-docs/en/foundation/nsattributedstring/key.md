---
title: NSAttributedString.Key
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key.json'
content_hash: 'sha256:40573dff9b0fe622'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# NSAttributedString.Key

<sub>Structure</sub>

The attributes you apply to ranges of characters in an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Key
```

## Discussion

The [Key](key.md) type defines the attributes you apply to ranges of characters in an attributed string. Some attributes provide information about how to render, lay out, or interpret the text, while other attributes provide transient or collaborative information. Attributes like the [font](key/font.md), [kern](key/kern.md), and [strokeColor](key/strokecolor.md) contain information that the rendering system uses to display the text. Attributes like the [spellingState](key/spellingstate.md), [textHighlightStyle](key/texthighlightstyle.md), or [accessibilityCustomText](key/accessibilitycustomtext.md) contain semantic information from other parts of the system. Some of these semantic attributes also affect how the system renders the text, but they are transient attributes unlike the core rendering attributes.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting rendering attribute keys

- [backgroundColor](key/backgroundcolor.md) — The color of the background behind the text.
- [baselineOffset](key/baselineoffset.md) — The vertical offset for the position of the text.
- [font](key/font.md) — The font of the text.
- [foregroundColor](key/foregroundcolor.md) — The color of the text.
- [glyphInfo](key/glyphinfo.md) — The name of a glyph info object.
- [kern](key/kern.md) — The kerning of the text.
- [ligature](key/ligature.md) — The ligature of the text.
- [paragraphStyle](key/paragraphstyle.md) — The paragraph style of the text.
- [strikethroughColor](key/strikethroughcolor.md) — The color of the strikethrough.
- [strikethroughStyle](key/strikethroughstyle.md) — The strikethrough style of the text.
- [strokeColor](key/strokecolor.md) — The color of the stroke.
- [strokeWidth](key/strokewidth.md) — The width of the stroke.
- [superscript](key/superscript.md) — The superscript of the text.
- [tracking](key/tracking.md) — The amount to modify the default tracking.
- [underlineColor](key/underlinecolor.md) — The color of the underline.
- [underlineStyle](key/underlinestyle.md) — The underline style of the text.
- [writingDirection](key/writingdirection.md) — The writing direction of the text.

### Getting text attribute keys

- [cursor](key/cursor.md) — The cursor object.
- [link](key/link.md) — The link for the text.
- [markedClauseSegment](key/markedclausesegment.md) — The index of the marked clause segment.
- [NSReplacementIndexAttributeName](key/replacementindex.md) — The replacement position associated with a format string specifier.
- [shadow](key/shadow.md) — The shadow of the text.
- [spellingState](key/spellingstate.md) — The spelling state of the text.
- [suggestionHighlight](key/suggestionhighlight.md) — A highlight associated with a Spotlight suggestion.
- [textAlternatives](key/textalternatives.md) — The alternatives for the text.
- [textEffect](key/texteffect.md) — An attribute that applies a text effect to the text.
- [textHighlightColorScheme](key/texthighlightcolorscheme.md) — The custom highlight color to apply to the text.
- [textHighlightStyle](key/texthighlightstyle.md) — An attribute that adds a highlight color to the text to emphasize it.
- [textItemTag](key/textitemtag.md) — The name of a custom tag associated with a text item.
- [toolTip](key/tooltip.md) — The tooltip text.

### Getting attachment attribute keys

- [adaptiveImageGlyph](key/adaptiveimageglyph.md) — The adaptive image glyph for the text.
- [attachment](key/attachment.md) — The attachment for the text.

### Getting accessibility attribute keys

- [accessibilityAlignment](key/accessibilityalignment.md)
- [accessibilityAnnotationTextAttribute](key/accessibilityannotationtextattribute.md)
- [accessibilityAttachment](key/accessibilityattachment.md) — Text attachment (`id`). _(deprecated)_
- [accessibilityAutocorrected](key/accessibilityautocorrected.md) — Autocorrected text (`NSNumber` as a Boolean value).
- [accessibilityBackgroundColor](key/accessibilitybackgroundcolor.md) — Text background color (`CGColorRef`).
- [accessibilityCustomText](key/accessibilitycustomtext.md)
- [accessibilityFont](key/accessibilityfont.md) — Font keys (`NSDictionary`).
- [accessibilityFontBoldAttribute](key/accessibilityfontboldattribute.md)
- [accessibilityFontItalicAttribute](key/accessibilityfontitalicattribute.md)
- [accessibilityForegroundColor](key/accessibilityforegroundcolor.md) — Text foreground color (`CGColorRef`).
- [accessibilityLanguage](key/accessibilitylanguage.md)
- [accessibilityLink](key/accessibilitylink.md) — Text link (`id`).
- [accessibilityListItemIndex](key/accessibilitylistitemindex.md)
- [accessibilityListItemLevel](key/accessibilitylistitemlevel.md)
- [accessibilityListItemPrefix](key/accessibilitylistitemprefix.md)
- [accessibilityMarkedMisspelled](key/accessibilitymarkedmisspelled.md) — Misspelled text that is visibly marked as misspelled (`NSNumber` as a Boolean value). If you’re implementing a custom text-editing app, use `NSAccessibilityMarkedMisspelledTextAttribute` to ensure that VoiceOver properly identifies misspelled text to users.
- [accessibilityMisspelled](key/accessibilitymisspelled.md) — Misspelled text that isn’t necessarily visibly marked as misspelled ([NSNumber](../nsnumber.md) as a Boolean value). Beginning in macOS 10.9, VoiceOver no longer checks for this attribute; instead, VoiceOver uses [accessibilityMarkedMisspelled](key/accessibilitymarkedmisspelled.md).
- [accessibilityShadow](key/accessibilityshadow.md) — Text shadow (`NSNumber` as a Boolean value).
- [accessibilitySpeechAnnouncementPriority](key/accessibilityspeechannouncementpriority.md)
- [accessibilitySpeechIPANotation](key/accessibilityspeechipanotation.md) — A key that indicates the pronunciation of a specific word or phrase, such as a proper name.
- [accessibilitySpeechLanguage](key/accessibilityspeechlanguage.md) — A key that indicates the language to use when speaking a string.
- [accessibilitySpeechPitch](key/accessibilityspeechpitch.md) — A key that indicates the pitch to apply to spoken content.
- [accessibilitySpeechPunctuation](key/accessibilityspeechpunctuation.md) — A key that indicates whether to speak punctuation.
- [accessibilitySpeechQueueAnnouncement](key/accessibilityspeechqueueannouncement.md) — A key that indicates whether to queue an announcement behind existing speech or to interrupt it.
- [accessibilitySpeechSpellOut](key/accessibilityspeechspellout.md)
- [accessibilityTextCustom](key/accessibilitytextcustom.md) — A key for specifying custom attributes to apply to the text.
- [accessibilityTextHeadingLevel](key/accessibilitytextheadinglevel.md) — A key for specifying the heading level of the text.
- [accessibilityStrikethrough](key/accessibilitystrikethrough.md) — Text strikethrough (`NSNumber` as a Boolean value).
- [accessibilityStrikethroughColor](key/accessibilitystrikethroughcolor.md) — Text strikethrough color (`CGColorRef`).
- [accessibilitySuperscript](key/accessibilitysuperscript.md) — Text superscript style (`NSNumber`). Values \> 0 are superscript; values \< 0 are subscript.
- [accessibilityUnderline](key/accessibilityunderline.md) — Text underline style (`NSNumber`).
- [accessibilityUnderlineColor](key/accessibilityunderlinecolor.md) — Text underline color (`CGColorRef`).
- [UIAccessibilityTextAttributeContext](key/uiaccessibilitytextattributecontext.md)

### Getting Markdown attribute keys

- [NSInlinePresentationIntentAttributeName](key/inlinepresentationintent.md) — An attribute that provides details for an inline Markdown element.
- [NSPresentationIntentAttributeName](key/presentationintentattributename.md) — An attribute that provides details for a block-level Markdown element.
- [NSMarkdownSourcePositionAttributeName](key/markdownsourceposition.md) — The position in a Markdown source string corresponding to some attributed text.
- [NSAlternateDescriptionAttributeName](key/alternatedescription.md) — An alternate description for a URL or image.
- [NSImageURLAttributeName](key/imageurl.md) — The URL for an image in Markdown text.

### Getting translation-related attribute keys

- [NSLanguageIdentifierAttributeName](key/languageidentifier.md) — The language identifier associated with the range of text.
- [NSMorphologyAttributeName](key/morphology.md) — An attribute that contains grammatical properties to apply to the text.
- [NSInflectionRuleAttributeName](key/inflectionrule.md) — An attribute that tells the system how to apply grammar rules and other modifiers to the range of text.
- [NSInflectionAlternativeAttributeName](key/inflectionalternative.md) — The alternative translation for a string when no suitable inflection exists.
- [NSInflectionAgreementArgumentAttributeName](key/agreewithargument.md) — An attribute key whose value indicates inflection agreement with a specific argument.
- [NSInflectionAgreementConceptAttributeName](key/agreewithconcept.md) — An attribute key whose value indicates inflection agreement with a specific concept.
- [NSInflectionReferentConceptAttributeName](key/referentconcept.md) — An attribute key whose value indicates the referent concept for inflection.
- [NSLocalizedNumberFormatAttributeName](key/localizednumberformat.md) — An attribute key whose value specifies a localized number format.

### Getting formatting attribute keys

- [NSListItemDelimiterAttributeName](key/listitemdelimiter.md) — The delimiter used when declaring the current list item.

### Getting writing tools attribute keys

- [writingToolsExclusionAttributeName](key/writingtoolsexclusionattributename.md)

### Deprecated Keys

- [expansion](key/expansion.md) — The expansion factor of the text. _(deprecated)_
- [obliqueness](key/obliqueness.md) — The obliqueness of the text. _(deprecated)_
- [verticalGlyphForm](key/verticalglyphform.md) — The vertical glyph form of the text. _(deprecated)_
- [characterShapeAttributeName](key/charactershapeattributename.md) — The character shape attribute. _(deprecated)_
- [usesScreenFontsDocumentAttribute](key/usesscreenfontsdocumentattribute.md) — The screen fonts attribute. _(deprecated)_

### Initializers

- [init(_:)](<key/init(__).md>) — Creates an attributed string key.
- [init(rawValue:)](<key/init(rawvalue_).md>) — Creates an attributed string key with the specified raw value.

## See Also

### Getting text content attributes

- [TextHighlightStyle](texthighlightstyle.md) — Constants that specify the type of highlight to apply to text.
- [TextHighlightColorScheme](texthighlightcolorscheme.md) — Constants that specify the highlight color to use with the text.
- [TextEffectStyle](texteffectstyle.md) — Constants for the type of effect to apply to the text.
- [SpellingState](spellingstate.md) — Constants for the spelling state attribute key.
- [NSUnderlineStyle](../../uikit/nsunderlinestyle.md) — Constants for the underline style and strikethrough style attribute keys.
- [NSWritingDirectionFormatType](../../uikit/nswritingdirectionformattype.md) — Constants for the writing direction attribute key.
