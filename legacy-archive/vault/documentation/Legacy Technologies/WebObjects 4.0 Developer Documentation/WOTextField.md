---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOTextField.html
archived_at: '2026-07-15T08:00:50.852413Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOTextField

---

# Synopsis

WOTextField { value=_aValue_; [formatter=_formatterObj_;] [dateformat=_dateFormatString_;] [numberformat=_numberFormatString_;] [name=_fieldName_;] [disabled=YES|NO;] ... };

---

# Description

A WOTextField represents itself as a text input field. It corresponds to the HTML element <INPUT TYPE="TEXT"...>.

---

# Bindings

**---

### value

During page generation, value sets the default value displayed in the single-line text field. During request handling, it holds the value the user entered into the field, or the default value if the user left the field untouched.

**---

### formatter

An instance of an NSFormatter subclass to be used to format object values for display as strings, and (in the case of NSTextField) format user entered strings back into object values. This attribute should specify a variable containing (or method returning) a preconfigured formatter object. For instance, a WOTextField might have the binding:****

> ```
> 	formatter = application.dateFormatter
> ```

With the following code:

> ```
>         // Application.wos
> ```

> ```
>         NSFormatter *_dateFormatter;
> ```

> ```
>
> ```

> ```
>         - (NSFormatter *)dateFormatter {
> ```

> ```
>             if (!_dateFormatter) {
> ```

> ```
>                 _dateFormatter = [[NSDateFormatter alloc]                       initWithDateFormat:@"%m/%d/%Y" allowNaturalLanguage:NO];
> ```

> ```
>             }
> ```

> ```
>             return _dateFormatter;
> ```

> ```
>         }
> ```

If a user an "unformattable" value, WOTextField passes the invalid value through, allowing you to send back an error page that shows the invalid value.

**---

### dateformat

A format string that specifies how value should be formatted as a date. If a date format is used, value must be assigned an NSCalendarDate object. If value can't be interpreted according to the format you specify, value is set to nil. See the NSCalendarDate class specification for a description of the date format syntax.

**---

### numberformat

A format string that specifies how value should be formatted as a number. If a number format is used, value must be assigned an NSNumber object. If the element's value can't be interpreted according to the format you specify, value is set to nil. See the NSNumberFormatter class specification for a description of the number format syntax.

**---

### name

Name that uniquely identifies this element within the form. You may specify a name or let WebObjects automatically assign one at runtime.

**---

### disabled

If disabled evaluates to YES, the element appears in the page but is not active. That is, value does not contain the user's input when the page is submitted.********

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
