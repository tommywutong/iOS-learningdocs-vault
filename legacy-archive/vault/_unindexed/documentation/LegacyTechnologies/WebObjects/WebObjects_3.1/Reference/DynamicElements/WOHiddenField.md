---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOHiddenField.html
archived_at: '2026-07-15T07:49:40.686749Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOGenericElement.md)

---

# __WOHiddenField__

### Synopsis

__WOHiddenField__ __{__ __value__=_`defaultValue`___;__ [ __name__=_`fieldName`___;__] [__disabled__=YES|NO__;__] ... __};

### Description__

A WOHiddenField adds hidden text to the HTML page. It corresponds to the HTML element <INPUT TYPE="HIDDEN"...>. Hidden fields are sometimes used to store application state data in the HTML page. In WebObjects, the WOStateStorage element is designed expressly for this purpose.

**__value__**
: Value for the hidden text field.

**__name__**
: Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**__disabled__**
: If disabled evaluates to YES, the element appears in the page but is not active.

### Examples

[Forms and input elements](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOHyperlink.md)
