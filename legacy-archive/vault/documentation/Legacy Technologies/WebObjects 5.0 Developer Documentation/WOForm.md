---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOForm.html
archived_at: '2026-07-15T08:14:38.972438Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOForm

## Element Description

A WOForm is a container element that generates a fill-in form.
It gathers the input from the input elements it contains and sends
it to the server for processing. WOForm corresponds to the HTML element `<FORM
... > ... </FORM>`.

## Synopsis

WOForm { [action=_aMethod_;
| href=_aURL_;] [multipleSubmit=_aBoolean_;]
... };

## Bindings

**href**
: URL specifying where the form will be submitted.

**action**
: Action method that's invoked when the form is submitted.
If the form contains a dynamic element that has its own action (such
as a [WOSubmitButton](WOSubmitButton.md#apple-ijduoqsbizeeg) or a [WOActiveImage](WOActiveImage.md#apple-ijdumqsdi5cue)), that action is invoked
instead of the WOForm's.

**multipleSubmit**
: If __multipleSubmit__ evaluates
to `true` (or `YES`),
the form can have more than one [WOSubmitButton](WOSubmitButton.md#apple-ijduoqsbizeeg), each with its own
action. By default, WOForm supports only a single [WOSubmitButton](WOSubmitButton.md#apple-ijduoqsbizeeg).

|  |
| --- |
| Some older browsers support only a single submit button in a form. |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
