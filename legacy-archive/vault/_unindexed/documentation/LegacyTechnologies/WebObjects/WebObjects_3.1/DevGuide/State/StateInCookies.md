---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/StateInCookies.html
archived_at: '2026-07-15T07:47:52.956405Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](StateInPage.md)

# State in Cookies

A "cookie" is another way that a web application can store state information in the client machine. Instead of being part of the HTML page as with the state-in-the-page mechanism, a cookie is passed as part of the HTTP header information. The syntax for the cookie header line is:

```
Set-Cookie: NAME=VALUE; expires=DATE; domain=DOMAIN_NAME; path=PATH; secure
```

The NAME=VALUE association is the only required field. It holds the cookie's data and the name by which it can be accessed. The other fields are optional and set limitations on when the data will be passed from the client back to the server:

---

**__expires__**
: The date after which the cookie is no longer valid. Once a cookie expires, the client will no longer return it to the server, and client is free to delete it.

**__domain__**
: The Internet domain name for which the cookie is valid. For example, if the specified domain is __apple.com__ for a given cookie, that cookie will be returned along with a request to any host whose domain ends with __apple.com__ (for example, __www.apple.com__)---assuming the URL is within the directories specified by __path__.

**__path__**
: The directories within a given domain for which this cookie is valid. For example, if a cookie has a domain of __www.apple.com__ and a path of __/devDoc__, the client will return the cookie to the server for any request that begins with __http://www.apple.com/devDoc...__

**__secure__**
: Specifies that the cookie can only be passed using a secure communications channel, such as SHTTP.

---

See __http://www.netscape.com/newsref/std/cookie_spec.html__ for a complete description of cookies.

WebObjects makes it simple to use cookies as a state storage mechanism. As you might expect, you generally set the application's session storage type in the __init__ method of the application script:

```
- init {
    [super init];
    [self setSessionStore:
        [WOSessionStore cookieSessionStoreWithDomain:@"" secure:NO]];
    return self;
}
```

In this case, we set the domain to the empty string so that cookies that this application sends to the user are valid for all domains. We also turn off the requirement for a secure communications channel. Note that the cookie store API doesn't allow for a path argument. WebObjects automatically restricts the path so that cookies that an application produces are only valid within the application directory. For example, if you set the SessionStores application to use a cookie session store, the client only returns a cookie if the request URLs have this prefix:

```
/cgi-bin/WebObjects/Examples/SessionStores.woa/
```

Once the cookie session store has been established as the application's state storage mechanism, WebObjects does the rest. Just as with storing state in the page, WebObjects packages the session state by archiving the session object (and all the component objects that it contains) into an NSData object. The NSData object is then asked for its ASCII representation. WebObjects pairs this data with names it generates and creates the Set-Cookie headers of the response page.

The process is reversed when a user submits a request containing cookies. The ASCII archive from the Set-Cookie headers is converted to its binary, NSData, representation. The session object and the components it contains are then unarchived from the NSData object, thus restoring the session state.

One of the big advantage of using cookies over state in the page is that cookie storage does not require your application to be designed around forms. As you recall, storing state in the page implied using hidden field elements, which must be located in HTML forms. Cookies, however, are stored in the HTTP header so are independent of the HTML elements in the page. With a cookie session store you could, for example, let users navigate from page to by using hyperlinks rather than by submitting forms. In addition (and for similar reasons), storing state in cookies works better with frames than does storing state in the page.

You should be aware, however, that the cookie mechanism has a size restriction that limits its usefulness. Currently, cookie data is passed from the HTTP server to the WebObjects application either through environment variables that typically are limited to 8K bytes or through a server's own API that in some cases is even more restrictive. We recommend that cookie state data (that is the ASCII representation of the state data) be kept to 2K bytes or less. Given these limitations, cookies can be best used for such things as storing keys used to fetch information from a database.

[!Table of Contents](ManagingState.book.md)
[!Next Section](CustomStorageOptions.md)
