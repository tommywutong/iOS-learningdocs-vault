---
title: Unicode.Scalar.Properties
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct.json'
content_hash: 'sha256:4d83d2e94dce4da3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [Scalar](../scalar.md)

# Unicode.Scalar.Properties

<sub>Structure</sub>

A value that provides access to properties of a Unicode scalar that are defined by the Unicode standard.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Properties
```

## Relationships

- **Conforms To**: [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Instance Properties

- [age](properties-swift.struct/age.md) — The earliest version of the Unicode Standard in which the scalar was assigned.
- [canonicalCombiningClass](properties-swift.struct/canonicalcombiningclass.md) — The canonical combining class of the scalar.
- [changesWhenCaseFolded](properties-swift.struct/changeswhencasefolded.md) — A Boolean value indicating whether the scalar’s normalized form differs from the case-fold mapping of each constituent scalar.
- [changesWhenCaseMapped](properties-swift.struct/changeswhencasemapped.md) — A Boolean value indicating whether the scalar may change when it undergoes case mapping.
- [changesWhenLowercased](properties-swift.struct/changeswhenlowercased.md) — A Boolean value indicating whether the scalar’s normalized form differs from the `lowercaseMapping` of each constituent scalar.
- [changesWhenNFKCCaseFolded](properties-swift.struct/changeswhennfkccasefolded.md) — A Boolean value indicating whether the scalar is one that is not identical to its NFKC case-fold mapping.
- [changesWhenTitlecased](properties-swift.struct/changeswhentitlecased.md) — A Boolean value indicating whether the scalar’s normalized form differs from the `titlecaseMapping` of each constituent scalar.
- [changesWhenUppercased](properties-swift.struct/changeswhenuppercased.md) — A Boolean value indicating whether the scalar’s normalized form differs from the `uppercaseMapping` of each constituent scalar.
- [generalCategory](properties-swift.struct/generalcategory.md) — The general category (most usual classification) of the scalar.
- [isASCIIHexDigit](properties-swift.struct/isasciihexdigit.md) — A Boolean value indicating whether the scalar is an ASCII character commonly used for the representation of hexadecimal numbers.
- [isAlphabetic](properties-swift.struct/isalphabetic.md) — A Boolean value indicating whether the scalar is alphabetic.
- [isBidiControl](properties-swift.struct/isbidicontrol.md) — A Boolean value indicating whether the scalar is a format control character that has a specific function in the Unicode Bidirectional Algorithm.
- [isBidiMirrored](properties-swift.struct/isbidimirrored.md) — A Boolean value indicating whether the scalar is mirrored in bidirectional text.
- [isCaseIgnorable](properties-swift.struct/iscaseignorable.md) — A Boolean value indicating whether the scalar is ignored for casing purposes.
- [isCased](properties-swift.struct/iscased.md) — A Boolean value indicating whether the scalar is considered to be either lowercase, uppercase, or titlecase.
- [isDash](properties-swift.struct/isdash.md) — A Boolean value indicating whether the scalar is a punctuation symbol explicitly called out as a dash in the Unicode Standard or a compatibility equivalent.
- [isDefaultIgnorableCodePoint](properties-swift.struct/isdefaultignorablecodepoint.md) — A Boolean value indicating whether the scalar is a default-ignorable code point.
- [isDeprecated](properties-swift.struct/isdeprecated.md) — A Boolean value indicating whether the scalar is deprecated.
- [isDiacritic](properties-swift.struct/isdiacritic.md) — A Boolean value indicating whether the scalar is a diacritic.
- [isEmoji](properties-swift.struct/isemoji.md) — A Boolean value indicating whether the scalar has an emoji presentation, whether or not it is the default.
- [isEmojiModifier](properties-swift.struct/isemojimodifier.md) — A Boolean value indicating whether the scalar is one that can modify a base emoji that precedes it.
- [isEmojiModifierBase](properties-swift.struct/isemojimodifierbase.md) — A Boolean value indicating whether the scalar is one whose appearance can be changed by an emoji modifier that follows it.
- [isEmojiPresentation](properties-swift.struct/isemojipresentation.md) — A Boolean value indicating whether the scalar is one that should be rendered with an emoji presentation, rather than a text presentation, by default.
- [isExtender](properties-swift.struct/isextender.md) — A Boolean value indicating whether the scalar’s principal function is to extend the value or shape of a preceding alphabetic scalar.
- [isFullCompositionExclusion](properties-swift.struct/isfullcompositionexclusion.md) — A Boolean value indicating whether the scalar is excluded from composition when performing Unicode normalization.
- [isGraphemeBase](properties-swift.struct/isgraphemebase.md) — A Boolean value indicating whether the scalar is a grapheme base.
- [isGraphemeExtend](properties-swift.struct/isgraphemeextend.md) — A Boolean value indicating whether the scalar is a grapheme extender.
- [isHexDigit](properties-swift.struct/ishexdigit.md) — A Boolean value indicating whether the scalar is one that is commonly used for the representation of hexadecimal numbers or a compatibility equivalent.
- [isIDContinue](properties-swift.struct/isidcontinue.md) — A Boolean value indicating whether the scalar is one which is recommended to be allowed to appear in a non-starting position in a programming language identifier.
- [isIDSBinaryOperator](properties-swift.struct/isidsbinaryoperator.md) — A Boolean value indicating whether the scalar is an ideographic description character that determines how the two ideographic characters or ideographic description sequences that follow it are to be combined to form a single character.
- [isIDSTrinaryOperator](properties-swift.struct/isidstrinaryoperator.md) — A Boolean value indicating whether the scalar is an ideographic description character that determines how the three ideographic characters or ideographic description sequences that follow it are to be combined to form a single character.
- [isIDStart](properties-swift.struct/isidstart.md) — A Boolean value indicating whether the scalar is one which is recommended to be allowed to appear in a starting position in a programming language identifier.
- [isIdeographic](properties-swift.struct/isideographic.md) — A Boolean value indicating whether the scalar is considered to be a CJKV (Chinese, Japanese, Korean, and Vietnamese) or other siniform (Chinese writing-related) ideograph.
- [isJoinControl](properties-swift.struct/isjoincontrol.md) — A Boolean value indicating whether the scalar is a format control character that has a specific function in controlling cursive joining and ligation.
- [isLogicalOrderException](properties-swift.struct/islogicalorderexception.md) — A Boolean value indicating whether the scalar requires special handling for operations involving ordering, such as sorting and searching.
- [isLowercase](properties-swift.struct/islowercase.md) — A Boolean value indicating whether the scalar’s letterform is considered lowercase.
- [isMath](properties-swift.struct/ismath.md) — A Boolean value indicating whether the scalar is one that naturally appears in mathematical contexts.
- [isNoncharacterCodePoint](properties-swift.struct/isnoncharactercodepoint.md) — A Boolean value indicating whether the scalar is permanently reserved for internal use.
- [isPatternSyntax](properties-swift.struct/ispatternsyntax.md) — A Boolean value indicating whether the scalar is recommended to have syntactic usage in patterns represented in source code.
- [isPatternWhitespace](properties-swift.struct/ispatternwhitespace.md) — A Boolean value indicating whether the scalar is recommended to be treated as whitespace when parsing patterns represented in source code.
- [isQuotationMark](properties-swift.struct/isquotationmark.md) — A Boolean value indicating whether the scalar is one that is used in writing to surround quoted text.
- [isRadical](properties-swift.struct/isradical.md) — A Boolean value indicating whether the scalar is a radical component of CJK characters, Tangut characters, or Yi syllables.
- [isSentenceTerminal](properties-swift.struct/issentenceterminal.md) — A Boolean value indicating whether the scalar is a punctuation mark that generally marks the end of a sentence.
- [isSoftDotted](properties-swift.struct/issoftdotted.md) — A Boolean value indicating whether the scalar has a “soft dot” that disappears when a diacritic is placed over the scalar.
- [isTerminalPunctuation](properties-swift.struct/isterminalpunctuation.md) — A Boolean value indicating whether the scalar is a punctuation symbol that typically marks the end of a textual unit.
- [isUnifiedIdeograph](properties-swift.struct/isunifiedideograph.md) — A Boolean value indicating whether the scalar is one of the unified CJK ideographs in the Unicode Standard.
- [isUppercase](properties-swift.struct/isuppercase.md) — A Boolean value indicating whether the scalar’s letterform is considered uppercase.
- [isVariationSelector](properties-swift.struct/isvariationselector.md) — A Boolean value indicating whether the scalar is a variation selector.
- [isWhitespace](properties-swift.struct/iswhitespace.md) — A Boolean value indicating whether the scalar is a whitespace character.
- [isXIDContinue](properties-swift.struct/isxidcontinue.md) — A Boolean value indicating whether the scalar is one which is recommended to be allowed to appear in a non-starting position in a programming language identifier, with adjustments made for NFKC normalized form.
- [isXIDStart](properties-swift.struct/isxidstart.md) — A Boolean value indicating whether the scalar is one which is recommended to be allowed to appear in a starting position in a programming language identifier, with adjustments made for NFKC normalized form.
- [lowercaseMapping](properties-swift.struct/lowercasemapping.md) — The lowercase mapping of the scalar.
- [name](properties-swift.struct/name.md) — The published name of the scalar.
- [nameAlias](properties-swift.struct/namealias.md) — The normative formal alias of the scalar.
- [numericType](properties-swift.struct/numerictype.md) — The numeric type of the scalar.
- [numericValue](properties-swift.struct/numericvalue.md) — The numeric value of the scalar.
- [titlecaseMapping](properties-swift.struct/titlecasemapping.md) — The titlecase mapping of the scalar.
- [uppercaseMapping](properties-swift.struct/uppercasemapping.md) — The uppercase mapping of the scalar.

## See Also

### Inspecting a Scalar

- [value](value.md) — A numeric representation of the Unicode scalar.
- [properties](properties-swift.property.md) — Properties of this scalar defined by the Unicode standard.
- [hash(into:)](<hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.
- [isASCII](isascii.md) — A Boolean value indicating whether the Unicode scalar is an ASCII character.
