---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WhatIsWOApp/RunningWOApp.html
archived_at: '2026-07-15T07:52:44.252578Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WhatIsWOApp.md) [!Previous Section](AppDir.md)

# Running a WebObjects Application

WebObjects applications run on a web server. Your users connect to a WebObjects application using web browsers that they run on their own (client) machines. How does a user start a WebObjects application, and how does the application communicate with the browser?
Users run a WebObjects application using a Uniform Resource Locator (URL) similar to the one shown in [Figure 4](#apple-g44tg). (Of course, you'd probably provide a button or a link on a static web page that would take users to this URL rather than forcing your users to type such a long string.)

!Figure 4. A URL to Start a WebObjects Application
To start your own applications, you open a command shell window, go to the directory that contains your application, and enter the application command. WebObjects starts up your application, opens the web browser, and enters the URL in the web browser for you. For example, to start the Java version of HelloWorld, go to the directory <DocRoot>__/WebObjects/Examples/Java/HelloWorldJava/HelloWorldJava.woa__, which contains the executable file, and enter __HelloWorld__ on the command line. On Windows NT, you can simply navigate to this directory in the Explorer and double-click the __HelloWorld.exe__ file.
When you run a WebObjects application, it communicates with the web browser through the chain of processes shown in [Figure 5](#apple-gqzdiny).

!Figure 5. Chain of Communication Between the Browser and Your WebObjects Application
Here is a brief description of these processes:

- __An HTTP server__. Any HTTP server that uses the Common Gateway Interface (CGI), the Netscape Server API (NSAPI), or the Internet Server API (ISAPI).
- __[A WebObjects adaptor](Adaptors.md)__
. A WebObjects adaptor connects WebObjects applications to the web by acting as an intermediary between web applications and HTTP servers.
- __[A WebObjects application executable](AppExecutables.md)___._ The application executable receives incoming requests and responds to them, usually by returning a dynamically generated HTML page.

Two of these, WebObjects adaptors and WebObjects application executables, are described next.

[!Table of Contents](WhatIsWOApp.md) [!Next Section](Adaptors.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
