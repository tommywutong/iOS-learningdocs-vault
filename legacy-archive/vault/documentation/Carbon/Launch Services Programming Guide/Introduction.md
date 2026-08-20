---
title: Launch Services Programming Guide
apple_id: TP30000999
resource_type: Guide
platform: macOS
topic: Data Management
technology: ApplicationServices
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/LaunchServicesConcepts/LSCIntro/LSCIntro.html
archived_at: '2026-07-15T05:23:18.513641Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Launch%20Services%20Concepts.md)

# Introduction

Launch Services is an API that enables a running application to open other applications or their document files or URLs (uniform resource locators) in a way similar to the Finder or the Dock. Using Launch Services, an application can perform such tasks as:

- Open (_launch_ or activate) another application
- Open a document or a URL in another application
- Identify the preferred application for opening a given document or URL
- Register information about the kinds of document files and URLs an application is capable of opening
- Obtain appropriate information for displaying a file or URL on the screen, such as its icon, display name, and kind string
- Maintain and update the contents of the Recent Items menu

Although most of these services are normally performed by the Finder, other applications may also find them useful for purposes such as opening email attachments, following URLs embedded in a document, running helper applications, or opening embedded document components that were created by another application or require it for viewing or editing.

Many of Launch Services’ capabilities were formerly provided by the Desktop Manager. With the advent of Mac app bundles, however, the Desktop Manager has lost its usefulness, since it is not knowledgeable about bundled applications and simply ignores them. Similarly, Launch Services’ facilities for dealing with URLs were formerly implemented through the Internet Config API. Launch Services replaces and supersedes the Desktop Manager and Internet Config with a new API providing similar functionality, but designed to operate properly in the OS X environment.

Launch Services was created specifically to avoid the common need for applications to ask the Finder to open an application, document, or URL for them. In the past, opening such items in a way similar to the Finder required knowledge of several APIs, including the Desktop Manager, File Manager, Translation Manager, Internet Config, Process Manager, and Apple Event Manager. The Finder also had implicit knowledge of the desktop database and other information not available elsewhere for determining the correct application with which to open a given document.

Launch Services removes this specialized knowledge from the Finder and isolates it in a single, straightforward API available to any application. The OS X Finder uses Launch Services to open applications, documents, and URLs at the user’s request. Since the Finder does no additional processing beyond calling Launch Services, any client using Launch Services for these purposes is guaranteed to behave identically to the Finder itself.

This document is intended for all developers whose applications need to open other applications, open document files or URLs belonging to them, or display files or URLs on the screen in a manner similar to the Finder. For more detailed information on the Launch Services API, see the related document _[Launch Services Reference](https://developer.apple.com/documentation/coreservices/launch_services)_, which provides a comprehensive description of Launch Services functions, data types, constants, and result codes.

This document has the following chapters:

- [Launch Services Concepts](Launch%20Services%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqgiwviubz) presents the conceptual ideas underlying the Launch Services API, from the standpoint of both the developer and the user.
- [Launch Services Tasks](Launch%20Services%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqgmwviubz) tells how to use Launch Services to perform common tasks in your application.
- [Glossary](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojzfvbuqmrqguwviubr) defines various terms relating to Launch Services and its operations.

[Next](Launch%20Services%20Concepts.md)

