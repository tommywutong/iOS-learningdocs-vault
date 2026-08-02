---
title: Properties versus methods in automatically generated 'aete' resources
apple_id: DTS10001389
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-17'
source_url: https://developer.apple.com/library/archive/qa/java/java14.html
archived_at: '2026-07-18T02:29:41.638514Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA14Properties versus methods in automatically generated 'aete' resources |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ---   Q: I am using AppleScript for Java and I have a routine that shows up as a property instead of a method in the automatically generated `'aete'` resource.  My method:   |  | | --- | | ``` public void setDictionaryName( String name ){...} ``` |   Shows up in the AppleScript dictionary as:   |  | | --- | | ``` Properties: <Inheritance> Object [r/o] dictionary name string -- public void foo.setDictionaryName(String) ``` |   I was expecting the dictionary to look like this:   |  | | --- | | ``` MyClass: setDictionaryName: public voidfoo.setDictionaryName(String) setDictionaryName reference parameters string ``` |   Why is this happening?  A: If you have a method that uses the standard Java bean syntax for property accessor routines (i.e., methods that are in the format `setX()`, `getX()`, or `isX()` where X is a property name), the introspector will assume that the routines are class properties.  The method you declared looks like a routine for setting the value of the `dictionaryName` property, so it is interpreted as a property accessor function. As a result, the default behavior for the automatic terminology generator creates an entry in the dictionary in the property format instead of a method format.  This behavior may actually be preferred since it is a lot easier to script an application as:   |  | | --- | | ``` set dictionary name of foo 1 to "English Language" ``` |   compared to:   |  | | --- | | ``` setDictionaryName of foo 1 parameters { "English Language" } ``` |    [May 17 1999] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
