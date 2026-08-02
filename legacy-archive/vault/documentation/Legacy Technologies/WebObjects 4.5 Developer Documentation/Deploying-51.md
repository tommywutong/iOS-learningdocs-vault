---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-51.html
archived_at: '2026-07-15T08:05:06.366105Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Deploying%20WebObjects%20Applications.md) [!](Using%20woservice%20on%20Mac%20OS%20X%20Server-2.md)

---

### The WebObjects Application URL

The typical WebObjects application URL has the following format:

`http://
host
[:
port
]/
cgi-bin
/
WebObjects
/
App
[[.woa][/
instance
]/
key
/...`

where the variables are defined as follows:

| Variable | Description |
| --- | --- |
| host | The host name of your computer or __localhost__ . |
| port | The port number. This is included if you want to direct connect. |
| cgi-bin | The cgi-bin directory of your server, usually __cgi-bin__ or __Scripts__ . |
| WebObjects | The name of the CGI adaptor, usually __WebObjects__ or __WebObjects.exe__ . |
| App | The application name. The __WOApplicationBaseURL__ option provides the path to the application. |
| instance | The application instance number. |
| key | The request handler key. This key specifies which WORequestHandler object should be used to process the request., and is typically either "wo" (the component request handler) or "wa" the direct action request handler). |
| ... | Information specific to the request handler. Each WORequestHandler uses a different format for the rest of the URL.  The two main request handlers are WOComponentRequestHandler and WODirectActionRequestHandler. The WOComponentRequestHandler's format for the rest of the URL is:  _componentName_ /_sessionID_ /_elementID_  WODirectActionRequestHandler handles direct actions. Its URLs have this format:  [_actionClass_ | _actionName_ | _actionClass_ /_actionName_ ][?_key_ =_value_ &_key_ =_value_ .....]  For more detailed information, see the _WebObjects Developer's Guide_ . |

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Deploying%20WebObjects%20Applications.md) [!](Using%20woservice%20on%20Mac%20OS%20X%20Server-2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
