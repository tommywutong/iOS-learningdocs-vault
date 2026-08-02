---
title: Code Speed Performance Guidelines
apple_id: 10000150i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeSpeed/Articles/CriticalCode.html
archived_at: '2026-07-18T01:46:49.567773Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Speed Performance Guidelines](Introduction%20to%20Code%20Speed%20Performance%20Guidelines.md)


[Next](Notifications.md)[Previous](Detecting%20Polling%20Behavior.md)

# Accelerating Critical Code

For code that is called frequently by your application, even small optimizations can have a significant impact on performance. The following sections provide some simple ways to speed up repetitive operations.

As with any optimization, you should always measure the initial performance of code you plan to optimize. Taking an initial set of measurements helps you identify whether optimizing the code is warranted, and if it is, provides you with a set of baseline metrics against which to compare your changes. Without these metrics, there is no way to tell if your optimizations are an improvement or a regression from the original implementation.

Because of their nature, loops are a good place to start looking for potential optimizations. The code in a loop operation is going to be performed multiple times in quick succession. If your operation is spending a lot of time inside of a single loop, you should look for ways to remove code from that loop.

The simplest improvement you can make is to remove invariant code from the body of a loop. In some special cases, you might even be able to remove the loop altogether and replace it with a more efficient implementation.

When you write loop code, try to remove any invariant operation, that is, operations whose outcome is the same each time. For example, if you have some mathematical equation in your loop, you might want to rearrange your equation so that you can precompute any constant values or perform those computations outside of the loop. Similarly, if you know that a particular function returns the same value each time it is called, move it outside the loop and use variables to store any needed values.

For example, suppose you have a loop that performs the same action on the items in an immutable array. You could write your code as follows to walk through the contents of the array and perform the action as follows:

```
for (i = 0; i < [myArray count]; i++)
{
    object = [myArray objectAtIndex: i];
    [object doSomething];
}
```

While this code works just fine, it is not the most efficient choice. In each loop iteration, it dispatches a message to get the number of items in the array, which is wasteful. If the number of items in the array never changes, you could assign that value to a variable and use that instead, as shown in the following code:

```
numItems = [myArray count];
for (i = 0; i < numItems; i++)
{
    object = [myArray objectAtIndex: i];
    [object doSomething];
}
```

Removing this one function call can improve performance in any loop, regardless of how many items are in the array. This technique also works for any technology as removing function calls means less code to execute during each loop iteration.

The process of unrolling a loop is a delicate one and should be approached very carefully. The only time you should consider this option is when doing so simplifies your loop code significantly. Even in the best situations, make sure to go back and evaluate the real-time performance of your unrolled loop code. Unrolling loop code usually leads to more code, which increases the size of your application’s memory footprint and can increase the possibility of paging.

One case where removing a loop can increase speed is in a Cocoa application where you have an array of objects and you want to send the same message to each object. NSArray implements the `makeObjectsPerformSelector:` and `makeObjectsPerformSelector:object:` methods for that exact purpose. In this case, the method performs the loop for you, using its knowledge of the array’s internal data structures to optimize the loop performance.

Whenever you send a message to an Objective-C object, the runtime system must perform a lookup to determine which selector to use for that message. While the Objective-C runtime is very fast at performing this lookup, the operation still takes a small amount of time. If you want to call the same method on a collection of objects, you can eliminate that lookup cost altogether by caching the method’s `IMP` pointer and calling it directly. Remember that the objects in the collection must be of the same type and have the same method implementation.

To cache an `IMP` pointer for an object derived from NSObject, call the `methodForSelector:` method of the object and store the returned value. The code in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3tcljzha3donbninfeer2kjbcuu) shows you how to get the `IMP` pointer and use it to call the method for a specific object. In this example, the last two statements are equivalent to a method invocation. The first of these statements does the method lookup, obtaining a pointer to the implementation of the method. The second statement calls the method implementation with the desired search parameters.

__Listing 1__  Caching IMPs

```objc
#import <Foundation/Foundation.h>
#include <objc/objc-class.h>

static void DoSomethingWithString( NSString *string )
{
    typedef NSRange (*RangeOfStringImp)(id object, SEL selector,
                                NSString * string, long options, NSRange range);

    NSRange             foundRange;
    NSRange             searchRange;
    RangeOfStringImp    rangeOfStringImp;

    searchRange = NSMakeRange(0, [string length]);

    // The following two lines of code are equivalent to this method invocation:
    // foundRange = [string rangeOfString:@"search string"
    //                      options:0
    //                      range:searchRange];

    rangeOfStringImp = (RangeOfStringImp)
                [string methodForSelector:@selector(rangeOfString:options:range:)];

    foundRange = (*rangeOfStringImp)(string,
                                    @selector(rangeOfString:options:range:),
                                    @"search string", 0, searchRange);

}
```

[Next](Notifications.md)[Previous](Detecting%20Polling%20Behavior.md)

