---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WOCookie.html
archived_at: '2026-07-15T08:15:15.442831Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOCookie

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

WOCookie is used for the creation and setting of cookies in your response objects. A cookie allows for the persistent storage of client state. Instead of using a WOSession object (which can potentially have a shorter life span), a cookie allows server-side applications to store state in client browsers for a specific or indeterminate amount of time. An advantage to cookies is that the data will be stored on the client and not on the server, allowing the server to maintain less state information. A specific advantage in WebObjects applications is that cookies allow the server to put state into the browser that is not bound to a session. Hence, the client can "leave" your application and return with its cookie's state intact.

A WOCookie object defines a cookie that can be added to the HTTP header for your response. You create a cookie using the static method [cookieWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pn5vwszjpmnxw623jmvlws5dijzqw2zi).

To add or remove cookies from the response, use the WOMessage methods addCookie and removeCookie. To retrieve cookie data, use the WORequest methods cookieValues, cookieValueForKey, and cookieValuesForKey. WORequest returns the data as name/value pairs and not as WOCookie objects, since browsers don't return the additional data WOCookies provide, such as path name and expiration date.

For more information about cookies and their implementation details, see Netscape's preliminary specification at __http://www.netscape.com/newsref/std/cookie_spec.html__ and RFC 2109 - HTTP State Management Mechanism at __http://www.cis.ohio-state.edu/htbin/rfc/rfc2109.html__.

If and when new details evolve in the implementation of cookies, you can subclass WOCookie and implement new behaviors. Pay particular attention to how you override [headerString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxwqzlbmrsxeu3uojuw4zy), which WOResponse uses to fill the HTTP response with a header string.

## Method Types

---

> **Constructors**
> : [WOCookie](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxvot2dn5xww2lf)
>
> **Creation**
> : [cookieWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pn5vwszjpmnxw623jmvlws5dijzqw2zi)
>
> **Obtaining a cookie's attributes**
> : [domain](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxwi33nmfuw4): [expires](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxwk6dqnfzgk4y): [headerString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxwqzlbmrsxeu3uojuw4zy): [isSecure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxws42tmvrxk4tf): [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxw4ylnmu): [path](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxayluna): [value](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxmylmovsq)
>
> **Setting a cookie's attributes**
> : [setDomain](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxgzluirxw2yljny): [setExpires](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxgzluiv4ha2lsmvzq): [setIsSecure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxgzlujfzvgzldovzgk): [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxgzlujzqw2zi): [setPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxgzlukbqxi2a): [setValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxgzlukzqwy5lf)

## Constructors

---

### WOCookie

`public WOCookie ( String aName, String aValue, String aPath, String aDomain, NSTimestamp aDate, boolean isSecure)`

This method is deprecated. Do not use it.

`public WOCookie ( String aName String aValue String aPath String aDomain int timeout boolean isSecure)`

This constructor initializes a newly-instantiated WOCookie with a name, value, path, domain, date, and a security flag.

`public WOCookie( String aName, String aValue)`

This constructor initializes a newly-instantiated WOCookie with just a name and its value.

A note on time out periods: time out periods are in seconds; a negative time out period indicates no time out; a time out of zero indicates expiration of all cookies with the given name.

__See Also:__ [cookieWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pn5vwszjpmnxw623jmvlws5dijzqw2zi), [setDomain](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxgzluirxw2yljny), [setExpires](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxgzluiv4ha2lsmvzq), [setIsSecure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxgzlujfzvgzldovzgk), [setName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxgzlujzqw2zi), [setPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxgzlukbqxi2a), [setValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxgzlukzqwy5lf)

---

## Static Methods

---

### cookieWithName

`public WOCookie ( String aName, String aValue, String aPath, String aDomain, NSTimestamp aDate, boolean isSecure)`

This method is deprecated. Do not use it.

`public static WOCookie cookieWithName( String aName, String aValue)`

Creates and returns a cookie with just a name and its value. This method sets the path attribute to your application's path.

`public static WOCookie cookieWithName ( String aName String aValue String aPath String aDomain int timeout boolean isSecure)`

Creates and returns a cookie, specifying all its attributes. For more information, see the descriptions of the methods that return attribute values.

A note on time out periods: time out periods are in seconds; a negative time out period indicates no time out; a time out of zero indicates expiration of all cookies with the given name.

__See Also:__ [domain](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxwi33nmfuw4), [expires](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxwk6dqnfzgk4y), [isSecure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxws42tmvrxk4tf), [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxw4ylnmu), [path](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxayluna), [value](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxmylmovsq)

---

## Instance Methods

---

### domain

`public String domain()`

Returns the value of the cookie's "domain" attribute. It's of the form "companyname.com".

---

### expires

`public NSTimestamp expires()`

This method is deprecated. Do not use it.

---

### headerString

`public String headerString()`

Returns the string that will be used in the HTTP header. The returned string has the format:

Set-cookie: name=_value_; expires=_date_; path=_path_; domain=_domain_; secure;

The calendar format for the expiration date is:

> ```
> @"%A, %d-%b-%Y %H:%M:%S GMT"
> ```

where all times are converted relative to Greenwich Mean Time.

This method is called by WOResponse when generating the response.

---

### isSecure

`public boolean isSecure()`

Returns the cookie's "secure" attribute. This attribute specifies whether the cookie should be transmitted only with secure HTTP. The default value is false.

---

### name

`public String name()`

Returns the cookie's "name" attribute. The name is similar to the key of a dictionary or hash table. Together, the name and value form the cookie's data.

---

### path

`public String path()`

Returns the value of the cookie's "path" attribute. Cookies for a specific path are sent only when accessing URLs within that path. For more information on cookies and their paths, see Netscape's preliminary specification at __http://www.netscape.com/newsref/std/cookie_spec.html__ and RFC 2109 - HTTP State Management Mechanism at __http://www.cis.ohio-state.edu/htbin/rfc/rfc2109.html__.

---

### setDomain

`public void setDomain(String aDomain)`

Sets the cookie's "domain" attribute to _aDomain_. For more information, see [domain](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxwi33nmfuw4).

__See Also:__ [cookieWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pn5vwszjpmnxw623jmvlws5dijzqw2zi)

---

### setExpires

`public void setExpires(NSTimestamp expirationDate)`

This method is deprecated. Do not use it.

---

### setIsSecure

`public void setIsSecure(boolean flag)`

Sets the cookie's "secure" attribute to _flag_. For more information, see [isSecure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxws42tmvrxk4tf)..

__See Also:__ [cookieWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pn5vwszjpmnxw623jmvlws5dijzqw2zi)

---

### setName

`public void setName(String aName)`

Sets the cookie's "name" attribute to _aName_. For more information, see [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxw4ylnmu)..

__See Also:__ [cookieWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pn5vwszjpmnxw623jmvlws5dijzqw2zi)

---

### setPath

`public void setPath(String aPath)`

Sets the cookie's "path" attribute to _aPath_. For more information, see [path](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxayluna)..

__See Also:__ [cookieWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pn5vwszjpmnxw623jmvlws5dijzqw2zi)

---

### setTimeOut

`public void setTimeOut(int timeOut)`

Description forthcoming.

---

### setValue

`public void setValue(String aValue)`

Sets the cookie's "value" attribute to _aValue_. For more information, see [value](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw623jmuxxmylmovsq)..

__See Also:__ [cookieWithName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6q3pn5vwszjpmnxw623jmvlws5dijzqw2zi)

---

### timeOut

`public int timeOut()`

Description forthcoming.

---

### __toString__

`public String toString()`

Returns a String containing a string representation of the receiver.

---

### value

`public String value()`

Returns the value of the cookie's value attribute. This attribute is similar to the value of a dictionary or hash table. Together, the name and value form the cookie's data.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
