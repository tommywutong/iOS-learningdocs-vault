---
title: Core Spotlight
framework: Core Spotlight
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.0+, macOS 10.13+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corespotlight
source_url: 'https://developer.apple.com/documentation/corespotlight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corespotlight.json'
content_hash: 'sha256:c9314fc9387bc533'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Core Spotlight

<sub>Framework</sub>

Add search capabilities to your app, and index your content so people can find it from Spotlight and Safari.

## Overview

Help people access activities and items within your app by adding details about those items to a Core Spotlight index. The framework provides APIs to add your content to an index, and search for items in that index. You decide what content makes sense to index, but typically you index anything that someone might look for in your app. For example, you might index photos, contacts, the items someone purchased, or data they see in your interface. You can then use Core Spotlight to search for your indexed content and display those results in your app.

> [!important] Important
> Spotlight File Import extensions don’t provide functionality in macOS. To make custom files available to Spotlight in macOS, create a Spotlight importer plugin. For more information, refer to [Spotlight Importer Programming Guide](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/MDImporters.html#//apple_ref/doc/uid/TP40001267).

Your app is responsible for indexing your app’s content and maintaining those indexes. You can index content when your app runs, or provide an app extension to index content when the system requests it. You can index any content your app manages, including files and other content that your app isn’t currently displaying. The indexes you create using Core Spotlight remain on device, and are private to the owner of the device. Devices don’t share indexed data with Apple, or synchronize that data with the person’s other devices.

In addition to indexing content, iOS provides additional strategies for making your app’s content searchable:

- Use the search-related properties of [NSUserActivity](foundation/nsuseractivity.md) to add items to the on-device index, with the option to identify the items as eligible for public indexing. Learn more about [NSUserActivity](foundation/nsuseractivity.md) in [Index Activities and Navigation Points](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/Activities.html#//apple_ref/doc/uid/TP40016308-CH6-SW1).
- Use web markup to index content on your web server in Apple’s server-side index, which makes the data available to all iOS users in Spotlight and Safari search results. For more information, see [Mark Up Web Content](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/WebContent.html#//apple_ref/doc/uid/TP40016308-CH8-SW1) in [App Search Programming Guide](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/index.html).

## Topics

### Essentials

- [Core Spotlight updates](updates/corespotlight.md) — Learn about important changes to Core Spotlight.
- [Adding your app’s content to Spotlight indexes](corespotlight/adding-your-app-s-content-to-spotlight-indexes.md) — Create a description for your app’s content and add it to a Spotlight index to make it searchable.

### Searchable items

- [CSSearchableItem](corespotlight/cssearchableitem.md) — The details of your app-specific content that someone might search for on their devices.
- [CSSearchableItemAttributeSet](corespotlight/cssearchableitemattributeset.md) — The detailed metadata for a searchable item.
- [CSCustomAttributeKey](corespotlight/cscustomattributekey.md) — A key associated with a custom attribute for a searchable item.
- [CSLocalizedString](corespotlight/cslocalizedstring.md) — An object that displays localized text in search results related to your app.
- [CSPerson](corespotlight/csperson.md) — An object that represents a person in the context of search results.

### Indexes

- [Generating summary and priority data for indexed items](corespotlight/generating-summary-and-priority-data-for-indexed-items.md) — Summarize mail, message, and audio transcripts or assess the priority of mail and messages using Spotlight and Apple Intelligence.
- [CSSearchableIndex](corespotlight/cssearchableindex.md) — An on-device index for your app’s searchable content.
- [CSSearchableIndexDelegate](corespotlight/cssearchableindexdelegate.md) — A protocol that defines methods a delegate object or app extension uses to handle communication from the on-device index.
- [CSSearchableIndexDescription](corespotlight/cssearchableindexdescription.md) _(beta)_

### Foundation models support

- [Spotlight search tool](corespotlight/spotlight-search-tool.md) — Make your app’s indexed content available to the system’s Foundation models as additional context to use when answering prompts.

### Spotlight app extensions

- [Regenerating your app’s indexes on demand](corespotlight/regenerating-your-app-s-indexes-on-demand.md) — Create an app extension to maintain your app’s indexes and regenerate them as needed.
- [CSIndexExtensionRequestHandler](corespotlight/csindexextensionrequesthandler.md) — An interface that implements an index-maintenance app extension.
- [CSImportExtension](corespotlight/csimportextension.md) — An object that provides searchable attributes for file types that the app supports.

### Queries

- [Building a search interface for your app](corespotlight/building-a-search-interface-for-your-app.md) — Add a search interface to your app to execute Spotlight queries and offer suggested text completions.
- [Searching for information in your app](corespotlight/searching-for-information-in-your-app.md) — Search for app-specific content and refine search results using predicates and filters.
- [CSUserQuery](corespotlight/csuserquery.md) — A type you use to initiate searches from your interface and offer suggested text completions.
- [CSUserQueryContext](corespotlight/csuserquerycontext.md) — The configuration details to apply to a user query.
- [CSSearchQuery](corespotlight/cssearchquery.md) — A type you use to programmatically search the indexed app content.
- [CSSearchQueryContext](corespotlight/cssearchquerycontext.md) — The behavior configuration to use for a search query.
- [CSSuggestion](corespotlight/cssuggestion.md) — The kind of suggestion to use in a query.

### Errors

- [CSIndexError](corespotlight/csindexerror.md) — Index errors returned by Core Spotlight.
- [CSSearchQueryError](corespotlight/cssearchqueryerror.md) — Search query errors returned by Core Spotlight.
- [CSIndex Errors](corespotlight/csindex-errors.md) — Index error codes and error domain.
- [CSSearchQuery Errors](corespotlight/cssearchquery-errors.md) — Search query error codes and error domain.

### Version

- [CoreSpotlightAPIVersion](corespotlight/corespotlightapiversion.md) — The API version number for Core Spotlight.

### Structures

- [SearchableItem](corespotlight/searchableitem.md) — A Swift value type representing a Spotlight search result. _(beta)_
