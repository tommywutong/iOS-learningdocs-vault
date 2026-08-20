---
title: SearchKit Programming Guide
apple_id: TP40001071
resource_type: Guide
platform: macOS
topic: User Experience
technology: CoreServices
published: '2005-12-06'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SearchKitConcepts/searchKit_intro/searchKit_intro.html
archived_at: '2026-07-18T02:12:49.418592Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Search%20Basics.md)

# Introduction

Search Kit is Apple’s content indexing and searching solution. It offers a powerful and streamlined procedural C framework, based on Core Foundation conventions, that you can use add information retrieval to your app, or command-line tool.

In OS X, Search Kit provides fast information retrieval in System Preferences, Address Book, Help Viewer, and Xcode. Apple’s Spotlight technology is built on top of Search Kit to provide content searching in Finder, Mail, and the Spotlight menu.

Search Kit’s features include:

- Fast indexing and asynchronous searching
- Search mode determined by a Google-like query syntax, including phrase-based searching
- Text summarization
- Control over index characteristics including minimum term length, stopwords, and synonyms/substitutions
- Flexible management of document hierarchies and indexes
- Unicode support for language independence
- Relevance ranking and statistical analysis of documents to improve search quality

Search Kit is not for locating the position of search terms within a document or for finding documents based on their file-system attributes. For information on these other types of search, see [How Search Kit Works With Documents](Search%20Kit%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbufvbecqseijfeoqy).

This guide provides the background you’ll need to use Search Kit to add fast content searching to your application. If your application focuses on metadata rather than document content, you may want to consider using Spotlight instead.

- Use the Search Kit API when you want your application to have full control over indexing and searching. Also use Search Kit when your “documents” are not necessarily files on disk but web pages, database records, and so on.
- Use the simpler Spotlight API either when your focus is local file metadata or when your application does not need precise control over indexing or of the document hierarchy, or both.

_Search Kit Programming Guide_ contains the following chapters:

- [Search Basics](Search%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbtfvkfawcsivddcmbr), an optional introductory chapter, gets you up to speed on some of the basics of information retrieval as a foundation for the rest of the book. If you are familiar with terms such as corpus, text extraction, inverted index, query, Boolean search, and relevance ranking, you can skip this chapter.
- [Search Kit Concepts](Search%20Kit%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbufvkfawcsivddcmbr) describes the elements of Search Kit’s approach to searching. Read this chapter to learn about Search Kit’s notion of documents, terms, indexes, queries, searches, and search results. This chapter also provides an overview of the workflow behind a user’s search, from text extraction to display of ranked results.
- [Search Kit Tasks](Search%20Kit%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzr) provides detailed instructions on how to accomplish each of the steps involved in a practical usage scenario with Search Kit. It also provides sample code excerpts illustrating each step.

A glossary at the end lists terms that you need in order to understand information retrieval in general and Search Kit in particular.

You may find this additional information from Apple helpful:

- _[Search Kit Reference](https://developer.apple.com/documentation/coreservices/search_kit)_ describes the entire Search Kit API in detail.
- _[Memory Management Programming Guide for Core Foundation](../../Core%20Foundation/Memory%20Management%20Programming%20Guide%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdo2i)_ provides an introduction to memory management in Core Foundation. Search Kit uses Apple's Core Foundation style for memory management.
- _[Debugging Programming Topics for Core Foundation](../../Core%20Foundation/Debugging%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Debugging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdm2i)_ provides an introduction to debugging and error handling in Core Foundation. Search Kit uses Apple's Core Foundation style for error handling.
- [Working With Spotlight](https://developer.apple.com/macosx/spotlight.html) provides an introduction to using Apple's Spotlight technology.
[Next](Search%20Basics.md)

