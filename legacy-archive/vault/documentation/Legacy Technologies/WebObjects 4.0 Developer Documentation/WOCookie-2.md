---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WOCookie.html
archived_at: '2026-07-18T01:28:53.689950Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WOContext-2.md)
[!](WODirectAction-2.md)

---

# WOCookie

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
WebObjects/WOCookie.h

---

## Class Description

WOCookie is used for the creation and setting of cookies in your response objects. A cookie allows for the persistent storage of client state. Instead of using a WOSession object (which can potentially have a shorter life span), a cookie allows server-side applications to store state in client browsers for a specific or indeterminate amount of time. An advantage to cookies is that the data will be stored on the client and not on the server, allowing the server to maintain less state information. A specific advantage in WebObjects applications is that cookies allow the server to put state into the browser that is not bound to a session. Hence, the client can "leave" your application and return with its cookie's state intact.

A WOCookie object defines a cookie that can be added to the HTTP header for your response. You create a cookie using one of two methods:

- [cookieWithName:value:](#apple-gezdqmru)
- [cookieWithName:value:path:domain:expires:isSecure:](#apple-gezdqmzu)

To add or remove cookies from the response, use the [WOResponse](WOResponse-2.md) methods [__addCookie:__](WOResponse-2.md#apple-he4tq) and [__removeCookie:__](WOResponse-2.md#apple-geytq). To retrieve cookie data, use the [WORequest](WORequest-2.md) methods [__cookieValues__](WORequest-2.md#apple-gy3q), [__cookieValueForKey:__](WORequest-2.md#apple-gyzq), and [__cookieValuesForKey:__](WORequest-2.md#apple-g4yq). WORequest returns the data as name/value pairs and not as WOCookie objects, since browsers don't return the additional data WOCookies provide, such as path name and expiration date.

For more information about cookies and their implementation details, see Netscape's preliminary specification at __http://www.netscape.com/newsref/std/cookie_spec.html__  and RFC 2109 - HTTP State Management Mechanism at __http://www.cis.ohio-state.edu/htbin/rfc/rfc2109.html__ .

If and when new details evolve in the implementation of cookies, you can subclass WOCookie and implement new behaviors. Pay particular attention to how you override [__headerString__](#apple-g42q), which WOResponse uses to fill the HTTP response with a header string.

---

## Method Types

**Creation**

**[+ cookieWithName:value:](#apple-gezdqmru)

**[+ cookieWithName:value:path:domain:expires:isSecure:](#apple-gezdqmzu)

**[- initWithName:value:path:domain:expires:isSecure:](#apple-gezdsnrq)******

**Obtaining a cookie's attributes**

**[- domain](#apple-he2ti)

**[- expires](#apple-g4yq)

**[- headerString](#apple-g42q)

**[- isSecure](#apple-hazq)

**[- name](#apple-gq3dina)

**[- path](#apple-heyq)

**[- value](#apple-geyts)**************

**Setting a cookie's attributes**

**[- setDomain:](#apple-he2q)

**[- setExpires:](#apple-he4q)

**[- setIsSecure:](#apple-geydg)

**[- setName:](#apple-geydo)

**[- setPath:](#apple-geytc)

**[- setValue:](#apple-geytk)************

---

## Class Methods

---

### cookieWithName:value:

+ (WOCookie \*)__cookieWithName:__ (NSString \*)_aName_ __value:__ (NSString \*)_aValue_

Creates and returns a cookie with just a name and its value. It sets the path attribute to your application's path.

__See also:__
[- __cookieWithName:value:path:domain:expires:isSecure:__](#apple-gezdqmzu)

---

### cookieWithName:value:path:domain:expires:isSecure:

+ (WOCookie \*)__cookieWithName:__ (NSString \*)_aName___value:__ (NSString \*)_aValue___path:__ (NSString \*)_aPath___domain:__ (NSString \*)_aDomain___expires:__ (NSDate \*)_expirationDate___isSecure:__ (BOOL)_flag_

Creates and returns a cookie, specifying all its attributes. For more information, see the descriptions of the methods that return attribute values.

__See also:__
[- __cookieWithName:value:__](#apple-gezdqmru), [- __domain__](#apple-he2ti), [- __expires__](#apple-g4yq), [- __isSecure__](#apple-hazq), [- __name__](#apple-gq3dina), [- __path__](#apple-heyq), [- __value__](#apple-geyts)

---

## Instance Methods

---

### domain

- (NSString \*)__domain__

_Returns the value of the cookie's "domain" attribute. It's of the form "companyname.com"._

---

### expires

- (NSDate \*)__expires__

_Returns the value of the cookie's "expires" attribute as an NSDate. The expiration date tells the browser how long to keep the cookie in its cache. To have the browser remove the cookie from its cache, set the expiration date to a date in the past._

---

### headerString

- (NSString \*)__headerString__

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

### initWithName:value:path:domain:expires:isSecure:

- __initWithName:__ (NSString \*)_aName___value:__ (NSString \*)_aValue___path:__ (NSString \*)_aPath___domain:__ (NSString \*)_aDomain___expires:__ (NSDate \*)_expirationDate___isSecure:__ (BOOL)_flag_

Initializes a cookie with all its attributes. For more information, see the descriptions of the methods that return attribute values.

__See also:__
[- __domain__](#apple-he2ti), [- __expires__](#apple-g4yq), [- __isSecure__](#apple-hazq), [- __name__](#apple-gq3dina), [- __path__](#apple-heyq), [- __value__](#apple-geyts)

---

### isSecure

- (BOOL)__isSecure__

_Returns the cookie's "secure" attribute. This attribute specifies whether the cookie should be transmitted only with secure HTTP. The default value is_ NO.

---

### name

- (NSString \*)__name__

Returns the cookie's "name" attribute. The name is similar to the key of a dictionary or hash table. Together, the name and value form the cookie's data.

---

### path

- (NSString \*)__path__

Returns the value of the cookie's "path" attribute. Cookies for a specific path are sent only when accessing URLs within that path. For more information on cookies and their paths, see Netscape's preliminary specification at __http://www.netscape.com/newsref/std/cookie_spec.html__  and RFC 2109 - HTTP State Management Mechanism at __http://www.cis.ohio-state.edu/htbin/rfc/rfc2109.html__ .

---

### setDomain:

- (void)__setDomain:__ (NSString \*)_aDomain_

Sets the cookie's "domain" attribute to _aDomain_. For more information, see [__domain__](#apple-he2ti).

__See also:__
[- __cookieWithName:value:path:domain:expires:isSecure:__](#apple-gezdqmzu)

---

### setExpires:

- (void)__setExpires:__ (NSDate \*)_expirationDate_

_Sets the cookie's "expires" attribute to expirationDate_. For more information, see [__expires__](#apple-g4yq).

__See also:__
[- __cookieWithName:value:path:domain:expires:isSecure:__](#apple-gezdqmzu)

---

### setIsSecure:

- (void)__setIsSecure:__ (BOOL)_flag_

Sets the cookie's "secure" attribute to _flag. For more information, see ___isSecure__ _._

__See also:__
[- __cookieWithName:value:path:domain:expires:isSecure:__](#apple-gezdqmzu)

---

### setName:

- (void)__setName:__ (NSString \*)_aName_

_Sets the cookie's "name" attribute to aName. For more information, see ___name__ _._

__See also:__
[- __cookieWithName:value:path:domain:expires:isSecure:__](#apple-gezdqmzu), [- __cookieWithName:value:__](#apple-gezdqmru)

---

### setPath:

- (void)__setPath:__ (NSString \*)_aPath_

_Sets the cookie's "path" attribute to aPath_. For more information, see ____path__ .

__See also:__
[- __cookieWithName:value:path:domain:expires:isSecure:__](#apple-gezdqmzu)

---

### setValue:

- (void)__setValue:__ (NSString \*)_aValue_

Sets the cookie's "value" attribute to _aValue_. For more information, see ____value__ .

__See also:__
[- __cookieWithName:value:path:domain:expires:isSecure:__](#apple-gezdqmzu), [- __cookieWithName:value:__](#apple-gezdqmru)

---

### value

- (NSString \*)__value__

Returns the value of the cookie's value attribute. This attribute is similar to the value of a dictionary or hash table. Together, the name and value form the cookie's data.

---

[!](WOContext-2.md)
[!](WODirectAction-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
