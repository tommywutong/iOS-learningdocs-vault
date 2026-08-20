---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WORequest.html
archived_at: '2026-07-15T08:15:15.748012Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WORequest

> **__Inherits from:__**
> : [WOMessage](WOMessage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpk5hu2zltonqwozi) : Object

> **__Implements:__**
> : Cloneable

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

A WORequest object typically represents an HTTP request and thus constitutes an event that requires a reaction from a WebObjects application. WORequest objects encapsulate the data transmitted to an HTTP server in a request. Requests usually originate from user actions in a browser, such as the submission of a URL or a mouse click on a hyperlink, button, or active image in a page. From the perspective of WebObjects, the URL identifies a WebObjects application and the click on a control usually results in the display of a page of a WebObjects application. Such actions cause the browser to send an HTTP request to an HTTP server, which forwards the request to a WebObjects adaptor, which converts it to a WORequest object and sends that object to the appropriate request handler.

WORequest objects can also be created from HTTP requests sent by client-side components (Java applets specially modified to interact with the server side of a WebObjects application), and from HTTP requests submitted by custom client-side programs that don't use the Java client-side components. As well, WORequest objects can originate from custom adaptors that handle HTTP requests _or_ non-HTTP events. (All the adaptors shipped with WebObjects handle HTTP events only).

Since adaptors usually create WORequest objects, and since you can usually use WebObjects' adaptors without modifications, you probably won't have to create your own instances of WORequest in your code (although you can if you need to). More typically, your code will obtain information from WORequest objects as they become available during certain points in the request-response loop. The application supplies WORequest objects as arguments in the __takeValuesFromRequest__ and __invokeActionForRequest__ methods, which are implementable by WOApplication, WOSession, WOComponent, and WOElement objects. You can also obtain the current WORequest object at any time during request handling through WOContext's request method.

|  |
| --- |
| __Note:__ Because WORequest objects usually correspond to HTTP requests, the data they encapsulate is almost the same as what you would find in an HTTP request. Thus an understanding of HTTP requests is important for understanding the data vended by WORequest objects. A recommended prerequisite therefore is to review the current HTTP specification or HTTP documentation. |

Note that WORequest inherits from WOMessage. Of particular interest are those WOMessage methods that allow you to access the request headers (headerForKey, headerKeys, headers, and headersForKey) and content and contentAsDOMDocument, which return the contents of the request.

## Programmatically Creating WORequest Objects

As stated above, in most WebObjects applications WORequest objects are created for you; your application is more concerned with interpreting and responding to WORequest objects. However, it is possible to place two WebObjects applications in a peer-to-peer configuration and have them communicate using WORequest and WOResponse objects. In situations like these, your application will need to create the WORequest objects itself and send them to the peer application using WOHTTPConnection.

The methods declared directly on WORequest allow you to extract information from a WORequest object. WORequest inherits a number of methods from WOMessage, however, that allow you to programmatically specify the contents of a request. In particular, the __appendContent...__ and setContent methods in the WOMessage class are designed to do this. For more information, see the WOMessage class specification.

## Constants

---

WORequest declares these constants:

|  |  |
| --- | --- |
|  |  |
| SessionIDKey | This class constant (a String) has the value "wosid" and is the key you use to obtain the session ID from a request (using methods like __formValueForKey(String)__ and __cookieValueForKey(String)__). |
| InstanceKey | This class constant (a String) has the value "woinst" and is the key you use to obtain the application number (instance) from a request (using methods like __formValueForKey(String)__ and __cookieValueForKey(String)__). |
| DataKey | This class constant (a String) has the value "wodata" and is the key you use to obtain from a request another key. You use this second key either to retrieve cached data from the WOResourceManager or to construct a query with which you can obtain a URL to the request data (using WOContext's __urlWithRequestHandlerKey()__ method). Use methods like __formValueForKey(String)__ and __cookieValueForKey(String)__ when querying the request with the `DataKey`. |
| ContextIDKey | This class constant (a String) has the value "wocid" and is used by the WOComponentRequestHandler to store to and retrieve from an NSDictionary the request's context ID. |
| SenderIDKey | This class constant (a String) has the value "woeid" and is used by the WOComponentRequestHandler to store to and retrieve from an NSDictionary the request's sender ID. |
| PageNameKey | This class constant (a String) has the value "wopage" and is used by the WOComponentRequestHandler to store to and retrieve from an NSDictionary the request's page name. |
| SingleInstanceIDString | This class constant contains, as a String , the application number used by applications deployed in single instance mode: "-1". |
| SingleInstanceID | This class constant contains, as an `int` , the application number used by applications deployed in single instance mode: -1. |

## Method Types

---

> **Constructors**
> : [WORequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6v2pkjsxc5lfon2a)
>
> **Working with cookies**
> : [cookieValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6y3pn5vwszkwmfwhkzkgn5zewzlz): [cookieValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6y3pn5vwszkwmfwhkzlt): [cookieValuesForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6y3pn5vwszkwmfwhkzltizxxes3fpe)
>
> **Form values**
> : [defaultFormValueEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6zdfmzqxk3duizxxe3kwmfwhkzkfnzrw6zdjnztq): [formValueEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ztpojwvmylmovsuk3tdn5sgs3th): [formValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ztpojwvmylmovsum33sjnsxs): [formValueKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ztpojwvmylmovsuwzlzom): [formValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ztpojwvmylmovsxg): [formValuesForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ztpojwvmylmovsxgrtpojfwk6i): [isFormValueEncodingDetectionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c62ltizxxe3kwmfwhkzkfnzrw6zdjnztuizlumvrxi2lpnzcw4ylcnrswi)
>
> **Request handling**
> : [requestHandlerKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c64tfof2wk43ujbqw4zdmmvzewzlz): [requestHandlerPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c64tfof2wk43ujbqw4zdmmvzfayluna): [requestHandlerPathArray](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c64tfof2wk43ujbqw4zdmmvzfaylunbaxe4tbpe)
>
> **Form Values**
> : [setDefaultFormValueEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c643forcgkztbovwhirtpojwvmylmovsuk3tdn5sgs3th): [setFormValueEncodingDetectionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c643fordg64tnkzqwy5lfivxgg33enfxgordforswg5djn5xek3tbmjwgkza)
>
> **Obtaining attributes**
> : [adaptorPrefix](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ylemfyhi33skbzgkztjpa): [applicationName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ylqobwgsy3boruw63somfwwk): [applicationNumber](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ylqobwgsy3boruw63soovwwezls): [browserLanguages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ytsn53xgzlsjrqw4z3vmftwk4y): [isFromClientComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c62ltizzg63kdnruwk3tuinxw24dpnzsw45a): [method](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c63lforug6za): [sessionID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c643fonzws33ojfca): [uri](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c65lsne)

## Constructors

---

### WORequest

`public WORequest( String aMethod, String anURL, String anHTTPVersion, NSDictionary someHeaders, NSData aContent, NSDictionary userInfo)`

Returns a WORequest object initialized with the specified parameters. The first two arguments are required:

- _aMethod_ must be either "GET" or "POST"; anything else causes an exception to be thrown.
- _aURL_ must be a valid URL; if the URL is invalid, an exception is thrown.

If either argument is omitted, the constructor throws an exception.

The remaining arguments are optional; if you specify __null__ for these, the constructor substitutes default values or initializes them to __null__. The _someHeaders_ argument (if not __null__) should be a dictionary whose String keys correspond to header names and whose values are arrays of one or more strings corresponding to the values of each header. The _userInfo_ dictionary can contain any information that the WORequest object wants to pass along to other objects involved in handling the request.

For more information on each argument, see the description of the corresponding accessor method.

__See Also:__ [method](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c63lforug6za), httpVersion (WOMessage class), content (WOMessage class), userInfo (WOMessage class)

---

## Instance Methods

---

### adaptorPrefix

`public String adaptorPrefix()`

Returns the part of the request's URI that is specific to a particular adaptor. This is typically a URL ending in "/WebObjects", "/WebObjects.exe", "/WebObjects.dll", or uppercase versions of these strings. WebObjects uses a request's adaptor prefix to set the adaptor prefix in the generated response's URL. A WORequest must always have an adaptor prefix.

__See Also:__ [applicationName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ylqobwgsy3boruw63somfwwk), [applicationNumber](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ylqobwgsy3boruw63soovwwezls), [uri](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c65lsne)

---

### applicationName

`public String applicationName()`

Returns the part of the request's URI that identifies the application the request is intended for. This name does not include the ".woa" extension of an application directory. A WORequest must always have an application name specified.

__See Also:__ [adaptorPrefix](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ylemfyhi33skbzgkztjpa), [applicationNumber](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ylqobwgsy3boruw63soovwwezls), [uri](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c65lsne)

---

### applicationNumber

`public int applicationNumber()`

Returns the part of the request's URI that identifies the particular application instance the request is intended for. This attribute is -1 if the request can be handled by any instance of the application, which is always the case for the first request in a session.

__See Also:__ [applicationName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ylqobwgsy3boruw63somfwwk), [uri](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c65lsne)

---

### __applicationURLPrefix__

`public String applicationURLPrefix()`

Description forthcoming.

---

### browserLanguages

`public NSArray browserLanguages()`

Returns the language preference list from the user's browser.

---

### __clone__

`public Object clone()`

Conformance to Cloneable.

---

### __cookies__

`public NSArray cookies()`

Returns an NSArray containing all cookies packaged as WOCookie objects.

---

### cookieValueForKey

`public String cookieValueForKey(String aKey)`

Returns a string value for the cookie key specified by _aKey_.

__See Also:__ [cookieValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6y3pn5vwszkwmfwhkzlt), [cookieValuesForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6y3pn5vwszkwmfwhkzltizxxes3fpe), WOCookie class specification

---

### cookieValues

`public NSDictionary cookieValues()`

Returns a dictionary of cookie values and cookie keys.

__See Also:__ [cookieValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6y3pn5vwszkwmfwhkzkgn5zewzlz), [cookieValuesForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6y3pn5vwszkwmfwhkzltizxxes3fpe), WOCookie class specification

---

### cookieValuesForKey

`public NSArray cookieValuesForKey(String aKey)`

Returns an array of values for the cookie key specified by _aKey_. Use this method to retrieve information stored in a cookie in an HTTP header. Valid keys are specified in the cookie specification.

__See Also:__ [cookieValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6y3pn5vwszkwmfwhkzkgn5zewzlz), [cookieValues](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6y3pn5vwszkwmfwhkzlt), WOCookie class specification

---

### defaultFormValueEncoding

`public String defaultFormValueEncoding()`

Returns the _default_ string encoding the WORequest object uses for converting form values from ASCII to Unicode. It uses the default encoding only when it can detect no encoding from the ASCII form values or if encoding detection is disabled. If no default form-value encoding is set, NSISOLatin1StringEncoding is used.

__See Also:__ [setDefaultFormValueEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c643forcgkztbovwhirtpojwvmylmovsuk3tdn5sgs3th)

---

### formValueEncoding

`public String formValueEncoding()`

Returns the encoding last used to convert form values from ASCII to Unicode. This encoding is either the result of an earlier detection of form-value encoding or the default form value encoding.

__See Also:__ [defaultFormValueEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6zdfmzqxk3duizxxe3kwmfwhkzkfnzrw6zdjnztq), [isFormValueEncodingDetectionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c62ltizxxe3kwmfwhkzkfnzrw6zdjnztuizlumvrxi2lpnzcw4ylcnrswi)

---

### formValueForKey

`public String formValueForKey(String aKey)`

Returns a form value identified by the name _aKey_. If there are multiple form values identified by the same name, only one of the values is returned, and which of these values is not defined. You should use this method for names that you know occur only once in the name/value pairs of form data.

---

### formValueKeys

`public NSArray formValueKeys()`

Returns an array of NSStrings corresponding to the names (or keys) used to access values of a form. The array is not sorted in any particular order, and is not necessarily sorted in the same order on successive invocations of this method.

---

### formValues

`public NSDictionary formValues()`

Returns an NSDictionary containing all of the form data name/value pairs.

---

### formValuesForKey

`public NSArray formValuesForKey(String aKey)`

Returns an array of all values (as Strings) of the form identified by the name _aKey_. This array is not sorted in any particular order, and is not necessarily sorted in the same order on successive invocations of this method. You should use this method when you know that a name (key) used for accessing form data can be matched with more than one value.

---

### isFormValueEncodingDetectionEnabled

`public boolean isFormValueEncodingDetectionEnabled()`

Returns whether detection of form-value encoding is allowed to take place when form values are obtained.

__See Also:__ [setFormValueEncodingDetectionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c643fordg64tnkzqwy5lfivxgg33enfxgordforswg5djn5xek3tbmjwgkza)

---

### isFromClientComponent

`public boolean isFromClientComponent()`

Returns whether the request originated from an event in a client-side component (that is, a Java applet that can interact with the server side of a WebObjects application).

If you use dynamic elements and write write HTML code in the response, you should check that the request is not from a client-side component before writing into the response.

---

### __isSessionIDInRequest__

`public boolean isSessionIDInRequest()`

Returns `true` if the session ID can be obtained from the request. Note that the session ID may either be included among the form values or encapsulated within a cookie. Use WORequest's __session()__ method to retrieve the value of the session ID from the request.

---

### method

`public String method()`

Returns the method the WORequest object was initialized with. A WORequest's method defines where it will look for form values. The only currently supported methods are "GET" and "PUT", which have the same meaning as the HTTP request method tokens of the same name.

__See Also:__ content (WOMessage class), httpVersion (WOMessage class)

---

### __queryString__

`public String queryString()`

Returns, as a String, the query portion of the URI.

---

### requestHandlerKey

`public String requestHandlerKey()`

Returns the part of the request's URI which identifies the request handler. This identifies the request handle which will process the request and cannot be null

---

### requestHandlerPath

`public String requestHandlerPath()`

Returns the part of the URL which identifies, for a given request handler, which information is requested. Different request handlers use this part of the URL in different ways.

---

### requestHandlerPathArray

`public NSArray requestHandlerPathArray()`

Returns the request handler path decomposed into elements.

---

### sessionID

`public String sessionID()`

Returns the session ID, or null if no session ID is found. This method first looks for the session ID in the URL, then checks the form values, and finally checks to see if the session ID is stored in a cookie.

---

### setDefaultFormValueEncoding

`public void setDefaultFormValueEncoding(String anEncoding)`

Sets the default string encoding for the receiver to use when converting its form values from ASCII to Unicode. The default string encoding is called into play if the WORequest cannot detect an encoding from the ASCII form values or if encoding detection is disabled. If no default form value encoding is explicitly set, the WORequest uses NSISOLatin1StringEncoding.

__See Also:__ [defaultFormValueEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6zdfmzqxk3duizxxe3kwmfwhkzkfnzrw6zdjnztq), [setFormValueEncodingDetectionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c643fordg64tnkzqwy5lfivxgg33enfxgordforswg5djn5xek3tbmjwgkza)

---

### setFormValueEncodingDetectionEnabled

`public void setFormValueEncodingDetectionEnabled(boolean flag)`

Enables or disables automatic detection of the best encoding for the receiver to use when it converts form values from ASCII to Unicode. When detection is enabled, a WORequest object scans the ASCII form values and applies heuristics to decide which is the best encoding to use. If no specific encoding is discernible, or if detection is disabled, the WORequest uses the default form value encoding for the conversion.

__See Also:__ [isFormValueEncodingDetectionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c62ltizxxe3kwmfwhkzkfnzrw6zdjnztuizlumvrxi2lpnzcw4ylcnrswi), [setDefaultFormValueEncoding](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c643forcgkztbovwhirtpojwvmylmovsuk3tdn5sgs3th)

---

### __toString__

`public String toString()`

Returns a String representation of the receiver. This string representation is suitable for debugging-it includes the URI, information on how the form values are encoded, and the form values themselves.

---

### uri

`public String uri()`

Returns the Uniform Resource Identifier (URI) the WORequest was initialized with. For a session's first request, the URI indicates the resource that the request is seeking (such as a WebObjects application); for subsequent requests in the session, the URI indicates which page of the application should handle the request. If the request was caused (as is usually the case) by a web browser submitting a URL to an HTTP server, the URI is that part of the URL that follows the port number. Because the format of WebObjects URLs and the corresponding request URI might change between different versions of WebObjects, you should not attempt to parse the URI returned by this method. Instead, use WORequest's accessor methods to access particular URI/URL components.

__See Also:__ [adaptorPrefix](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ylemfyhi33skbzgkztjpa), [applicationName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ylqobwgsy3boruw63somfwwk), [applicationNumber](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxc5lfon2c6ylqobwgsy3boruw63soovwwezls)

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
