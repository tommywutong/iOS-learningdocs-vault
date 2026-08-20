---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOText.html
archived_at: '2026-07-15T07:49:46.727891Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOSubmitButton.md)

---

# __WOText__

### Synopsis

__WOText {__ __value__=_`defaultValue`___;__ [__name__=_`fieldName`___;__] [__disabled__=YES|NO__;__] ... __};

### Description__

WOText generates a multi-line field for text input and display. It corresponds to the HTML element <TEXTAREA>.

**__value__**
: During page generation, __value__ specifies the text that is displayed in the text field. During request handling, __value__ contains the text as the user left it.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assigns one at runtime.

**__disabled__**
: If __disabled__ evaluates to YES, the text area appears in the page but no input is allowed.

### Examples

[Forms and input elements](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOTextField.md)
