---
title: Documentation Set Guide
apple_id: TP40005266
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2009-05-05'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/Documentation_Sets/000-Introduction/introduction.html
archived_at: '2026-07-15T07:24:23.101970Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Documentation%20Sets.md)

# Introduction

Xcode, Apple’s integrated development environment, includes documentation access features that allows users to easily search and view Apple’s developer documentation. If your documentation is properly packaged, it can also take part in these features, and appear in Xcode's documentation and Quick Help windows.

This document explains how to package and build a documentation set for use with Xcode. If you have a developer-targeted software product, this document shows you how to integrate documentation for that product with the Xcode Documentation window. This document assumes that you have existing HTML or PDF documentation files; it does not describe how to write or generate these documentation files.

Before reading this document, you should be familiar with the documentation viewing and access features that are available in Xcode. For a complete description of these features and how to use them, see [Documentation Access](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeWorkspace/200-Documentation_Access/documentation_access.html#//apple_ref/doc/uid/TP40006920-CH260) in _[Xcode Workspace Guide](../Xcode%20Workspace%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dsmrq)_.

In this document the term _documentation producer_ (or producer for short) identifies a person involved in creating documentation sets. The term _documentation user_ (or user for short) refers to Xcode users who access documentation sets installed on their file systems using the Xcode Documentation window or Quick Help.

This document contains the following chapters:

- [Documentation Sets](Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjtfvjvonq) introduces the documentation set bundle and provides an overview of how to create a documentation set.
- [Creating Documentation Sets](Creating%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmznknltg) describes how to create and name the folder hierarchy for your documentation set bundle, as well as how to choose where to install that bundle.
- [Configuring Documentation Sets](Configuring%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjrfvjvomq) introduces the `Info.plist` and `Nodes.xml` files, which are required for any documentation set. This chapter shows how to use these files to describe the documentation set and its contents.
- [Supporting API Lookup in Documentation Sets](Supporting%20API%20Lookup%20in%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjsfvjvomi) shows how to create a tokens file to support API search in your documentation set.
- [Indexing Documentation Sets](Indexing%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqnznknltc) describes the `docsetutil` indexing tool and shows how to use it to index your documentation set, so that Xcode can access and display its contents.
- [Internationalizing Documentation Sets](Internationalizing%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqnrnknlto) shows how to support multiple languages by localizing all or some of the contents of the documentation set bundle.
- [Acquiring Documentation Sets Through Web Feeds](Acquiring%20Documentation%20Sets%20Through%20Web%20Feeds.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjqfvjvomi) describes how to support automatic detection and downloading of documentation set updates, using an RSS or Atom feed.
- [Testing and Packaging Documentation Sets](Testing%20and%20Packaging%20Documentation%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjwfvjvomy) tells how to test documentation set indexes and whether Xcode can access and display your documentation. Also shows how to package your documentation set bundle as an XAR archive.
- [docsetutil Reference](docsetutil%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjvfvjvomi) describes the command-line utility for creating, testing, and querying full-text and API indexes for a documentation set.
- [Documentation-Set Property List Key Reference](Documentation-Set%20Property%20List%20Key%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqnbnknltc) describes the keys that Xcode recognizes.
- [Documentation-Set Nodes Schema Reference](Documentation-Set%20Nodes%20Schema%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqojnknltk) lists all of the elements supported in the nodes file format.
- [Documentation-Set Tokens Schema Reference](Documentation-Set%20Tokens%20Schema%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tenrwfvbuqmjufvjvomjq) lists all of the elements supported in the tokens file format.

In addition to the material in this document, you may find the following resource helpful:

- The [AtomEnabled website](http://atomenabled.org/) provides information about the Atom format, which you’ll find useful if you plan to provide Atom feeds for documentation sets.
[Next](Documentation%20Sets.md)

