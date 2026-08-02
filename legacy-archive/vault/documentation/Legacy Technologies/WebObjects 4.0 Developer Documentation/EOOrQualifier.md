---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOOrQualifier.html
archived_at: '2026-07-18T01:28:27.117227Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOObserverProxy.md)
[!](EOQualifier.md)

---

# EOOrQualifier

__Inherits From:__
EOQualifier

__Implements:__
EOQualifierEvaluation
NSCoding (Java Client only)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

EOOrQualifier is a subclass of EOQualifier that contains multiple qualifiers. EOOrQualifier implements the EOQualifierEvaluation interface, which defines the method [__evaluateWithObject__](EOQualifierEvaluation.md)for in-memory evaluation. When an EOOrQualifier object receives an [__evaluateWithObject__](EOQualifierEvaluation.md)message, it evaluates each of its qualifiers until one of them returns true. If one of its qualifiers returns true, the EOOrQualifier object returns true immediately. If all of its qualifiers return false, the EOOrQualifier object returns false.

## Interfaces Implemented

**EOQualifierEvaluation**

**[- evaluateWithObject](EOQualifierEvaluation.md)**

**NSCoding (Java Client only)**

**classForCoder

**encodeWithCoder****

## Constructors

---

#### EOOrQualifier

public __EOOrQualifier__ (NSArray _qualifiers_)

Creates and returns a new EOOrQualifier.

If qualifiers is specified, the EOOrQualifier is initialized with the qualifiers in _qualifiers_.

## Instance Methods

---

#### evaluateWithObject:

EOQualifierEvaluation interface

public boolean __evaluateWithObject__ (java.lang.Object _anObject_)

Returns __true__ if _anObject_ satisfies the qualifier, __false__ otherwise. When an EOOrQualifier object receives an `evaluateWithObject` message, it evaluates each of its qualifiers until one of them returns __true__ . If any of its qualifiers returns __true__ , the EOOrQualifier object returns __true__ immediately. If all of its qualifiers return __false__ , the EOOrQualifier object returns __false__ . This method can throw one of several possible exceptions if an error occurs. If your application allows users to construct arbitrary qualifiers (such as through a user interface), you may want to write code to catch any exceptions and respond to errors (for example, by displaying a panel saying that the user typed a poorly formed qualifier).

---

#### qualifiers

NSArray __qualifiers__ ()

**Returns the receiver's qualifiers.**

---

[!](EOObserverProxy.md)
[!](EOQualifier.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
