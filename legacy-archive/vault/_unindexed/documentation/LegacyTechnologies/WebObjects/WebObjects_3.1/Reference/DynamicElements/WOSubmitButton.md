---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOSubmitButton.html
archived_at: '2026-07-15T07:49:46.205937Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOString.md)

---

# __WOSubmitButton__

### Synopsis

__WOSubmitButton__ __{__ __action__=_`submitForm`___;__ __value__=_`aString`___;__ [__disabled__=YES|NO__;__] [__name__=_`aName`___;__] ... __};

### Description__

A WOSubmitButton element generates a submit button in an HTML page. This element is used within HTML forms.

**__action__**
: Action method to invoke when the form is submitted.

**__value__**
: Title of the button.

**__disabled__**
: If __disabled__ evaluates to YES, the element appears in the page but is not active.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assigns one at runtime.

### Examples

[Forms and input elements](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOText.md)
