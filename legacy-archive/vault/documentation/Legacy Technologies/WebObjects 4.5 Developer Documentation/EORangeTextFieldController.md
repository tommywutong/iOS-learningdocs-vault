---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EORangeTextFieldControllr.html
archived_at: '2026-07-15T08:11:43.955810Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOGeneration Reference

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

# EORangeTextFieldController

> **__Inherits
> from:__**
> : [EORangeValueController](EORangeValueController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhveylom5svmylmovsug33oorzg63dmmvza) : [EORangeWidgetController](EORangeWidgetController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhveylom5svo2lem5sxiq3pnz2he33mnrsxe) : [EOWidgetController](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOWidgetController.html#//apple_ref/java/cl/EOWidgetController) :
> EOComponentController (eoapplication) :
> EOController (eoapplication) :
> Object

> **__Implements:__**
> : EOWidgetController.FormatWidget
> : EOWidgetController.QueryWidget

> **__Package:__**
> : com.apple.client.eogeneration

---

## Class Description

---

Documentation for this class is forthcoming.
For information on using this class, see the book _Getting Started
with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| `RANGETEXTFIELDCONTROLLER` | `widgetController` |

## Method Types

---

> **All methods**
> : [EORangeTextFieldController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpivhveylom5svizlyordgszlmmrbw63tuojxwy3dfoi)
> : [formatClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpmzxxe3lborbwyyltom)
> : [formatForMaximumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpmzxxe3lbordg64snmf4gs3lvnvaxg43pmnuwc5djn5xa)
> : [formatForMinimumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpmzxxe3lbordg64snnfxgs3lvnvaxg43pmnuwc5djn5xa)
> : [formatPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpmzxxe3lborigc5dumvzg4)
> : [isFormatAllowed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpnfzum33snvqxiqlmnrxxozle)
> : [isQueryWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpnfzvc5lfoj4vo2lem5sxi)
> : [newMaximumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpnzsxotlbpbuw25lnifzxg33dnfqxi2lpny)
> : [newMinimumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpnzsxotljnzuw25lnifzxg33dnfqxi2lpny)
> : [newWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpnzsxov3jmrtwk5a)
> : [preferredUsesLabelComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rpobzgkztfojzgkzcvonsxgtdbmjswyq3pnvyg63tfnz2a)
> : [setAlignmentForWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rponsxiqlmnftw43lfnz2em33sk5uwiz3foq)
> : [setFormatAllowed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rponsxirtpojwwc5cbnrwg653fmq)
> : [setFormatClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rponsxirtpojwwc5cdnrqxg4y)
> : [setFormatPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rponsxirtpojwwc5cqmf2hizlsny)
> : [setIsQueryWidget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkrsxq5cgnfswyzcdn5xhi4tpnrwgk4rponsxisltkf2wk4tzk5uwiz3foq)

## Constructors

---

### EORangeTextFieldController

`public EORangeTextFieldController(com.apple.client.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

---

## Instance Methods

---

### formatClass

`public Class formatClass()`

---

### formatForMaximumAssociation

`protected java.text.Format formatForMaximumAssociation()`

---

### formatForMinimumAssociation

`protected java.text.Format formatForMinimumAssociation()`

---

### formatPattern

`public String formatPattern()`

---

### isFormatAllowed

`public boolean isFormatAllowed()`

---

### isQueryWidget

`public boolean isQueryWidget()`

---

### newMaximumAssociation

`protected com.apple.client.eointerface.EOAssociation newMaximumAssociation(
javax.swing.JComponent aJComponent,
com.apple.client.eointerface.EODisplayGroup anEODisplayGroup,
String aString,
com.apple.client.eointerface.EODisplayGroup anEODisplayGroup)`

---

### newMinimumAssociation

`protected com.apple.client.eointerface.EOAssociation newMinimumAssociation(
javax.swing.JComponent aJComponent,
com.apple.client.eointerface.EODisplayGroup anEODisplayGroup,
String aString,
com.apple.client.eointerface.EODisplayGroup anEODisplayGroup)`

---

### newWidget

`protected javax.swing.JComponent newWidget()`

---

### preferredUsesLabelComponent

`protected boolean preferredUsesLabelComponent()`

---

### setAlignmentForWidget

`protected void setAlignmentForWidget(
javax.swing.JComponent aJComponent,
int anInt)`

---

### setFormatAllowed

`public void setFormatAllowed(boolean aBoolean)`

---

### setFormatClass

`public void setFormatClass(Class aClass)`

---

### setFormatPattern

`public void setFormatPattern(String aString)`

---

### setIsQueryWidget

`public void setIsQueryWidget(boolean aBoolean)`

---

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

__DRAFT__
