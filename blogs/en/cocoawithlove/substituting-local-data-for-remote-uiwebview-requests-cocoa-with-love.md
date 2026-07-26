---
title: 'Substituting local data for remote UIWebView requests | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/09/substituting-local-data-for-remote.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:322307c1f9cee08f'
translated: false
---

> 原文：[Substituting local data for remote UIWebView requests | Cocoa with Love](https://www.cocoawithlove.com/2010/09/substituting-local-data-for-remote.html)　·　Cocoa with Love (Matt Gallagher)

In this post, I'll show you how you can load a webpage in a UIWebView in iOS while using a modified NSURLCache to substitute local copies of resources within the webpage for the remote copies referred to by the actual page.

## Introduction

Normally if you're writing an iOS app with network connectivity, you'll want to put a native iOS interface on all data received over the network.

However, there are always scheduling and other constraints on a project that limit what you can implement and sometimes you may simply choose to show a regular, webpage to the user.

If you choose to take this approach, it is best to make sure the web interface feels as smooth as possible. One of the steps you can take to ensure this is to include local copies of all image and other non-updating resources within the application itself.

To use a local resource in an iOS webpage loaded from a remote location, either the remote page must refer to the local resource in some way (e.g. through a custom URL scheme) or you must swap a local location in place of a remote locations.

In this post, I'll look at how we can substitute a local resource when the webpage contains references to remote resources.

## NSURLCache

On the Mac, you could use a range of different approaches in the `WebViewDelegate` to do this, including implementing `webView:resource:willSendRequest:redirectResponse:fromDataSource:` to substitute one `NSURLRequest` for another. Unfortunately, the `UIWebViewDelegate` in iOS is not nearly as capable so we need to do this another way.

Fortunately, there is one point you can hook into that is invoked for (almost) every request: the `NSURLCache`.

Normally, very little is actually cached in the `NSURLCache`, particularly on older iOS devices where the cache size is downright miniscule. Even if you use the `setMemoryCapacity:` method to increase the size of the cache, it seems significantly less likely to store resources than the NSURLCache on the Mac.

Of course that doesn't matter in this case, since we're going to subclass `NSURLCache` and implement our own version that will be guaranteed to hold all the resources we need and won't need pre-caching (all the resources will be there before the program is started).

## cachedResponseForRequest:

The only important method we need to override is `cachedResponseForRequest:`. This will allow us to examine every request before it is sent and return local data if we prefer.

For this code, I'll use a dictionary that maps remote URLs to local file names in the Resources folder of the application bundle. If any request is made for the specified URLs, the contents of the local file will be returned instead.

So given the following dictionary containing a single path for substitution:

```objc
- (NSDictionary *)substitutionPaths
{
    return
        [NSDictionary dictionaryWithObjectsAndKeys:
            @"fakeGlobalNavBG.png",
            @"http://images.apple.com/global/nav/images/globalnavbg.png",
        nil];
}
```

The following `cachedResponseForRequest:` implementation will substitute the contents of the `fakeGlobalNavBG.png` file in the Resources folder any time the URL `http://images.apple.com/global/nav/images/globalnavbg.png` is requested.

```objc
- (NSCachedURLResponse *)cachedResponseForRequest:(NSURLRequest *)request
{
    // Get the path for the request
    NSString *pathString = [[request URL] absoluteString];
    
    // See if we have a substitution file for this path
    NSString *substitutionFileName = [[self substitutionPaths] objectForKey:pathString];
    if (!substitutionFileName)
    {
        // No substitution file, return the default cache response
        return [super cachedResponseForRequest:request];
    }
    
    // If we've already created a cache entry for this path, then return it.
    NSCachedURLResponse *cachedResponse = [cachedResponses objectForKey:pathString];
    if (cachedResponse)
    {
        return cachedResponse;
    }
    
    // Get the path to the substitution file
    NSString *substitutionFilePath =
        [[NSBundle mainBundle]
            pathForResource:[substitutionFileName stringByDeletingPathExtension]
            ofType:[substitutionFileName pathExtension]];
    NSAssert(substitutionFilePath,
        @"File %@ in substitutionPaths didn't exist", substitutionFileName);
    
    // Load the data
    NSData *data = [NSData dataWithContentsOfFile:substitutionFilePath];
    
    // Create the cacheable response
    NSURLResponse *response =
        [[[NSURLResponse alloc]
            initWithURL:[request URL]
            MIMEType:[self mimeTypeForPath:pathString]
            expectedContentLength:[data length]
            textEncodingName:nil]
        autorelease];
    cachedResponse =
        [[[NSCachedURLResponse alloc] initWithResponse:response data:data] autorelease];
    
    // Add it to our cache dictionary for subsequent responses
    if (!cachedResponses)
    {
        cachedResponses = [[NSMutableDictionary alloc] init];
    }
    [cachedResponses setObject:cachedResponse forKey:pathString];
    
    return cachedResponse;
}
```

## Setting our cache as the shared cache

A `UIWebView` will try to use the current `+[NSURLCache sharedURLCache]`. To get our code called, you'll need to create an instance of our `NSURLCache` subclass and invoke `+[NSURLCache setSharedURLCache:]`.

A big warning here: once you set a new web cache, you probably want to leave it set until your program exits.

When the `UIWebView` requests resources from your `NSURLCache`, it assumes that the `NSURLCache` retains the `NSCachedURLResponse`. If you release the `NSCachedURLResponse` while any `UIWebView` is using it, it will probably crash your app.

Unfortunately, it is pretty hard to force WebKit to let go of its references — it can hold onto them indefinitely in some cases. Until WebKit itself chooses to invoke `removeCachedResponseForRequest:` to tell you that you can throw away the resource you must hold onto it.

What this means is that you should only have one `NSURLCache` in your program. Set it in your `application:didFinishLaunchingWithOptions:` method and never remove it.

## A limitation...

Obviously, if you're overriding the cache to substitute local data, it will only work if the request actually looks at the cache.

This means that if the URL is requested with `requestWithURL:cachePolicy:timeoutInterval:` with a cache policy of `NSURLRequestReloadIgnoringCacheData`, the the request will bypass this local substitution.

By default, `NSURLRequest`s have a cache policy of `NSURLRequestUseProtocolCachePolicy`. The HTTP cache policy is pretty complicated and while I've never actually seen a normal `NSURLRequest` actually bypass the cache, the number of rules involved create a situation where it seems like it may be possible in some situations. Your app should not misbehave if this were to happen for some reason.

## The LocalSubstitutionCache sample app

> LocalSubstitutionCache.zip
> 
> (66kb) sample project

Here's a small screenshot of today's [http://www.apple.com](http://www.apple.com) running in a `UIWebView`:

![](https://www.cocoawithlove.com/assets/objc-era/screenshot.png)

## Conclusion

The purpose of this work is to allow `UIWebView`s to feel more responsive and a bit more like native user-interfaces.

In reality, a `UIWebView` will never feel as responsive or integrated as a native user-interface but sometimes making one screen of your app a remote webpage is a big enough saving in developer resources that you're prepared to make the sacrifice in user quality. Making sure as many resources as possible are stored locally will help make any negative impact on user quality as minor as possible.
