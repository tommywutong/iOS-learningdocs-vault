---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.039.html
archived_at: '2026-07-15T07:58:45.357366Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](WOMailDelivery%20Class.md)

# Cookie API

The WebObjects Framework contains new classes and methods that allow you to use cookies more easily:

- The WORequest class has new methods that allow you to extract cookie data from the request.
- The WOResponse class has new methods that allow you to add a cookie to the response.
- The WOSession class has new methods that enable and disable the cookie mechanism, and control various aspects of that mechanism.
- A new class, WOCookie, defines the cookies that you add to the response.

  |  WORequest Cookie Methods |  |
  |  Method |  Description |
  |  cookieValuesForKey: |  Returns an array of values for a cookie key. Use this method to retrieve information stored in a cookie in an HTTP header. Valid keys are specified in the cookie specification. |
  |  cookieValueForKey: |  Returns a string value for a cookie key. |
  |  cookieValues |  Returns a dictionary of cookie values and cookie keys. |

```
```

  |  WOResponse Cookie Methods |  |
  |  Method |  Description |
  |  addCookie: |  Adds a WOCookie object to the response. |
  |  removeCookie: |  Removes a WOCookie object from the response. |
  |  cookies |  Returns an array of WOCookie objects to be included in the response. |

```
```

  |  WOSession Cookie Methods |  |
  |  Method |  Description |
  |  setStoresIDsInCookies: |  Enables and disables the storing of session and instance IDs in cookies. |
  |  storesIDsInCookies |  Returns whether session and instance IDs are stored in cookies. |
  |  expirationDateForIDCookies (Objective-C only) |  Override to return an expiration date for cookies created for the purpose of storing session and instance IDs (by default, no expiration is set). |
  |  domainForIDCookies (Objective-C only) |  Returns the path passed when creating a session or instance ID cookie. |

```
```


A WOCookie object defines a cookie that can be added to the HTTP header for your response. You create a cookie using one of two methods:

|  WOCookie Creation Methods |
|  Method |
|  cookieWithName:value: (Objective-C)  cookieWithName(String, String) (Java) |
|  cookieWithName:value:path:domain:expires:isSecure: (Objective-C)  cookieWithName(String, String, String, String, NSDate, boolean) (Java) |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.040.md)
