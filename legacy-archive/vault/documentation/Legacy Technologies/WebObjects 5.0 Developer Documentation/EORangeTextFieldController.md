---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOGenerationRef/Java/eogeneration.client/Classes/EORangeTextFieldControlle.html
archived_at: '2026-07-15T08:13:50.826661Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration.client/Art/up.gif)](../../WebObjectsTOC.md)

# EORangeTextFieldController

> **__Inherits from:__**
> : [EORangeValueController](EORangeValueController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhveylom5svmylmovsug33oorzg63dmmvza): [EORangeWidgetController](EORangeWidgetController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhveylom5svo2lem5sxiq3pnz2he33mnrsxe): [EOWidgetController](EOWidgetController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvo2lem5sxiq3pnz2he33mnrsxe): EOComponentController (eoapplication) : [EOController (eoapplication)](EOController-2.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza): Object

> **__Implements:__**
> : EOWidgetController.FormatWidget: EOWidgetController.QueryWidget

> **__Package:__**
> : com.webobjects.eogeneration.client

---

## Class Description

---

Documentation for this class is forthcoming. For information on using this class, see the book _Getting Started with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| `RANGETEXTFIELDCONTROLLER` | `widgetController` |

## Method Types

---

> **All methods**
> : [EORangeTextFieldController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpivhveylom5svizlyordgszlmmrbw63tuojxwy3dfoi): [formatClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpmzxxe3lborbwyyltom): [formatForMaximumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpmzxxe3lbordg64snmf4gs3lvnvaxg43pmnuwc5djn5xa): [formatForMinimumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpmzxxe3lbordg64snnfxgs3lvnvaxg43pmnuwc5djn5xa): [formatPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpmzxxe3lborigc5dumvzg4): [isFormatAllowed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpnfzum33snvqxiqlmnrxxozle): [isQueryWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpnfzvc5lfoj4vo2lem5sxi): [newMaximumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpnzsxotlbpbuw25lnifzxg33dnfqxi2lpny): [newMinimumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpnzsxotljnzuw25lnifzxg33dnfqxi2lpny): [newWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpnzsxov3jmrtwk5a): [preferredUsesLabelComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpobzgkztfojzgkzcvonsxgtdbmjswyq3pnvyg63tfnz2a): [setAlignmentForWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rponsxiqlmnftw43lfnz2em33sk5uwiz3foq): [setFormatAllowed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rponsxirtpojwwc5cbnrwg653fmq): [setFormatClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rponsxirtpojwwc5cdnrqxg4y): [setFormatPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rponsxirtpojwwc5cqmf2hizlsny): [setIsQueryWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rponsxisltkf2wk4tzk5uwiz3foq)

## Constructors

---

### EORangeTextFieldController

`public EORangeTextFieldController(com.webobjects.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

Description forthcoming.

---

## Instance Methods

---

### formatClass

`public Class formatClass()`

Description forthcoming.

---

### formatForMaximumAssociation

`protected java.text.Format formatForMaximumAssociation()`

Description forthcoming.

---

### formatForMinimumAssociation

`protected java.text.Format formatForMinimumAssociation()`

Description forthcoming.

---

### formatPattern

`public String formatPattern()`

Description forthcoming.

---

### isFormatAllowed

`public boolean isFormatAllowed()`

Description forthcoming.

---

### isQueryWidget

`public boolean isQueryWidget()`

Description forthcoming.

---

### newMaximumAssociation

`protected com.webobjects.eointerface.EOAssociation newMaximumAssociation( javax.swing.JComponent aJComponent, com.webobjects.eointerface.EODisplayGroup anEODisplayGroup, String aString, com.webobjects.eointerface.EODisplayGroup anEODisplayGroup)`

Description forthcoming.

---

### newMinimumAssociation

`protected com.webobjects.eointerface.EOAssociation newMinimumAssociation( javax.swing.JComponent aJComponent, com.webobjects.eointerface.EODisplayGroup anEODisplayGroup, String aString, com.webobjects.eointerface.EODisplayGroup anEODisplayGroup)`

Description forthcoming.

---

### newWidget

`protected javax.swing.JComponent newWidget()`

Description forthcoming.

---

### preferredUsesLabelComponent

`protected boolean preferredUsesLabelComponent()`

Description forthcoming.

---

### setAlignmentForWidget

`protected void setAlignmentForWidget( javax.swing.JComponent aJComponent, int anInt)`

Description forthcoming.

---

### setFormatAllowed

`public void setFormatAllowed(boolean aBoolean)`

Description forthcoming.

---

### setFormatClass

`public void setFormatClass(Class aClass)`

Description forthcoming.

---

### setFormatPattern

`public void setFormatPattern(String aString)`

Description forthcoming.

---

### setIsQueryWidget

`public void setIsQueryWidget(boolean aBoolean)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration.client/Art/up.gif)](../../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
