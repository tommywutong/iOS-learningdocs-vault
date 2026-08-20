---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOConditional.html
archived_at: '2026-07-15T08:00:35.601209Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOConditional

---

# Synopsis

WOConditional { condition=YES|NO; [negate=YES|NO;] ... };

---

# Description

A WOConditional object controls whether a portion of the HTML page will be generated, based on the evaluation of its assigned condition.

---

# Bindings

**---

### condition

Expression to evaluate. If the expression evaluates to YES (assuming negate is NO), the HTML code controlled by the WOConditional object is emitted; otherwise it is not.

**---

### negate

Inverts the sense of the condition. By default, negate is assumed to be NO.****

---

# Example

 The negate attribute lets you use the same test to display mutually exclusive information; for example:

---

## HTML file

> ```
> <HTML>
> ```

> ```
> <WEBOBJECTS NAME="PAYING_CUSTOMER">Thank you for your order!</WEBOBJECTS>
> ```

> ```
> <WEBOBJECTS NAME="WINDOW_SHOPPER">Thanks for visiting!</WEBOBJECTS>
> ```

> ```
> </HTML>
> ```

---

## Declarations File

> ```
> PAYING_CUSTOMER: WOConditional {condition=payingCustomer;};
> ```

> ```
> WINDOW_SHOPPER: WOConditional {condition=payingCustomer; negate=YES;};
> ```

---

## Script File

> ```
> - payingCustomer {
> ```

> ```
> 	if (/* ordered something */) {
> ```

> ```
> 		return YES;
> ```

> ```
> 	}
> ```

> ```
> 	return NO;
> ```

> ```
> }
> ```

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
