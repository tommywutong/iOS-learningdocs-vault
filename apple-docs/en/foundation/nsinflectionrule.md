---
title: NSInflectionRule
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsinflectionrule
source_url: 'https://developer.apple.com/documentation/foundation/nsinflectionrule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinflectionrule.json'
content_hash: 'sha256:95ca84f80a7cc165'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSInflectionRule

<sub>Class</sub>

A rule that affects how an attributed string performs automatic grammatical agreement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface NSInflectionRule : NSObject
```

## Overview

Most apps can rely on loading localized strings to perform automatic grammar agreement. Typically, your app’s strings files use the Markdown extension syntax to indicate portions of the string that may require inflection to agree grammatically. This transformation occurs when you load the attributed string with methods like `NSLocalizedAttributedString`.

However, if the system lacks information about the words in the string, you may need to apply an inflection rule programmatically. For example, a social networking app may have gender information about other users that you want to apply at runtime. When performing manual inflection at runtime, you use an inflection rule to indicate to the system what portions of a string should be automatically edited, and what to match. Add the attribute [NSInflectionRuleAttributeName](nsattributedstring/key/inflectionrule.md) with an [NSInflectionRule](nsinflectionrule.md) on an [NSAttributedString](nsattributedstring.md), then call [- attributedStringByInflectingString](<nsattributedstring/inflecting().md>) to perform the grammar agreement and produce an edited string.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSInflectionRuleExplicit](nsinflectionruleexplicit.md)

- **Conforms To**: [NSCopying](nscopying.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Performing Automatic Inflection

- [automaticRule](nsinflectionrule/automaticrule.md) — An inflection rule that performs automatic grammar agreement with default transformations.

### Determining Availability

- [canInflectLanguage:](nsinflectionrule/caninflectlanguage_.md) — Returns a Boolean value that indicates whether the rule can inflect a given language.
- [canInflectPreferredLocalization](nsinflectionrule/caninflectpreferredlocalization.md) — A Boolean value that indicates whether the rule can inflect the user’s current preferred localization.

## See Also

### Automatic grammar agreement

- [NSInflectionRuleExplicit](nsinflectionruleexplicit.md) — An inflection rule that uses a morphology instance to determine how to inflect attribued strings.
- [NSMorphology](nsmorphology.md) — A description of the grammatical properties of a string.
- [NSTermOfAddress](nstermofaddress.md) — The type for representing grammatical gender in localized text.
- [NSMorphologyPronoun](nsmorphologypronoun.md) — A custom pronoun for referring to a third person.
