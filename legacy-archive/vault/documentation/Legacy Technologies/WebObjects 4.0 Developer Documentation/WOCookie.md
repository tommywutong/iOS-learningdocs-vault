---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WOCookie.html
archived_at: '2026-07-18T01:28:51.371492Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WOContext.md)
[!](WODirectAction.md)

---

# WOCookie

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

WOCookie is used for the creation and setting of cookies in your response objects. A cookie allows for the persistent storage of client state. Instead of using a WOSession object (which can potentially have a shorter life span), a cookie allows server-side applications to store state in client browsers for a specific or indeterminate amount of time. An advantage to cookies is that the data will be stored on the client and not on the server, allowing the server to maintain less state information. A specific advantage in WebObjects applications is that cookies allow the server to put state into the browser that is not bound to a session. Hence, the client can "leave" your application and return with its cookie's state intact.

A WOCookie object defines a cookie that can be added to the HTTP header for your response. You create a cookie using the static method [`cookieWithName`](#apple-geztinjv). To add or remove cookies from the response, use the [WOResponse](WOResponse.md) methods [`addCookie`](WOResponse.md#apple-he4tq) and [`removeCookie`](WOResponse.md#apple-geytq). To retrieve cookie data, use the [WORequest](WORequest.md) methods [`cookieValues`](WORequest.md#apple-gy3q), [`cookieValueForKey`](WORequest.md#apple-gyzq), and [`cookieValuesForKey`](WORequest.md#apple-g4yq). WORequest returns the data as name/value pairs and not as WOCookie objects, since browsers don't return the additional data WOCookies provide, such as path name and expiration date.

For more information about cookies and their implementation details, see Netscape's preliminary specification at `http://www.netscape.com/newsref/std/cookie_spec.html` and RFC 2109 - HTTP State Management Mechanism at `http://www.cis.ohio-state.edu/htbin/rfc/rfc2109.html`.

If and when new details evolve in the implementation of cookies, you can subclass WOCookie and implement new behaviors. Pay particular attention to how you override [`headerString`](#apple-g42q), which WOResponse uses to fill the HTTP response with a header string.

---

## Method Types

**Constructors**

**[WOCookie](#apple-geztimrv)**

**Creation**

**[cookieWithName](#apple-geztinjv)**

**Obtaining a cookie's attributes**

**[domain](#apple-he2ti)

**[expires](#apple-g4yq)

**[headerString](#apple-g42q)

**[isSecure](#apple-hazq)

**[name](#apple-gq3dina)

**[path](#apple-heyq)

**[value](#apple-geyts)**************

**Setting a cookie's attributes**

**[setDomain](#apple-he2q)

**[setExpires](#apple-he4q)

**[setIsSecure](#apple-geydg)

**[setName](#apple-geydo)

**[setPath](#apple-geytc)

**[setValue](#apple-geytk)************

---

## Constructors

---

### WOCookie

public `WOCookie`()

Creates and returns a new empty cookie. To set its attributes, use the appropriate `set` methods.

__See also:__
[`cookieWithName`](#apple-geztinjv), [`setDomain`](#apple-he2q), [`setExpires`](#apple-he4q), [`setIsSecure`](#apple-geydg), [`setName`](#apple-geydo), [`setPath`](#apple-geytc), [`setValue`](#apple-geytk)

---

## Class Methods

---

### cookieWithName

public static WOCookie `cookieWithName`(java.lang.String _aName_, java.lang.String _aValue_)

Creates and returns a cookie with just a name and its value. This method sets the path attribute to your application's path.

public static WOCookie `cookieWithName`(java.lang.String _aName_,
java.lang.String _aValue_,
java.lang.String _aPath_,
java.lang.String _aDomain_,
NSDate _expirationDate_,
boolean _flag_)

Creates and returns a cookie, specifying all its attributes. For more information, see the descriptions of the methods that return attribute values.

__See also:__
[`domain`](#apple-he2ti), [`expires`](#apple-g4yq), [`isSecure`](#apple-hazq), [`name`](#apple-gq3dina), [`path`](#apple-heyq), [`value`](#apple-geyts)

---

## Instance Methods

---

### domain

public java.lang.String `domain`()

_Returns the value of the cookie's "domain" attribute. It's of the form "companyname.com"._

---

### expires

public NSDate `expires`()

_Returns the value of the cookie's "expires" attribute as an NSDate. The expiration date tells the browser how long to keep the cookie in its cache. To have the browser remove the cookie from its cache, set the expiration date to a date in the past._

---

### headerString

public java.lang.String `headerString`()

Returns the string that will be used in the HTTP header. The returned string has the format:

> ```
> Set-cookie: name=value; expires=date; path=path; domain=domain; secure;
> ```

The calendar format for the expiration date is:

> ```
> @"%A, %d-%b-%Y %H:%M:%S GMT"
> ```

where all times are converted relative to Greenwich Mean Time.

This method is called by WOResponse when generating the response.

---

### isSecure

public boolean `isSecure`()

_Returns the cookie's "secure" attribute. This attribute specifies whether the cookie should be transmitted only with secure HTTP. The default value is_ false.

---

### name

public java.lang.String `name`()

Returns the cookie's "name" attribute. The name is similar to the key of a dictionary or hash table. Together, the name and value form the cookie's data.

---

### path

public java.lang.String `path`()

Returns the value of the cookie's "path" attribute. Cookies for a specific path are sent only when accessing URLs within that path. For more information on cookies and their paths, see Netscape's preliminary specification at `http://www.netscape.com/newsref/std/cookie_spec.html` and RFC 2109 - HTTP State Management Mechanism at `http://www.cis.ohio-state.edu/htbin/rfc/rfc2109.html`.

---

### setDomain

public void `setDomain`(java.lang.String _aDomain_)

Sets the cookie's "domain" attribute to _aDomain_. For more information, see [`domain`](#apple-he2ti).

__See also:__
[`cookieWithName`](#apple-geztinjv)

---

### setExpires

public void `setExpires`(NSDate _expirationDate_)

_Sets the cookie's "expires" attribute to expirationDate_. For more information, see [`expires`](#apple-g4yq).

__See also:__
[`cookieWithName`](#apple-geztinjv)

---

### setIsSecure

public void `setIsSecure`(boolean _flag_)

Sets the cookie's "secure" attribute to _flag. For more information, see _`isSecure`_._

__See also:__
[`cookieWithName`](#apple-geztinjv)

---

### setName

public void `setName`(java.lang.String _aName_)

_Sets the cookie's "name" attribute to aName. For more information, see _`name`_._

__See also:__
[`cookieWithName`](#apple-geztinjv)

---

### setPath

public void `setPath`(java.lang.String _aPath_)

_Sets the cookie's "path" attribute to aPath_. For more information, see __`path`.

__See also:__
[`cookieWithName`](#apple-geztinjv)

---

### setValue

public void `setValue`(java.lang.String _aValue_)

Sets the cookie's "value" attribute to _aValue_. For more information, see __`value`.

__See also:__
[`cookieWithName`](#apple-geztinjv)

---

### value

public java.lang.String `value`()

Returns the value of the cookie's value attribute. This attribute is similar to the value of a dictionary or hash table. Together, the name and value form the cookie's data.

---

[!](WOContext.md)
[!](WODirectAction.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
