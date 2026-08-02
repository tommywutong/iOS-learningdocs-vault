---
title: Publication Subscription Programming Guide
apple_id: TP40004945
resource_type: Guide
platform: macOS
topic: null
technology: PublicationSubscription
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/InternetWeb/Conceptual/PubSub/subscribing/subscribing.html
archived_at: '2026-07-15T07:43:37.528029Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Publication Subscription Programming Guide](Introduction.md)


[Next](Viewing%20and%20Retrieving%20Content.md)[Previous](Publication%20Subscription%20Overview.md)

# Subscribing to a Feed

To view a feed, your application needs to either register with the PubSub Agent and subscribe to the feed, or download the feed and use the Publication Subscription framework to parse it. This chapter describes how to perform both of these tasks, as well as how to adjust the preferences for retrieving the feed.

To register your application with Publication Subscription, create a client object. Sending `applicationClient` to the `PSClient` class returns a client object for the current application, as the following code shows.

```
PSClient *client = [PSClient applicationClient];
```

You can also create a client object to inspect feeds of another application. To create this client object, you need the bundle identifier of the other application. The bundle identifier is a string using the reverse-DNS naming convention that uniquely identifies each application that uses Publication Subscription. Rather than using the `applicationClient` method to create the new client object, send `clientForBundleIdentifier:` to the `PSClient` class and pass the bundle identifier.

For example, for your application to view the feeds that Mail subscribes to, you would use:

```
PSClient *mailClient = [PSClient clientForBundleIdentifier:@"com.apple.mail"];
```


After your application has its client object, it can subscribe to feeds. First, create an `NSURL` object containing the URL to the feed. Then, use the client object method `addFeedWithURL:` to subscribe the client to the feed and return a newly initialized `PSFeed` object. The code should look like Listing 3-1. Keep in mind that the `addFeedWithURL:` method does not create duplicate entries in the database. If you add the same feed twice, you receive the same data from the original database entry.

__Listing 3-1__  Subscribing a client to a feed

```
NSURL    *url    = [NSURL URLWithString:
                          @"http://www.apple.com/main/rss/hotnews/hotnews.rss"];
PSFeed   *feed   = [client addFeedWithURL:url];
```

Some feeds may require a user name and password for users to access them through HTTP authentication. Store the authorization information with the feed by setting the `login` property of the feed object for the user name, and use the `setPassword:` method to store the password in the user’s default keychain. Publication Subscription also uses the same cookie database as Safari, so if the user is logged into the site of the feed through Safari, Publication Subscription also has access. If you don’t store the authorization information with the feed and the user is not logged in through Safari, the PubSub Agent requests the authorization information from the user. Listing 3-2 shows how to store the user name and password in the feed object.

__Listing 3-2__  Accessing a protected feed

```
// Place user name and password in NSString objects
NSString *login = @"username";
NSString *password = @"password";

// Store the authorization information in the feed
feed.login = username;
[feed setPassword: password];
```


You can create a feed object without subscribing to the feed. In this situation, you need to use the feed object method `initWithURL:` and pass the URL of the feed. See Listing 3-3.

__Listing 3-3__  Initializing a `PSFeed` object without a subscription

```
NSURL    *url    = [NSURL URLWithString:
                          @"http://www.apple.com/main/rss/hotnews/hotnews.rss"];
PSFeed   *feed   = [[PSFeed alloc] initWithURL:url];
NSError *error;
[feed refresh:&error];
```

If you do this, the feed is not automatically updated as a subscribed feed would be. Instead, you are using the Publication Subscription framework to parse the feed.

A client can subscribe to multiple feeds, but not all feeds are updated at the same interval. You may have one feed that needs to be checked every five minutes, while another feed only needs to be updated every three hours. Similarly, you may want the time it takes an entry to expire to depend on the feed. The feed settings objects allow you to customize the preferences for each feed. Each feed object is instantiated with a group of default settings.

To customize the preferences for a feed, obtain a feed settings object by either using the `settings` property of a feed object, or the `PSFeedSettings` `defaultFeedSettings` class method. Then adjust the settings as you see fit with the different properties. Store the updated feed settings in the feed object.

Listing 3-4 retrieves the settings object, sets the entries to expire after 30 days, sets the feed to update every 30 minutes, and then puts the settings object back in the feed.

__Listing 3-4__  Modifying the settings of a feed

```
// Retrieve PSFeedSettings object from feed
PSFeedSettings *feedSettings = feed.settings;

// Set entries to expire after 30 days (60 s/m * 60m/h * 24 h/d * 30 d)
feedSettings.expirationInterval = 2592000;

// Set feed to check for updates every 30 minutes (60 s/m * 30m)
feedSettings.refreshInterval = 1800;

// Store settings back in the feed
feed.settings = feedSettings;
```

You can also set the feed settings for a client. If you do, a feed that uses the default settings inherits the client’s settings instead of the default ones. However, any settings unique to a feed overrides the settings of the client.

You now know how to create a feed object for any web feed and adjust the preferences for them. The next chapter, Viewing and Retrieving Content, explains how to obtain the entries and other information in the feed.

[Next](Viewing%20and%20Retrieving%20Content.md)[Previous](Publication%20Subscription%20Overview.md)

