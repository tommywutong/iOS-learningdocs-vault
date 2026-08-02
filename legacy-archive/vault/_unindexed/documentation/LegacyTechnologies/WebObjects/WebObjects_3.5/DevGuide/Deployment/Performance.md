---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Deployment/Performance.html
archived_at: '2026-07-15T07:51:25.094343Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Deployment.md) [!Previous Section](TerminateApp.md)

# Performance Tips

As more users access your application, you may become more concerned about its performance. Here are some suggestions about how to improve an application's performance.
__Note:__  This section covers only programmatic ways to improve performance. Performance is affected by several factors, such as the load on your system, the amount of memory available, and whether the load is shared among multiple application instances. For information about other ways to improve performance, see the online document [_Serving WebObjects_](../../ServingWebObjects/ServingWebObjectsTOC.md). In particular, you may want to check out the section "Testing Performance," which describes some tools you can use to do performance testing.

## Cache Component Definitions

As described in the chapter ["WebObjects Viewed Through Its Classes"](../HowWOWorks/HowWOWorks.md#apple-gy3a), each component has a component definition consisting of the component's template (the result of parsing the __.html__ and __.wod__ files) and information about resources the component uses. If you cache component definitions, the __.html__ and __.wod__ files are parsed only once per application rather than once per new instance of that component. To cache component definitions, use WOApplication's __setCachingEnabled:__ method.

```
    public Application() {
        super();
        this.setCachingEnabled(true);
        ...
    }
```


By default, this type of caching is disabled as a convenience for debugging. If component-definition caching is disabled and you're writing an entirely scripted application, you can change code in a scripted component and see the effects of that change without having to relaunch the application. You should always enable component-definition caching when you deploy an application, since performance improves significantly.
Instead of using __setCachingEnabled:__, you can also include the __-c__ option on the command line to perform component-definition caching.

```
    WODefaultApp -c
```


For more information on command-line options, see the online document [_Serving WebObjects_](../../ServingWebObjects/ServingWebObjectsTOC.md).

## Compile the Application

Applications written entirely in WebScript run more slowly than applications written in a compiled language such as Java or Objective-C. You may want to write in WebScript at first to speed the development cycle. Then, when you're ready to deploy, consider translating your WebScript code into a compiled language.

## Control Memory Leaks

Make sure that all objects allocated by your application are being deallocated. OpenStep provides some tools that can help you check your code for memory leaks. For more information, see the Debugging section of Project Builder's online help.
Another way to control leaks is to have the application shut down and restart periodically, as described in the section ["Automatically Terminating an Application"](TerminateApp.md#apple-gq3temy).

## Limit State Storage

As the amount of memory required by an application becomes large, its performance decreases. You can solve this problem by limiting the amount of state stored in memory or by storing state using some other means, as described in the chapter ["Managing State"](../State/StateTOC.md#apple-gu4tmmq). You can also set up the application so that it shuts down if certain conditions occur, as described in the section ["Automatically Terminating an Application"](TerminateApp.md#apple-gq3temy).

One common mistake is neglecting to set a session time-out value. By default, sessions almost never expire, so the application may be using valuable memory to store sessions that users have long forgotten. When you set the session time-out value, if the session is idle for that amount of time, it terminates and its state is removed from memory. This is described in more detail in the chapter ["Managing State"](../State/StateTOC.md#apple-gu4tmmq).

## Limit Database Fetches

Every database access that your application performs is a potential drag on performance. One easy way to limit trips to the database is to perform prefetching. For more information, see the chapter "Answers to Common Design Questions" in the _Enterprise Objects Framework Developer's Guide_.

## Limit Page Sizes

Be aware of the size of the HTML pages that you are downloading to the client machine. The larger the page, the more time it takes to download and draw. At first glance, your component's HTML might not seem unreasonably large; however, be sure you take into account the following:

- __Image files.__ Does the page download a lot of images? If so, how large are these images? If image files are making the page too large, consider using GIF images, which are often much smaller than other formats, or consider limiting the number of images you use.
- __Reusable components.__ Does the page include reusable components? If so, does the reusable component itself contain any reusable components? You must factor in the size of each component included and all of the image files that each component uses.
- __Repetitions.__ If the page uses a repetition, how large it the array that the repetition iterates over? How large is the amount of HTML generated for each element in the array? In particular, if you have a repetition that generates a table row for each element in a large array, the page may take a long time to render.

Consider implementing a batching display mechanism to display the information in the table. For example, if the array contains hundreds of entries, you might choose to only display the first 10 and provide a button that allows the user to see the next 10 entries. If the repetition is populated by a WODisplayGroup, you can use WODisplayGroup's __setNumberOfObjectsPerBatch:__ method to set up this batching, and it then controls the display for you. For more information, see the WODisplayGroup class specification in the online book _[WebObjects Class Reference](../../Reference/Reference.md)_.

[!Table of Contents](Deployment.md) [!Next Section](Install.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
