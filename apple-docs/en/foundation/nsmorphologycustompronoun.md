---
title: NSMorphologyCustomPronoun
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, macOS 12.0+（14.0 起废弃）, tvOS 15.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 8.0+（10.0 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsmorphologycustompronoun
source_url: 'https://developer.apple.com/documentation/foundation/nsmorphologycustompronoun'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmorphologycustompronoun.json'
content_hash: 'sha256:8ffe34ae61039631'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMorphologyCustomPronoun

<sub>Class</sub>

A custom pronoun behavior for use in a specific langauge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface NSMorphologyCustomPronoun : NSObject
```

## Overview

Set a [NSMorphologyCustomPronoun](nsmorphologycustompronoun.md) instance on a [NSMorphology](nsmorphology.md) instance when you want to provide a langauge-specific customization of pronoun use in that language. Different languages have different requirements for the grammatical information needed to apply a custom pronoun, so you set custom pronoun behavior on a per-language basis.

The example below shows how to create English “ze” and “hir” custom pronouns:

```objc
let ze = [[NSMorphologyCustomPronoun alloc] init];
ze.subjectForm = "ze";
ze.objectForm = "hir";
ze.possessiveForm = "hir";
ze.possessiveAdjectiveForm = "hir";
ze.reflexiveForm = "hirself";
```

[NSMorphologyCustomPronoun](nsmorphologycustompronoun.md) only supports third-person pronouns. Use this feature when your app needs to refer to third parties with a specific pronoun.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](nscopying.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Assessing Custom Pronoun Support

- [isSupportedForLanguage:](nsmorphologycustompronoun/issupportedforlanguage_.md) — Returns a Boolean value that indicates whether the given language supports setting custom pronouns. _(deprecated)_
- [requiredKeysForLanguage:](nsmorphologycustompronoun/requiredkeysforlanguage_.md) — Returns a collection of the custom pronoun keys required by this language. _(deprecated)_

### Determining Pronoun Forms

- [subjectForm](nsmorphologycustompronoun/subjectform.md) — The subject pronoun form to apply when using this custom pronoun behavior. _(deprecated)_
- [objectForm](nsmorphologycustompronoun/objectform.md) — The object pronoun form to apply when using this custom pronoun behavior. _(deprecated)_
- [possessiveForm](nsmorphologycustompronoun/possessiveform.md) — The posessive pronoun form to apply when using this custom pronoun behavior. _(deprecated)_
- [possessiveAdjectiveForm](nsmorphologycustompronoun/possessiveadjectiveform.md) — The posessive adjective pronoun form to apply when using this custom pronoun behavior. _(deprecated)_
- [reflexiveForm](nsmorphologycustompronoun/reflexiveform.md) — The reflexive pronoun form to apply when using this custom pronoun behavior. _(deprecated)_

## See Also

### Accessing Per-Language Features

- [setCustomPronoun:forLanguage:error:](nsmorphology/setcustompronoun_forlanguage_error_.md) — Sets a custom pronoun behavior for this morphology to apply to the given language. _(deprecated)_
- [customPronounForLanguage:](nsmorphology/custompronounforlanguage_.md) — Returns any custom pronoun behavior this morphology applies to the given language. _(deprecated)_
