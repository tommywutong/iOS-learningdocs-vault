---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WORequest.html
archived_at: '2026-07-18T01:28:54.163578Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WOMailDelivery-2.md)
[!](WORequestHandler-2.md)

---

# WORequest

__Inherits From:__
NSObject

__Declared in:__
WebObjects/WORequest.h

---

## Class Description

A WORequest object typically represents an HTTP request and thus constitutes an event that requires a reaction from a WebObjects application. WORequest objects encapsulate the data transmitted to a HTTP server in a request. Requests originate from user actions in a browser, such as the submission of a URL or a mouse click on a hyperlink, button, or active image in a page; from the perspective of WebObjects, the URL identifies a WebObjects application and the click on a control usually results in the display of a page of a WebObjects application. Such actions cause the browser to send an HTTP request to an HTTP server, which forwards the request to a WebObjects adaptor, which converts it to a WORequest object and sends that object to the appropriate request handler.

WORequest objects can also be created from HTTP requests sent by client-side components (Java applets specially modified to interact with the server side of a WebObjects application), and from HTTP requests submitted by custom client-side programs that don't use the Java client-side components. More rarely, WORequest objects can originate from custom adaptors that handle HTTP requests _or_ non-HTTP events. (All the adaptors shipped with WebObjects handle HTTP events only).

Since adaptors usually create WORequest objects, and since you can usually use WebObjects' adaptors without modifications, you probably won't have to create your own instances of WORequest in your code (although you can if you need to). More typically, your code will obtain information from WORequest objects as they become available during certain points in the request-response loop. The application supplies WORequest objects as arguments in the __takeValuesFromRequest:inContext:__  and __invokeActionForRequest:inContext:__  methods, which are implementable by WOApplication, [WOSession](WOSession-2.md), [WOComponent](WOComponent-2.md), and [WOElement](WOElement-2.md) objects. You can also obtain the current WORequest object at any time during request handling through WOContext's [__request__](WOContext-2.md#apple-geydk) method.

__Note:__
Because WORequest objects usually correspond to HTTP requests, the data they encapsulate is
almost the same as what you would find in an HTTP request. Thus an understanding of HTTP
requests is important for understanding the data vended by WORequest objects. A recommended
prerequisite therefore is to review the current HTTP specification or HTTP documentation.

---

# Adopted Protocols

**NSCopying**

**- copy

**- copyWithZone:****

---

## Method Types

**Working with cookies**

**[- cookieValueForKey:](#apple-gyzq)

**[- cookieValues](#apple-gy3q)

**[- cookieValuesForKey:](#apple-g4yq)******

**Form values**

**[- defaultFormValueEncoding](#apple-g42q)

**[- formValueEncoding](#apple-g44q)

**[- formValueForKey:](#apple-hazq)

**[- formValueKeys](#apple-ha3q)

**[- formValues](#apple-heyq)

**[- formValuesForKey:](#apple-he2q)

**[- isFormValueEncodingDetectionEnabled](#apple-geyts)**************

**Headers**

**[- headerForKey:](#apple-he4q)

**[- headerKeys](#apple-geydg)

**[- headersForKey:](#apple-geydo)******

**Request handling**

**[- requestHandlerKey](#apple-geztc)

**[- requestHandlerPath](#apple-gqzdgmq)

**[- requestHandlerPathArray](#apple-gezts)******

**Form Values**

**[- setDefaultFormValueEncoding:](#apple-guztomi)

**[- setFormValueEncodingDetectionEnabled:](#apple-ge2do)****

**Obtaining attributes**

**[- adaptorPrefix](#apple-gqzq)

**[- applicationName](#apple-gq3q)

**[- applicationNumber](#apple-guyq)

**[- browserLanguages](#apple-gu2q)

**[- content](#apple-gu4q)

**[- httpVersion](#apple-geytc)

**[- isFromClientComponent](#apple-gezdg)

**[- initWithMethod:uri:httpVersion:headers:content:userInfo:](#apple-geztcnzw)

**[- method](#apple-gezdo)

**[- uri](#apple-ge2tc)

**[- userInfo](#apple-ge2tk)**********************

---

## Instance Methods

---

### adaptorPrefix

- (NSString \*)__adaptorPrefix__

Returns the part of the request's URI that is specific to a particular adaptor. This is typically a URL ending in "/WebObjects", "/WebObjects.exe", "/WebObjects.dll", or uppercase versions of these strings. WebObjects uses a request's adaptor prefix to set the adaptor prefix in the generated response's URL. A WORequest must always have an adaptor prefix.

__See also:__
[- __applicationName__](#apple-gq3q), [- __applicationNumber__](#apple-guyq), [- __uri__](#apple-ge2tc)

---

### applicationName

- (NSString \*)__applicationName__

Returns the part of the request's URI that identifies the application the request is intended for. This name does not include the ".woa" extension of an application directory. A WORequest must always have an application name specified.

__See also:__
[- __adaptorPrefix__](#apple-gqzq), [- __applicationNumber__](#apple-guyq), __[- uri](#apple-ge2tc)__

---

### applicationNumber

- (int)__applicationNumber__

Returns the part of the request's URI that identifies the particular application instance the request is intended for. This attribute is -1 if the request can be handled by any instance of the application, which is always the case for the first request in a session.

__See also:__
[- __applicationName__](#apple-gq3q), [- __uri__](#apple-ge2tc)

---

### browserLanguages

- (NSArray \*)__browserLanguages__

Returns the language preference list from the user's browser.

---

### content

- (NSData \*)__content__

Returns the content the WORequest was initialized with (which defaults to __nil__ ). The format of the data is undefined, but you can usually identify it by the value of the "content-type" header.

__See also:__
[- __httpVersion__](#apple-geytc), [- __method__](#apple-gezdo)

---

### cookieValueForKey:

- (NSString \*)__cookieValueForKey:__ (NSString \*)_aKey_

Returns a string value for the cookie key specified by _aKey_.

__See also:__
[- __cookieValues__](#apple-gy3q), [- __cookieValuesForKey:__](#apple-g4yq), [WOCookie](WOCookie-2.md) class specification

---

### cookieValues

- (NSDictionary \*)__cookieValues__

Returns a dictionary of cookie values and cookie keys.

__See also:__
[- __cookieValueForKey:__](#apple-gyzq), [- __cookieValuesForKey:__](#apple-g4yq), [WOCookie](WOCookie-2.md) class specification

---

### cookieValuesForKey:

- (NSArray \*)__cookieValuesForKey:__ (NSString \*)_aKey_

Returns an array of values for the cookie key specified by _aKey_. Use this method to retrieve information stored in a cookie in an HTTP header. Valid keys are specified in the cookie specification.

__See also:__
[- __cookieValueForKey:__](#apple-gyzq), [- __cookieValues__](#apple-gy3q), [WOCookie](WOCookie-2.md) class specification

---

### defaultFormValueEncoding

- (NSStringEncoding)__defaultFormValueEncoding__

Returns the _default_ string encoding the WORequest object uses for converting form values from ASCII to Unicode. It uses the default encoding only when it can detect no encoding from the ASCII form values or if encoding detection is disabled. If no default form-value encoding is set, NSISOLatin1StringEncoding is used.

__See also:__
__[- setDefaultFormValueEncoding:](#apple-guztomi)__

---

### formValueEncoding

- (NSStringEncoding)__formValueEncoding__

Returns the encoding last used to convert form values from ASCII to Unicode. This encoding is either the result of an earlier detection of form-value encoding or the default form value encoding.

__See also:__
[- __defaultFormValueEncoding__](#apple-g42q), __[- isFormValueEncodingDetectionEnabled](#apple-geyts)__

---

### formValueForKey:

- id __formValueForKey:__ (NSString \*)_aKey_

Returns a form value identified by the name _aKey_. If there are multiple form values identified by the same name, only one of the values is returned, and which of these values is not defined. You should use this method for names that you know occur only once in the name/value pairs of form data.

---

### formValueKeys

- (NSArray \*)__formValueKeys__

Returns an array of NSStrings corresponding to the names (or keys) used to access values of a form. The array is not sorted in any particular order, and is not necessarily sorted in the same order on successive invocations of this method.

---

### formValues

- (NSDictionary \*)__formValues__

Returns an NSDictionary containing all of the form data name/value pairs.

---

### formValuesForKey:

- (NSArray \*)__formValuesForKey:__ (NSString \*)_aKey_

Returns an array of all values (as NSStrings) of the form identified by the name _aKey_. This array is not sorted in any particular order, and is not necessarily sorted in the same order on successive invocations of this method. You should use this method when you know that a name (key) used for accessing form data can be matched with more than one value.

---

### headerForKey:

- (NSString \*)__headerForKey:__ (NSString \*)_aKey_

Returns one value of a particular header in the header dictionary the request was initialized with. This will be a string corresponding to one of the values of the header whose name is passed in as the key argument. If the specified header has multiple values, only one of these values is returned, and which one of them this is is not defined. However, on successive invocations of this method, the same value will always be returned. This method is intended to be used for headers that are known to have only one value.

---

### headerKeys

- (NSArray \*)__headerKeys__

Returns an array of the keys of the header dictionary the request was initialized with (which default to an empty dictionary). This will be an array of strings corresponding to the headers' names. The array is not sorted in any particular order, and not necessarily sorted in the same order on successive invocations of this method.

---

### headersForKey:

- (NSArray \*)__headersForKey:__ (NSString \*)_aKey_

Returns the values of a particular header that is identified by _aKey_. The returned object contains NSStrings sorted in no particular order, but which will always be sorted in the same order on successive invocations of this method. Use this method for headers that you know have (or can have) multiple values.

---

### httpVersion

- (NSString \*)__httpVersion__

Returns the HTTP version the request was initialized with. An application uses the WORequest's HTTP version to initialize the HTTP version of the response that is generated by request handling. The WORequest's HTTP version typically derives from the HTTP version of the client (for example, the browser) that initiated the request.

---

### initWithMethod:uri:httpVersion:headers:content:userInfo:

- (id)__initWithMethod:__ (NSString \*)_aMethod_ __uri:__ (NSString \*)_aURL_ __httpVersion:__ (NSString \*)_anHTTPVersion_ __headers:__ (NSDictionary \*)_someHeaders_ __content:__ (NSData \*)_aContent_ __userInfo:__ (NSDictionary \*)_userInfo_

Returns a WORequest object initialized with the specified parameters. The first two arguments are required:

- _aMethod_ must be either "GET" or "POST"; anything else causes an exception to be raised.
- _aURL_ must be a valid URL; if the URL is invalid, an exception is raised.

If either argument is omitted, an exception is raised.

The remaining arguments are optional; if you specify __nil__  for these, the designated initializer substitutes default values or initializes them to __nil__ . The _someHeaders_ argument (if not __nil__ ) should be a dictionary whose NSString keys correspond to header names and whose values are arrays of one or more strings corresponding to the values of each header. The _userInfo_ dictionary can contain any information that the WORequest object wants to pass along to other objects involved in handling the request.

For more information on each argument, see the description of the corresponding accessor method.

---

### isFormValueEncodingDetectionEnabled

- (BOOL)__isFormValueEncodingDetectionEnabled__

Returns whether detection of form-value encoding is allowed to take place when form values are obtained.

__See also:__
__[- setFormValueEncodingDetectionEnabled:](#apple-ge2do)__

---

### isFromClientComponent

- (BOOL)__isFromClientComponent__

Returns whether the request originated from an event in a client-side component (that is, a Java applet that can interact with the server side of a WebObjects application).

If you use dynamic elements and write write HTML code in the response, you should check that the request is not from a client-side component before writing into the response.

---

### method

- (NSString \*)__method__

Returns the method the WORequest object was initialized with. A WORequest's method defines where it will look for form values. The only currently supported methods are "GET" and "PUT", which have the same meaning as the HTTP request method tokens of the same name.

__See also:__
[- __content__](#apple-gu4q), __[- httpVersion](#apple-geytc)__

---

### requestHandlerKey

- (NSString \*)__requestHandlerKey__

_Returns the part of the request's URI which identifies the request handler. This identifies the request handle which will process the reuquest and cannot be_ _null__._

---

### requestHandlerPath

- (NSString \*)__requestHandlerPath__

_Returns the part of the URL which identifies, for a given request handler, which information is requested. Different request handlers use this part of the URL in different ways._

---

### requestHandlerPathArray

- (NSArray \*)__requestHandlerPathArray__

_Returns the request handler path decomposed into elements._

---

### sessionID

- (NSString \*)__sessionID__

Returns the session ID, or __nil__  if no session ID is found. This method first looks for the session ID in the URL, then checks the form values, and finally checks to see if the session ID is stored in a cookie.

---

### setDefaultFormValueEncoding:

- (void)__setDefaultFormValueEncoding:__ (NSStringEncoding)_anEncoding_

Sets the default string encoding for the receiver to use when converting its form values from ASCII to Unicode. The default string encoding is called into play if the WORequest cannot detect an encoding from the ASCII form values or if encoding detection is disabled. If no default form value encoding is explicitly set, the WORequest uses NSISOLatin1StringEncoding.

__See also:__
[- __defaultFormValueEncoding__](#apple-g42q), __[- setFormValueEncodingDetectionEnabled:](#apple-ge2do)__

---

### setFormValueEncodingDetectionEnabled:

- (void)__setFormValueEncodingDetectionEnabled:__ (BOOL)_flag_

Enables or disables automatic detection of the best encoding for the receiver to use when it converts form values from ASCII to Unicode. When detection is enabled, a WORequest object scans the ASCII form values and applies heuristics to decide which is the best encoding to use. If no specific encoding is discernible, or if detection is disabled, the WORequest uses the default form value encoding for the conversion.

__See also:__
[- __isFormValueEncodingDetectionEnabled__](#apple-geyts),__[- setDefaultFormValueEncoding:](#apple-guztomi)__

---

### uri

- (NSString \*)__uri__

Returns the Uniform Resource Identifier (URI) the WORequest was initialized with. For a session's first request, the URI indicates the resource that the request is seeking (such as a WebObjects application); for subsequent requests in the session, the URI indicates which page of the application should handle the request. If the request was caused (as is usually the case) by a web browser submitting a URL to an HTTP server, the URI is that part of the URL that follows the port number. Because the format of WebObjects URLs and the corresponding request URI might change between different versions of WebObjects, you should not attempt to parse the URI returned by this method. Instead, use WORequest's accessor methods to access particular URI/URL components.

__See also:__
[- __adaptorPrefix__](#apple-gqzq), [- __applicationName__](#apple-gq3q), __[- applicationNumber](#apple-guyq)__

---

### userInfo

- (NSDictionary \*)__userInfo__

Returns the value of the user information the receiver was initialized with (__nil__  by default). WebObjects imposes no restrictions on the format or content of the user information dictionary. In fact, WebObjects classes do not themselves use the dictionary, but just pass it around as the request is handled. Custom adaptors, for example, could initialize the dictionary with special information for other objects of an application.

****

---

[!](WOMailDelivery-2.md)
[!](WORequestHandler-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
