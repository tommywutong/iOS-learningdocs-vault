---
title: NSProgress
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/03/nsprogress/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:aa483497b9c8b846'
translated: false
---

> 原文：[NSProgress](https://oleb.net/blog/2014/03/nsprogress/)　·　Ole Begemann

# NSProgress

**Update October 16, 2018:** Five years after its introduction, it’s safe to say that `NSProgress` (or [`Progress`](https://developer.apple.com/documentation/foundation/progress) in Swift) isn’t universally loved among developers in the Apple community. While this article addresses some issues, it does paint a fairly rosy picture and ignores some substantial problems, namely performance.

If you’d like to read a counterpoint before deciding if `NSProgress` is the right choice for you, I recommend reading [the readme of CSProgress](https://github.com/CharlesJS/CSProgress/blob/master/README.md) (an open-source reimplementation of `NSProgress`), which does a good job explaining some of the downsides `NSProgress` has.

---

Apple introduced the [`NSProgress`](https://developer.apple.com/library/ios/documentation/Foundation/Reference/NSProgress_Class/Reference/Reference.html) class in iOS 7 and OS X 10.9 with the goal of establishing a standard mechanism for reporting progress of long-running tasks. The central idea behind `NSProgress` is to allow progress reporting between multiple modules in an app without the need for tight [coupling](https://en.wikipedia.org/wiki/Coupling_%28computer_programming%29) between them. For instance, an image processing operation running on a background queue should be able to notify a view controller of its progress (and the view controller should be able to pause or cancel the operation) even though the two objects may not hold a reference to the other.^[1](#fn:1)

# Design Goals

The best documentation on `NSProgress` can currently be found in the [Foundation release notes for OS X 10.9](https://developer.apple.com/librarY/mac/releasenotes/Foundation/RN-Foundation/index.html#//apple_ref/doc/uid/TP30000742-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_11). The [class reference documentation](https://developer.apple.com/library/ios/documentation/Foundation/Reference/NSProgress_Class/Reference/Reference.html) exists, too, but I found it pretty hard to understand how I am supposed to work with the class.

In the release notes, Apple states four main design goals for `NSProgress`:

- Loose coupling
- Composability
- Reusability
- Usability

Let’s have a look at each one of them. The quotes that follow are all taken from the Foundation release notes.

## Loose Coupling

> Loose coupling. Code that does work can report the progress of that work regardless of what is observing it, or even whether it is being observed at all. To a lesser degree, code that observes progress and presents it to the user does not have to account for how the code that does the work is structured. Most of this goal is achieved simply by there being a single NSProgress class that can be used by a wide variety of progress reporters and observers.

Apple is setting a new standard here that will hopefully be widely adopted by the open-source community. If you write code that would potentially benefit from reporting progress of the work it does, you should strongly consider adding support for `NSProgress`. As we will see, you won’t even have to modify your code’s public API to do that. In most cases, it is enough to add just a few lines of code to the method that performs the actual work. By using an established standard, you will make your code easier to use for other developers and easier to integrate with other components.

## Composability

> Composability. Code that does work can report progress without taking into account whether that work is actually just part of a larger operation whose total progress is what’s really interesting to the user. To this end every NSProgress can have a single parent and multiple children. An NSProgress representing the total progress of an operation that’s interesting to the user typically has no parent. If there are suboperations then their progress is represented by child NSProgresses. Reports of progress being made propagate from children to parents. Requests for cancellation propagate from parents to children. The subdivision of progress into a tree of NSProgresses enables solutions to problems like how the progress of work performed by disparate pieces of code should be used to calculate one overall progress number worth presenting to the user. For example, see -[NSProgress fractionCompleted], which returns a value that takes into account both the receiver and its children.

`NSProgress` objects live in a hierarchy not unlike the view hierarchy in UIKit. At the root of the tree, the UI layer (e.g., a view controller) can create a progress object whenever it wants to monitor the progress of a task. By making this object the so-called _current progress_ before invoking the method that performs the task, this object will automatically act as the parent for any child progress instances created by the lower-level code. As the work proceeds and the child progresses get updated, the updates will propagate to the parent progress. Thus, by observing properties of the root progress object (via KVO), the UI layer can display the compounded progress of the child progresses. And by telling the root progress object to cancel or pause, the UI layer also has the ability to interact with the worker code through the progress hierarchy.

Unlike the view hierarchy, there exists no public API to traverse the progress hierarchy from parent to children or vice versa. Progress objects need not be concerned with their position in the tree and whether they actually have a parent or children. The event propagation and computation of overall progress is done entirely behind the scenes.

## Reusability

> Reusability. NSProgress is meant to be used by virtually all code that can link to the Foundation framework and that makes user-presentable progress. On Mac OS X, NSProgress includes a mechanism for publishing progress in one process and observing the progress in others.

See above. If your code does any form of progress reporting, you should consider adopting `NSProgress`.

## Usability

> Usability. In many cases a substantial obstacle to using NSProgress would be arranging for code that does work to find the exact instance of NSProgress it should use to report its progress. The size of this obstacle depends on many things, like how layered your code is (would you have to pass the NSProgress as an argument through many layers of functions and methods?), how it is already being used by multiple projects (can you even add NSProgress parameters without breaking things?), how it is divided between framework and application code (does all of this code ship at the same time?), and so on. To help surmount this obstacle there is a notion of current progress, which is the instance of NSProgress that should be the parent for any new progress objects that represent a subdivision of work. You can set a progress object as the current progress, then call into a framework or other section of code. If it supports progress reporting, it can find the current progress object using the currentProgress method, attach its own children if required, and do its work.

The notion of a current progress (each thread can have its own current progress) largely relieves developers of the need to pass `NSProgress` instances back and forth between different layers of code (as we often do with [`NSError`](https://developer.apple.com/library/ios/documentation/cocoa/reference/foundation/classes/NSError_Class/Reference/Reference.html) objects, for example).^[2](#fn:2) This design accounts for the fact that the code that displays progress (the UI) is often several levels removed from the code that does the actual work. On the other hand, it feels like a code smell. The current progress is basically a thread-local global variable, something which developers are generally taught to avoid.

The design also means that supporting `NSProgress` in a library that performs any kind of long-running task usually does not require the developer to change the library’s public API. While this is generally a good thing, it can turn into a major discoverability problem. Since the API does not contain any reference to `NSProgress`, the developer of the library must take extra care to explicitly document its support for `NSProgress`.

For instance, did you know that [`NSData`](https://developer.apple.com/library/ios/documentation/cocoa/reference/foundation/classes/NSData_Class/Reference/Reference.html) now comes with built-in `NSProgress` support for the `dataWithContentsOfURL:options:error:` method? I didn’t until I stumbled over it by chance in the [Foundation release notes](https://developer.apple.com/librarY/mac/releasenotes/Foundation/RN-Foundation/index.html#//apple_ref/doc/uid/TP30000742-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_11) — the `NSData` class reference documentation does not mention it (yet). On the other hand, seeing that even the venerable `NSData` now used `NSProgress` led me to the assumption that [`NSURLSession`](https://developer.apple.com/library/ios/documentation/Foundation/Reference/NSURLSession_class/Introduction/Introduction.html) — a brand new class introduced at the same time as `NSProgress` — surely had to come with great `NSProgress` support out of the box. I invested several hours trying to get it to work before I came to the conclusion that it doesn’t.

# Using NSProgress

Let’s have a look at how you would use `NSProgress` in practice. Again, the best sample code from Apple can currently be found in the [Foundation release notes](https://developer.apple.com/librarY/mac/releasenotes/Foundation/RN-Foundation/index.html#//apple_ref/doc/uid/TP30000742-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_11). There are two perspectives to consider: displaying progress in the UI and reporting progress in a method that performs work. I’ll discuss each of them in turn.

## Displaying Progress in the UI

Follow these steps in the view or view controller that should display the progress:

1. Before you invoke a long-running task, create an `NSProgress` instance with `+progressWithTotalUnitCount:`. The `totalUnitCount` argument should contain the total number of units of work to be carried out.

  It is important to understand that this number is entirely from the perspective of your UI layer; you are not being asked to guess how many units of work and of what kind (bytes? pixels? lines of text?) the actual worker object uses. So the parameter will often simply be `1` or perhaps the number of elements in a collection if you iterate over the collection and plan to invoke the worker object for each element.
2. Use [KVO](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html) to register yourself as an observer for the progress’s `fractionCompleted` property. Like [`NSOperation`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/NSOperation_class/Reference/Reference.html), `NSProgress` is designed to be used with KVO. On the Mac, this makes it extremely easy to bind an `NSProgress` instance to a progress bar or label using [Cocoa Bindings](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html). On iOS, you should manually update your UI in the KVO observer handler.

  In addition to the `fractionCompleted`, `completedUnitCount` and `totalUnitCount` properties, `NSProgress` also has a `localizedDescription` (`@"50% completed"`) and a `localizedAdditionalDescription` (`@"3 of 6"`), which can be bound to text labels.

  KVO notifications are sent out on the thread that changes the value of the property on the `NSProgress` object, so make sure to schedule your UI updates manually on the main thread.
3. Make the newly created progress object the current progress by invoking `-becomeCurrentWithPendingUnitCount:`. Here, the `pendingUnitCount` argument represents the portion of work to be performed in relation to the total number of units of work to be performed by the receiver. You can call this method several times and each time pass the portion of the `totalUnitCount` that will be performed by the code that follows. In our example of iterating over the elements of a collection, we would call `[progress becomeCurrentWithPendingUnitCount:1];` in each iteration.
4. Invoke the method on the worker object that does the work. Since the current progress is a thread-local concept, you must to do this on the same thread you called `becomeCurrentWithPendingUnitCount:` on. This is not a problem if the worker object’s API is designed to be invoked on the main thread, as I think most APIs should be (and [Brent Simmons thinks so, too](http://inessential.com/2014/03/08/api_design_the_main_thread_and_queues)).

  But if your UI layer is creating a background queue and invoking the worker object synchronously from that queue, make sure to place the calls to `becomeCurrentWithPendingUnitCount:` and `resignCurrent` into that same `dispatch_async()` block.
5. Invoke `-resignCurrent` on your progress object. This is the counterpart to `-becomeCurrentWithPendingUnitCount:` and should be called the same number of times. You can call `resignCurrent` before the actual work has been completed, so you don’t have to wait with this until you get a completion notification from the worker object.

  The only thing that must have happened between `becomeCurrent…`/`resignCurrent` calls is that the worker object must have created one or more child progresses (see below). If the worker object does not do this, the `resignCurrent` call will consider the task to be completed and automatically increase the `completedUnitCount` by the pending unit count.
6. When the worker object has completed its work, unregister from KVO on the progress object.

In code, it could look like this for a hypothetical image filtering task:

```
static void *ProgressObserverContext = &ProgressObserverContext;

- (void)startFilteringImage
{
    NSProgress *progress = [NSProgress progressWithTotalUnitCount:1];
    [progress addObserver:self
               forKeyPath:NSStringFromSelector(@selector(fractionCompleted))
                  options:NSKeyValueObservingOptionInitial
                  context:ProgressObserverContext];
    [progress becomeCurrentWithPendingUnitCount:1];

    // ImageFilter is a custom class that performs the work
    ImageFilter *imageFilter = [[ImageFilter alloc] initWithImage:self.image];
    [imageFilter filterImageWithCompletionHandler:
        ^(UIImage *filteredImage, NSError *error)
    {
        [progress removeObserver:self
            forKeyPath:NSStringFromSelector(@selector(fractionCompleted))
            context:ProgressObserverContext];

        // Image filtering finished
        ...
    }];

    [progress resignCurrent];
}

- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object
    change:(NSDictionary *)change context:(void *)context
{
    if (context == ProgressObserverContext)
    {
        [[NSOperationQueue mainQueue] addOperationWithBlock:^{
            NSProgress *progress = object;
            self.progressBar.progress = progress.fractionCompleted;
            self.progressLabel.text = progress.localizedDescription;
            self.progressAdditionalInfoLabel.text =
                progress.localizedAdditionalDescription;
        }];
    }
    else
    {
        [super observeValueForKeyPath:keyPath ofObject:object
            change:change context:context];
    }
}
```

## Reporting Progress

The worker object should perform these steps when invoked:

1. Create an `NSProgress` object with `+progressWithTotalUnitCount:`. The `totalUnitCount` should represent units of work in terms of your algorithm, so depending on the type of work you perform, it could be the length of a file in bytes, the number of pixels in an image, the number of characters in a string, or something else. The method will call `-[NSProgress initWithParent:userInfo:]` and pass `+[NSProgress currentProgress]` as the `parent` argument, thus establishing a parent-child relationship between the current progress (which is our UI layer’s progress object at this moment) and the newly created progress instance that the worker object will use to report its own progress.

  Because the current progress is thread-specific, it is important that the worker object creates its progress object on the same thread it was invoked on. Otherwise, the parent-child relationship will not be set up correctly. Once created, `NSProgress` objects are thread-safe. The worker object can later update properties on the progress from any thread/queue.

  If you don’t know the `totalUnitCount` yet (for example, because you are downloading a file and the file size is not known until you get a network response), feel free to create the progress object directly with `NSProgress *progress = [[NSProgress alloc] initWithParent:[NSProgress currentProgress] userInfo:nil];`. You can set the `totalUnitCount` later.
2. Optionally, configure your progress object by setting other properties like `cancellable` and `pausable`. When dealing with files, you can also set `kind = NSProgressKindFile`, in which case the progress’s `localizedDescription` and `localizedAdditionalDescription` will return more specific text. To make this work, you are also expected to add at least the `NSProgressFileOperationKindKey` key to the progress’s `userInfo` dictionary. Check the documentation for details.
3. Perform the actual work in a background queue. Periodically update your progress’s `completedUnitCount`. This will automatically propagate to the parent progress and trigger a UI update through the KVO setup discussed above.

  Alternatively, if your work is comprised of several smaller subtasks, you are free to create a deeper progress hierarchy. Just like the UI layer above, your worker object would call `becomeCurrentWithPendingUnitCount:` to make itself the current progress and then fire off subtasks that in turn use `NSProgress` to report their own progress up the chain. You should not mix both approaches with one progress object, however. If no child progress is created between calls to `becomeCurrentWithPendingUnitCount:` and `resignCurrent`, the `resignCurrent` call will automatically set the receiver’s `fractionCompleted` to 1.

  If your progress is cancellable or pausable, you should also check periodically whether the progress’s `cancelled` or `paused` properties are `YES` and react accordingly. Changes to these properties propagate down from parent to children (usually in response to a user action). The correct response to cancelling is to stop the work you are doing and report an appropriate `NSError`.

Sample code:

```
@implementation ImageFilter

...

- (void)filterImageWithCompletionHandler:
    (void(^)(UIImage *filteredImage, NSError *error))completionHandler
{
    int64_t numberOfRowsInImage = (int64_t)self.image.size.height;
    NSProgress *progress = [NSProgress progressWithTotalUnitCount:
        numberOfRowsInImage];
    progress.cancellable = YES;
    progress.pausable = NO;

    dispatch_queue_t backgroundQueue =
        dispatch_queue_create("image filter queue", DISPATCH_QUEUE_SERIAL);
    dispatch_async(backgroundQueue, ^{
        NSError *error = nil;
        UIImage *filteredImage = nil;
        for (int64_t row = 0; row < numberOfRowsInImage; row++) {
            // Check if cancelled
            if (progress.cancelled) {
                error = [NSError errorWithDomain:NSCocoaErrorDomain
                    code:NSUserCancelledError userInfo:nil];
                break;
            }

            // Do the work for this row of pixels
            ...

            // Update progress
            progress.completedUnitCount++;
        }

        // We assume work is complete and either filteredImage has been set
        // or the task has been cancelled and error has been set above.
        if (completionHandler) {
            dispatch_async(dispatch_get_main_queue(), ^{
                completionHandler(filteredImage, error);
            });
        }
    });
}

@end
```

# Conclusion

I think `NSProgress` is an exciting new addition to Foundation that will become more and more useful to app developers as Apple itself and the open-source community will adopt it widely. Understanding its design, especially the concept of a thread-local current progress object, is a fundamental requirement to using it effectively.

If you implement an API that would benefit from progress reporting, you should strongly consider adding `NSProgress` support. When you do so, make sure to document this clearly as users of your API will not be able to tell from the API alone. Apple should lead by example in this regard, but unfortunately the current documentation is lacking. Aside from the remark about `NSData` in the Foundation Release Notes and an explicit use of `NSProgress` in the [Multipeer Connectivity framework](https://developer.apple.com/library/ios/documentation/MultipeerConnectivity/Reference/MultipeerConnectivityFramework/_index.html), I have not been able to find any mention of it in other APIs.

1. On the Mac, `NSProgress` can even exchange data between processes. Safari uses this feature to communicate download progress to the Finder and allow the user to cancel a running download from the Finder or Dock. [↩︎](#fnref:1)
2. It is still perfectly possible to use `NSProgress` in the “traditional” way of passing `NSProgress` instances to other parts of your app as parameters of delegate methods or blocks. Using `NSProgress` in such a way mimics the design `NSURLConnection` has always used to report progress in the form of the [`connection:didSendBodyData:totalBytesWritten:totalBytesExpectedToWrite:`](https://developer.apple.com/library/ios/documentation/Foundation/Reference/NSURLConnectionDataDelegate_protocol/Reference/Reference.html#//apple_ref/doc/uid/TP40011348-CH1-SW6) delegate method, with the advantage of encapsulating progress information in a dedicated object. Apple uses this approach in the Multipeer Connectivity framework (check out the [`MCSessionDelegate`](https://developer.apple.com/library/ios/documentation/MultipeerConnectivity/Reference/MCSessionDelegateRef/Reference/Reference.html#//apple_ref/doc/uid/TP40013318) protocol) [↩︎](#fnref:2)
