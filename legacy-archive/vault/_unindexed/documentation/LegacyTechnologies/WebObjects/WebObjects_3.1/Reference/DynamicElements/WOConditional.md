---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOConditional.html
archived_at: '2026-07-15T07:49:37.675383Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOCheckBox.md)

---

# __WOConditional__

### Synopsis

__WOConditional__ __{__ __condition__=YES|NO__;__ [__negate__=YES|NO;] ... __};

### Description__

A WOConditional object controls whether a portion of the HTML page will be generated, based on the evaluation of its assigned condition.

**__condition__**
: Expression to evaluate. If the expression evaluates to YES (assuming __negate__ is NO), the HTML code controlled by the WOConditional object is emitted; otherwise it is not.

**__negate__**
: Inverts the sense of the condition. By default, __negate__ is assumed to be NO.

The negate attribute lets you use the same test to display mutually exclusive information; for example:

#### __HTML file__

```
<HTML>
<WEBOBJECTS NAME="PAYING_CUSTOMER">Thank you for your order!</WEBOBJECTS>
<WEBOBJECTS NAME="WINDOW_SHOPPER">Thanks for visiting!</WEBOBJECTS>
</HTML>
```

#### __Declarations File__

```
PAYING_CUSTOMER: WOConditional {condition=payingCustomer;};
WINDOW_SHOPPER: WOConditional {condition=payingCustomer; negate=YES;};
```

#### __Script File__

```
- payingCustomer {
```

```
  if (/* ordered something */) {
```

```
    return YES;
```

```
  }
```

```
  return NO;
```

```
}
```

### Examples

[Conditional display](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=ConditionalEx1)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOEmbeddedObject.md)
