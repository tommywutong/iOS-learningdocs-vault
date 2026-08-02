---
title: Unsolicited About Boxes
apple_id: DTS10003370
resource_type: QA
platform: Java
topic: Cross Platform
technology: null
published: '2011-05-05'
source_url: https://developer.apple.com/library/archive/qa/qa1363/_index.html
archived_at: '2026-07-18T02:30:26.299006Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1363

# Unsolicited About Boxes

## Q:  My Java application has an ApplicationListener with a handleAbout() method, but the default about box still appears over my own when "About MyApp" is selected from the Application menu. Why?

A: Important:

This Q&A refers to the eAWT APIs that were introduced with Java 1.4.1 on Mac OS X. These APIs were deprecated in Java SE 6 and J2SE 5.0 with the release of "Java for Mac OS X 10.6 Update 3" and "Java for Mac OS X 10.5 Update 8".

Please use the [Application.setAboutHandler(AboutHandler)](https://developer.apple.com/library/mac/documentation/Java/Reference/JavaSE6_AppleExtensionsRef/api/com/apple/eawt/Application.html#setAboutHandler%28com.apple.eawt.AboutHandler%29) and [Application.setQuitHandler(QuitHandler)](https://developer.apple.com/library/mac/documentation/Java/Reference/JavaSE6_AppleExtensionsRef/api/com/apple/eawt/Application.html#setQuitHandler%28com.apple.eawt.QuitHandler%29) which do not require explicit event overriding by design.

The problem is that the `ApplicationEvent` received by `handleAbout()` needs to marked as handled; otherwise the eAWT does not know if you have actually handled the request. This is stated in the [eAWT javadocs](https://developer.apple.com/library/mac/documentation/Java/Reference/JavaSE6_AppleExtensionsRef/api/com/apple/eawt/ApplicationListener.html#handleAbout%28com.apple.eawt.ApplicationEvent%29), but commonly overlooked.

Below is a simplified example of a proper `handleAbout` method. Note that at the end of the method, a call to `ApplicationEvent.setHandled(true)` is made. Without this call, the eAWT will assume that you have not actually handled the event and will put up its own default about box.

__Listing 1__  Suppressing the default aboutBox using setHandled(true).

```
public void handleAbout(ApplicationEvent e) {
   new AboutBox().show();
   // Tell eAWT you've handled the request, disabling the default about box.
   e.setHandled(true);
}
```

A similar problem may occur with the `handleQuit` method; in this case, you actually call `ApplicationEvent.setHandled(true)` to allow the application to quit. In other words, you have successfully handled the quit request and are ready for the default handler to continue.

__Listing 2__  Authorizing a quit using setHandled(true).

```
public void handleQuit(ApplicationEvent e) {
   cleanupResources();
   // The quit request is handled; proceed with app termination
   e.setHandled(true);
}
```

If you wish to have complete control over the quit and call `System.exit()` yourself, for example, set the event's state to false in your `handleQuit` method. Note that although the default handled state of an `ApplicationEvent` is false, we still recommend setting the state explicitly to ensure the behavior you want.

__Listing 3__  Rejecting a quit using setHandled(false).

```
public void handleQuit(ApplicationEvent e) {
   // Reject the quit request and handle it as we see fit
   e.setHandled(false);
   String msg = "Are you sure you want to quit?"
   int result = JOptionPane.showConfirmDialog(mainFrame, msg);
   if (result == JOptionPane.YES_OPTION) {
      System.exit(0);
   }
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-05-05 | Fixing dead link to the eAWT reference. |
| 2004-08-31 | Formatting changes in code listings |
| 2004-08-25 | New document that how to override the default eAWT about and quit behaviors in Java |

