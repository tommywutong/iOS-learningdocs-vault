---
title: Hang launching signed Applets from JavaScript
apple_id: DTS10003464
resource_type: QA
platform: macOS
topic: Languages & Utilities
technology: null
published: '2004-12-02'
source_url: https://developer.apple.com/library/archive/qa/qa1395/_index.html
archived_at: '2026-07-18T02:30:31.396487Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1395

# Hang launching signed Applets from JavaScript

## Q:  I use LiveConnect in a JavaScript `onLoad()` handler, and my Applet hangs before it's finished loading.

A: In Java 1.4.2 Update 2 on Mac OS X 10.3 there is a potential for a hang if LiveConnect is used to call a method in a signed applet if the applet has not yet been loaded and the certificate used to sign the applet has not yet been authenticated as trusted.

To workaround the issue, make sure the signed applet is trusted before making LiveConnect calls to the applet's methods. Since JavaScript can't detect if the applet is loaded and trusted without using LiveConnect, an easy solution is for the applet to call out to a JavaScript function to let it know that it is loaded and that it is safe to call applet methods. For example, if the JavaScript function being used to notify it that an applet has been loaded is called `appletLoaded()`, as shown in Listing 1, the following listings show how to call it from the applet's `init()` method. Listings 2, and 3 show example java code that can be used by the applet to call out to the JavaScript. Listing 2 shows calling out to JavaScript using the applet's context, and Listing 3 shows calling out to JavaScript using LiveConnect. Using the applet's context as show in Listing 2 requires less overhead because LiveConnect doesn't need to be initialized, but the end result is the same for both.

__Listing 1__  HTML and JavaScript showing the example appletLoaded() function.

```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"         "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en"> <html> <head>     <title>LiveConnect Applet Example</title> </head>     <body>         <script type="text/javascript" language="JavaScript">             <!--             var OkToScriptJavaToJavaScriptApplet = 0;              function appletLoaded() {                OkToScriptJavaToJavaScriptApplet = 1;                // It is now safe to call back into the applet from JavaScript                // Either call needed functions directly from this function,                // or verify that OkToScriptJavaToJavaScriptApplet is not zero                // before calling it from another function.                }             //-->          </script>         <applet archive="JavaToJavaScriptApplet.jar" code="JavaToJavaScriptApplet"             width=600 height=100 name=JavaToJavaScriptApplet mayscript>             Your browser does not support Java, so nothing is displayed.         </applet>     </body> </html>
```


__Listing 2__  Calling JavaScript from Java using the showDocument method.

```
public void init() { try {     getAppletContext().showDocument(new java.net.URL("javascript:appletLoaded()"), "_self");     } catch (java.net.MalformedURLException e) {e.printStackTrace();} }
```


__Listing 3__  Calling JavaScript from Java using LiveConnect.

```
public void init() {     JSObject win = JSObject.getWindow(this);     win.eval("appletLoaded()"); }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-12-02 | New document that making a LiveConnect call to a signed Applet before that Applet has finished loading can cause a hang. |

