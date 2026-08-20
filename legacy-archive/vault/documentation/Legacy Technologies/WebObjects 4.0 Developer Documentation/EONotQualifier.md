---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EONotQualifier.html
archived_at: '2026-07-18T01:28:26.577365Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOKeyValueQualifier.md)
[!](EONullValue.md)

---

# EONotQualifier

__Inherits From:__
EOQualifier

__Implements:__
EOQualifierEvaluation
NSCoding (Java Client only)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

EONotQualifier is a subclass of EOQualifier that contains a single qualifier. When an EONotQualifier object is evaluated, it returns the inverse of the result obtained by evaluating the qualifier it contains.

EONotQualifier implements the EOQualifierEvaluation interface, which defines the method [__evaluateWithObject__](EOQualifierEvaluation.md)for in-memory evaluation. When an EONotQualifier object receives an [__evaluateWithObject__](EOQualifierEvaluation.md)message, it evaluates the given object to determine if it satisfies the qualifier criteria.

## Interfaces Implemented

**EOQualifierEvaluation**

**[- evaluateWithObject](EOQualifierEvaluation.md)**

**NSCoding (Java Client only)**

**classForCoder

**encodeWithCoder****

## Constructors

---

#### EONotQualifier

public com.apple.yellow.eocontrol.__EONotQualifier__ (EOQualifier _aQualifier_)

Creates and returns a new EONotQualifier

If aQualifier is specified, it is used as the qualifier. For example, the following code excerpt constructs a qualifier, `baseQual`, and uses it to initialize an EONotQualifier, `negQual`. The EONotQualifier `negQual` is then used to filter an in-memory array. The code excerpt returns an array of Guest objects whose __lastName__ properties do _not_ have the same value as the __lastName__ property of the guest's sponsoring member (this example is based on the Rentals sample database). In other words, the EONotQualifier `negQual` inverts the effects of `baseQual`.

> ```
> NSArray guests /* Assume this exists */
> EOQualifier baseQual;
> EONotQualifier negQual;
>
> baseQual = EOQualifier.qualifierWithQualifierFormat("lastName = member.lastName", null);
> negQual = new EONotQualifier(baseQual);
> return EOQualifier.filteredArrayWithQualifier(guests, negQual);
> ```

## Instance Methods

---

#### evaluateWithObject

EOQualifierEvaluation interface

public boolean __evaluateWithObject__ (java.lang.Object _anObject_)

Returns __true__ if the object _anObject_ satisfies the EONotQualifier, __false__ otherwise. This method can throw one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

#### qualifier

EOQualifier __qualifier__ ()

Returns the receiver's qualifier_._

---

[!](EOKeyValueQualifier.md)
[!](EONullValue.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
