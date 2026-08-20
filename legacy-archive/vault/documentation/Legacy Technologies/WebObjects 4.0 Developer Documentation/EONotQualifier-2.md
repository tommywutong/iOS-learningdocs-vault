---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EONotQualifier.html
archived_at: '2026-07-18T01:28:36.576398Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOKeyValueQualifier-2.md)
[!](EONull.md)

---

# EONotQualifier

__Inherits From:__
EOQualifier : NSObject

__Conforms To:__ EOQualifierEvaluation
EOQualifierSQLGeneration

__Declared in:__ EOControl/EOQualifier.h

EONotQualifier is a subclass of EOQualifier that contains a single qualifier. When an EONotQualifier object is evaluated, it returns the inverse of the result obtained by evaluating the qualifier it contains.

EONotQualifier adopts the EOQualifierEvaluation protocol, which defines the method [__evaluateWithObject:__](EOQualifierEvaluation-2.md)for in-memory evaluation. When an EONotQualifier object receives an [__evaluateWithObject:__](EOQualifierEvaluation-2.md)message, it evaluates the given object to determine if it satisfies the qualifier criteria.

---

## Adopted Protocols

**EOQualifierEvaluation**

**[- evaluateWithObject:](EOQualifierEvaluation-2.md)**

**EOQualifierSQLGeneration**

**- sqlStringForSQLExpression:

**- schemaBasedQualifierWithRootEntity:****

---

#### evaluateWithObject:

@protocol EOQualifierEvaluation

- (BOOL)`evaluateWithObject:`_anObject_

Returns YES if the object _anObject_ satisfies the EONotQualifier, NO otherwise. This method can raise one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to put exception handlers around this method to properly respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

#### initWithQualifier:

- `initWithQualifier:`(EOQualifier \*)_aQualifier_

Initializes the receiver with the EOQualifier _aQualifier_. For example, the following code excerpt constructs a qualifier, `baseQual`, and uses it to initialize an EONotQualifier, `negQual`. The EONotQualifier `negQual` is then used to filter an in-memory array. The code excerpt returns an array of Guest objects whose __lastName__ properties do _not_ have the same value as the __lastName__ property of the guest's sponsoring member (this example is based on the Rentals sample database). In other words, the EONotQualifier `negQual` inverts the effects of `baseQual`.

> ```
> NSArray *guests;     /* Assume this exists. */
> EOQualifier *baseQual, *negQual;
>
> baseQual = [EOQualifier qualifierWithQualifierFormat:@"lastName =
>     member.lastName"];
> negQual = [[EONotQualifier alloc] initWithQualifier:baseQual];
> return [guests filteredArrayUsingQualifier:negQual];
> ```

---

#### qualifier

- (EOQualifier \*)`qualifier`

Returns the receiver's qualifier_._

---

[!](EOKeyValueQualifier-2.md)
[!](EONull.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
