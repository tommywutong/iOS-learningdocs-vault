---
title: Safari Client-Side Storage and Offline Applications Programming Guide
apple_id: TP40007256
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Data Management
technology: null
published: '2011-09-21'
source_url: https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/SafariJSDatabaseGuide/Introduction/Introduction.html
archived_at: '2026-07-18T02:27:25.079986Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](HTML5%20Offline%20Application%20Cache.md)

# Introduction

If you develop websites, or if you are trying to decide whether to write a native iOS app or a web app, you should learn about HTML5 client-side caching and storage.

![../Art/splash.png](attachments/Art/splash.png)![../Art/splash.png](attachments/Art/splash.png)

No matter what kind of website you develop, you can use Safari's HTML5 client-side storage to make your work easier and improve your site. For example, you can:

- Make your website work even when the user is offline or loses network connectivity by caching code and data locally.
- Make your website more responsive by caching resources—including audio and video media—so they aren't reloaded from the web server each time a user visits your site.
- Make your web app more user-friendly by saving user-generated data locally at frequent intervals, while reducing server load and delay by saving to your server only occasionally.
- Make every user interaction with your site faster by replacing large cookies with local storage. (Cookies are sent back to your site with every HTTP request, increasing network overhead.)
- Simplify your scripts by replacing unstructured data stored in cookies with structured key-value storage.
- Reduce server load by replacing server-side programs with client-side scripts, storing even large amounts of structured data locally using an SQL-compatible JavaScript database.

HTML5 client-side storage can make a web app nearly identical to a native app on iOS-based devices. Even without client-side storage, a web app can look and act much like an iOS native app—you can hide Safari’s UI so your web app uses the full screen, use CSS to rotate the view when the user flips the device between portrait and landscape modes, and provide an icon that launches your web app from the user’s start screen, just like a native app. When you add client-side storage to these other features, your web app comes very close to being a native app—the app is stored on the device, launched from the start screen, works when the user is offline, stores data locally, and looks and feels like a native app. Of course, there are still good reasons to write a native app and distribute it through the app store, but client-side storage puts web apps on a much more equal footing.

HTML5 client-side storage is supported in Safari on all platforms: Mac OS X, Windows, and iOS.

There are three main components to HTML5 client-side storage in Safari: the offline application cache, key-value storage, and JavaScript database storage. Each of the three components is independent of the others and can be used by itself or in combination with either or both of the others.

### Use the Offline Application Cache to Make Your Website Usable Offline

To use the offline application cache, make a text file listing the resources of your website that you want to keep cached locally, then add an attribute to your HTML that identifies the list as a cache manifest. Safari loads the resources on the list into a cache that is dedicated to your domain; on subsequent visits to your website, the resources are loaded directly from the cache.

If the user is online, Safari compares the cached version of the manifest with the version on your website. If the manifest has changed, Safari checks each item on the manifest to see if the item has changed, then downloads any modified items. Items added to the manifest are automatically downloaded.

If your web app is a canvas-based game or a JavaScript calculator, for example, the entire website can be stored in the cache, allowing people to run your app even when they are offline. If your web app can be used offline, but relies on data from the web, such as an e-reader, for example, the offline application cache can be used to store webpages “lazily,” as the user loads them, or the offline cache can be combined with key-value storage or a JavaScript database to store the most recent data—or user-selected data—allowing the user to read cached articles or access cached data when offline.

### Lighten Your Cookie Load By Using Key-Value Storage

Most websites store data on the user's computer by setting cookies. Cookies are strings of unstructured data, typically limited to about 4 KB each. You can expand the limit by creating multiple cookies, but this too has restrictions; some browsers limit the number of cookies per domain, and—since all the cookies in your domain are returned to you with every HTTP request—the HTTP header size itself can become a limit.

Cookies are a great place to store HTTPS authentication tokens, but for most other data storage needs, key-value storage is a better approach. Key-value storage is structured and plays well with JavaScript, has a size limit measured in Megabytes instead of Kilobytes, and doesn't add overhead to every interaction with your website by cluttering the HTTP header.

There are two types of key-value storage: session storage and local storage. Session storage is local to a browser window and goes away when the user closes the browser window or loads a new site. Local storage is shared among all open windows and is persistent, even if the user clears all cookies.

Put data into storage by defining properties of the `localStorage` or `sessionStorage` objects. For example:

`localStorage.zip="92104"`

The previous snippet creates a key named "zip" with a value of "92104" and puts the key-value pair into local storage. Retrieving data is just as easy:

`var userZip = localStorage.zip`

Key-value storage uses strings as values. Other data types can be serialized, but to store significant amounts of non-string data, a JavaScript database is probably more useful. For details, see [Using the JavaScript Database](Using%20the%20JavaScript%20Database.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqmznknltc).

### Do the Heavy Lifting on the Client Instead of Your Server

When you have large amounts of data that the client needs to access in complex ways, the best approach is usually to create a relational database and provide client access using a GUI as a front end for SQL queries.

You can maintain a database on your server and use your website to provide a GUI to generate queries that your server executes, but this approach has some drawbacks:

- User-generated data needs to be sent to and stored on your server.
- The processing load for the SQL queries falls on your server, making it less responsive.
- The global data set is potentially exposed to SQL hacking.

Using an HTML5 JavaScript database lets you keep user-generated and user-consumed data on the user's computer, moves the processing load from your server to the user's CPU, and lets you limit the data set accessible to SQL over the Internet.

If the user needs access to large amounts of data stored on your server, and your server has enough power to handle multiple simultaneous user queries, a server-side database is probably best. If, on the other hand, the data is largely user-centric, or the number of simultaneous queries is creating bottlenecks on your server, a JavaScript database might be a better option.

A JavaScript database is also useful when you have large amounts of non-string data to store on the user's computer. There is more overhead to set up and maintain a relational database than a key-value store, however, so there is a trade-off involved.

You create a JavaScript database using the HTML5 `openDatabase` and `CREATE TABLE` methods. Access the database using the `executeSql` method, passing in SQL transaction strings.

### Debug Client-Side Storage and Caching Using the Web Inspector

Safari includes a set of built-in tools you can use to inspect and debug the offline application cache, key-value storage, JavaScript databases, as well as the HTML, CSS, and JavaScript that glues them all together.

To turn on the debugging tools, enable the Develop Menu in Safari Preferences Advanced pane. Once the Develop Menu is enabled, choose Show Web Inspector from the Develop menu and click the Resources button to inspect local storage and caching. Click the Scripts button to interactively debug JavaScript. For more about how to use the debugging tools, see _[Safari Web Inspector Guide](../../Apple%20Applications/Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_.

You can inspect and debug key-value storage and JavaScript databases using local files or using a website loaded from a web server. To use the offline application cache, however, you must load the site from a web server.

### Use the Companion File

Click the Companion File button at the top of the HTML version of this document to download a `.zip` file containing working sample code that shows you how to use a JavaScript database.

You need a general familiarity with HTML and JavaScript to use this document effectively.

You may find the following documents helpful when working with caching and offline storage:

- [HTML5 Web Storage Specification](http://dev.w3.org/html5/webstorage/)—Defines the HTML and JavaScript API for key-value storage.
- _[DOMApplicationCache Class Reference](https://developer.apple.com/documentation/webkitjs/domapplicationcache)_—Describes the JavaScript API for the application cache.
- _[TicTacToe with HTML5 Offline Storage](../../../samplecode/TicTacToe%20with%20HTML5%20Offline%20Storage/TicTacToe%20with%20HTML5%20Offline%20Storage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamzqhe)_—Sample code containing a game that maintains the current game state persistently using local key-value storage.
- _[Safari Web Inspector Guide](../../Apple%20Applications/Safari%20Web%20Inspector%20Guide/About%20Safari%20Web%20Inspector.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzu)_—Shows how to enable and use Safari’s built-in tools for inspecting and debugging local storage, databases, JavaScript, HTML, and CSS.
[Next](HTML5%20Offline%20Application%20Cache.md)

