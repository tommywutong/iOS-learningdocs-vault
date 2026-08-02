---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOString.html
archived_at: '2026-07-15T08:00:48.765476Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOString

---

# Synopsis

WOString { value=_aString_; [formatter=_formatterObj_;] [escapeHTML=YES|NO; ] [dateformat=_dateFormatString_;] [numberformat=_numberFormatString_;] ... };

---

# Description

A WOString represents itself in the HTML page as a dynamically generated string.

---

# Bindings

**---

### value

Text to display in the HTML page. value is typically assigned an NSString object, an object that responds to a description message by returning an NSString, or a method that returns an NSString. The NSString's contents are substituted into the HTML in the place occupied by this dynamic element.

**---

### escapeHTML

If escapeHTML is YES (the default), the string rendered by value is converted so that characters which would be interpretted as HTML control characters become their escaped equivalent. By default, WebObjects tries to ensure that data displays in the client browser just as it does in a normal editor. Thus, if a your value is "a <b>bold</b> idea", the string passed to the client browser would be "a <B>bold</B> idea", but it would display in the browser as "a <b>bold</b> idea". If escapeHTML is NO, WebObjects simply passes your data to the client browser "as is." In this case, the above example would display in the client browser as "a bold idea". If you are certain that your strings have no characters in them which might be interpretted as HTML control characters, you get better performance if you set escapeHTML to NO.

**---

### formatter

An instance of an NSFormatter subclass to be used to format object values for display as strings, and (in the case of NSTextField) format user entered strings back into object values. This attribute should specify a variable containing (or method returning) a preconfigured formatter object. For instance, a WOString might have the binding:******

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

If a user an "unformattable" value, WOString passes the invalid value through, allowing you to send back an error page that shows the invalid value.

**---

### dateformat

A format string that specifies how value should be formatted as a date. If a date format is used, value must be assigned an NSCalendarDate object. If value can't be interpreted according to the format you specify, value is set to nil. See the NSCalendarDate class specification for a description of the date format syntax.

**---

### numberformat

A format string that specifies how value should be formatted as a number. If a number format is used, value must be assigned an NSNumber object. If the element's value can't be interpreted according to the format you specify, value is set to nil. See the NSNumberFormatter class specification for a description of the number format syntax.****

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
