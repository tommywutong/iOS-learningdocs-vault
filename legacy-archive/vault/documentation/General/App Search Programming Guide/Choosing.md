---
title: App Search Programming Guide
apple_id: TP40016308
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2016-12-15'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/AppSearch/Choosing.html
archived_at: '2026-07-15T07:32:53.543988Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Search Programming Guide](index.md)



## Example Implementations

The way you implement search varies depending on the usage model and user experience of your app.

At a high level, your implementation decisions rest on a few primary questions:

- Do you have a website that hosts some or all of the content that’s in your app?
- Does your app contain user-generated or user-specific data?
- Does your app contain content that users are likely to want to revisit?

Keep the answers to these questions in mind as you review the following examples.

### Social Networking

Users of social networking apps intend to share data with others, but they also expect to keep some data private. A social networking app can enhance the user experience by making public profile and other public data universally searchable, while also making it easier for individual users to search the on-device index for their private messages and personal data. Table 2-1 lists some examples of how a social networking app can use search APIs.

__Table 2-1__Example API usage for a social networking app

| API | Example usage |
| --- | --- |
| `NSUserActivity` | Use [eligibleForPublicIndexing](https://developer.apple.com/documentation/foundation/nsuseractivity/1414701-iseligibleforpublicindexing) and [eligibleForSearch](https://developer.apple.com/documentation/foundation/nsuseractivity/1417761-iseligibleforsearch) to mark activities that represent public profiles and pages.  Use `eligibleForSearch` to mark activities that represent private groups so that users can easily find them. |
| Core Spotlight | Use Core Spotlight APIs to add details about the user’s first-degree connections and private messages to the on-device index.  To learn more, see _[Core Spotlight Framework Reference](https://developer.apple.com/documentation/corespotlight)_. |
| Web markup | On your website, add deep links and metadata to public profiles, pages, and groups to enrich the information about these items in search results.  Use universal links to let users open your app when they tap a link to your website. |

### News

A news app typically helps users access a lot of information over a broad range of topics while also helping users drill down to get details. Most of the information that a news app handles is public, but users expect their interaction with news data to stay private. Table 2-2 lists some examples of how a news app can use search APIs.

__Table 2-2__Example API usage for a news app

| API | Example usage |
| --- | --- |
| `NSUserActivity` | Use [eligibleForPublicIndexing](https://developer.apple.com/documentation/foundation/nsuseractivity/1414701-iseligibleforpublicindexing) and [eligibleForSearch](https://developer.apple.com/documentation/foundation/nsuseractivity/1417761-iseligibleforsearch) to mark activities that represent interesting navigation points in your app, such as “Politics” or “Sports” news categories. Indexing these items helps current users revisit favorite app locations.  You can also index articles the user has viewed and use the [expirationDate](https://developer.apple.com/documentation/foundation/nsuseractivity/1413745-expirationdate) property to specify a date after which the article is no longer relevant. |
| Core Spotlight | Use Core Spotlight APIs to:   - Index the most recent, trending, and relevant articles and add attributes such as location or topic - Index articles the user marks as favorite or for reading later - Remove articles from the index after a period of time to keep the index fresh   To learn more, see _[Core Spotlight Framework Reference](https://developer.apple.com/documentation/corespotlight)_. |
| Web markup | On your website, add deep links and metadata to articles so that search results can display useful information, such as images.  Use universal links to let users open your app when they tap a link to your website. |

### Ticket Sales

A ticket sales app needs to make it easy for all users to find information about future events and buy tickets while also helping individual users keep track of their receipts and upcoming events. Table 2-3 lists some examples of how a ticket sales app can use search APIs.

__Table 2-3__Example API usage for a ticket sales app

| API | Example usage |
| --- | --- |
| `NSUserActivity` | Use [eligibleForPublicIndexing](https://developer.apple.com/documentation/foundation/nsuseractivity/1414701-iseligibleforpublicindexing) and [eligibleForSearch](https://developer.apple.com/documentation/foundation/nsuseractivity/1417761-iseligibleforsearch) to mark activities that represent viewed venues, bands, or teams. |
| Core Spotlight | Use Core Spotlight APIs to:   - Index ticket purchase receipts - Index bands or teams that the user has marked as favorites - Index events near the user’s location - Remove past events from the index to keep the index useful for planning ahead   To learn more, see _[Core Spotlight Framework Reference](https://developer.apple.com/documentation/corespotlight)_. |
| Web markup | On your website, add deep links and use structured data markup to provide information such as images and prices associated with an event.  Use universal links to let users open your app when they tap a link to your website. |

### Travel

In terms of search functionality, a travel app is similar to a ticket sales app, because it helps users plan for future events and buy related items. In addition, users typically expect a travel app to provide information about locations, events, and transportation options while also helping them access their private booking or receipt information. Table 2-4 lists some examples of how a travel app can use search APIs.

__Table 2-4__Example API usage for a travel app

| API | Example usage |
| --- | --- |
| `NSUserActivity` | Use [eligibleForPublicIndexing](https://developer.apple.com/documentation/foundation/nsuseractivity/1414701-iseligibleforpublicindexing) and [eligibleForSearch](https://developer.apple.com/documentation/foundation/nsuseractivity/1417761-iseligibleforsearch) to mark activities that represent viewed hotels, locations, and restaurants, in addition to useful navigation points in your app, such as flight or tour searches. |
| Core Spotlight | Use Core Spotlight APIs to index:   - Reservations - Places near the user’s location - Restaurants, hotels, and other items that the user has marked as favorites   To learn more, see _[Core Spotlight Framework Reference](https://developer.apple.com/documentation/corespotlight)_. |
| Web markup | On your website, add deep links and use structured data markup to provide information such as ratings, prices, special offers, and addresses associated with locations and attractions.  Use universal links to let users open your app when they tap a link to your website. |

[Search Drives User Engagement](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dgmbyfvbuqnbnknltc)

[Index Activities and Navigation Points](Activities.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dgmbyfvbuqnrnknltc)
