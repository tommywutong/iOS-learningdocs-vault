---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WORadioButton.html
archived_at: '2026-07-15T08:09:53.456210Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

# WORadioButton

## Element Description

WORadioButton represents itself as an on-off switch. Radio
buttons are normally grouped, since the most important aspect of
their behavior is that they allow the user to select no more than
one of several choices. If the user selects one button, the previously
selected button (if any) becomes deselected.

Since radio buttons normally appear as a group, WORadioButton
is commonly found within a [WORepetition](WORepetition.md#apple-infemrkhincus).
Alternatively, you can use the [WORadioButtonList](WORadioButtonList.md#apple-irausr2civauc) element.

## Synopsis

WORadioButton {value=_defaultValue_;
[selection=_selectedValue_;] [name=_fieldName_;] [disabled=_aBoolean_;]
... };
WORadioButton {checked=_aBoolean_;
[name=_fieldName_;] [disabled=_aBoolean_;]
... };

## Bindings

|  |
| --- |
| in a WORadioButton declaration you must supply either __checked__ or __value__, but not both: they are mutually exclusive. |

**value**
: Value of this input element. If not specified, WebObjects
provides a default value.

**selection**
: If __selection__ and __value__ are
equal when the page is generated, the radio button is selected. When
the page is submitted, __selection__ is assigned
the value of the radio button.

**checked**
: During page generation, if __checked__ evaluates
to `true` (or `YES`),
the radio button appears in the selected state. During request handling, __checked__ reflects
the state the user left the radio button in: `true` (or `YES`)
if checked; `false` (or `NO`)
if not.

**name**
: Name that identifies the radio button's group. Only
one radio button at a time can be selected within a group.

**disabled**
: If __disabled__ evaluates to `true` (or `YES`),
this element appears in the page but is not active. That is, __selection__ does
not contain the user's selection when the page is submitted.

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
