---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/BackForwardList.html
archived_at: '2026-07-15T07:14:47.835934Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Managing%20History.md)[Previous](Loading%20Resources.md)

# Paging Back and Forward

A WebView object uses a _[WebBackForwardList Class Reference](https://developer.apple.com/documentation/webkit/webbackforwardlist)_ object to maintain a list of visited pages used to page back and forward to the most recent page. WebView provides methods to handle the action of going forward or backward in this list; therefore, you can easily add Back and Forward buttons to your application.

By default, every `WebView` object maintains its own back-forward list object. There is some overhead in maintaining this list. If you don't want to use this feature, send a [setMaintainsBackForwardList:](https://developer.apple.com/documentation/webkit/webview/1408510-setmaintainsbackforwardlist) message to your `WebView` object as in:

```
[webView setMaintainsBackForwardList:NO];
```

Otherwise, history items, which encapsulate visited page information, are automatically added and removed from the back-forward list as webpages are loaded and displayed in a WebView. If you maintain a back-forward list in your `WebView` object, then you should add some buttons to your user interface so that users can use this feature.

You don't have to write a single line of code to implement Back and Forward buttons in your application. Follow these steps to add these buttons:

1. Using Interface Builder, add a Back and Forward button to your window.
2. Using Interface Builder, connect the Back and Forward buttons to the WebView object by selecting, respectively, the [goBack:](https://developer.apple.com/documentation/webkit/webview/1408482-goback) and [goForward:](https://developer.apple.com/documentation/webkit/webview/1408365-goforward) actions.
3. Build and run your application.

When running your application, connect to a URL, follow a few links (to generate some history items in your back-forward list), and then click the Back and Forward buttons. WebKit maintains the back-forward list for you, and the action methods initiate new page requests.

You can use back-forward lists to maintain a page cache too. Because pages in the cache are rendered quickly, using this feature improves the performance of the back-forward action methods. You can turn this feature on or off by setting the cache size using the `WebBackForwardList` object’s [setPageCacheSize:](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419961-setpagecachesize) method. If you set the page cache size to `0`, the page cache is disabled; otherwise, the size of the cache is limited to the number of pages you specify. The default page cache size may vary depending on your computer’s configuration. Use the [pageCacheSize](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419946-pagecachesize) method to get the current setting.

You can also limit the capacity of the back-forward list itself using the [capacity](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419938-capacity) property. Setting the capacity affects only the number of history items allowed in the back-forward list. It doesn't affect the page cache. Use the `capacity` property to get the current setting.

If you manipulate a back-forward list directly, you need to be aware of how it works. A back-forward list is like an array that can expand in both the negative and positive directions. History items are typically inserted in the order in which they are visited. Items have indices which are relative to the current item. The current item is always at index `0`, the preceding item is at index `-1`, the following item is at index `1`, and so on.

When manipulating the contents of a back-forward list be aware that some methods change the current item and therefore the indices of all other items. The [goBack](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419959-goback) and [goForward](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419955-goforward) methods, their equivalent action methods, and the [goToItem:](https://developer.apple.com/documentation/webkit/webbackforwardlist/1419950-gotoitem) method all change the current item. All other WebBackForwardList accessor methods do not effect the current item.

If there are no history items, or there are no items preceding or following the current item, then a back or forward action does nothing. Therefore you might want to track the state of the back-forward list and enable or disable the Back and Forward buttons accordingly.

You can do this by implementing the `webView:didFinishLoadForFrame:` delegate method to check the state of the back-forward list. Sending [canGoBack](https://developer.apple.com/documentation/webkit/webview/1408500-cangoback) and [canGoForward](https://developer.apple.com/documentation/webkit/webview/1408444-cangoforward) to the WebView object returns `YES` if you can go in that direction. Therefore, you might implement the `webView:didFinishLoadForFrame:` method as follows, where `backButton` and `forwardButton` are your button outlets:

```objc
- (void)webView:(WebView *)sender didFinishLoadForFrame:(WebFrame *)frame
{
    // Only report feedback for the main frame.
    if (frame == [sender mainFrame]){
    [backButton setEnabled:[sender canGoBack]];
    [forwardButton setEnabled:[sender canGoForward]];
    }
}
```

[Next](Managing%20History.md)[Previous](Loading%20Resources.md)

