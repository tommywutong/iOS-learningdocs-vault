---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOForm.html
archived_at: '2026-07-15T08:09:52.451311Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

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

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
