---
title: Safari Web Content Guide
apple_id: TP40002051
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/Client-SideStorage/Client-SideStorage.html
archived_at: '2026-07-15T05:19:07.863791Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Web Content Guide](Developing%20Web%20Content%20for%20Safari.md)


[Next](Getting%20Geographic%20Locations.md)[Previous](Creating%20Video.md)

# Storing Data on the Client

There are several ways for a web application or website to store data on the client. You can use the JavaScript database classes, described in _[Safari Client-Side Storage and Offline Applications Programming Guide](../../iPhone/Safari%20Client-Side%20Storage%20and%20Offline%20Applications%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjw)_, for storing application data or use the HTML5 application cache for storing resources on the client so webpages continue to display offline when there is no network connection on the desktop and iOS. You can also use the application cache to load webpages faster when there is a slow network connection. This chapter describes how to store data locally using this HTML5 application cache.

To store resources on the client first you create a manifest file specifying which resources to cache. You declare the manifest file in the main HTML file. Then you manipulate the cache and handle related events using JavaScript. Webpages that were previously loaded and contain the resources you specify continue to display correctly when there is no network. The application cache also persists between browser sessions. So, a web application that was previously used on the computer or device can continue to work offline—for example, when iOS has no network or is in airplane mode.

The manifest file specifies the resources—such as HTML, JavaScript, CSS, and image files —to downloaded and store in the application cache. After the first time a webpage is loaded, the resources specified in the manifest file are obtained from the application cache, not the web server.

The manifest file has the following attributes:

- It must be served with type `text/cache-manifest`.
- The first line must contain the text `CACHE MANIFEST`.
- Subsequent lines may contain URLs for each resource to cache or comments.
- Comments must be on a single line and preceded by the `#` character.
- The URLs are file paths to resources you want to download and cache locally. The file paths should be relative to the location of the manifest file—similar to file paths used in CSS—or absolute.
- The HTML file that declares the manifest file, described in [Declaring a Manifest File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjrfvbuqnbnknltg), is automatically included in the application cache. You do not need to add it to the manifest file.

For example, Listing 11-1 shows a manifest file that contains URLs to some image resources.

__Listing 11-1__  Sample manifest file

```
CACHE MANIFEST

demoimages/clownfish.jpg
demoimages/clownfishsmall.jpg
demoimages/flowingrock.jpg
demoimages/flowingrocksmall.jpg
demoimages/stones.jpg
demoimages/stonessmall.jpg
```


After you create a manifest file you need to declare it in the HTML file. You do this by adding a `manifest` attribute to the `<html>` tag as follows:

```
<html manifest="demo.manifest">
```

The argument to the `manifest` attribute is a relative or absolute path to the manifest file.

In most cases, creating a manifest file and declaring it is all you need to do to create an application cache. After doing this, the resources are automatically stored in the cache the first time the webpage is displayed and loaded from the cache by multiple browser sessions thereafter. Read the following sections if you want to manipulate this cache from JavaScript.

You can wait for the application cache to update automatically or trigger an update using JavaScript. The application cache automatically updates only if the manifest file changes. It does not automatically update if resources listed in the manifest file change. The manifest file is considered unchanged if it is byte-for-byte the same; therefore, changing the modification date of a manifest file also does not trigger an update. If this is not sufficient for your application, you can update the application cache explicitly using JavaScript.

Note that errors can also occur when updating the application cache. If downloading the manifest file or a resource specified in the manifest file fails, the entire update process fails. If the update process fails, the current application cache is not corrupted—the browser continues to use the previous version of the application cache. If the update is successful, webpages begin using the new cache when they reload.

Use the following JavaScript class to trigger an update to the application cache and check its status. There is one application cache per document represented by an instance of the [DOMApplicationCache](https://developer.apple.com/documentation/webkitjs/domapplicationcache) class. The application cache is a property of the `DOMWindow` object.

For example, you get the `DOMApplicationCache` object as follows:

```
cache = window.applicationCache;
```

You can check the status of the application cache as follows:

```
if (window.applicationCache.status == window.applicationCache.UPDATEREADY)...
```

If the application cache is in the `UPDATEREADY` state, then you can update it by sending it the `update()` message as follows:

```
window.applicationCache.update();
```

If the update is successful, swap the old and new caches as follows:

```
window.applicationCache.swapCache();
```

The cache is ready to use when it returns to the `UPDATEREADY` state. See the documentation for [DOMApplicationCache](https://developer.apple.com/documentation/webkitjs/domapplicationcache) for other status values. Again, only webpages loaded after an update use the new cache, not webpages that are currently displayed by the browser.

You can also listen for application cache events using JavaScript. Events are sent when the status of the application cache changes or the update process fails. You can register for these events and take the appropriate action.

For example, register for the `updateready` event to be notified when the application cache is ready to be updated. Also, register for the `error` event to take some action if the update process fails—for example, log an error message using the console.

```
cache = window.applicationCache;
cache.addEventListener('updateready', cacheUpdatereadyListener, false);
cache.addEventListener('error', cacheErrorListener, false);
```

See the documentation for [DOMApplicationCache](https://developer.apple.com/documentation/webkitjs/domapplicationcache) for a complete list of event types.

[Next](Getting%20Geographic%20Locations.md)[Previous](Creating%20Video.md)

