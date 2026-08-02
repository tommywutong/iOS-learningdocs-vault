---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/EOQualifierEvaluation.html
archived_at: '2026-07-15T08:13:48.186838Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOQualifierEvaluation

> __Implemented by:__ : EOAndQualifier: EOKeyComparisonQualifier: EOKeyValueQualifier: EONotQualifier: EOOrQualifier:

> **__Package:__**
> : com.webobjects.eocontrol

---

## Interface Description

---

The EOQualifierEvaluation interface defines a method, [evaluateWithObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkf2wc3djmzuwk4sfozqwy5lboruw63rpmv3gc3dvmf2gkv3jorue6ytkmvrxi), that performs in-memory evaluation of qualifiers. All qualifier classes whose objects can be evaluated in memory must implement this interface.

## Instance Methods

---

### evaluateWithObject

`public abstract boolean evaluateWithObject(NSKeyValueCodingAdditions object)`

Returns true if the argument _object_ satisfies the qualifier, false otherwise. This method can throw one of several possible exceptions if an error occurs, depending on the implementation.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
