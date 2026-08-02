---
title: iOS Search API Best Practices and FAQs
apple_id: DTS40016269
resource_type: Technical Note
platform: iOS
topic: Data Management
technology: null
published: '2015-08-03'
source_url: https://developer.apple.com/library/archive/technotes/tn2416/_index.html
archived_at: '2026-07-26T19:54:15.000877Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2416

# iOS Search API Best Practices and FAQs

Guidance for best practices, and answers to common questions related to integrating iOS Search APIs into apps and websites.

iOS 9 introduces a variety of APIs to enable indexing of user-generated content, features in your app, and public website content. This indexed content is then accessible to people in iOS 9 Search as well as from Safari. Content generally falls into one of two categories:

__Table 1__  Public versus Private

| Category | Description |
| Private | Private content is indexed directly by your app using the NSUserActivity or CoreSpotlight APIs. Your app can index content that the user has created (e.g. documents or messages), or points of interest in your app such as main views (e.g. Steps in the Health app). This content remains on the user's device and is only searchable locally. |
| Public | Public content comes from your website. Apple uses a web crawler, called Applebot, to gather publicly available content that has been marked up using standard web markup techniques. This information is then presented to users when they use Search in iOS 9 or from Safari suggestions. |

We encourage all apps to implement NSUserActivity since it’s the best way to surface what users truly care about the most and improve your search result ranking. We also recommend marking activities as public whenever applicable since it will help you reach new users. Furthermore, implementing Web Markup is strongly recommended for any app with at least some mirrored content from the web. Finally, use CoreSpotlight to index any private information or user-generated content.

The following sections discuss various best practices for getting the best results from iOS Search, along with some frequently asked questions about integrating the APIs into your app.

[Search Best Practices](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpuerktkrpvausbinkesq2fkm)[NSUserActivity API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpuerktkrpvausbinkesq2fkmwu4u2vkncveqkdkrevmskulfpucucj)[CoreSpotlight API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpuerktkrpvausbinkesq2fkmwugt2sivjvat2ujreuoscul5avasi)[Web Markup API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpuerktkrpvausbinkesq2fkmwvorkcl5gucuslkvif6qkqje)[Search API FAQ](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkr)[What are the benefits of using the various search APIs?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkrfvluqqkul5averk7kreekx2civhekrsjkrjv6t2gl5kvgskoi5pviscfl5lecusjj5kvgx2tivaveq2il5avasktl4)[Which is the right API for me to use?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkrfvluqskdjbpusu27kreekx2sjfduqvc7ifiesx2gj5jf6tkfl5ke6x2vkncv6)[What content should I index?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkrfvluqqkul5bu6tsuivhfix2tjbhvktcel5ev6skoircvqxy)[I don’t have a publicly accessible website, and my app has thousands of public items that users can browse. How should I get them to be searchable?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkrfvev6rcpjzpv6x2ul5eecvsfl5av6ucvijgesq2mlfpucq2divjvgskcjrcv6v2fijjusvcfl5puctsel5gvsx2bkbif6scbknpviscpkvjuctseknpu6rs7kbkuetcjinpusvcfjvjv6vciifkf6vktivjfgx2difhf6qssj5lvgrk7l5pv6scpk5pvgscpkvgeix2jl5dukvc7kreektk7krhv6qsfl5jukqksineecqsmivpq)[I added code to use these APIs but my app is not showing in the search results. What should I do?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkrfvev6qkeircuix2dj5cekx2uj5pvku2fl5keqrktivpucucjknpuevkul5gvsx2bkbif6sktl5he6vc7knee6v2jjzdv6skol5keqrk7kncucusdjbpverktkvgfiu27l5pvoscbkrpvgscpkvgeix2jl5ce6xy)[How can I improve my ranking?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkrfvee6v27inau4x2jl5eu2ucsj5lekx2nlfpveqkojneu4r27)[How can I deep link from my web site to my app?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkrfvee6v27inau4x2jl5cekrkql5gestsll5dfet2nl5gvsx2xivbf6u2jkrcv6vcpl5gvsx2bkbif6)[Which of the schemas are supported for Web Markup?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkrfvluqskdjbpu6rs7kreekx2tineektkbknpucusfl5jvkucqj5jfirkel5de6us7k5cuex2nifjewvkql4)[How can I add actions to my search results such as calling or getting directions?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkrfvee6v27inau4x2jl5auirc7ifbviskpjzjv6vcpl5gvsx2tivaveq2il5jeku2vjrkfgx2tkvbuqx2bknpugqkmjreu4r27j5jf6r2fkrkestshl5cesusfinkest2oknpq)[How is the privacy of my app’s users protected?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkrfvee6v27jfjv6vciivpvausjkzaugwk7j5df6tkzl5avauc7l5pvgx2vkncveu27kbje6vcfinkekrc7)[Which devices are these APIs supported on?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkrfvluqskdjbpuirkwjfbuku27ifjekx2ujbcvgrk7ifiesu27knkvaucpkjkekrc7j5hf6)[Are these new Search APIs available on OS X?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkrfvaverk7kreeku2fl5hekv27kncucusdjbpucucjknpucvsbjfgecqsmivpu6ts7j5jv6wc7)[When do search results show up in Safari?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewugsbrfvjukqksinef6qkqjfpumqkrfvluqrkol5ce6x2tivaveq2il5jeku2vjrkfgx2tjbhvox2vkbpusts7knaumqksjfpq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmmrwhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Search Best Practices

- Drive interactions with your search result to improve ranking. Having rich search results is the best way to foster engagement. Include images, reviews, ratings and actions whenever possible.
- When responding to search result engagement, go straight to the content in your app, avoid any mid-steps, splash-screens or interstitial views.
- Speed matters. Time from tapping a search result to the content in your app is measured and used in ranking.
- Always index user-generated content.
- Use the same identifier when indexing the same item with multiple APIs in order to avoid duplicates and help your app rank higher. For example, if using all 3 APIs we recommend using the URL as the NSUserActivity’s `relatedUniqueIdentifier` and `webPageURL`, and the CoreSpotlight’s `uniqueIdentifier` on CSSearchableItem.

### NSUserActivity API

- Use public activities if your app has public content to increase discoverability of your app.
- Use the `contentAttributeSet` (defined in [CSSearchableItemAttributeSet](https://developer.apple.com/library/prerelease/ios/documentation/CoreSpotlight/Reference/CSSearchableItemAttributeSet_Class/index.html#//apple_ref/occ/cl/CSSearchableItemAttributeSet)) to include images and descriptions in order to make your search results stand out.
- Use NSUserActivity to leverage Handoff, App Search, and Siri suggestions and reminders.
- Include keywords to associate your results with different queries. Each item should have 3 to 5 keywords, including synonyms, abbreviations, and category terms.

### CoreSpotlight API

- Use [CSSearchableItemAttributeSet](https://developer.apple.com/library/prerelease/ios/documentation/CoreSpotlight/Reference/CSSearchableItemAttributeSet_Class/index.html#//apple_ref/occ/cl/CSSearchableItemAttributeSet) to include images and descriptions in order to make your search results stand out. See the various CSSearchableItemAttributeSet categories listed in CSSearchableItemAttributeSet_Categories.h for more details on the types of attributes available.
- Update and remove items on the index to keep your search results relevant over time.
- Pay attention to the appropriate data protection level for your user's content. Use the corresponding CSSearchableIndex API to control the data protection level indexed items are stored using.

### Web Markup API

- Use the support and marketing URL field in iTunesConnect to ensure that Apple's crawler notices your website. Be sure that the crawler can get to the content you want to index from those URLs.
- Use Universal Links instead of a custom URL scheme. They are unique, more secure, flexible and they work seamlessly across your app and website. See [What's New in iOS](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-DontLinkElementID_2) for details on how to use Universal Links.
- Use Smart App Banners to drive installs of your app. Do this even if you implement Universal Links. See [Promoting Apps with Smart App Banners](https://developer.apple.com/library/mac/documentation/AppleApplications/Reference/SafariWebContent/PromotingAppswithAppBanners/PromotingAppswithAppBanners.html) for more details.
- Implement structured data markup and schemas in order to make your search results richer. Specifically if you have phone numbers or addresses that the user can engage with directly from search results.
[Back to Top](#)

## Search API FAQ

### What are the benefits of using the various search APIs?

Using the various search APIs will increase the engagement and discovery of your app and content your users care about by showing results in Spotlight and Safari. Even if your app is not installed, search results can be displayed for your app, enabling people to install your app. If you have already integrated Handoff, the work required to make activities your app generates searchable is minimal and can enable users to search their history of using your app along with finding features and points of interest in your app's UI.

### Which is the right API for me to use?

There are 3 different points of integration that you can consider:

__Table 2__

| Category | Usage |
| NSUserActivity | New methods and properties in the NSUserActivity class help you to index items from your app as a user does an activity in the app. This could include creating or visiting a piece of content, viewing a set of items (such as a results list) or visiting a navigation point. As users do these activities in your app, you index the activity by submitting it to NSUserActivity for indexing in the private on-device’ index. By default activities that are marked as searchable are kept private to people's devices, but If the activity being indexed is public and viewable by all users, then mark the activity as public. For example, the Health app can add activities that let users search for "Steps" and be taken directly to that pane in the Health app. |
| CoreSpotlight | This framework enables indexing of app content that is searchable privately on a person's device. You can add, update, and delete items in the CoreSpotlight index and that information will be searchable for easy access. Using a search extension, you can index content in the background even if your app is not running. This allows you to keep the index up to date as content changes even if the user isn't actively using your app. This is great for things like messages and conversations stored on your server but accessed through your app, or for locally generated user content. |
| Web Markup | This is useful for apps that have mirrored content from the web. Applebot crawls your website and show its content on search results. By implementing Web Markup you can make your results look richer, increase engagement and seamless redirect users to that specific content in your App. |

### What content should I index?

Index any content viewed, created, or curated by the user. Important navigation points and features of your app. Messages, content, or items arriving on people's devices (even if your app isn't frontmost).

### I don’t have a publicly accessible website, and my app has thousands of public items that users can browse.  How should I get them to be searchable?

Use NSUserActivity public indexing and CoreSpotlight to index a subset of content that is most relevant for the user, such as the most popular items or the ones in the geographic location. You should not blindly add thousands of items using NSUserActivity and CoreSpotlight. Instead, focus on adding items that users actually interact with or have identified as meaningful in some way to people.

### I added code to use these APIs but my app is not showing in the search results. What should I do?

Results should show up immediately on the device if NSUserActivity and CoreSpotlight are implemented. Try using different keywords. In the case of Web Markup, results will only show up after the page has been crawled by Applebot, and once a certain level of relevance has been attained.

### How can I improve my ranking?

Providing rich results to drive engagement is the best way to improve your ranking. Always include a relevant thumbnail, title and a unique description. When possible, add metadata for ratings and actions such as dialing a phone number, or getting directions to an address. Since your engagement-to-shown ratio will be an important factor, only showing results when your app has a compelling answer is crucial.  When using keywords, only include terms related to the items such as synonyms or abbreviations.  Providing users with a great experience, minimizing time from result to content and avoiding any interstitials or multi-steps are very important. When handling results in your app, get the user to the relevant content as quickly as possible.

### How can I deep link from my web site to my app?

The best way is to use Universal Links and [Smart App Banners](https://developer.apple.com/library/mac/documentation/AppleApplications/Reference/SafariWebContent/PromotingAppswithAppBanners/PromotingAppswithAppBanners.html). You can also use Twitter Cards and Facebook App Links.

### Which of the schemas are supported for Web Markup?

We support [Open Graph](http://ogp.me) and AggregateRating, Offers, PriceRange. InteractionCount, Organization, Recipe, SearchAction and ImageObject from [Schema.org](http://schema.org).

### How can I add actions to my search results such as calling or getting directions?

Two actions are currently supported: calling a phone number and getting directions to an address. In order to enable these actions you must implement either the telephone item from the Organization schema or the Postal Address schema from Schema.org.

### How is the privacy of my app’s users protected?

The CoreSpotlight index is stored in the private on-device index. Each device contains a private index whose information is never shared with Apple or synced between devices. Items crawled by Applebot are indexed in Apple’s server-side index, since they are already publicly available on the web. Items indexed with NSUserActivity will be added to the private on-device index. Activities marked as eligibleForPublicIndexing are kept on the private on-device index in iOS 9.0, however, they may be eligible for crowd-sourcing to Apple’s server-side index in a future release.

### Which devices are these APIs supported on?

App Search comes with iOS9, available as a free software update for iPhone 4s and later, iPod touch (5th generation), iPad 2 and later, iPad mini and later. However, the search functionality of NSUserActivity and CoreSpotlight are not supported on the iPhone 4s, iPad 2, iPad (3rd generation), iPad mini, and iPod touch (5th generation).

### Are these new Search APIs available on OS X?

CoreSpotlight and the search functionality of NSUserActivity are not supported on OS X.  However, web search results may be shown on OS X.

### When do search results show up in Safari?

Only items indexed using web markup are eligible to show in Safari.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-08-03 | Editorial changes. |
| 2015-07-13 | Minor additions and clarifications. |
| 2015-06-29 | New document that frequently asked questions and best practices related to iOS 9 Search APIs, including NSUserActivity additions, CoreSpotlight, and web markup. |

