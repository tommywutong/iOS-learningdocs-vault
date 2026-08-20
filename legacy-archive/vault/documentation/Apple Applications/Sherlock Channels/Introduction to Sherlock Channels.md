---
title: Sherlock Channels
apple_id: 10000121i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-04-09'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Sherlock/Sherlock.html
archived_at: '2026-07-15T05:18:56.628840Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Architecture%20of%20Sherlock%20Channels.md)

# Introduction to Sherlock Channels

The Sherlock application provides Macintosh users with a powerful tool for searching the Web. Users access different types of information in Sherlock through channels.

Prior to Mac OS X 10.2, channels in Sherlock were implemented as plug-ins that the user (or Sherlock) downloaded from the web and installed locally. These plug-ins provided a mapping for Sherlock to use in interpreting search results from an online source. The Sherlock application then merged the results from multiple sources and displayed them in a unified interface. Beginning with Mac OS X 10.2, Sherlock uses a powerful, new model for channels that gives channel developers more flexibility in how their data is displayed.

Sherlock channels provide a way to organize search results in a more intuitive and useful way. A channel implements a front-end interface for a Web-based search engine or other information database. However, unlike most browser-based searches, channels display the results using an Aqua interface and are capable of dynamically updating information.

Although it might seem like using Aqua to display search results would be a lot of work, Sherlock provides a significant amount of infrastructure to simplify the code required for your channel. Sherlock provides infrastructure for running the interface, dispatching events, managing network connections, parsing XML, and executing script code is transparent to the channel developer. With this infrastructure in place, channel developers are free to concentrate on the appearance and custom behavior of their channel.

This document describes how to create and manage a Sherlock channel and how to load the channel from a web page.

This programming topic contains the following articles:

- [Architecture of Sherlock Channels](Architecture%20of%20Sherlock%20Channels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4delkcineumqscjbdq)
- [Developing Channels](Developing%20Channels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dglkdjjbeoqkeizda)
- [Sherlock Scripting Language Support](Sherlock%20Scripting%20Language%20Support.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dilkcijbugr2gindq)
- [Sherlock Reference](Sherlock%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dklkciffeersjifcq)
- [Creating a New Channel](Creating%20a%20New%20Channel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dmlkcineusrckirbq)
- [Accessing Channels](Accessing%20Channels.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dolkcineusrckirbq)
- [Printing Your Channel’s Content](Printing%20Your%20Channel%E2%80%99s%20Content.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dqlkcineusrckirbq)
- [Using Web Services](Using%20Web%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4dslkcineusrckirbq)
- [Trigger Examples](Trigger%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga4talkcineusrckirbq)

For more information about Sherlock, and to obtain a copy of the Sherlock SDK, please visit the Sherlock Channel Development page: [http://developer.apple.com/macosx/sherlock/](https://developer.apple.com/macosx/sherlock/).

The channel architecture described in this document is available only versions of Sherlock that shipped in Mac OS X 10.2 or later. You cannot create channels for earlier versions of Sherlock using this architecture. If you want to build channels for earlier versions of Sherlock, you need to use the Sherlock plug-in architecture described in _Technical Note TN1141: Extending and Controlling Sherlock_.

The Sherlock channel architecture uses XML and supports the use of the JavaScript and XQuery languages for writing script code. Developing your channel interface requires Interface Builder with the Sherlock palette installed.

[Next](Architecture%20of%20Sherlock%20Channels.md)

