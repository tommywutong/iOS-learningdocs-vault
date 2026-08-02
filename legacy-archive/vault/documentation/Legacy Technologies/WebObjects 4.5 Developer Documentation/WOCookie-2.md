---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WOCookie.html
archived_at: '2026-07-15T08:11:47.469986Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOCookie

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  WebObjects/WOCookie.h

---

## Class Description

---

WOCookie is used for the creation and setting of cookies in
your response objects. A cookie allows for the persistent storage
of client state. Instead of using a WOSession object (which can
potentially have a shorter life span), a cookie allows server-side
applications to store state in client browsers for a specific or
indeterminate amount of time. An advantage to cookies is that the
data will be stored on the client and not on the server, allowing
the server to maintain less state information. A specific advantage
in WebObjects applications is that cookies allow the server to put
state into the browser that is not bound to a session. Hence, the
client can "leave" your application and return with its cookie's
state intact.

A WOCookie object defines a cookie that can be added to the
HTTP header for your response. You create a cookie using one of
two methods:

- [cookieWithName:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2)
- [cookieWithName:value:path:domain:expires:isSecure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2obqxi2b2mrxw2yljny5gk6dqnfzgk4z2nfzvgzldovzgkoq)

To add or remove cookies from the response, use the [WOMessage](WOMessage-2.md#apple-k5hvezltobxw443f) methods [addCookie:](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxwczdeinxw623jmu5a) and [removeCookie:](WOMessage-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2nmvzxgylhmuxxezlnn53gkq3pn5vwszj2). To retrieve cookie
data, use the [WORequest](WORequest-2.md#apple-k5hvezlrovsxg5a) methods [cookieValues](WORequest-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwg33pnnuwkvtbnr2wk4y), [cookieValueForKey:](WORequest-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwg33pnnuwkvtbnr2wkrtpojfwk6j2),
and [cookieValuesForKey:](WORequest-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvyxkzltoqxwg33pnnuwkvtbnr2wk42gn5zewzlzhi).
WORequest returns the data as name/value pairs and not as WOCookie objects,
since browsers don't return the additional data WOCookies provide,
such as path name and expiration date.

For more information about cookies and their implementation
details, see Netscape's preliminary specification at __http://www.netscape.com/newsref/std/cookie_spec.html__ and
RFC 2109 - HTTP State Management Mechanism at __http://www.cis.ohio-state.edu/htbin/rfc/rfc2109.html__.

If and when new details evolve in the implementation of cookies,
you can subclass WOCookie and implement new behaviors. Pay particular
attention to how you override [headerString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5ugkylemvzfg5dsnfxgo), which WOResponse uses
to fill the HTTP response with a header string.

## Method Types

---

> **Creation**
> : [+ cookieWithName:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2)
> : [+ cookieWithName:value:path:domain:expires:isSecure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2obqxi2b2mrxw2yljny5gk6dqnfzgk4z2nfzvgzldovzgkoq)
> : [- initWithName:value:path:domain:expires:isSecure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5uw42luk5uxi2comfwwkotwmfwhkzj2obqxi2b2mrxw2yljny5gk6dqnfzgk4z2nfzvgzldovzgkoq)
>
> **Obtaining a cookie's
> attributes**
> : [- domain](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5sg63lbnfxa)
> : [- expires](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5sxq4djojsxg)
> : [- headerString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5ugkylemvzfg5dsnfxgo)
> : [- isSecure](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5uxgu3fmn2xezi)
> : [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5xgc3lf)
> : [- path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5ygc5di)
> : [- value](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff53gc3dvmu)
>
> **Setting a cookie's
> attributes**
> : [- setDomain:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5zwk5cen5wwc2lohi)
> : [- setExpires:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5zwk5cfpbygs4tfom5a)
> : [- setIsSecure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5zwk5cjonjwky3vojstu)
> : [- setName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5zwk5comfwwkoq)
> : [- setPath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5zwk5cqmf2gqoq)
> : [- setValue:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5zwk5cwmfwhkzj2)

## Class Methods

---

### cookieWithName:value:

`+ (WOCookie *)cookieWithName:(NSString
*)aName
value:(NSString *)aValue`

Creates and returns a cookie with just a name
and its value. It sets the path attribute to your application's
path.

__See Also:__  [- cookieWithName:value:path:domain:expires:isSecure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2obqxi2b2mrxw2yljny5gk6dqnfzgk4z2nfzvgzldovzgkoq)

---

### cookieWithName:value:path:domain:expires:isSecure:

`+ (WOCookie *)cookieWithName:(NSString
*)aName
value:(NSString *)aValue
path:(NSString *)aPath
domain:(NSString *)aDomain
expires:(NSDate *)expirationDate
isSecure:(BOOL)flag`

Creates and returns a cookie, specifying all
its attributes. For more information, see the descriptions of the
methods that return attribute values.

__See
Also:__  [- cookieWithName:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2), [- domain](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5sg63lbnfxa), [- expires](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5sxq4djojsxg), [- isSecure](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5uxgu3fmn2xezi), [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5xgc3lf), [- path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5ygc5di), [- value](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff53gc3dvmu)

---

## Instance Methods

---

### domain

`- (NSString *)domain`

Returns the value of the cookie's "domain"
attribute. It's of the form "companyname.com".

---

### expires

`- (NSDate *)expires`

Returns the value of the cookie's "expires"
attribute as an NSDate. The expiration date tells the browser how
long to keep the cookie in its cache. To have the browser remove
the cookie from its cache, set the expiration date to a recent date
in the past (see [setExpires:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5zwk5cfpbygs4tfom5a) for
more information).

---

### headerString

`- (NSString *)headerString`

Returns the string that will be used in
the HTTP header. The returned string has the format:

Set-cookie:
name=_value_; expires=_date_;
path=_path_; domain=_domain_;
secure;

The calendar format for the expiration
date is:

> ```
> @"%A, %d-%b-%Y %H:%M:%S GMT"
> ```

where all times are
converted relative to Greenwich Mean Time.

This method
is called by WOResponse when generating the response.

---

### initWithName:value:path:domain:expires:isSecure:

`- (id)initWithName:(NSString
*)aName
value:(NSString *)aValue
path:(NSString *)aPath
domain:(NSString *)aDomain
expires:(NSDate *)expirationDate
isSecure:(BOOL)flag`

Initializes a cookie with all its attributes.
For more information, see the descriptions of the methods that return
attribute values.

__See Also:__  [- domain](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5sg63lbnfxa), [- expires](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5sxq4djojsxg), [- isSecure](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5uxgu3fmn2xezi), [- name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5xgc3lf), [- path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5ygc5di), [- value](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff53gc3dvmu)

---

### isSecure

`- (BOOL)isSecure`

Returns the cookie's "secure" attribute.
This attribute specifies whether the cookie should be transmitted
only with secure HTTP. The default value is NO.

---

### name

`- (NSString *)name`

Returns the cookie's "name" attribute.
The name is similar to the key of a dictionary or hash table. Together,
the name and value form the cookie's data.

---

### path

`- (NSString *)path`

Returns the value of the cookie's "path"
attribute. Cookies for a specific path are sent only when accessing
URLs within that path. For more information on cookies and their
paths, see Netscape's preliminary specification at __http://www.netscape.com/newsref/std/cookie_spec.html__ and
RFC 2109 - HTTP State Management Mechanism at __http://www.cis.ohio-state.edu/htbin/rfc/rfc2109.html__.

---

### setDomain:

`- (void)setDomain:(NSString
*)aDomain`

Sets the cookie's "domain" attribute to _aDomain_.
For more information, see [domain](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5sg63lbnfxa).

__See
Also:__  [- cookieWithName:value:path:domain:expires:isSecure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2obqxi2b2mrxw2yljny5gk6dqnfzgk4z2nfzvgzldovzgkoq)

---

### setExpires:

`- (void)setExpires:(NSDate
*)expirationDate`

Sets the cookie's "expires" attribute
to _expirationDate_.

If
you want to set the cookie's expiration date to some date in the
distant past-for instance, in order to erase the cookie-don't
use `[NSDate distantPast]`. __distantPast__ returns
a date from the year 1 AD, and some browsers incorrectly interpret
this as the year 2001. Instead, set the cooke's expiration date
to an actual date in the recent past.

__See
Also:__  [- cookieWithName:value:path:domain:expires:isSecure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2obqxi2b2mrxw2yljny5gk6dqnfzgk4z2nfzvgzldovzgkoq), [- expires](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5sxq4djojsxg)

---

### setIsSecure:

`- (void)setIsSecure:(BOOL)flag`

Sets the cookie's "secure" attribute to _flag_.
For more information, see [isSecure](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5uxgu3fmn2xezi).

__See
Also:__  [- cookieWithName:value:path:domain:expires:isSecure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2obqxi2b2mrxw2yljny5gk6dqnfzgk4z2nfzvgzldovzgkoq)

---

### setName:

`- (void)setName:(NSString
*)aName`

Sets the cookie's "name" attribute to _aName_.
For more information, see [name](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5xgc3lf).

__See
Also:__  [- cookieWithName:value:path:domain:expires:isSecure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2obqxi2b2mrxw2yljny5gk6dqnfzgk4z2nfzvgzldovzgkoq), [- cookieWithName:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2)

---

### setPath:

`- (void)setPath:(NSString
*)aPath`

Sets the cookie's "path" attribute to _aPath_.
For more information, see [path](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff5ygc5di).

__See
Also:__  [- cookieWithName:value:path:domain:expires:isSecure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2obqxi2b2mrxw2yljny5gk6dqnfzgk4z2nfzvgzldovzgkoq)

---

### setValue:

`- (void)setValue:(NSString
*)aValue`

Sets the cookie's "value" attribute to _aValue_.
For more information, see [value](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2dn5xww2lff53gc3dvmu).

__See
Also:__  [- cookieWithName:value:path:domain:expires:isSecure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2obqxi2b2mrxw2yljny5gk6dqnfzgk4z2nfzvgzldovzgkoq), [- cookieWithName:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpk5hug33pnnuwkl3dn5xww2lfk5uxi2comfwwkotwmfwhkzj2)

---

### value

`- (NSString *)value`

Returns the value of the cookie's value attribute.
This attribute is similar to the value of a dictionary or hash table.
Together, the name and value form the cookie's data.

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
