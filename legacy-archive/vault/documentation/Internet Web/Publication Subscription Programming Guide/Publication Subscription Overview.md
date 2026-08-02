---
title: Publication Subscription Programming Guide
apple_id: TP40004945
resource_type: Guide
platform: macOS
topic: null
technology: PublicationSubscription
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/InternetWeb/Conceptual/PubSub/overview/overview.html
archived_at: '2026-07-15T07:43:35.395304Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Publication Subscription Programming Guide](Introduction.md)


[Next](Subscribing%20to%20a%20Feed.md)[Previous](Understanding%20Feeds.md)

# Publication Subscription Overview

When used properly, Publication Subscription allows your application to subscribe to feeds, and update the feeds transparently. However, the technology requires the cooperation of multiple components. This chapter describes the major components of Publication Subscription, along with the architecture of the framework.

The Publication Subscription technology provides an architecture for your application to subscribe feeds. There are three major components to the technology: the Publication Subscription framework (`PubSub.framework`), the PubSub Agent, and the PubSub Database.

The framework is a collection of Objective-C classes that provide an abstraction for each piece of a feed. The framework uses a background application to perform such tasks as downloading feeds from the Internet, and updating feeds. This background application, called the PubSub Agent, is also responsible for sending notifications to clients of the Publication Subscription framework, and receiving interprocess communications (IPCs) from the clients when necessary.

When feeds are downloaded, the PubSub Agent stores the new information into a database known as the PubSub Database. For each user account there is a single PubSub Database, so a feed is only stored once per user account. If two separate applications are subscribing to the same feed, only one copy is stored in the database.

The Publication Subscription components can be seen in Figure 2-1.

__Figure 2-1__  Publication Subscription layers

!

The Publication Subscription framework is designed to have a similar structure to that of a set of feeds. Each component of a feed (including the feed itself) is stored as an object, and the object’s hierarchy mimics that of a feed (see Figure 2-2). At the same time, the Publication Subscription framework follows the observer design pattern. The observer design pattern defines a one-to-many dependency between objects so that when the subject object changes state, all its dependents are notified and updated automatically. (For more information about the observer design pattern, read [Cocoa Design Patterns](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaFundamentals/CocoaDesignPatterns/CocoaDesignPatterns.html#//apple_ref/doc/uid/TP40002974-CH6).)

__Figure 2-2__  A feed structure as a set of objects

!

For your application to communicate with the PubSub Agent, it needs to register itself with Publication Subscription by generating a client object (`PSClient`). Each application that uses Publication Subscription needs its own client object. If you want to subscribe to a feed, you need to tell the client object. Similarly, if there is a change in a feed your application subscribes to, the client notifies your application. In terms of the observer model, the subject object of the Publication Subscription framework is the client object.

The client object maintains a set of feed objects, one for each feed that it is subscribed to. A feed object (`PSFeed`) stores information about a feed, such as its title, its URL, the time when it was last updated, and the entries associated with it. Just as a feed contains a number of entries, feed objects contain a number of entry objects (`PSEntry`). An entry object contains the content (`PSContent`), the author (`PSAuthor`), and (if necessary) the enclosure (`PSEnclosure`) of the entry. Figure 2-3 shows an entry, and each of its components, viewed using Safari.

__Figure 2-3__  An entry viewed with Safari

!

You can adjust the settings for each client and feed object. For example, you can specify how often to check for feed updates or how long entries should be stored in the PubSub Database. You specify the settings with a settings object (`PSFeedSettings`). A settings object can be associated with either a client or a feed.

The structure of the subscription objects can be seen in Figure 2-4.

__Figure 2-4__  Subscription object structure

!

Understanding the components of Publication Subscription and the Publication Subscription framework is necessary for subscribing to feeds within your application. The next two chapters explain how to use the Publication Subscription framework in an application.

[Next](Subscribing%20to%20a%20Feed.md)[Previous](Understanding%20Feeds.md)

