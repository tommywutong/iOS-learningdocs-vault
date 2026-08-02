---
title: Publication Subscription Programming Guide
apple_id: TP40004945
resource_type: Guide
platform: macOS
topic: null
technology: PublicationSubscription
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/InternetWeb/Conceptual/PubSub/UnderstandingFeeds/UnderstandingFeeds.html
archived_at: '2026-07-15T07:43:34.175141Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Publication Subscription Programming Guide](Introduction.md)


[Next](Publication%20Subscription%20Overview.md)[Previous](Introduction.md)

# Understanding Feeds

Before you use Publication Subscription, it is important to understand what feeds are and how they work. This chapter explains the data structure of a feed, how a feed is created, the different types of feeds, and how to use different feed namespaces.

A _feed_ is an XML document that contains frequently updated information. A feed provides information or data independent of presentation. Thus, an XML document can be parsed by an application to retrieve information without the additional style of an entire webpage. Additionally, the parsing application can determine what information is new and mark it as such.

There’s a good chance you’ve already used a feed, even if you didn’t know it. When you run Safari in OS X v10.4 Tiger, there are a number of preinstalled bookmarks in the bookmarks bar. In the News folder (in Figure 1-1), many of the bookmarks, such as the Washington Post and CNET News, are feeds, not webpages. Every 30 minutes, Safari downloads each of these feeds and checks for any new headlines. If there are new headlines, Safari places a number next to the bookmark corresponding to the number of new entries (Figure 1-1). Safari also shows you the article if you choose the bookmark.

__Figure 1-1__  Feed bookmarks in Safari

!

News headlines are usually stored as a feed. When a new headline is available, it is added to the feed as an _entry_. Then, an application on the user’s system (such as Safari) downloads the updated feed, parses it, and checks for the new headline. Figure 1-2 shows how Safari displays a feed of the New York Times entries.

__Figure 1-2__  A feed viewed in Safari

!

Feeds are not limited to text; you can make a feed that links to any type of data. For example, a podcast is simply a feed with audio files in addition to text. Similarly, a photocast is a feed with images.

Feeds can also be used for publishing any binary data. For instance, you could create a feed that contains software updates for your application. Your application can check the feed and, when a new update is available, download it from the server.

Since feeds are simply XML documents, they can be created using a text editor. Adding new entries by hand, however, is a tedious and error-prone process. Typically, the life of a feed begins when the user creates an entry (text, graphics, audio, and the like) and adds it to a database. Then an application takes the entries from the database and produces a feed. Often the application creates more than just a feed; it also generates a webpage. The application that generates the feed can be either local to the user’s system or web-based. See Figure 1-3.

__Figure 1-3__  Feed generation workflow

!

A feed format is a specific set of XML _elements_ used in a feed. Publication Subscription supports four commonly used feed formats:

- RSS 0.9
- RSS 1.0
- RSS 2.0
- Atom Syndication Format

Even though these standards have similar names, their elements are very different. For example, compare the XML elements for an entry in RSS 2.0 format (Listing 1-1) with the elements in the Atom Syndication Format (Listing 1-2). You’ll notice that while the content of both entries is the same, the elements that define them are different.

__Listing 1-1__  A feed entry in RSS 2.0

```
<item>
    <title>Welcome!</title>
    <pubdate>Fri, 27 Oct 2006 18:51:39 GMT</pubdate>
    <author>Matt</author>
    <description>Hello World!</description>
</item>
```


__Listing 1-2__  A feed entry in the Atom Syndication Format

```
<entry>
    <author>
        <name>Matt</name>
    </author>
    <title>Welcome!</title>
    <modified>2006-10-27T18:51:39Z</modified>
    <issued>2006-10-27T18:51:39Z</issued>
    <content type="text/plain">Hello World!</content>
</entry>
```

Publication Subscription is designed to interpret each of these four formats. Since the API encapsulates each of the formats, no matter which format your feed is in, the methods to interpret them are the same.

For more information about each of the XML formats:

- Read [http://en.wikipedia.org/wiki/Really_Simple_Syndication](http://en.wikipedia.org/wiki/Really_Simple_Syndication) to learn more about the RSS 0.9, RSS 1.0 and RSS 2.0 formats
- Read [http://en.wikipedia.org/wiki/Atom_%28standard%29](http://en.wikipedia.org/wiki/Atom_%28standard%29) to learn more about the Atom Syndication Format.

There may be times when the feed you subscribe to uses elements that are not part of one of the feed formats. _Extension XML_ extends the specifications to support application-specific data or objects, similar to a plug-in system for feeds. Extension XML refers to a collection of elements outside of the feed format, also known as _namespace_. Each namespace is identified by a unique URL. Namespace URLs are defined at the beginning of a feed, and are often associated with an easier to remember string. This string is known as a _namespace prefix_.

For example, a feed that has bank account information might use a bank namespace identified by the URL `http://www.example.com/bank`, and a namespace prefix of `bank`. This namespace might have elements such as `owner`, `address`, `checking` and `savings`. An entry using this namespace would look like the one in Listing 1-3.

__Listing 1-3__  An Atom extension XML example

```
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:bank="http://www.example.com/bank">

...

<item>
    <title>Account2004</title>
    <bank:owner>John Doe</bank:owner>
    <bank:address>1 Infinite Loop, Cupertino, CA 95014</bank:address>
    <bank:checking>111829384</bank:checking>
    <bank:savings>949289291</bank:savings>
</item>
```

There are many additional namespaces already defined. One of the most popular ones if for an [iTunes podcast](http://www.apple.com/itunes/store/podcaststechspecs.html). A good resource for finding namespaces is [The Dublin Core Metadata Initiative](http://dublincore.org/), as well as [rss-extensions.org](http://www.rss-extensions.org/).

Understanding the structure and workflow of a feed is important to using the Publication Subscription framework. Knowing about the components of a feed and the organization of the four major feed standards will help you understand the organization of the Publication Subscription framework and its components.

[Next](Publication%20Subscription%20Overview.md)[Previous](Introduction.md)

