---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOConditional.html
archived_at: '2026-07-15T07:55:23.854900Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOCheckBox.md)

## WOConditional

### Synopsis

__WOConditional__ __{__ __condition__=YES|NO__;__ [__negate__=YES|NO;] ... __};__

### Description

A WOConditional object controls whether a portion of the HTML page will be generated, based on the evaluation of its assigned condition.

**__condition__**
: Expression to evaluate. If the expression evaluates to YES (assuming __negate__ is NO), the HTML code controlled by the WOConditional object is emitted; otherwise it is not.

**__negate__**
: Inverts the sense of the condition. By default, __negate__ is assumed to be NO.

The negate attribute lets you use the same test to display mutually exclusive information; for example:

#### HTML file

```
<HTML>
<WEBOBJECTS NAME="PAYING_CUSTOMER">Thank you for your order!</WEBOBJECTS>
<WEBOBJECTS NAME="WINDOW_SHOPPER">Thanks for visiting!</WEBOBJECTS>
</HTML>
```


#### Declarations File

```
PAYING_CUSTOMER: WOConditional {condition=payingCustomer;};
WINDOW_SHOPPER: WOConditional {condition=payingCustomer; negate=YES;};
```


#### Script File

```
- payingCustomer {
    if (/* ordered something */) {
        return YES;
    }
    return NO;
}
```


### Examples

[Conditional display](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=ConditionalEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOEmbeddedObject.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
