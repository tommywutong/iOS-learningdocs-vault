---
title: Continuing to build News Feed for all types of connections
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2015/12/09/android/continuing-to-build-news-feed-for-all-types-of-connections/'
original_language: en
published: 2015-12-10
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9d651e16f23e449f'
translated: false
---

> 原文：[Continuing to build News Feed for all types of connections](https://engineering.fb.com/2015/12/09/android/continuing-to-build-news-feed-for-all-types-of-connections/)　·　Meta Engineering — iOS

Our mission with News Feed is to connect people with the stories that matter most to them, but if people’s News Feeds aren’t loading because of poor internet connections, we can’t show them the most relevant stories. People are coming online at a staggering rate in emerging markets, and in most cases they’re doing so on mobile via 2G connections. To improve News Feed so it works seamlessly and quickly for people in all parts of the world, we’re focused on designing it to operate well regardless of device or network connection.

As a next step in improving people’s experiences on slower internet connections, we are shipping several changes that will more efficiently show you relevant stories in your News Feed when you’re on a slow connection and will let you compose comments on posts when you’re offline.

![](https://engineering.fb.com/wp-content/uploads/2015/12/GPl1vABRt7X33RYBAC21EEkAAAAAbj0JAAAB.jpg)

## Showing you relevant stories on slower connections

Anytime someone loads News Feed, we retrieve the latest and most relevant stories for each person. But most people don’t scroll through all stories when they look at News Feed.

In the past, if you were on a poor internet connection or had no connection, you might need to wait for stories to load when you opened News Feed. We are now testing an update in which we look at all the previously downloaded stories present on your phone that you have not yet viewed, and rank them based on their relevance. We also factor in whether the images for the story are available. This way we can immediately display relevant stories you haven’t seen yet, instead of showing a spinner while you wait for new stories. When we receive new stories from the server when you’re back online, we load and rank those stories normally.

We rank relevant, already downloaded stories upon startup of the app, when you navigate to News Feed from the app or pull down to refresh stories at the top of your feed, or as you are scrolling through your News Feed.

We’re also testing improvements to keep these stories up to date throughout the day by periodically retrieving new stories when you have a good connection. This helps us make sure the stories we have available are the most relevant and current.

## Providing more options to join the conversation

You can now also comment on stories you see when you don’t have an internet connection. While the ability to like and share posts when you’re offline has been available for some time, now you can comment on posts and the comment will be posted whenever you next have a connection.

For example, if you see a post about a friend’s engagement when you’re not connected to the internet, you can compose a congratulatory comment, and it will appear on his or her post when you’re back online.

These changes will help anyone who is on a poor internet connection — even those whose network connectivity is generally good but who have intermittent connections in places like subways and tunnels, or at large events. None of these changes affect News Feed ranking. We are simply showing you the most relevant content as efficiently as possible. We’ll be testing and rolling this out over time to gather feedback.

We’re excited to continue improving News Feed for everyone, no matter your connection speed or device.
