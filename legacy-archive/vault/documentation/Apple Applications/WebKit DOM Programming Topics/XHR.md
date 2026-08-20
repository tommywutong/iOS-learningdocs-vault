---
title: WebKit DOM Programming Topics
apple_id: TP40001483
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: WebKit
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/XHR.html
archived_at: '2026-07-15T05:18:15.849129Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit DOM Programming Topics](index.md)



## Fetching with XMLHttpRequest

Safari, Dashboard, and WebKit-based applications support the JavaScript `XMLHttpRequest` object. `XMLHttpRequest` (often abbreviated as XHR) allows you to easily fetch content from a server and use it within your webpage or widget without requiring a page reload.

For example, you can use XHR to update a store search page so that when the user enters a Zip code, your site can display stores within a reasonable distance. Clicking on a store could then fill a particular content div with details on that store.

Of course, you could do any of these things without XHR (by requiring a full page load or by including information about every store in the country in a single page), but XHR provides a way to do this more efficiently with less bandwidth.

### About XMLHttpRequest

`XMLHttpRequest` is a JavaScript object provided by WebKit that fetches data via HTTP for use within your JavaScript code. It’s tuned for retrieving XML data but can be used to perform any HTTP request. XML data is made available in a DOM object that lets you use standard DOM operations, as discussed in [Using the Document Object Model](DOM.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiztolkciffeosskifea), to extract data from the request response.

Typically, you define an `XMLHttpRequest` object’s options and provide an `onload` or `onreadystatechange` handler, then send the request. When the request is complete, you work with either the request’s response text or its response XML, as discussed in [XMLHttpRequest Responses](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3demrxfvjvomq).

### Defining an XMLHttpRequest Object

To create a new instance of the `XMLHttpRequest` object, call the object’s constructor with the `new` keyword and save the result in a variable, like this:

1. `var myRequest = new XMLHttpRequest();`

> [!NOTE]
> 

After you have created a new `XMLHttpRequest` object, call `open` to initialize the request:

1. `myRequest.open("GET", "http://www.apple.com/");`

The `open` method requires two arguments: the HTTP method and the URI of the data to fetch. It also can take three more arguments: an asynchronous flag, a username, and a password. By default, `XMLHttpRequest` executes asynchronously.

After you open the request, use `setRequestHeader` to provide any optional HTTP headers for the request, like this:

1. `myRequest.setRequestHeader("Cache-Control", "no-cache");`

> [!NOTE]
> 

To handle the different states of a request, set a handler function for the `onreadystatechange` event:

1. `myRequest.onreadystatechange = myReadyStateChangeHandlerFunction;`

If the only state you’re concerned about is the `loaded` state (state `4`), try using the `onload` event instead:

1. `myRequest.onload = myOnLoadHandlerFunction;`

When the request is ready, use the `send` method to send it:

1. `myRequest.send();`

If your request is sending content, like a string or DOM object, pass it in as the argument to the `send` method.

### XMLHttpRequest Responses

After you send your request, you can abort it using the `abort` method:

1. `myRequest.abort();`

If you provided an `onreadystatechange` handler, you can query your request to find its current state using the readyState property:

1. `var myRequestState = myRequest.readyState;`

A `readyState` value of `4` means that content has loaded. This is similar to providing an `onload` handler, which is called when a request’s `readyState` equals `4`.

When a request is finished loading, you can query its HTTP status using the `status` and `statusText` properties:

1. `var myRequestStatus = myRequest.status;`
2. `var myRequestStatusText = myRequest.statusText;`

Also, you can fetch the request’s HTTP response headers using the `getResponseHeader` method:

1. `var aResponseHeader = myRequest.getResponseHeader("Content-Type");`

To obtain a list of all of the response headers for a request, use `getAllResponseHeaders`:

1. `var allResponseHeaders = myRequest.getAllResponseHeaders();`

To obtain the request’s response XML as a DOM object, use the responseXML property:

1. `var myResponseXML = myRequest.responseXML;`

This object responds to standard DOM methods, like `getElementsByTagName`. If the response is not in a valid XML format, use the `responseText` property to access the raw text response:

1. `var myResponseText = myRequest.responseText;`

### Security Considerations

Within Safari, the `XMLHttpRequest` object can only make requests to `http` and `https` URIs in the same domain as the webpage.

As an exception, however, beginning with Safari 4.0, a website can allow content served by other websites to request data from specific `http` and `https` URLs on their servers.

> [!NOTE]
> 

### Using XMLHttpRequest for Cross-Site Requests

For the most part, the `XMLHttpRequest` object works the same way when used in a cross-site fashion. There are a few exceptions, however.

- cookies—Because the JavaScript code is not in the same domain, it is not possible to set or read cookies for that domain.
- authentication tokens—As with cookies, it is not possible to add or read authentication information for the remote domain.

  > [!NOTE]
  > 
- `Referer` header—Because it can contain confidential path information, the `Referer` header is not sent to the remote site. You can, however, check the `Origin` header to determine the domain name of the referring page.
- other headers—Most HTTP headers are explicitly scrubbed both when sending and receiving. The only headers that are sent are:

  - `Accept`—a comma-separated list of Internet Media Type values (as defined in [RFC 1590](http://www.ietf.org/rfc/rfc1590.txt)) that are acceptable as a response for the request. These may be tagged with quality values to indicate a preference for one type over another.

    For example, Accept: `text/html, text/plain;q=.5` indicates that the caller prefers HTML data with an implied quality of `1`, but will also accept plain text data with an explicit quality of `0.5`

    The second field may be replaced with an asterisk (\*) wildcard character (`Accept: text/*`, for example). The first field may also be a wildcard if and only if the second field contains a wildcard (`Accept: */*`).
  - `Accept-Language`—a comma-separated list of natural languages preferred by the user, optionally tagged with quality values for each language. The language tag values are defined by [RFC 1766](http://www.ietf.org/rfc/rfc1766.txt).

    For example, `Accept-Language: de, en-gb;q=.5, es` indicates the user prefers German or Spanish with implied quality of `1`, but will tolerate British English with an explicit quality of `0.5`.
  - `Content-Language`—the natural language of the content of the request (`en-US`, for example), as defined by [RFC 1766](http://www.ietf.org/rfc/rfc1766.txt).
  - `Content-Type`—the Internet Media Type for the data in the request (`Content-Type: text/html`, for example), as defined in [RFC 1590](http://www.ietf.org/rfc/rfc1590.txt).
  - `Origin`—sent by the browser to indicate the domain from which the request was sent. This field contains the non-path portion of the URL (`http://example.com`, for example).

    > [!NOTE]
    > 

  The only headers your script can expect to receive from the server (after the browser filters them) are:

  - `Host`—provides the host name and port number of the server sending a response.
  - `Cache-Control`—provides caching policy information.
  - `Content-Language`—a comma-separated list of natural language of the content (`en-US`, for example), as defined by [RFC 1766](http://www.ietf.org/rfc/rfc1766.txt).
  - `Content-Type`—the Internet Media Type for the data in the response (`Content-Type: text/html`, for example), as defined in [RFC 1590](http://www.ietf.org/rfc/rfc1590.txt).
  - `Expires`—the date and time at which any cache of this data should be discarded. The date format is specified by [RFC 1123](http://www.ietf.org/rfc/rfc1123.txt).
  - `Last-Modified`—the most recent date and time when the document’s contents were modified. The date format is specified by [RFC 1123](http://www.ietf.org/rfc/rfc1123.txt).
  - `Pragma`—used for optional implementation-specific directives that may apply to intermediate web caches, the browser, and so on.

  All other headers may be scrubbed.

> [!WARNING]
> 

### Access Control Request Headers

Before performing the actual request, the browser first sends an `OPTIONS` query to the server to ask if it is allowed to send the actual request. The following headers are sent by the browser as part of this query and may be used by scripts on the remote web server when deciding whether or not to allow the request:

|  |  |
| --- | --- |
| **`Origin`** | : Contains the non-path portion of the resource making the request (for example, `http://example.com`). |
| **`Access-Control-Request-Method`** | : Contains the method that the actual request will use (`GET` or `POST`, for example). |
| **`Access-Control-Request-Headers`** | : Indicates which HTTP headers will be sent in the actual request. |

### Access Control Response Headers

Before performing the actual request, the browser first sends an `OPTIONS` query to the server to ask if it is allowed to send the actual request. The following headers may be sent by the remote web server (or scripts running on that server) in response to this request to control cross-site access policies:

|  |  |
| --- | --- |
| **`Access-Control-Allow-Origin`** | : Indicates that a particular origin can access the resource. The value may be either a specific origin (`http://example.com`, for example) or an asterisk (`*`) wildcard, which allows any domain to access the resource. |
| **`Access-Control-Max-Age`** | : Indicates how long a browser should continue to cache the site’s acceptance of requests from other domains. If your site only allows requests from other domains after some specific handshake by a user, for example, you might set this to a short value. |
| **`Access-Control-Allow-Credentials`** | : Indicates that the request may be made with credentials. The only allowable value is `true`. To disallow credentials, omit this header. |
| **`Access-Control-Allow-Methods`** | : Provides a request method that the script may use for future requests (`GET` or `POST`, for example). The valid methods are defined in [RFC 2616](http://www.ietf.org/rfc/rfc2616). This field may be specified more than once to allow multiple methods. |
| **`Access-Control-Allow-Headers`** | : Provides a header field name that the client has permission to use in the actual request. |

[Responding to Force Touch Events](RespondingtoForceTouchEventsfromJavaScript.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnrsfvjvomi)

[Sending Notifications](SendingNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsmzsfvjvomi)
