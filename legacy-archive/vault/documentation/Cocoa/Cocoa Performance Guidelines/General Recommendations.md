---
title: Cocoa Performance Guidelines
apple_id: TP40001448
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2009-08-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaPerformance/Articles/GeneralInfo.html
archived_at: '2026-07-15T07:13:17.678905Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Performance Guidelines](Introduction%20to%20Cocoa%20Performance%20Guidelines.md)


[Next](Unblocking%20Your%20User%20Interface.md)[Previous](Introduction%20to%20Cocoa%20Performance%20Guidelines.md)

# General Recommendations

The following sections provide some basic guidance for achieving good performance with the Cocoa framework.

Never assume you know where performance problems lie. The only way to know for sure is to measure the actual performance of your Cocoa application and use data from various tools to identify the real problems.

Choose a scalable application architecture. Your choice of algorithms can make a big difference in performance. Choose algorithms that scale well to the intended data set. Test your program on large data sets to make sure your performance is appropriate.

The Cocoa [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) provides many of the features you need to implement advanced applications. In addition, improvements to Cocoa are being made regularly. By taking advantage of the facilities Cocoa provides for extending or modifying framework behavior, such as delegation and subclassing, you make your applications more likely to benefit from future improvements.

Be sure to use data structures and data types that are compatible with the methods you need to call. Constructing or converting a data structure at runtime solely for the purpose of calling a system function adds an unnecessary performance penalty to your application. If you can incorporate a compatible version of the data structure into your model, you can eliminate that penalty.

Because of latency and transfer speeds, file-system and network requests can potentially take much longer to complete than other types of operations. If you access file or network data synchronously, your application might appear frozen while it waits for the data to return. Therefore, it is usually better to perform these types of operations asynchronously or on a secondary thread. You might also want to consider firing off a timer if the operation does not complete within a certain amount of time. You can use this timer to notify the user of the delay or provide an option to cancel the operation.

You should always approach data caching carefully and measure the performance of your implementation. Data caching can significantly improve the speed of your code or hopelessly degrade it. Identifying the right data to cache is a difficult task and is dependent on your design. If you cache the wrong data, you could waste memory storing unused data. Even if you cache the right data, that data could still be paged to disk during low-memory conditions.

Be sure to test your caching implementation under a variety of circumstances, especially in low-memory situations. If you find your data is being paged out to disk, consider reducing the size of your cache or eliminating it altogether. At that point, caches could cause three disk operations instead of just one.

Reducing the amount of work you do at critical moments is one of the best ways to give users the perception of speed in your application. Deferring operations whose results are not needed right away can help improve performance at those critical moments, as well as at other times too.

Drawing is a particular area where deferring operations can yield significantly better performance. Rather than force your window to update each time you make a change, simply invalidate areas that need to be redrawn. There is a good chance that more updates might have come before the window contents actually need to be redrawn. By invalidating, you can coalesce those drawing operations and perform them all at once.

Another place where applications typically take a big performance hit is in loading plug-ins and other external code modules that are not needed right away. If you load a code module or plug-in that is never used, it is a waste of both CPU time and memory. If you wait until the code is actually called, you may incur a small penalty by loading the code at that time but you guarantee that the code is actually used.

If you are loading data dynamically and displaying it in a view, avoid telling your view to update itself too often. It is better to delay the display of that data a short amount of time rather than force your view to redraw its contents immediately, especially if more data could arrive at any time.

For example, suppose you have a script that generates data to be displayed in a table view. If the script provides an initial flood of data and then sends periodic updates, calling the `reloadData` method each time you received a piece of the data could lead to numerous useless updates. Instead, you should defer the call to the `reloadData` method until a certain amount of time has passed. If more data comes in during that time, you can then cancel the current request and initiate a new one. Listing 1 shows you some sample code for how to do this.

__Listing 1__  Cancelling and restarting a reloadData operation

```
// Cancel the old request
[NSObject cancelPreviousPerformRequestsWithTarget:myTableView selector:@selector(reloadData) object:nil];

// Initiate a new request after a brief delay.
[myTableView performSelector:@selector(reloadData) withObject:nil afterDelay:0.3];
```


If you use the NSPropertyListSerialization class to read and write [property-list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) information, you should format your property list files as binary XML whenever possible. Binary data is significantly more compact than its text-based counterpart. As a result, reading and writing binary-based data is significantly faster (often 5 to 20 times faster) than reading and writing the corresponding text-based data.

Support for the binary XML format was introduced in OS X v10.2. Although users cannot view the contents of a binary property-list file directly using a text editor, they can use the Property List Editor application to read them.

For more information on property lists and binary file formats, see _[Property List Programming Guide](../Property%20List%20Programming%20Guide/Introduction%20to%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2i)_.

[Next](Unblocking%20Your%20User%20Interface.md)[Previous](Introduction%20to%20Cocoa%20Performance%20Guidelines.md)

