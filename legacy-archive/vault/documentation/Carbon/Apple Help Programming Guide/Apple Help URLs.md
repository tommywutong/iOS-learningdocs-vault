---
title: Apple Help Programming Guide
apple_id: TP30000903
resource_type: Guide
platform: macOS
topic: User Experience
technology: Carbon
published: '2013-01-28'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProvidingUserAssitAppleHelp/appendix_b/appendixb.html
archived_at: '2026-07-15T05:24:23.252682Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Help Programming Guide](Introduction%20to%20Apple%20Help%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Apple%20Help%20Meta%20Tag%20Properties.md)

# Apple Help URLs

Table B-1 lists the help-specific URLs supported by Help Viewer. Use these URLs in your help book to link to other help topics and additional help resources. Arguments to help-specific URLs can either be enclosed in single quotes or can use standard URL encoding; for example the book name “SurfWriter Help” would be specified as `SurfWriter%20Help`. See [Using Help URLs in Your Help Book](Authoring%20Apple%20Help.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbtfvbuqmrqgywviucykjcummjrga) for some examples of use of these URLs.

__Table B-1__  Help URLs

| URL | Syntax | Action | Cross reference |
| `help:anchor` | `help:anchor=anchor_name`  `bookID=help_book_id` | Opens Help Viewer to the location in a help book identified by the given anchor. | [Creating a Link to an Anchor Location](Authoring%20Apple%20Help.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbtfvbuqmrqgywviucykjcummjrgi) |
| `help://full/path.html` | `help://path/to/page.html` | Opens the specified file in Help Viewer. | Providing Your Own Online Support Articles |
| `help:openbook` | `help:openbook=help_book_id` | Opens the specified help book in Help Viewer. | [Opening Other Help Books](Authoring%20Apple%20Help.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbtfvbuqmrqgywvgvzrge) |
| `help:search` | `help:search='search_string'`  `bookID='help_book_id'` | Initiates a search of a help book using the specified search criteria. Help Viewer then displays the search results. | [Initiating a Search from Your Help Book](Authoring%20Apple%20Help.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbtfvbuqmrqgywviucykjcummjrge) |

[Next](Document%20Revision%20History.md)[Previous](Apple%20Help%20Meta%20Tag%20Properties.md)

