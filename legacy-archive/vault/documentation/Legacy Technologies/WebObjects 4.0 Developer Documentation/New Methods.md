---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.037.html
archived_at: '2026-07-15T07:58:44.287031Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](Improved%20Image%20Loading.md)

# New Methods

This section details various new methods added to the classes that make up the WebObjects Framework.

|  WOAdaptor |  |
|  Method |  Description |
|  runOnce |  The main application run loop invokes this method for each iteration through the request-response loop. This method is where adaptors should do the bulk of their work. |
|  doesBusyRunOnce |  An adaptor should implement this method to return whether repeatedly invoking __runOnce__ would result in busy waiting. |
|  dispatchesRequestsConcurrently |  An adaptor should implement this method to return __YES__ or true if the adaptor contains multiple threads and concurrently invokes request handlers. |

```
```

|  WOApplication |  |
|  Method |  Description |
|  handleInitialTimer |  Initial timer callback method. |
|  cancelInitialTimer |  Cancels the initial timer. |

```
```

|  WOComponent |  |
|  Method |  Description |
|  validationFailedWithException:value:keyPath: (Objective-C)  validationFailedWithException (Java) |  Called when an enterprise object or a formatter failed validation during an assignment. The default implementation of this method ignores the error. Subclassers can override it to record the error and possibly return a different page for the current action. |
|  hasSession |  A convenience method that returns __YES__ or __true__ if there is a current session. |
|  pageWithName: |  A convenience method that returns the WOComponent with the specified name. |

```
```

|  WOContext |  |
|  Method |  Description |
|  contextWithRequest: |  Returns a new WOContext for the specified WORequest object. |
|  initWithRequest: (Objective-C only) |  Initializes a newly-created WOContext object with the specified WORequest. |
|  hasSession |  Returns whether the session exists. |
|  isInForm |  Returns whether WebObjects is executing code within a WOForm. Invoking __setInForm:__ with __true__ or __YES__ also causes this method to return __true__ or __YES__. Use this method when writing your own WOForm dynamic element, or an input type dynamic element. |
|  setInForm: |  Forces the value returned by __isInForm__. Invoking this method impacts all elements processed thereafter. Use this method when writing your own WOForm dynamic element, or an input type dynamic element. |
|  directActionURLForActionNamed:queryDictionary: (Objective-C)  directActionURLForActionNamed (Java) |  Returns the full URL for the named action. |
|  componentActionURL |  Returns the full URL for the element you are currently at. |
|  urlWithRequestHandlerKey:path:queryString: (Objective-C)  urlWithRequestHandlerKey (Java) |  Returns a URL relative to cgi-bin/WebObjects for the specified request handler. |
|  completeURLWithRequestHandlerKey:path: queryString:isSecure:port: (Objective-C)  completeURLWithRequestHandlerKey (Java) |  Returns the complete URL for the specified request handler, including __http://__ or __https://__. |

```
```

|  WODisplayGroup |  |
|  Method |  Description |
|  setSelectedObjects: |  Sets the selected objects. |
|  setSelectedObject: |  Sets the selected object. |
|  indexOfFirstDisplayedObject |  Returns the index of the first object in the current batch. |
|  indexOfLastDisplayedObject |  Returns the index of the last object in the current batch. |

```
```

|  WORequest |  |
|  Method |  Description |
|  browserLanguages |  Returns the language preference list from the user's browser. |
|  formValues |  Returns an NSDictionary containing all of the form data name/value pairs. |

```
```

|  WOResponse |  |
|  Method |  Description |
|  disableClientCaching |  Disables caching of this response in the user's browser. |
|  defaultEncoding (Objective-C) |  Returns the default character encoding used to construct WOResponses. By default, this encoding is NSISOLatin1. |
|  setDefaultEncoding: (Objective-C) |  Allows you to specify the character encoding that is used by default when constructing WOResponses. |
|  stringByEscapingHTMLString: |  Returns the supplied string with certain characters escaped out. Use this method to escape strings which will appear in the visible part of an html file (that is, not inside a tag). |
|  stringByEscapingHTMLAttributeValue: |  Returns the supplied string with certain characters escaped out. Use this method to escape strings which will appear as attribute values of a tag. |

```
```

|  WOSession |  |
|  Method |  Description |
|  removeObjectForKey: (Objective-C only) |  Removes the object from the session dictionary that corresponds to the specified key. |
|  setDefaultEditingContext: |  Sets the editing context to be returned by __defaultEditingContext__. This can be used to set an editing context initialized with a parent object store other than the default (useful, for instance, when each session needs its own login to the database). |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](WOMailDelivery%20Class.md)
