---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOForm.html
archived_at: '2026-07-15T07:55:24.897684Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOEmbeddedObject.md)

## WOForm

### Synopsis

__WOForm__ __{__ [__action__=_aMethod___;__ | __href__=_aURL___;__] [__multipleSubmit__=YES|NO__;__] ... __};__

### Description

A WOForm is a container element that generates a fill-in form. It gathers the input from the input elements it contains and sends it to the server for processing. WOForm corresponds to the HTML element <FORM ... > ... </FORM>.

**__href__**
: URL specifying where the form will be submitted.

**__action__**
: Action method that's invoked when the form is submitted. If the form contains a dynamic element that has its own action (such as a WOSubmitButton or a WOActiveImage), that action is invoked instead of the WOForm's.

**__multipleSubmit__**
: If __multipleSubmit__ evaluates to YES, the form can have more than one WOSubmitButton, each with its own action. By default, WOForm supports only a single WOSubmitButton. __Note:__ Some older browsers support only a single submit button in a form.

### Examples

[Forms and input elements](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=FormEx1)

[Form with multiple submits](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=FormEx2)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOFrame.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
