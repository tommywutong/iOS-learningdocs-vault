---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOAndQualifier.html
archived_at: '2026-07-18T01:28:24.412743Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOArrayDataSource.md)
[!](EOClassDescription.md)

---

# EOAndQualifier

__Inherits From:__
Object (Java Client)
NSObject (Yellow Box)

__Implements:__
EOQualifierEvaluation
NSCoding (Java Client only)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

EOAndQualifier is a subclass of EOQualifier that contains multiple qualifiers. EOAndQualifier implements the EOQualifierEvaluation interface, which defines the method __evaluateWithObject__ for in-memory evaluation. When an EOAndQualifier object receives an __evaluateWithObject__ message, it evaluates each of its qualifiers until one of them returns __false__ . If one of its qualifiers returns __false__ , the EOAndQualifier object returns __false__ immediately. If all of its qualifiers return __true__ , the EOAndQualifier object returns __true__ .

## Interfaces Implemented

**EOQualifierEvaluation**

**[- evaluateWithObject](EOQualifierEvaluation.md)**

**NSCoding (Java Client only)**

**classForCoder

**encodeWithCoder****

## Constructors

---

#### EOAndQualifier

public __EOAndQualifier__ (NSArray _qualifiers_)

Creates a new EOAndQualifier. If _qualifiers_ is provided, the new EOAndQualifier is initialized with the EOQualifier objects in _qualifiers_.

## Instance Methods

---

#### evaluateWithObject

EOQualifierEvaluation Interface

Java Client:

public boolean __evaluateWithObject__ (EOKeyValueCodingAdditions _anObject_)

Yellow Box:

public boolean __evaluateWithObject__ (java.lang.Object _anObject_)

Returns __true__ if _anObject_ satisfies the qualifier, __false__ otherwise. When an EOAndQualifier object receives an [__evaluateWithObject__](EOQualifierEvaluation.md)message, it evaluates each of its qualifiers until one of them returns __false__ . If any of its qualifiers returns __false__ , the EOAndQualifier object returns __false__ immediately. If all of its qualifiers return __true__ , the object returns __true__ . This method can throw one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and properly respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

#### qualifiers

public NSArray __qualifiers__ ()

Returns the receiver's qualifiers.

---

[!](EOArrayDataSource.md)
[!](EOClassDescription.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
