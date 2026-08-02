---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOQualifierVariable.html
archived_at: '2026-07-15T08:13:47.328869Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

# EOQualifierVariable

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : NSCoding: EOKeyValueArchiving: Serializable

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EOQualifierVariable defines objects that serve as placeholders in the qualifier. When you create a qualifier programmatically, you typically do something like this:

> ```
> aQual = [EOQualifier qualifierWithQualifierFormat:"dateReleased = %@", aDate];
> ```

where _aDate_ is a variable that contains the actual date you want to query upon. When you store the qualifier in an EOModel, there is no way to know the actual value to query upon or the variable that will contain that value. The EOQualifierVariable object acts as a placeholder for the actual variable that will represent the right side of the expression. You specify an EOQualifierVariable by using a $, as in the following:

> ```
> dateReleased = $aDate
> ```

Variable values must be substituted for using qualifierWithBindings.

## Interfaces Implemented

---

> : NSCoding: [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4swmfzgsylcnrss6y3mmfzxgrtpojbw6zdfoi): [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzfmylsnfqwe3dff5sgky3pmrsu6ytkmvrxi): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4swmfzgsylcnrss6zlomnxwizkxnf2gqq3pmrsxe): : EOKeyValueArchiving: [decodeWithKeyValueUnarchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6ulvmfwgsztjmvzfmylsnfqwe3dff5sgky3pmrsvo2lunbfwk6kwmfwhkzkvnzqxey3inf3gk4q): [encodeWithKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkf2wc3djmzuwk4swmfzgsylcnrss6zlomnxwizkxnf2gqs3fpflgc3dvmvaxey3inf3gk4q):

## Constructors

---

### __EOQualifierVariable__

`public EOQualifierVariable(String key)`

Creates and returns a new EOQualifierVariable object with the specified name. For example, if your qualifier is "dateReleased = $aDate", then this method would be invoked with the key "aDate".

---

## Static Methods

---

### decodeObject

`public static Object decodeObject(NSCoder coder)`

Conformance to NSCoding.

---

### decodeWithKeyValueUnarchiver

`public static Object decodeWithKeyValueUnarchiver(EOKeyValueUnarchiver unarchiver)`

Conformance to EOKeyValueArchiving.

---

## Instance Methods

---

### classForCoder

`public Class classForCoder()`

Conformance to NSCoding.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder coder)`

Conformance to NSCoding.

---

### encodeWithKeyValueArchiver

`public void encodeWithKeyValueArchiver(EOKeyValueArchiver archiver)`

Conformance to EOKeyValueArchiving.

---

### key

`public String key()`

Returns the key of the variable qualifier.

---

### __toString__

`public String toString()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
