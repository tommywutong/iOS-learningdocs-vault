---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOForm.html
archived_at: '2026-07-15T07:49:38.679349Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOEmbeddedObject.md)

---

# __WOForm__

### Synopsis

__WOForm__ __{__ [__action__=_`aMethod`___;__ | __href__=_`aURL`___;__] [__multipleSubmit__=YES|NO__;__] ... __};

### Description__

A WOForm is a container element that generates a fill-in form. It gathers the input from the input elements it contains and sends it to the server for processing. WOForm corresponds to the HTML element <FORM ... > ... </FORM>.

**__href__**
: URL specifying where the form will be submitted.

**__action__**
: Action method that's invoked when the form is submitted. If the form contains a dynamic element that has its own action (such as a WOSubmitButton or a WOActiveImage), that action is invoked instead of the WOForm's.

**__multipleSubmit__**
: If __multipleSubmit__ evaluates to YES, the form can have more than one WOSubmitButton, each with its own action. By default, WOForm supports only a single WOSubmitButton. __Note:__ Some older browsers support only a single submit button in a form.

### Examples

[Forms and input elements](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=FormEx1)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOFrame.md)
