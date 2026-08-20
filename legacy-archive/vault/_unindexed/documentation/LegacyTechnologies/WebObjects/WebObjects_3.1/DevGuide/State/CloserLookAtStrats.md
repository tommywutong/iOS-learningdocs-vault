---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/CloserLookAtStrats.html
archived_at: '2026-07-15T07:47:39.371145Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](StoreCompTable.md)

# A Closer Look at Storage Strategies

The SessionStores example application that accompanies this documentation demonstrates various ways to store state. The code excerpts used in the following sections come from the SessionStores example, so please refer to the example itself for more details about the implementation.

__Note:__  The SessionStores example was designed to illustrate WebObjects' support for various state storage strategies and so lets you switch between strategies while the application is running. This is not a design you should emulate in your applications---changing storage strategies mid-session can cause errors. For example, imagine an application that stores state in the page during the first half of a session and stores state in cookies for the second. Now suppose that the user backtracks from a page in the second half to one in the first and resubmits the page. The application's strategy and the actual storage mechanism won't match, and state will be lost.

The SessionStores application presents the user with a choice of storage strategies:

!

__Figure 1.__  SessionStores: Storage Choices

Once an initial choice has been made, the application plays a guessing game with the user:

!

__Figure 2.__  SessionStores: Guessing Game

As you can see, the application keeps track of a user's previous guesses within a session---this, in part, is the state that must be stored from transaction to transaction.

This application switches between storage strategies through the facilities of the WOApplication and WOSessionStore classes. WOApplication declares the __setSessionStore:__ method that lets you switch between strategies, and WOSessionStore declares the following methods to create specific types of session stores:

- serverSessionStore
- pageSessionStore
- cookieSessionStoreWithDistributionDomain:secure:

In the SessionStores example, the __setStateStorageStrategy__ method demonstrates how these methods work together to set the application's storage type (from __StoreSwitch.wos__). When the user makes a choice from the strategy list, the __setStateStorageStrategy__ method is invoked and sets the desired strategy:

```
- setStateStorageStrategy {
    id sessionStore;
    id strategyIndex;
    ...
    // Code to determine the value of strategyIndex
    // which indicates which choice the user has made
    ...
    // Set the state storage strategy
    if ( strategyIndex == 0 ) {
        sessionStore = [WOSessionStore serverSessionStore];
    } else if ( strategyIndex == 1 ) {
        sessionStore = [WOSessionStore pageSessionStore];
    } else if ( strategyIndex == 2 ) {
        sessionStore = [WOSessionStore
            cookieSessionStoreWithDistributionDomain:@"" secure:NO];
    } else if ( strategyIndex == 3 ) {
        // Use a custom session store
        sessionStore = [[[FileSessionStore alloc] init] autorelease];
    }
    [[self application] setSessionStore:sessionStore];
    ...
    return [[self application] pageWithName:@"Pages/Guess"];
}
```

(Notice too that this application lets the user choose to store state in the file system using the custom FileSessionStore class. We'll examine this approach in "[Custom State Storage Options](CustomStorageOptions.md)" below.)

Normally, an application chooses just one storage strategy for the duration of its execution and so establishes that strategy in the __init__ method of the __Application.wos__ file.

[!Table of Contents](ManagingState.book.md)
[!Next Section](StateInServer.md)
