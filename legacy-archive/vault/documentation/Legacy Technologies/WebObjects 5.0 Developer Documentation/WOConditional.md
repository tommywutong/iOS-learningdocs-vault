---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOConditional.html
archived_at: '2026-07-15T08:14:38.930265Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOConditional

## Element Description

A WOConditional object controls whether a portion of the HTML
page will be generated, based on the evaluation of its assigned
condition.

## Synopsis

> ```
> WOConditional { condition=aBoolean; [negate=aBoolean;] ... };
> ```

## Bindings

**condition**
: If __condition__ evaluates to `YES` or `true`,
and assuming that __negate__ isn't in effect,
the HTML code controlled by the WOConditional object is emitted;
otherwise it is not.

**negate**
: Inverts the sense of the condition. By default, __negate__ is
assumed to be `false` or `NO`.

## Example

The negate attribute lets you use the same test to display
mutually exclusive information; for example:

## HTML file:

> ```
> <HTML>
> <WEBOBJECTS NAME="PAYING_CUSTOMER">Thank you for your order!</WEBOBJECTS>
> <WEBOBJECTS NAME="WINDOW_SHOPPER">Thanks for visiting!</WEBOBJECTS>
> </HTML>
> ```

## Declarations File:

> ```
> PAYING_CUSTOMER: WOConditional {condition=payingCustomer;};
> WINDOW_SHOPPER: WOConditional {condition=payingCustomer; negate=YES;};
> ```

## Script File:

> ```
> - payingCustomer {
>     if (/* ordered something */) {
>         return YES;
>     }
>     return NO;
> }
> ```

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
