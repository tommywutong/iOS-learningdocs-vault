---
title: App Search Programming Guide
apple_id: TP40016308
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2016-12-15'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/AppSearch/CombiningAPIs.html
archived_at: '2026-07-15T07:32:54.011312Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Search Programming Guide](index.md)



## Combine APIs to Increase Coverage

Core Spotlight, [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity), and web markup are designed to work together, so it’s best when you can combine these APIs in your app. Combining these APIs can give users even richer information and access to your content from more places.

In your app, using multiple APIs often means that you index the same content in more than one way. On these occasions, it's crucial that you relate the various representations of a single item so that you can avoid giving users duplicate items in search results. Avoiding duplication can also help improve the ranking of your items.

Use the following strategies to avoid creating duplicate representations of a single item:

- If you’re using both [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) and Core Spotlight APIs to index an item, use the same value for [relatedUniqueIdentifier](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621569-relateduniqueidentifier) and [uniqueIdentifier](https://developer.apple.com/documentation/corespotlight/cssearchableitem/1621672-uniqueidentifier) to link the representations of the item. Note that if the Core Spotlight metadata for an item differs from an `NSUserActivity` object’s metadata for the same item, the Core Spotlight metadata is shown in search results and the `NSUserActivity` metadata is used in Siri suggestions.

  > [!IMPORTANT]
  > 
- If you’re using both `NSUserActivity` and web markup to index an item, set the user activity object’s [webpageURL](https://developer.apple.com/documentation/foundation/nsuseractivity/1418086-webpageurl) property to the relevant URL on your website.

  > [!NOTE]
  > 
- If you’re using all three APIs, it works well to use the URL of the relevant webpage as the value for [uniqueIdentifier](https://developer.apple.com/documentation/corespotlight/cssearchableitem/1621672-uniqueidentifier), [relatedUniqueIdentifier](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621569-relateduniqueidentifier), and [webpageURL](https://developer.apple.com/documentation/foundation/nsuseractivity/1418086-webpageurl).

Combining the search-related APIs also helps you index a broader range of your users’ interests. A good way to start your investigation into potential searchable items is to examine the analytics for your app. For example, you might index:

- Content that the user views (using [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity))
- Frequently used navigation points and features (using `NSUserActivity`)
- Content created or curated by the user, such as photos or a list of favorites (using Core Spotlight APIs)
- New messages, content, or items that arrive on the device (using Core Spotlight APIs)
- Content that lives in both your app and your website (using web markup)

Ultimately, it’s essential to maintain a good engagement ratio for your searchable items so that they continue to be displayed in search results. The engagement ratio is based on the number of times that users tap an item related to your app and the number of app-related items that are displayed in search results. A low engagement ratio for an item can mean that the item won’t appear in search results. For some tips on ways to increase the engagement ratio for your items, see [Improve the Ranking of Your Results](SearchUserExperience.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dgmbyfvbuqmjrfvjvomi).

[Help Users Find Your Images](FindingImages.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dgmbyfvbuqmjufvjvomi)

[Enhance Your Search Results](SearchUserExperience.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dgmbyfvbuqmjrfvjvomi)
