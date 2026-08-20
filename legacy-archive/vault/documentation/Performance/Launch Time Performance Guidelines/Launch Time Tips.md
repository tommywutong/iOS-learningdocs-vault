---
title: Launch Time Performance Guidelines
apple_id: 10000148i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/LaunchTime/Articles/LaunchTips.html
archived_at: '2026-07-18T01:48:46.269290Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Launch Time Performance Guidelines](Introduction%20to%20Launch%20Time%20Performance%20Guidelines.md)


[Next](Gathering%20Launch%20Time%20Metrics.md)[Previous](Introduction%20to%20Launch%20Time%20Performance%20Guidelines.md)

# Launch Time Tips

Launch time is an important metric to measure for any application. It is the first experience a user has with your application, and it is something the user sees on a regular basis. The less time it takes your application to launch, the faster your application will seem to the user.

Your overriding goal during launch should be to display the application’s menu bar and main window and then start responding to user commands as quickly as possible. Making your application responsive to commands quickly provides a better experience for the user. The following sections provide some general tips on how to make your application launch faster.

Regardless of what techniques you choose to improve your launch times, the only way to know you’ve improved performance is through measurement. Gather and record launch time metrics early in your development process and monitor them especially when implementing new optimizations. For information on how to measure launch-time performance, see [Gathering Launch Time Metrics](Gathering%20Launch%20Time%20Metrics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha2tmlkdjjbeursjirca).

Many applications spend a lot of time initializing code that isn’t used until much later. Delaying the initialization of subsystems that are not immediately needed can speed up your launch time considerably. Remember that the goal is to display your application interface quickly, so try to initialize only the subsystems related to that goal initially.

Once you have posted your interface, your application can continue to initialize additional subsystems as needed. However, remember that just because your application is able to process commands does not mean you need all of that code right away. The preferred way of initializing subsystems is on an as-needed basis. Wait until the user executes a command that requires a particular subsystem and then initialize it. That way, if the user never executes the command, you will not have wasted any time running the code to prepare for it.

For a Carbon application, you should perform your basic initialization before beginning your application’s main event loop. Once that loop is running, you can set up a one-shot timer to execute any additional code that your application absolutely requires for basic operation. Do not load code for specific features until the user chooses a command that uses that feature.

For a Cocoa application, avoid putting a lot of extraneous initialization code in your `awakeFromNib` methods. The system calls the `awakeFromNib` method of your main nib file before your application enters its main event loop. Use that method to initialize the objects in that nib and to prepare your application interface. For all other initialization, use the `applicationDidFinishLaunching` method of your NSApplication object instead. For more information on nib files and how they are loaded, see _[Resource Programming Guide](../../Cocoa/Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_.

Loading a nib file is an expensive process that can slow down your application launch time if you are not careful. When a nib file is loaded, all of the objects in that file are instantiated and made ready for use. The more objects you include in your application’s main nib, the more time it takes to load that file and launch your application.

The instantiation process for objects in a nib file requires that any frameworks used by those objects must themselves be resident in memory. Thus loading a nib for a Cocoa application would likely require the loading of both the AppKit and Foundation frameworks, if they were not already resident in memory. Similarly, if you declare a custom class in your main nib file and that class relies on other frameworks, the system must load those frameworks as well.

When designing your application’s main nib file, you should include only those objects needed to display your application’s initial user interface. Usually, this would involve just your application’s menu bar and initial window, if any. For any custom classes you include in the nib, make sure their initialization code is as minimal as possible. Defer any time-consuming operations or memory allocations until after the class is instantiated.

For both applications and frameworks, be careful not to declare global variables that require significant amounts of initialization. The system initializes global variables before calling your application’s `main` routine. If you use a global variable to declare an object, the system must call the constructor or initialization method for that object during launch time. In general, it’s best to avoid declaring objects as global variables altogether when you can use a pointer instead.

If you are implementing a framework, or any type of reusable code module for that matter, you should also minimize the number of global variables you declare. Each application that links to a framework acquires a copy of that framework’s global variables. These variables might require several pages of virtual memory, which then increases the memory footprint of the target application. An increased memory footprint can lead to paging in the application, which has a tremendous impact on performance.

One way to minimize the global variables in a framework is to store the variables in a malloc-allocated block of memory instead. In this technique, you access the variables through a pointer to the memory, which you store as a global variable. Another advantage of this technique is that it allows you to defer the creation of any global variables until the first time they are actually used. See [Optimizing Your Memory Allocations](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/MemoryAlloc.html#//apple_ref/doc/uid/20001881) in _[Memory Usage Performance Guidelines](../Memory%20Usage%20Performance%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3da2i)_ for more information.

Loading large numbers of unused strings at launch time adds an unnecessary burden to your application’s memory footprint. In low-memory situations, a larger footprint could trigger paging and impact the launch time of your application. If you find yourself loading hundreds of unused strings at launch time, you might consider using separate resource files to store those strings not needed to launch the application.

In general, minimizing the number of strings in your `Localizable.strings` file is a good idea and can improve your application launch time. You must be careful, though, not to break up your remaining strings files too much in an effort to minimize the number of strings loaded by each successive operation. Separating your strings into many small files increases the overall amount of time spent doing file I/O, which can hinder performance rather than improve it. Before breaking your strings files into more than a few files, you should gather metrics to make sure it is warranted.

Application launch time is not the time to perform any operation involving a potentially large data set. If your application handles a scalable data set, make sure to gather performance metrics with a large data set. Even with efficient algorithms, processing large amounts of data takes time and should be deferred until after your application finishes launching.

If you must load data early, try to do so in a way that reduces the impact on your application’s launch time. One way is to design your program in a way that lets you load only a portion of the data set. For a really large data set, the user will be unable to see it all on the screen at one time anyway. Loading and displaying data incrementally improves launch time as well as the general performance of your application. Another way is to use a background thread to load the data shortly after the launch cycle completes.

For more information about improving the speed of your operations, see _[Code Speed Performance Guidelines](../Code%20Speed%20Performance%20Guidelines/Introduction%20to%20Code%20Speed%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2ta2i)_.

Allocating and deleting memory takes time. If you find your algorithms allocating and deleting temporary memory in a tight loop, you might think of a way to remove those allocation routines from the loop. Rather than create a new string object each time, you could create one string object and re-initialize its contents with each pass of the loop.

One way to determine if you’re allocating too much memory at launch time is to launch your application running under MallocDebug or ObjectAlloc. These tools show you the allocation patterns of your application. If you find your application allocating large amounts of temporary memory, you might go back through your algorithms to see if there are any blocks you can reuse or recycle.

For information about the OS X virtual memory system and how to allocate memory efficiently, see _[Memory Usage Performance Guidelines](../Memory%20Usage%20Performance%20Guidelines/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3da2i)_.

At launch time, it’s important to know where your resources are located. All of your application’s critical resources should be located inside the application bundle itself. Searching for resources outside of the bundle has potentially serious costs, as you may not know whether the resource is local or on the network. In particular, you should keep in mind that items such as plug-ins, loadable bundles, and user preferences may reside somewhere out on the network. Attempting to load these resources at launch time can delay the availability of your application.

It’s best to avoid accessing external resources at launch time. If a resource is on a network server and the network is not available, your application could hang while it waits for the needed resource to become available. This is not a desirable situation and should be avoided by eliminating startup dependencies on these types of resources. If you do need to load these resources early, try loading them after your application has finished launching or from a background thread.

[Next](Gathering%20Launch%20Time%20Metrics.md)[Previous](Introduction%20to%20Launch%20Time%20Performance%20Guidelines.md)

