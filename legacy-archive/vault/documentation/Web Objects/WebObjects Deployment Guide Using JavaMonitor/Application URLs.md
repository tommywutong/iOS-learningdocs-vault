---
title: WebObjects Deployment Guide Using JavaMonitor
apple_id: TP30001009
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Deployment/Deploying_Applications/ApplicationURL/ApplicationURL.html
archived_at: '2026-07-18T02:15:18.575154Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Deployment Guide Using JavaMonitor](Introduction%20to%20WebObjects%20Deployment%20Guide%20Using%20JavaMonitor.md)


[Next](JMX%20Monitoring.md)[Previous](Application%20Administration.md)

# Application URLs

An application URL with a specific format is used to make an initial request to a WebObjects application. The host identified in the URL receives the request and passes it to the WebObjects adaptor identified in the URL. The adaptor receives the request, repackages it into a standard format, and sends it to the appropriate WebObjects application instance. This section describes the format of this URL so that you can connect directly to an application instance from a browser. This URL is very useful for both development and deployment.

There are three ways to connect to an application instance:

- Connect directly to an application instance. The browser sends requests and receives responses directly from the application—the web server is not involved. The browser is connected directly to the port used by the application. Application resources—such as images—are served by the application. This approach does not require use of wotaskd or JavaMonitor.

  This is an example of a direct connect URL:

  `http://localhost:2001/cgi-bin/WebObjects/MyApp.woa`
- Connect through the web server to a deployed application. The browser communicates with the web server typically using port `80`. The web server passes requests to the WebObjects HTTP adaptor, which passes it to the application. The application sends responses to the adaptor, the adaptor sends them to the web server, and the web server sends them to the browser. Application resources are served by the web server. Therefore, this approach requires a split installation.

  This is an example of a deployed URL:

  `http://host/cgi-bin/WebObjects/MyApp.woa`
- Connect through the web server to a development application—an application that is running but not deployed. This approach is similar to accessing a deployed application except that load-balancing between instances does not occur. Use this approach to test an application through the web server without fully deploying it.

  This is an example of a development URL:

  `http://host/cgi-bin/WebObjects/MyApp.woa/-2001`

The format of a WebObjects application URL depends on the type of URL connection.

The URL format for an application in direct connect mode is:

```
http:// host:port/ cgi-bin / WebObjects / App[.woa [/ key /  ...]]
```

The URL format for an application in deployment mode is:

```
http:// host / cgi-bin / WebObjects / App [.woa [/ instance [/ key /...]]]
```

The URL format for an application in development mode is:

```
http: // host / cgi-bin / WebObjects / App.woa / -port [/ key / ... ]
```

Table 7-1 describes the variables in these URL formats.

__Table 7-1__  WebObjects application URL variables

| Variable | Description |
| `host` | The host name of your computer or `localhost`. |
| `port` | The port number. If you are connecting directly to the application instance, include the port number. |
| `cgi-bin` | The `cgi-bin` directory of your server, usually `cgi-bin` or `Scripts`. |
| `WebObjects` | The name of the CGI adaptor, usually `WebObjects`. |
| `App` | The application name. The `WOApplicationBaseURL` property described in _[WebObjects Application Properties Reference](../WebObjects%20Application%20Properties%20Reference/Introduction%20to%20WebObjects%20Application%20Properties%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamrq)_ specifies the path to the application. |
| `instance` | The application instance number. |
| `key` | The request handler key. This key specifies which WORequestHandler object should be used to process the request and is typically either `wo` (the component request handler) or `wa` (the direct action request handler). |
| ... | Information specific to the request handler. Each WORequestHandler uses a different format for the rest of the URL. See Table 7-2 for component actions and Table 7-3 for direct actions. |

The two main request handlers are `WOComponentRequestHandler` and `WODirectActionRequestHandler` for component action URLs. The rest of the format for component action URLs is:

```
componentName / sessionID / elementID
```

Table 7-2 describes the variables in a component action URL.

__Table 7-2__  Component action URL variables

| Variable | Description |
| `componentName` | Name of the WOComponent class. |
| `sessionID` | The session identifier. |
| `elementID` | The element identifier. |

`WODirectActionRequestHandler` handles direct actions. The rest of the format for direct action URLs is:

```
[ actionClass | actionName | actionClass / actionName ][? key = value &amp; key = value .....]
```

Table 7-3 describes the variables in a direct action URL.

__Table 7-3__  Direct action URL variables

| Variable | Description |
| `actionClass` | The name of the WODirectAction class in which the action method is defined. If actionClass is not specified, class DirectAction is assumed. |
| `actionName` | The name of the action method. If `actionName` is not specified, the `defaultAction` method on `actionClass` is assumed. |
| `key` | The key portion of a key-value pair in the URL query string |
| `value` | The value portion of a key-value pair in the URL query string. |

[Next](JMX%20Monitoring.md)[Previous](Application%20Administration.md)

