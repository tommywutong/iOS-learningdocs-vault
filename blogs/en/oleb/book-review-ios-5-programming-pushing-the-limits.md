---
title: 'Book Review: iOS 5 Programming – Pushing the Limits'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/09/ios-5-programming-pushing-the-limits/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b0a42960f85025ee'
translated: false
---

> 原文：[Book Review: iOS 5 Programming – Pushing the Limits](https://oleb.net/blog/2012/09/ios-5-programming-pushing-the-limits/)　·　Ole Begemann

# Book Review: iOS 5 Programming – Pushing the Limits

[![iOS 5 Programming – Pushing the Limits Book Cover](https://oleb.net/media/ios-5-programming-pushing-the-limits-cover.png)](https://www.amazon.com/iOS-Programming-Pushing-Limits-Extraordinary/dp/1119961327/)

**Update September 12, 2012:** I updated the article with some fixes for places where I was wrong, comments from Rob Napier and Mugunth Kumar, the two authors, and added a few more references. I apologize for the wrong statements I made. See the highlighted paragraphs below.

I really wanted to like this book. The market for books about iOS development is saturated with introductory books but titles that target the intermediate or advanced level are rare. I suppose this is understandable because beginners are the biggest market for programming books. So I was excited about [iOS 5 Programming – Pushing the Limits](https://www.amazon.com/iOS-Programming-Pushing-Limits-Extraordinary/dp/1119961327/) (published in early 2012) by [Rob Napier](http://robnapier.net/) and [Mugunth Kumar](http://mugunthkumar.com).

Despite my initial excitement, having read the book thoroughly, I cannot recommend it to anyone. You really should not buy it. It is difficult for me to advise so strongly against a book by two authors whom I greatly respect for their contributions to the developer community, be it their blogs, open-source components or tweets. Also, I know it’s so much easier to criticize the work of others than creating it so I hope Rob and Mugunth don’t take this review personal. I will still follow their writings, I just don’t think they have delivered their best work with this book. Let me explain.

# Factual Errors

My main reason for not recommending the book is the sheer number of factual errors. By that, I do not mean typos or small oversights but essential statements that can often be refuted by a look in the documentation. Or disputable opinions given as facts with no evidence at all. I will list most of the errors I have found at the bottom of this article.

Not as bad as blatant factual errors, but almost as important in my opinion, is the multitude of wrong or sloppy wording throughout the book. An experienced programmer can gloss over sentences where protocols are confounded with classes, classes with instances or drawing with compositing. In a book that targets intermediate developers who may not yet have internalized every term, mix-ups like these can leave the reader more confused than he was before. Again, refer to the bottom of this article for relevant examples.

To me, the errors I found are a sign of either serious sloppiness or lack of knowledge on part of the authors. I do realize that books about new technologies are regularly written under considerable time pressure and that it is nearly impossible to get every fact correct. In fact, nobody expects this. I my opinion, the mistakes in this book are more severe than usual and cannot just be explained with time constraints. The book could have benefited immensely from a thorough technical review.

# Pushing the Limits?

My other criticism is about the level of the book and therefore much more subjective. In my opinion, only about one third of the contents really are about “pushing the limits” in that it deals with truly advanced topics. Some examples that I liked:

- A description of the `CALayer` drawing model.
- An explanation of the notion of time in Core Animation animations.
- The discussion of `NSCache` and `NSPurgeableData` and the differences between dirty and resident memory in Instruments’ VM Tracker.
- An explanation of run loops and blocking, read/write locks with concurrent queues and `dispatch_barrier_async`.
- The very thorough chapter on Security with tutorials about verifying and trusting certificates, as well as symmetric encryption.
- The how-to on the inner workings of key-value coding and observing.
- The chapter on Core Foundation with a discussions on memory management, memory allocators, strings and collections. (Which pointed me to this wonderful [Ridiculous Fish article on the origins of toll-free bridging](http://ridiculousfish.com/blog/posts/bridge.html).)
- The chapter on the Objective-C runtime.

On the other side of the spectrum are introductory chapters on Xcode and basic language features like naming conventions, categories and properties that should not waste space in an advanced book. Readers know this stuff already. If they don’t, they know they should read a beginner’s book first.

Sort of in between are topics that would warrant a deep discussion but are only mentioned briefly. At times, this reads like Apple’s [What’s New in iOS 5](http://developer.apple.com/library/ios/releasenotes/General/WhatsNewIniPhoneOS/Articles/iOS5.html#//apple_ref/doc/uid/TP30915195-SW1) document. I got the feeling the authors felt they needed to mention new technologies like storyboards or appearance customization but did not want to expend too much time investigating them. The most glaring example of this is the section on iCloud. The meagre two pages the book devotes to this topic sound more like a marketing document from Apple about iCloud’s amazing capabilities than an informed discussion by people who actually used the APIs. Given the problems many developers had with implementing iCloud in their apps, it sounds even more ridiculous in hindsight. If you don’t have anything to add, better leave it out in the first place.

## Reads Like a Recipes Book

Finally, some parts of the book read like a recipes book. For instance, rather than explaining how one can implement pull to refresh for a table view, the authors explain the usage of a [third-party pull to refresh component](https://github.com/enormego/EGOTableViewPullRefresh), thereby spending little more than one page on the task, with no word on _how_ the implementation works. Similarly, readers are advised to use a third-party networking library rather than learn about the intricacies of `NSURLConnection` and how one would go about integrating it with an `NSOperationQueue`. To me, this is exactly the wrong emphasis. And whatever it does, it doesn’t push the limits. I expected more from a book with this title.

Any criticism of the book’s level of difficulty and emphasis on certain topics is obviously debatable and I recognize that, being a somewhat experienced iOS developer, I may not be among the book’s target audience and therefore not the best judge of these aspects so take it as it is: an opinion. The factual errors I mentioned above are far more important.

# List of Errors

The following is a list of most errors and inaccuracies I found in the book. It makes for some very dull reading but I feel I had to be thorough in my documentation. I hope it does not sound too nit-picky. The list is roughly in the order the issues appear in the book.

Page

Problem

—

Throughout the book, selectors are often listed without the trailing colon (e.g. `drawRect` instead of the correct `drawRect:`).

—

Throughout the book, the authors speak of “category classes” when they mean Objective-C categories. Drives me crazy.

28

Talking about Build Schemes in Xcode:

> You can duplicate the profile scheme so that you have two schemes: one launching Leaks and the other launching Time Profiler.

It would be great if Xcode schemes worked that way but unfortunately they don't. It's not possible to create custom or duplicate existing _actions_ (such as Profile) in a scheme; the only thing you can do is duplicate the entire scheme with all its actions, which is overkill and hard to manage if all you want is edit a parameter for one of the several actions.

39

> Suffix instance variables (ivars) with an underscore or prefix them with `m`. I avoid prefixing with underscore because Apple reserves the leading underscore

No, Apple does not reserve the leading underscore for ivars. In fact, [they recommend using it](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/NamingIvarsAndTypes.html#//apple_ref/doc/uid/20001284-1001757). Rob Napier [acknowledges this error in the errata](http://iosptl.com/posts/leading-underscores/).

42

The discussion of Automatic Reference Counting is confusing in places. The authors say multiple times that, under ARC, you should not call `retain`, `release` or `autorelease` anymore, but fail to mention that doing so is explicitly forbidden. Readers will quickly notices because the compiler will throw an error but I think things like this should be noted in a book.

> **Rob Napier:** The lead-in paragraph is ARC introduces four restrictions on your code… followed by No calls to `retain`, `release`, or `autorelease` as one of the four restrictions. Is “restrictions” and “No” not explicit enough?

72

In the discussion of the singleton pattern, ~~the authors do not distinguish between real singletons (classes of which only one instance can exist) and classes like `NSNotificationCenter`, which aren't singletons despite the fact that only one instance of these will exist in most apps (in this case, the `+defaultCenter`). Furthermore,~~ the authors recommend a pattern for implementing a singleton that is no longer the recommended way. The better method is [mentioned in the errata](http://iosptl.com/posts/the-singleton-pattern/).

> **Rob Napier:** I really tried to explain the difference between real (I call them “strict”) and “shared” singletons on pp. 70-71. Is this not clear? Agreed that my pattern was out-dated, which is why I wrote the errata.

Upon re-reading this section, I have to agree with Rob. This is well described in this section and I did not read it carefully enough. I apologize for pointing this out as an error.

76

The protocols `UITableViewDelegate` and `UITableViewDataSource` are labeled “classes”.

77

> In most cases, nib files do not lower the performance compared to an equivalently coded UI.

If there is any evidence for cases where NIB files cause significantly lower performance than a UI created in code, the authors fail to mention it. The example they give compares a table cell composed in Interface Builder (with multiple subviews) to a [performance-optimized table cell that does its own drawing](https://atebits.tumblr.com/post/197580827/fast-scrolling-in-tweetie-with-uitableview), which I don't consider equivalent.

79

The sample code to manually load a NIB file uses `-[NSBundle loadNibNamed:owner:option:]`. Using the `UINib` class (available since iOS 4) would be more appropriate and probably faster since `UINib` caches the NIB file.

**Update:** Here's a relevant quote from the [`UINib` class reference](http://developer.apple.com/library/ios/#documentation/uikit/reference/UINib_Ref/Reference/Reference.html):

> Your application should use `UINib` objects whenever it needs to repeatedly instantiate the same nib data. For example, if your table view uses a nib file to instantiate table view cells, caching the nib in a `UINib` object can provide a significant performance improvement.

87

> once loaded, nibs are cached.

The authors provide no reference for this statement and I could not find any place where this is documented. My understanding is that the `UINib` class (which is not used in the book) was introduced for exactly that reason and that `loadNibNamed:owner:options:` does not provide any caching. If this is not the case, I do not see why `UINib` should even exist. From the [documentation for `UINib`](http://developer.apple.com/library/ios/#documentation/uikit/reference/UINib_Ref/Reference/Reference.html):

> An UINib object caches the contents of a nib file in memory, ready for unarchiving and instantiation. When your application needs to instantiate the contents of the nib file it can do so without having to load the data from the nib file first, improving performance.

91

The authors confound the terms “superclass” and “owning object”:

> But a good design practice is to let the table cell handle the delegate and notify its super class.

The cell should notify its owner or delegate. It rarely makes sense for an instance to notify its superclass about an event.

107

The authors make no distinction between drawing and compositing systems. UIKit and Core Animation (mostly compositing systems, except for some drawing functionality in UIKit) are lumped together with Core Graphics under the term “drawing systems”. I doubt this makes the responsibilities of each framework any clearer to the reader. Later, Core Graphics is named as the primary drawing system underlying UIKit. I see what they mean here, but I would object. The system underlying UIKit is Core Animation. Core Graphics is largely unrelated.

Also:

> [UIKit] is the highest-level interface, and the only interface in Objective-C.

Wrong. Core Animation and Core Image also have object-oriented interfaces.

124

Sample drawing code steps down to the Core Graphics level to set various advanced line drawing options [line join and line width] not available with `UIBezierPath` when, in fact, `UIBezierPath` does support these attributes.

128

> iOS does not perform partial view drawing, and `setNeedsDisplayInRect:` is the same as `setNeedsDisplay`. The entire view will be redrawn.

[The documentation says the opposite](http://developer.apple.com/library/ios/documentation/uikit/reference/uiview_class/UIView/UIView.html#//apple_ref/doc/uid/TP40006816-CH3-BBCCCHHI). It's in the hand of the programmer whether the entire view will be redrawn or not. It's your responsibility to check the argument of `drawRect:` and decide what needs to be drawn. The authors seem to not have understood how `setNeedsDisplayInRect:` and `drawRect:` are related or they fail to mention it.

**Update:** [Ole Zorn pointed me](https://twitter.com/olemoritz/statuses/245638200478031872) to a quote in [Apple's Technical Q&A QA1708](https://developer.apple.com/library/ios/#qa/qa1708/_index.html):

> **Important** Each `UIView` is treated as a single element. When you request a redraw, in part or whole, by calling `-setNeedsDisplayInRect:` or `-setNeedsDisplay:`, the entire view will be marked for updates.

I tested this again and I can confirm that, on iOS 5.1.1, UIKit definitely passes the rectangle specified in `setNeedsDisplayInRect:` to `drawRect:`, so the developer can choose to only redraw those elements that are inside that area. It seems to me that the information in QA1708 is incorrect.

133

Again, UIKit is called the Objective-C descendant of Core Graphics. I imagine that this is confusing for readers who are not certain about the terminology themselves.

138

> [UIView] is a pretty heavyweight object, so you need to be careful about how many of them you use.

The authors don't offer evidence for this assumption. In my experiments with hundreds of views and layers, the memory overhead of views is negligible and the animation performance of views and layers is identical. From the standpoint of the graphics system, views and layers are identical.

144

The authors call `+[CATransaction disableActions]` and `+[CATransaction setDisableActions:]` a property when, in fact, it is a set of class methods.

148

In the discussion of the `anchorPoint` property of `CALayer`, the book claims that the lower-right corner [of the layer] is (1.0, 1.0) (in terms of the `anchorPoint`) ~~when, in fact, (1.0, 1.0) sets the anchor point in the upper-right corner. Core Animation's coordinate system has its origin in the lower left.~~

**Update:** I was wrong about this one. On iOS, the origin of Core Animation's coordinate system is in fact [the upper left corner, with the y axis pointing downwards](http://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/CoreAnimation_guide/Articles/Layers.html#//apple_ref/doc/uid/TP40006082-SW9). Thanks to Nico Schmidt and [Felix Gabel](https://twitter.com/blinker13/statuses/245594968662618112) for pointing it out.

182/183

Sample code using ARC uses the `__block` specifier in order to avoid a retain cycles caused by a block. `__block` does no longer avoid the retaining of an object by the block under ARC, you have to use `__weak` instead. [Acknowleged in the errata](http://iosptl.com/posts/chapter-9-block-correction/).

191

On `NSXMLParser`:

> Because the parser uses delegation to return data, you need a subclass of NSXMLParser for every object you are handling.

On the contrary. Because it uses delegation, you don't have to subclass `NSXMLParser`, ever. The authors probably want to say that they recommend to create a new custom `NSObject` subclass to act as a delegate for each type of XML data you want to parse, which is good advice.

191

Under the headline _Parsing XML on iOS_, the book discusses both XML SAX and DOM parsers. As an example of the latter, the authors talk briefly about `NSXMLDocument`, despite the fact that it is only available on OS X.

193

> Internally, every web server is coded using some object-oriented programming language.

This claim is obviously wrong and also beside the point. The book is not about web server API design.

193/194

Something from the WTF? department in a discussion about designing model objects that should interface with web services:

> When the reconstructed objects on your iOS app match 100 percent with the objects on the server, the goal of data exchange is attained and your app will be error free.

I never knew it was so easy to make my app error free.

195

The authors claim `NSURLConnection` is part of the CFNetwork framework, which is not true. `NSURLConnection` is part of Foundation.

198

When adding a delegate attribute to a singleton class, the authors chose the unconventional way of defining class methods `+delegate` and `+setDelegate:` rather than instance methods (or a plain property declaration). For a singleton, the result is equivalent but the variant with class methods has the disadvantages of making the class harder to convert into a “pseudo singleton” (a class of which usually only one instance exists but that allows to create more instances if required) and of confusing the reader since all other methods on the class are declared as instance methods. I'd expect an explanation for such a choice, but none is given. Moreover, they then use an instance variable(!) as the backing store for the class's delegate.

In the book's downloadable sample code, [this mess is not present](https://github.com/rnapier/ios5ptl/blob/master/ch10/iHotelApp/iHotelApp/RESTEngine/RESTEngine.h); instead, the authors used a `@property` declaration, as it should be. [The errata](http://iosptl.com/posts/category/updates/) don't mention the change.

The sample code also does not specify the protocol the delegate should conform to in the method declaration (`+ (id)delegate` instead of `+ (id <RESTEngineDelegate>)delegate`).

200

A custom setter method for a retain-property is wrong. In it, the authors first `release` the object that the backing ivar currently points to and then assign and `retain` the new object to the ivar. However, they don't check whether the old and new value for the property are one and the same. If they are, the object gets released before it gets retained again, which could lead to a premature deallocation.

In the same context, the reader learns that he has to include KVO notifications (`willChangeValueForKey:` and `didChangeValueForKey:`) in any custom accessor he writes, [which is totally not true](http://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/KeyValueObserving/Articles/KVOCompliance.html#//apple_ref/doc/uid/20002178-SW1) (the authors say it correctly on p. 295).

214

> The `Library/Caches` directory is special because it isn't backed up but is preserved between application upgrades. This is where you should put most things you don't want copied to the desktop [i.e., the stuff you don't want to be visible to the user of the app].

This is very dangerous advice because the authors neglect to mention that the Caches directory is not guaranteed to remain intact. The OS is free to purge it at regular intervals or when storage space is limited. If an app puts data into the Caches directory that it cannot recreate, it will be irretrievably lost.

[Apple modified the OS's cleaning behavior](http://www.marco.org/2011/10/13/ios5-caches-cleaning) regarding the Caches directory in iOS 5. Given the book's timeframe, it was perhaps difficult to say anything concrete about the actual behavior of the OS, but the authors should definitely not have advised reader to put stuff into the Caches directory that is not meant for caching.

> **Rob Napier:** Apple [explicitly recommend](http://developer.apple.com/library/ios/#documentation/FileManagement/Conceptual/FileSystemProgrammingGUide/FileSystemOverview/FileSystemOverview.html) putting files here you don't want backed up, and it wasn't clear during the betas that these files could be deleted (they weren't in iOS 4). This should have made the errata, however. It has been fixed in the iOS 6 book.

214

> If you have information that you would rather the user not have access to, you can store it in the keychain or in `Library/Caches` because these are not backed up.

Again, this is a totally wrong way to use the Caches directory. If you don't want files to be readable in a device backup, use Apple's own [Data Protection API](http://developer.apple.com/library/ios/DOCUMENTATION/iPhone/Conceptual/iPhoneOSProgrammingGuide/AdvancedAppTricks/AdvancedAppTricks.html#//apple_ref/doc/uid/TP40007072-CH7-SW11), which seamlessly encrypts files on disk and has been available since iOS 4 (a topic the authors even discuss a few pages later).

> **Rob Napier:** The Data Protection API does not apply if the user does not provide a PIN. So if the goal is to provide a little data hiding from casual investigation (which is the topic here), then Data Protection can't help. Given the pre-5.0GM behavior of not deleting these files, I believe this was reasonable advice when it was written. There are better ways now and the book has been updated.

243

In a code snippet, a view controller registers itself as a listener for a notification in the `viewDidLoad` method. The authors recommend placing the corresponding code to unregister from the notification in `viewDidUnload`, which is problematic since `viewDidUnload` is not guaranteed to be called.

272

The occasional plug for your own projects in your book is totally fine, especially if it is about stuff you're not making any money off. In fact, I'd expect it. I'd also expect that you disclose the fact that you are recommending your own stuff. In the chapter about in-app purchase, the authors recommend Mugunth Kumar's own [MKStoreKit](https://github.com/MugunthKumar/MKStoreKit) without mentioning this. The book devotes five pages to MKStoreKit alone and they sound like a commercial in places:

> MKStoreKit … reduces [coding effort] to somewhere near zero. … With frameworks like MKStoreKit minimizing your coding efforts, why not give it a try?

> **Mugunth Kumar:** We talk about ASIHTTPRequest, DTCoreText, EGOPullToRefreshView, SFHFKeychainUtils, SBJSON, JSONKit and a variety of selectively chosen third-party libraries as well. You can't push the limits if you write every component yourself. One should get rid of the “Not-invented-here” syndrome, choose the right third-party component and try to understand and use the library in their app. MKStoreKit has been used in a majority of games, including some from big-named publishers. Thirdly, I'm not selling MKStoreKit. There are no “commercial” intentions behind.

291

Sample code that uses key-value coding to send regular messages to objects:

```
NSArray *array = [NSArray arrayWithObjects:@"foo", @"bar", @"baz", nil];
NSArray *capitalLength = [array valueForKeyPath:@"capitalizedString.length"];
```

While technically correct, this is horrible code! Please use a method like `enumerateObjectsUsingBlock:` to do something like this (or write your own `-mapUsingBlock:` method with it).

> **Rob Napier:** The goal here was to demonstrate higher order messaging in a simple example. I don't think enumerateObjectsUsingBlock: is the obvious solution … But that's not the point. The point was to demonstrate higher order messaging, which can be very powerful. For instance, the string above could be looked up dynamically, or even built dynamically, which allows operations that are can be difficult using blocks. It's not an everyday tool, but it is useful to know it exists.

I stand by my point that using KVC for other purposes than accessing attributes is a very bad practice. There are clearer ways to implement [higher order messaging](https://en.wikipedia.org/wiki/Higher_order_message) in Cocoa (blocks, invocations). Granted, these other solutions are not one-liners, but you don't need a one-liner for something you rarely use and can encapsulate nicely. A very good example of this concept (not using blocks) is given in [Cocoa Design Patterns](https://oleb.net/blog/2010/01/book-review-cocoa-design-patterns/) on pp. 321-326.

305

The authors implement a `UIAlertView` category that uses blocks instead of delegation. In the implementation, they use a static variable to store the completion block and therefore this category only works for one alert view at a time. I don't necessarily expect perfect sample code in a book. But an ackknowledgement of the limitations of your own code would be nice – especially when it helps learning. Since [associative references](https://oleb.net/blog/2011/05/faking-ivars-in-objc-categories-with-associative-references/) were mentioned much earlier in the book, I'd rather have seen an implementation using that technique.

> **Mugunth Kumar:** True, but this was intentional. I wanted to focus on one thing. That one thing here is blocks. Talking about associative references + blocks + delegates means the chapter will lose its essence. Readers are not going to understand anything.

318

> Any sqlite3 library … is almost always going to be slower than Core Data.

Again, a claim with no evidence. It goes on:

> In addition, while sqlite3 is thread-safe, the binary bundled with iOS is not. So unless you ship a custom-built sqlite3 library (compiled with the thread-safe flag), it becomes your responsibility to ensure that data access to and from the sqlite3 database is thread-safe. Because Core Data has so much more to offer and is thread-safe, I suggest avoiding native SQLite as far as possible on iOS.

That sounds as if Core Data made multi-threaded access really easy. My experience is rather different.

> **Mugunth Kumar:** A book is not a research publication where every claim needs evidence. In a chapter that doesn't talk about Core Data (this chapter talks about caching), I wouldn't prefer writing in depth about multi-threading with Core Data.

338

In a discussion about `-[CALayer renderInContext:]`:

> For web views larger than 1024×1024, you need to break them up into smaller pieces and render them individually.

I am not entirely certain, but I believe this advice is no longer correct. Views had a maximum size of 1024×1024 in the early days of iOS but this limit is long gone. If I remember correctly, I just recently used `renderInContex:` successfully on a web view that was larger than 1024 points in one dimension (though not in both).

342

> Core Text was originally designed on the Mac, and it performs all calculations in Mac coordinates. The origin is in the lower-left corner

Really, Mac coordinates? As if Core Graphics used different coordinate systems on iOS and Mac.

> **Rob Napier:** I think “Mac coordinates” is a fair way to describe lower-left origin without confusing the reader.

# The iOS 6 Edition

I regret the unfortunate timing of this review. The [new edition of the book](http://blog.mugunthkumar.com/products/ios-6-programming-pushing-the-limits/), updated for iOS 6, is not yet out but from what I’ve read, it’s probably too late in the production process to incorporate any of the changes I recommend here. The fact that the [errata for the iOS 5 edition](http://iosptl.com/posts/category/updates/) are currently very short makes me worry that most problems I identified have not been fixed in the new edition.

I’d love to be proven wrong.
