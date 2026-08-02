---
title: NSNetServices and CFNetServices Programming Guide
apple_id: TP40002736
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSNetServiceProgGuide/Articles/BrowsingForDomains.html
archived_at: '2026-07-15T08:18:17.944972Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [NSNetServices and CFNetServices Programming Guide](About%20NSNetServices%20and%20CFNetServices.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20CFNetServices.md)

# Browsing for Domains

Depending on your app, you may or may not need to browse for domains. You should consider browsing for domains if:

- You want to provide the ability for the user to control which domains are used for service-browsing purposes.
- You want to provide the ability for the user to control which domains your app uses when publishing its services.
- You are writing a specialized Bonjour browser and you want to show all possible domains in your service-browsing results, even if those domains did not return any results.
- You need to obtain a complete list of all domains that the computer knows about, even if they are not enabled by default.

If your app does not meet any of those criteria, you probably do not need to browse for domains. However, if your app lets the user browse for services, you should still design your user interface in such a way that the user can distinguish between multiple identical results provided by different domains.

This chapter explains how to discover what domains are available for use in future browsing or service registration activities.

The [NSNetServiceBrowser](https://developer.apple.com/documentation/foundation/netservicebrowser) class provides methods for browsing available domains. Use these methods if you are writing an app that needs to publish or browse domains other than the default domains.

Because domain browsing can take time, `NSNetServiceBrowser` objects perform browsing asynchronously by registering with a run loop. Browsing results are returned to your app through delegate methods. To correctly use an `NSNetServiceBrowser` object, you must assign it a delegate.

Browsing for domains takes three steps:

1. Initialize an `NSNetServiceBrowser` instance, and assign a delegate to the object.
2. Begin a search for domains (either for registration or for browsing).
3. Handle search results and other messages sent to the delegate object.

The following sections describe these steps in detail.

To initialize an `NSNetServiceBrowser` object, use the `init` method. This method sets up the browser and adds it to the current run loop. If you want to use a run loop other than the current one, use the `removeFromRunLoop:forMode:` and `scheduleInRunLoop:forMode:` methods.

After you initialize the object, you can use it to search for domains in which you can register services (with the `searchForRegistrationDomains` method) or browse for services (with the `searchForBrowseDomains` method).

When you are finished, call the `stop` method. You should perform any necessary cleanup in the `netServiceBrowserDidStopSearch:` delegate callback.

Listing B-1 demonstrates how to browse for registration domains with `NSNetServiceBrowser`. The code initializes the object, assigns a delegate, and begins a search for available domains.

__Listing B-1__  Browsing for registration domains

```
id delegateObject; // Assume this object exists.
NSNetServiceBrowser *domainBrowser;

domainBrowser = [[NSNetServiceBrowser alloc] init];
[domainBrowser setDelegate:delegateObject];
[domainBrowser searchForRegistrationDomains];
```


`NSNetServiceBrowser` returns all browsing results to its delegate. If you are using the class to browse for domains, your delegate object should implement the following methods:

- `netServiceBrowserWillSearch:`
- `netServiceBrowserDidStopSearch:`
- `netServiceBrowser:didNotSearch:`
- `netServiceBrowser:didFindDomain:moreComing:`
- `netServiceBrowser:didRemoveDomain:moreComing:`

The `netServiceBrowserWillSearch:` method notifies the delegate that a search is commencing. You can use this method to update your user interface to reflect that a search is in progress. When browsing stops, the delegate receives a `netServiceBrowserDidStopSearch:` message. In that delegate method, you can perform any necessary cleanup.

If the delegate receives a `netServiceBrowser:didNotSearch:` message, it means that the search failed for some reason. You should extract the error information from the dictionary with the `NSNetServicesErrorCode` key and handle the error accordingly. See [NSNetServicesError](https://developer.apple.com/documentation/foundation/netservice/errorcode) for a list of possible errors.

You track domains with two methods—`netServiceBrowser:didFindDomain:moreComing:` and `netServiceBrowser:didRemoveDomain:moreComing:`—which indicate that a service has become available or has shut down. The `moreComing` parameter indicates whether more results are on the way. If this parameter is `YES`, you should not update any user interface elements until the method is called with a `moreComing` parameter of `NO`. If you want a list of available domains, you need to maintain your own array based on the information provided by delegate methods.

Listing B-2 shows the interface for a class that responds to the `NSNetServiceBrowser` delegate methods required for domain browsing, and Listing B-3 shows its implementation. You can use this code as a starting point for your domain browsing code.

__Listing B-2__  Interface for an `NSNetServiceBrowser` delegate object used when browsing for domains

```objc
#import <Foundation/Foundation.h>

@interface NetServiceDomainBrowserDelegate : NSObject <NSNetServiceBrowserDelegate>
{
    // Keeps track of available domains
    NSMutableArray *domains;

    // Keeps track of search status
    BOOL searching;
}

// NSNetServiceBrowser delegate methods for domain browsing
- (void)netServiceBrowserWillSearch:(NSNetServiceBrowser *)browser;
- (void)netServiceBrowserDidStopSearch:(NSNetServiceBrowser *)browser;
- (void)netServiceBrowser:(NSNetServiceBrowser *)browser
        didNotSearch:(NSDictionary *)errorDict;
- (void)netServiceBrowser:(NSNetServiceBrowser *)browser
        didFindDomain:(NSString *)domainString
        moreComing:(BOOL)moreComing;
- (void)netServiceBrowser:(NSNetServiceBrowser *)browser
        didRemoveDomain:(NSString *)domainString
        moreComing:(BOOL)moreComing;

// Other methods
- (void)handleError:(NSNumber *)error;
- (void)updateUI;

@end
```


__Listing B-3__  Implementation for an `NSNetServiceBrowser` delegate object used when browsing for domains

```objc
#import "NetServiceDomainBrowserDelegate.h"

@implementation NetServiceDomainBrowserDelegate

- (id)init
{
    self = [super init];
    if (self) {
        domains = [[NSMutableArray alloc] init];
        searching = NO;
    }
    return self;
}

// Sent when browsing begins
- (void)netServiceBrowserWillSearch:(NSNetServiceBrowser *)browser
{
    searching = YES;
    [self updateUI];
}

// Sent when browsing stops
- (void)netServiceBrowserDidStopSearch:(NSNetServiceBrowser *)browser
{
    searching = NO;
    [self updateUI];
}

// Sent if browsing fails
- (void)netServiceBrowser:(NSNetServiceBrowser *)browser
        didNotSearch:(NSDictionary *)errorDict
{
    searching = NO;
    [self handleError:[errorDict objectForKey:NSNetServicesErrorCode]];
}

// Sent when a domain appears
- (void)netServiceBrowser:(NSNetServiceBrowser *)browser
        didFindDomain:(NSString *)domainString
        moreComing:(BOOL)moreComing
{
    [domains addObject:domainString];
    if(!moreComing)
    {
        [self updateUI];
    }
}

// Sent when a domain disappears
- (void)netServiceBrowser:(NSNetServiceBrowser *)browser
        didRemoveDomain:(NSString *)domainString
        moreComing:(BOOL)moreComing
{
    [domains removeObject:domainString];

    if(!moreComing)
    {
        [self updateUI];
    }
}

// Error handling code
- (void)handleError:(NSNumber *)error
{
    NSLog(@"An error occurred. Error code = %@", error);
    // Handle error here
}

// UI update code
- (void)updateUI
{
    if(searching)
    {
        // Update the user interface to indicate searching
        // Also update any UI that lists available domains
    }
    else
    {
        // Update the user interface to indicate not searching
    }
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](Using%20CFNetServices.md)

