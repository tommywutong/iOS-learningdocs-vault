---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOQualifierVariable.html
archived_at: '2026-07-15T08:11:39.994256Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOQualifierVariable

> **__Inherits
> from:__**
> : NSObject

> **__Conforms to:__**
> : NSCoding
> : EOKeyValueArchiving

> __Declared in:__ : EOControl/EOQualifier.h

---

## Class Description

---

EOQualifierVariable defines objects that serve as placeholders
in the qualifier. When you create a qualifier programmatically,
you typically do something like this:

> ```
> aQual = EOQualifier.qualifierWithQualifierFormat("dateReleased = %@", aDate);
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

Variable values must be substituted for using [qualifierWithBindings:requiresAllVariables:](EOQualifier-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2rovqwy2lgnfsxel3rovqwy2lgnfsxev3joruee2lomruw4z3thjzgk4lvnfzgk42bnrwfmylsnfqwe3dfom5a).

## Constants

---

In EOQualifier.h, EOControl defines the
following NSString constant as the type of exception that's raised
when an EOQualifierVariable object requires bindings for all its
variables and one or more variable is missing from the bindings
(see [qualifierWithBindings:requiresAllVariables:](EOQualifier-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2rovqwy2lgnfsxel3rovqwy2lgnfsxev3joruee2lomruw4z3thjzgk4lvnfzgk42bnrwfmylsnfqwe3dfom5a) in
the [EOQualifier](EOQualifier-3.md#apple-ijbesrcgjfees) class specification):

- EOQualifierVariableSubstitutionException

## Adopted Protocols

---

> NSCoding: `- initWithCoder:`
> : `- encodeWithCoder:`
>
> EOKeyValueArchiving: `- initWithKeyValueUnarchiver:`
> : `- encodeWithKeyValueArchiver:`

## Class Methods

---

### variableWithKey:

`+ (id)variableWithKey:(NSString
*)key`

Creates and returns a new EOQualifierVariable
object with the specified key. For example, if your qualifier is
"dateReleased = $aDate", then this method would be invoked with
the key "aDate".

---

## Instance Methods

---

### initWithKey:

`- (id)initWithKey:(NSString
*)key`

Initializes a new EOQualifierVariable object
with the specified key. For example, if your qualifier is "dateReleased
= $aDate", then this method would be invoked with the key "aDate".

---

### key

`- (NSString *)key`

Returns the key of the variable qualifier.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
