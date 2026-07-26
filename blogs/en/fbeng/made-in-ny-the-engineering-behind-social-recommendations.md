---
title: 'Made in NY: The engineering behind social recommendations'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2016/12/08/android/made-in-ny-the-engineering-behind-social-recommendations/'
original_language: en
published: 2016-12-08
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:865fc97540ef7ae3'
translated: false
---

> 原文：[Made in NY: The engineering behind social recommendations](https://engineering.fb.com/2016/12/08/android/made-in-ny-the-engineering-behind-social-recommendations/)　·　Meta Engineering — iOS

We recently rolled out a variety of new features that help people discover new things in the world around them, decide what to do or where to go, and connect with local businesses in easier and faster ways.

As part of these new tools, we launched [Recommendations](http://newsroom.fb.com/news/2016/10/getting-things-done-with-the-help-of-your-friends/). Today, when you write a Facebook post looking for advice on local places or services and you turn on the Recommendations feature, comments to your post receive Place Cards, which highlight the suggested replies with links to relevant information, including hours of operation, phone number, address, and more. The recommended locations are also added to a map that is inserted into your original post.

The idea for Recommendations emerged from a hackathon in Facebook's New York office. We built Recommendations quickly with the initial rollout to people in the United States, after receiving positive internal feedback on our prototype and building out the product. We're glad to share some of the challenges we faced and opportunities for further development below.

## Local Search and Recommendations at Facebook New York

As engineers with the Facebook Local Search and Recommendations teams, we help connect people to the places they care about, while building a database of business information (names, addresses, and contact details) that is accurate and useful. We work on everything from technologies to help return queries for place searches to identifying recommendations for locations from friends in structured form, not only so that we can provide more utility to people who receive these recommendations but also so this data can be used to improve the local search experience, annotate place data, and provide valuable data to drive improvements to algorithmic place recommendations.

We made the decision early on that we didn't want people to have to do extra work to recommend places — no dedicated button, etc. Most of the time, you can simply post and comment, as you normally would, and this added functionality happens automatically.

Behind the scenes, however, making the product work is a lot more complex. In order to turn a free-text comment into a place recommendation, we have to understand the text and extract the most likely place(s). Furthermore, because each comment affects the original post, we built new functionality across all platforms that ensures the feed story remains consistent as the story dynamically updates.

## Functional overview

![](https://engineering.fb.com/wp-content/uploads/2016/12/GPxu6gDfYFwW784AAAAAAAACRrkJbj0JAAAB.jpg)

Let's consider a sample post and response:

- "Hey y'all. Where should I go eat tonight in NYC?”
- Comment: “Hey man, you should totally go check out Manolito's — great for ramen!”

The challenge of Recommendation extraction is to determine — with no additional input from the commenter — that the recommended place in this comment is Manolito's. This is an exceedingly difficult problem, but one of the exciting things about developing products at Facebook is the access to expert teams whose work is already laying the groundwork to solve them. Throughout the product builds, our New York teams worked closely with the members of the Applied Machine Learning team who focus on conversational understanding (CU) to identify relevant posts and find the corresponding text in the comments that contains the recommendation.

In the example, CU would feed the initial query (“Where should I go eat tonight in NYC?”) to our local places search engine developed at FBNY, which merges user-specific information from the commenter's social graph (such as user check-in history, post location, etc.) with our places data graph to produce the most likely place matches.

In this example, we would have to resolve “Manolito's”to the proper entity. This is harder than it sounds, as there might be many “Manolito's” across the globe, and we have to surface the correct one (i.e., one that is in NYC, for this case). If we are confident in the results, we'll insert the place card directly into the comment and add a location pin to the feed story. We also made the decision to design the product in a way that did not affect the typical post+comment behavior people are accustomed to. We wanted people to be able to interact with Recommendations by commenting as they normally would, and make any necessary modifications after the comment is created, with functionality built directly into the post and comment attachments.

To solve each of these challenges, we created dynamically updating attachments. For posts, we'd continuously update the feed story map with new pins as recommendations were added in the comments. For comments, we'd enable people to interactively correct their extracted recommendations, in case we missed one.

## General tech stack for Local Search

Our tech stack for matching a recommendation to an existing business or place entity involves retrieving and scoring selections from our database and returning our best guess result and associated place card.

**Entity retrieval:** When a recommendation triggers a query for a place entity, that query is then parsed into a set of terms based on such factors as the spelling of the word, the tokens of the words, the category in the query, and various other characteristics. Parsing these categories properly, along with the location of these categories ( “Bars in NYC,” for example), is only part of the challenge. Not only do many places share names, but the intent behind a simple term, like “Paris Bar,” could indicate a bar by that name, or a bar in Paris, or any number of other variations. These terms are used to retrieve documents (or place entities) that then receive a score to determine likely relevance and usefulness.

**Entity scoring:** The scoring process is our way of ordering entities to determine relevance and deliver the proper query result. To create the score of a given entity, we analyze a collection of attributes that relate to the searcher, the place in question to be scored, the query, and many other factors. For example, we first fit a Gaussian mixture model (based on check-in location and check-in time) to previous check-ins on the place — we do this offline. We then use a model based on the LambdaMART algorithm that uses click data to collect relevance characteristics, such as the person's location in respect to the place, the time of day at the location, and many other features, to determine the probability that a location is most relevant to the individual and that the person would be likely to check in. After all features are calculated for the given search, the places are fed through the model, which are then ordered by score. The place entity with the top score is returned with the proper place card into the comment.

## Tech stack for dynamic feeds

A single Recommendations post can appear in multiple surfaces (e.g., News Feed and Timeline). Within our current architecture, each surface has a separate model for that single post, and simple story updates (e.g., Likes and comment counts) are propagated across all views. Recommendations posts, however, introduce an additional level of complexity that needed to be managed programmatically.

- We can't update just the UI alone — we also have to update the data model that backs the UI.
- We want to fetch as little data as possible from the server to update the model in order to minimize data consumption. Thus, the response we get back from the server after a Recommendation is added contains only the minimal amount of information we need to update the model.
- The GraphQL framework is currently capable of automatically updating only scalar objects (for example, incrementing a Like counter). A recommendation contains lots of bits of information (e.g., place name or latitude-longitude coordinates) and cannot be automatically updated by our framework. While the GraphQL team is actively working on automatically updating more complex objects, given the timeframe of the Recommendations project, we had to pursue a rapid solution.

To maintain the consistency of the complex dynamic story updates that the new type of post requires, we manually managed the caching of recommendations in both Android and iOS versions of the app, separately, across each view. While we realized that it was redundant to have code on the client that performs essentially the same model manipulations that occurred on the server, we believed that making sure things look consistent across multiple locations and reducing the amount of data we consume was a worthwhile tradeoff that enabled us to release Recommendations as quickly as possible.

### Dynamic feed rendering — Android

Thanks to the work from the GraphQL infrastructure team and the Android News Feed team, there is already a framework in place that allowed us to find the model object for the post that has been updated and, assuming object updates on all client caches go smoothly, minimally update the UI so that the changes are visible for all surfaces' models after a response came back from the server. Much of our development then was focused on updating the model object by performing a local version of the operations that the server performed and making sure we did all three on the client as quickly as possible, lest someone see a stale version of the post.

### Dynamic feed rendering — iOS

Facebook's feed on iOS is rendered with ComponentKit. For those who are not familiar with it, ComponentKit is a view framework that takes a functional, declarative approach to building UI and emphasizes a one-way data flow from immutable models to immutable components that describe how views should be configured.

Our feed framework has mechanisms in place to re-render each component as necessary when the underlying data is updated. However, as mentioned above, feed story attachments do not get this benefit because they are just a container around various types of data (e.g., photo, external link, etc.) and do not have a unique identifier. We wanted to move fast for our first product iteration, so we found a simple alternative using component states.

The state is internal to each component, and can influence the current look and behavior (e.g a Like button component can have two states: initial and liked). The state can also be any object, so we can have the list of recommended places be the state.

```
@implementation RecommendationsAttachmentComponentState
(instancetype)initWithPlaceList:(NSArray *)placeList
{
  if (self = [super init]) {
    _placeList = placeList;
  }
  return self;
}
@end
```

If we use the underlying data inside the state to render our component, whenever we need to update the map attachment we'll just have to call the code below, and the component will re-render with the new list of places:

```
[self.component updateState:^(id oldState){
  return [[RecommendationsAttachmentComponentState alloc] initWithPlaceList:placeList];
} mode:CKUpdateModeAsynchronous];
```

## Opportunities for further development

As use of the product continues to scale, we are already thinking of ways to upgrade the infrastructure behind Recommendations to deliver an even more elegant solution.

For much of the Recommendations location-related functionality, for example, we've been leveraging the model used for Facebook check-ins. However, when you are looking for a restaurant or other location on Facebook to check in to, finding your desired location second on a list of query results is not a problem.

With Recommendations, we have only one chance to return the right location to a suggested comment. As a result, we have been toying with a few things in hopes of streamlining this functionality. The first thing we thought of is tweaking how we represent places for location-related queries. We currently default the query location's latitude and longitude to the center of the desired city. In check-in search it makes sense to return results for locations nearest to the location of the requestor, as people tend to check in close to where they are. In contrast, for Recommendations, we want to uniformly distribute results over the entire city, as a recommendation could be for anywhere. So we are working on tweaking distance to allow for equal weighting throughout the city.

Likewise, we don't want to surface poor matches, as this could lower people's trust in our product. To help alleviate this, we are attempting to implement a suppression layer in our backend based on the query string, the distance of the place from the requestor, and relative score to other places. Moving forward, we will continue to work on the engineering behind this functionality to deliver a sound, robust, and flexible solution.

Moreover, as mobile frameworks develop, and in particular as GraphQL enables consistent updates across views, both clients will migrate to built-in solutions that keep dynamically updating comment and story attachments current.

Our team has seen great interest in this new paradigm of dynamically updating feed and comment attachments, and is currently designing new experiences that leverage the infrastructure we already built out with Recommendations.

Recommendations was launched in the U.S. in October. You can create your first Recommendations post at [facebook.com/recommendations](http://facebook.com/recommendations).

_Recommendations was a joint effort across teams in New York and Menlo Park._
