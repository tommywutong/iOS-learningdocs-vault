---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOQualifierVariable.html
archived_at: '2026-07-15T08:11:37.935261Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOQualifierVariable

> **__Inherits from:__**
> : (com.apple.client.eocontrol) Object
>
> (com.apple.yellow.eocontrol) NSObject

> **__Implements:__**
> : (com.apple.client.eocontrol only) NSCoding

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

EOQualifierVariable defines objects that serve as placeholders
in the qualifier. When you create a qualifier programmatically,
you typically do something like this:

> ```
> aQual = [EOQualifier qualifierWithQualifierFormat:"dateReleased = %@", aDate];
> ```

where _aDate_ is a variable that
contains the actual date you want to query upon. When you store
the qualifier in an EOModel, there is no way to know the actual
value to query upon or the variable that will contain that value.
The EOQualifierVariable object acts as a placeholder for the actual
variable that will represent the right side of the expression. You
specify an EOQualifierVariable by using a $, as in the following:

> ```
> dateReleased = $aDate
> ```

Variable values must be substituted for using [qualifierWithBindings](EOQualifier.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4rpof2wc3djmzuwk4sxnf2gqqtjnzsgs3thom).

## Constants

---

(com.apple.yellow.eocontrol only) EOQualifierVariable defines
the following String constant as the type of exception that's
raised when an EOQualifierVariable object requires bindings for
all its variables and one or more variable is missing from the bindings
(see [qualifierWithBindings](EOQualifier.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4rpof2wc3djmzuwk4sxnf2gqqtjnzsgs3thom) in the [EOQualifier](EOQualifier.md#apple-ijbesrcgjfees) class specification):

- QualifierVariableSubstitutionException

## Interfaces Implemented

---

> NSCoding: `classForCoder`
> : `encodeWithCoder`

## Constructors

---

### `EOQualifierVariable`

`public EOQualifierVariable(String key)`

Creates and returns a new EOQualifierVariable
object with the specified name. For example, if your qualifier is
"dateReleased = $aDate", then this method would be invoked with
the key "aDate".

---

## Static Methods

---

### variableWithKey

`public static Object variableWithKey(String key)`

(com.apple.yellow.eocontrol only) Creates and
returns a new EOQualifierVariable object with the specified key.
For example, if your qualifier is "dateReleased = $aDate", then
this method would be invoked with the key "aDate".

---

## Instance Methods

---

### key

`public String key()`

Returns the key of the variable qualifier.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
