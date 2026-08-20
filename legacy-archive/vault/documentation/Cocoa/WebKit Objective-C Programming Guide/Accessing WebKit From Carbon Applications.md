---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/CarbonApps.html
archived_at: '2026-07-15T07:14:48.291993Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Determining%20WebKit%20Availability.md)[Previous](Spoofing.md)

# Accessing WebKit From Carbon Applications

To access WebKit from a Carbon application, you use the Carbon WebKit API to create a Carbon web view. Once you have added the view to a window, you need to load and display URL content using native Cocoa classes.

Before using any web views, you need to call the `WebInitForCarbon` function. Doing so initializes Cocoa so you can access WebKit from your Carbon application.

To create a web view, you simply call the `HIWebViewCreate` function. This function returns an HIView reference, and as such you can use any of the standard HIView manipulation functions on it. For example, you can embed the web view within another window or view, resize it, and so on.

For example, the following code fragment creates a web view and embeds it in a window:

```
    WindowRef       window;
    HIViewRef       webView, contentView;
    HIRect          bounds;
    CFURLRef        url;

    // Create your window here
    …

    // Get a URL here, as a CFURL
    …

    WebInitForCarbon(); // initialize WebKit

    HIWebViewCreate( &webView ); // create the web view

    // Now obtain the content view associated with the window
    HIViewFindByID( HIViewGetRoot( window ), kHIViewWindowContentID,
                     &contentView );

    // Set the bounds of the web view to be the same as the content view
    HIViewGetBounds( contentView, &bounds );
    HIViewSetFrame( webView, &bounds );

    // Embed the web view in the content view and make it visible
    HIViewAddSubview( contentView, webView );
    HIViewSetVisible( webView, true );

    // Make a call to load URL content */
    LoadURL( webView, url );
```

To manipulate the contents of the web view, you need access to the actual Cocoa view. You obtain a reference to the Cocoa WebView object by calling the `HIWebViewGetWebView` function. You can then make Objective-C calls to WebKit using that object. The example function `LoadURL` shows how you could do this:

```
static void LoadURL( HIViewRef inView, CFURLRef inURL )
{
    WebView*            nativeView;
    NSURLRequest*       request;
    WebFrame*           mainFrame;

    nativeView = HIWebViewGetWebView( inView ); // get the Cocoa view

    // Use Objective-C calls to load the actual content
    request = [NSURLRequest requestWithURL:(NSURL*)inURL];
    mainFrame = [nativeView mainFrame];
    [mainFrame loadRequest:request];
}
```

See _WebKit C Reference_ for more details about the Carbon WebKit functions.

[Next](Determining%20WebKit%20Availability.md)[Previous](Spoofing.md)

