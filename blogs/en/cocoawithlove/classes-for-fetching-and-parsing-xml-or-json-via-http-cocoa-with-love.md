---
title: 'Classes for fetching and parsing XML or JSON via HTTP | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2011/05/classes-for-fetching-and-parsing-xml-or.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:dc847aab64705532'
translated: false
---

> 原文：[Classes for fetching and parsing XML or JSON via HTTP | Cocoa with Love](https://www.cocoawithlove.com/2011/05/classes-for-fetching-and-parsing-xml-or.html)　·　Cocoa with Love (Matt Gallagher)

In this post I show two reusable classes for fetching data via HTTP: one that parses the result as XML and another that parses as JSON. These are relatively simple tasks but due to the number of required steps, they can become tiresome if you don't have robust, reusable code for the task. These classes will work on iOS or on the Mac but the optional error alerts and password dialogs are only implemented for iOS.

## Introduction

In my experience, "fetching data via HTTP" is probably the second most common task that iOS applications perform after "displaying a list of things in a table". Since I [wrote a recent post showing how I handle display in tables](https://www.cocoawithlove.com/2010/12/uitableview-construction-drawing-and.html), showing my reusable classes for fetching via HTTP seemed like a reasonable follow up.

As with the post on `UITableView` management, this post is all about trying to make the HTTP fetching, handling and processing as simple and reusable as possible.

What I hope to demonstrate is that even though the Cocoa API makes it look like you need to bolt `NSURLConnection` delegate methods onto your own classes every time you need a network connection, it doesn't mean that you actually need to do all this work every time you need a network connection. For the most common tasks like this, you should develop your own, reusable approaches that you like, that serve your needs and that make new code easier.

There are lots of alternative approaches around that demonstrate similar ideas. My implementation is a simple implementation compared to full frameworks (for a more thorough implementation along similar lines, you may want to look at [RestKit](http://restkit.org/)). I hope you'll still be able to see the contrast compared to ad hoc solutions though, especially if you've ever jammed HTTP communication into your projects without thinking about keeping the interface clean and simple.

> HTTPXMLJSONFetchers.zip
> 
> (16kB)

## HTTP connections in Cocoa

BSD sockets and `CFHTTPStream` are generally too low level to use regularly. Unless your program requires meticulous control of the network layer, you probably want to use `NSURLConnection` for handling HTTP fetching.

Technically, `NSURLConnection` can perform network connections in a single instruction: `+[NSURLConnection sendSynchronousRequest:returningResponse:error:]`. Synchronous connection should be avoided in all but a few rare worker-thread situations because it stops your program's user-interface and it doesn't allow careful error handling.

This means that when fetching via HTTP, you should be using `NSURLConnection`'s delegate methods. The delegate methods are:

```objc
- (void)connection:(NSURLConnection *)connection didReceiveResponse:(NSURLResponse *)response
- (void)connection:(NSURLConnection *)connection didReceiveData:(NSData *)data
- (void)connection:(NSURLConnection *)connection didFailWithError:(NSError *)error
- (void)connection:(NSURLConnection *)aConnection didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *)aChallenge
- (void)connectionDidFinishLoading:(NSURLConnection *)connection
```

and a thorough implementation means implementing all 5 of these methods.

A commonly seen case for this is to add the `NSURLConnection` delegate methods to your `UITableViewController` and make that view controller manage the connection.

While this might seem like a good idea (the view controller can track the status of the connection and provide visual updates and also present its own errors) the reality is that fully handling the connection takes a lot of code. How much code? The code I use is 530 lines long (including comments and spacing).

But there's also a more serious problem: bolting `NSURLConnection` to your `UITableViewController` limits code reuse. If your network code is tied closely to the view controller, there's more work involved in adding network behaviors to other view controllers or parts of your program.

Why do `NSURLConnection` delegates take so much code to implement? In the simplest case, they don't (you could probably manage a connection in 20 lines or so) but you'd be overlooking a lot of subtler behaviors. Errors, password authentication, cancelling the connection cleanly and offering simple construction versus meticulous construction are the type of behaviors that get left out if you're rewriting the code every time or operating under serious time constraints.

## HTTPFetcher

The idea behind my `HTTPFetcher` class is really simple: it's reusable `NSURLConnection` delegate. It handles all the `NSURLConnection` delegate work and calls back when it has the results. It provides default error handling, password authentication and while it has a very simple default constructor, it still provides enough hooks that you can customize its behavior.

The interface to the class is really just construction methods, a start, a cancel and some properties. The `assign` properties are for configuring the connection before you start it. The `readonly` properties are for gathering information once the connection is complete.

```objc
@interface HTTPFetcher : NSObject &lt;UITextFieldDelegate&gt;

@property (nonatomic, readonly) NSData *data;
@property (nonatomic, readonly) NSURLRequest *urlRequest;
@property (nonatomic, readonly) NSDictionary *responseHeaderFields;
@property (nonatomic, readonly) NSInteger failureCode;
@property (nonatomic, assign) BOOL showAlerts;
@property (nonatomic, assign) BOOL showAuthentication;
@property (nonatomic, assign) void *context;

- (id)initWithURLRequest:(NSURLRequest *)aURLRequest
    receiver:(id)aReceiver
    action:(SEL)receiverAction;
- (id)initWithURLString:(NSString *)aURLString
    receiver:(id)aReceiver
    action:(SEL)receiverAction;
- (id)initWithURLString:(NSString *)aURLString
    timeout:(NSTimeInterval)aTimeoutInterval
    cachePolicy:(NSURLCacheStoragePolicy)aCachePolicy
    receiver:(id)aReceiver
    action:(SEL)receiverAction;
- (void)start;
- (void)cancel;

@end
```

You initialize the class in whatever way you choose (the middle init method shown here is the simplest), optionally configure the class (the most common configuration is to set the `context` pointer so that when the connection completes, you can remember where to set the data), start the connection and then it will invoke the `receiverAction` on your `receiver` object (the receiver action takes one parameter: the `HTTPFetcher` itself).

```objc
// Example fetcher creation
fetcher = [[HTTPFetcher alloc]
    initWithURLString:@"http://some-domain.com/some/path"
    receiver:self
    action:@selector(receiveResponse:)];
[fetcher start];

// Example fetcher response handling
- (void)receiveResponse:(HTTPFetcher *)aFetcher
{
    NSAssert(aFetcher == fetcher,
        @"In this example, aFetcher is always the same as the fetcher ivar we set above");
    if ([fetcher.data length] &gt; 0)
    {
        [self doSomethingWithTheData:fetcher.data];
    }
    [fetcher release];
    fetcher = nil;
}
```

Ordinarily, your program will want to customize the code that presents the errors and make the presentation consistent to your application. You can do this with the `HTTPFetcher` class by either subclassing or editing the class itself or you can disable the alerts and authentication functionality and perform the work outside the class. However, if you don't have time to do this customization, there is default behavior in the class that will suffice.

> : the
> 
> does not retain itself while running and does not retain the
> 
> . This is because the expected behavior is that the receiver retains the
> 
> and we don't want a
> 
> retain cycle
> 
> . If you create the
> 
> and don't have a retain count on it, it will immediately auto-
> 
> itself and
> 
> .

## XMLFetcher

The `HTTPFetcher` is fine if you simply want the data from an HTTP connection. For my own purposes though, I've never used the `HTTPFetcher` on its own — I've always used it as the base-class for classes which post-process the HTTP data before invoking the receiver's callback method.

The `XMLFetcher` class is for turning an XML response into something more useful. Instead of needing to look at the `data` property of the `HTTPFetcher`, you can use the `results` property which is the array of nodes matching a given XPath query on the XML result.

```objc
@interface XMLFetcher : HTTPFetcher

@property (nonatomic, copy, readonly) NSString *xPathQuery;
@property (nonatomic, retain, readonly) NSArray *results;

- (id)initWithURLString:(NSString *)aURLString
    xPathQuery:(NSString *)query
    receiver:(id)aReceiver
    action:(SEL)receiverAction;

@end
```

I've [previously spoken](https://www.cocoawithlove.com/2008/10/using-libxml2-for-parsing-and-xpath.html) about how I'm not a fan of the event-driven model (sometimes called a SAX parser) promoted by Apple in the iOS API. It is certainly memory efficient and faster for large files but it requires you perform your own structured handling which is tiresome, prone to mistakes and not really reusable. I personally prefer a document-based model like the `NSXML` API that exists in Mac OS X but not in iOS.

The `XMLFetcher` class blends the libXML-based XPath based parsing and querying with the `HTTPFetcher`.

However, I've addressed a number of the shortcomings of my previous libXML-based parsing. The biggest problem with that earlier code was that it simply packaged the XML into `NSDictionary`s (which is inelegant at best) — so instead, the results are now a dedicated `XPathResultNode` class which can cleanly represent `attributes`, `childNodes` and `contentString`s. There's also better handling of content strings either side of subnodes and concatenating of text data spread over subnodes.

```objc
@interface XPathResultNode : NSObject

@property (nonatomic, retain, readonly) NSString *name;
@property (nonatomic, retain, readonly) NSMutableDictionary *attributes;
@property (nonatomic, retain, readonly) NSMutableArray *content;

+ (NSArray *)nodesForXPathQuery:(NSString *)query onHTML:(NSData *)htmlData;
+ (NSArray *)nodesForXPathQuery:(NSString *)query onXML:(NSData *)xmlData;

- (NSArray *)childNodes;
- (NSString *)contentString;
- (NSString *)contentStringByUnifyingSubnodes;

@end
```

XPath query note: XPath queries can be a little difficult to get used to — if you're not accustomed to XPath, it can be hard to extract the exact nodes you want. Like regular expressions though, they're a highly specialized language for extracting data and once you understand the different functions available, they are the quickest way of getting specific nodes out of XML.

> : the XPathResultNode.m file contains a comment at the time which explains the Xcode compiler settings required to make it work. Basically, you need to include libxml in the include path and link your project with libxml2.dylib.

## JSONFetcher

The `JSONFetcher` is really just the same idea as the `XMLFetcher` — parse the result from `HTTPFetcher` once complete, this time as JSON data.

The class I've written relies on [SBJSON](http://stig.github.com/json-framework/), Stig Brautaset's BSD-licensed JSON parsing library. You will need to download these files separately and include them in your project (it's 3 .m files and 4 .h files).

SBJSON isn't your only option for JSON handling in iOS or Mac OS X. There are a few other [JSON libraries for iOS and Mac discussed here on Stackoverflow](http://stackoverflow.com/questions/2256625/comparison-of-json-parser-for-objective-c-json-framework-yajl-touchjson-etc) if you'd prefer options. Obviously though, you'd need to make minor adjustments to integrate a different parser.

With a JSON response, there's not the same expectation of needing to find a subnode within a larger result (as is the common case for XML), so the JSON parser simply parses the whole JSON structure and returns it all.

```objc
@interface JSONFetcher : HTTPFetcher

@property (nonatomic, readonly) id result;

@end
```

## Conclusion

> HTTPXMLJSONFetchers.zip
> 
> (16kB)

I've presented my classes for handling these tasks. I don't expect that everyone has the same data and network requirements as I do, so there's every chance that you would need very different classes to suit your own exact needs.

The point is really to consider reuse in your own code — how can you evolve your classes so that when you start a new project you need to rewrite as little as possible — you can simply bring in your own class for handling network data, pass different parameters into its constructor and your network connection is done.

Until I had composed these classes for my own purposes, new projects involved hundreds of lines of code that went through a copy, paste, refactor process from existing projects I'd written. While copy, paste, refactor will work, it is slower, more prone to errors and harder to keep up-to-date than properly reusable classes. In most cases, you should view copy and paste as a failure of your own processes. That's a hard rule to adhere to, since copy, paste, refactor is faster than designing a reusable class — or at least it is initially (compared to an up-front design effort). You need to have the discipline to recognize the common behaviors between classes or projects and refactor into shared classes if required.

A final thought: I realize I I haven't really shown these classes at work in an example program. If you can't work out how to use them in a real program, please wait a week or two: I plan to share a real-world project that uses them to handle all its network communication.
