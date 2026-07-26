---
title: Morphology.CustomPronoun
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, macOS 12.0+（14.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+, watchOS 8.0+（10.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/morphology/custompronoun
source_url: 'https://developer.apple.com/documentation/foundation/morphology/custompronoun'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/morphology/custompronoun.json'
content_hash: 'sha256:3b49c0b1f8e48444'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Morphology](../morphology.md)

# Morphology.CustomPronoun

<sub>Structure</sub>

A custom pronoun behavior for use in a specific langauge.

> [!warning] Deprecated
> Use TermOfAddress instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CustomPronoun
```

## Overview

Set a [CustomPronoun](custompronoun.md) instance on a [Morphology](../morphology.md) instance when you want to provide a langauge-specific customization of pronoun use in that language. Different languages have different requirements for the grammatical information needed to apply a custom pronoun, so you set custom pronoun behavior on a per-language basis.

The example below shows how to create English “ze” and “hir” custom pronouns:

```swift
let ze = Morphology.CustomPronoun()
ze.subjectForm = "ze"
ze.objectForm = "hir"
ze.possessiveForm = "hir"
ze.possessiveAdjectiveForm = "hir"
ze.reflexiveForm = "hirself"
```

[CustomPronoun](custompronoun.md) only supports third-person pronouns. Use this feature when your app needs to refer to third parties with a specific pronoun.

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a Custom Pronoun

- [init()](<custompronoun/init().md>) — Creates an empty custom pronoun. _(deprecated)_

### Assessing Custom Pronoun Support

- [isSupported(forLanguage:)](<custompronoun/issupported(forlanguage_).md>) — Returns a Boolean value that indicates whether the given language supports setting custom pronouns. _(deprecated)_
- [requiredKeys(forLanguage:)](<custompronoun/requiredkeys(forlanguage_).md>) — Returns a collection of the custom pronoun keys required by this language. _(deprecated)_

### Determining Pronoun Forms

- [subjectForm](custompronoun/subjectform.md) — The subject pronoun form to apply when using this custom pronoun behavior. _(deprecated)_
- [objectForm](custompronoun/objectform.md) — The object pronoun form to apply when using this custom pronoun behavior. _(deprecated)_
- [possessiveForm](custompronoun/possessiveform.md) — The posessive pronoun form to apply when using this custom pronoun behavior. _(deprecated)_
- [possessiveAdjectiveForm](custompronoun/possessiveadjectiveform.md) — The posessive adjective pronoun form to apply when using this custom pronoun behavior. _(deprecated)_
- [reflexiveForm](custompronoun/reflexiveform.md) — The reflexive pronoun form to apply when using this custom pronoun behavior. _(deprecated)_

## See Also

### Accessing Per-Language Features

- [setCustomPronoun(_:forLanguage:)](<setcustompronoun(__forlanguage_).md>) — Sets a custom pronoun behavior for this morphology to apply to the given language. _(deprecated)_
- [customPronoun(forLanguage:)](<custompronoun(forlanguage_).md>) — Returns any custom pronoun behavior this morphology applies to the given language. _(deprecated)_
