---
title: Providing User Assistance With Apple Help
apple_id: TP40006563
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LegacyAppleHelpConcepts/appendix_b/appendixb.html
archived_at: '2026-07-18T02:11:29.372734Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Providing User Assistance With Apple Help](Introduction%20to%20Providing%20User%20Assistance%20With%20Apple%20Help.md)


[Next](Apple%20Help%20Segments.md)[Previous](Apple%20Help%20Meta%20Tag%20Properties.md)

# Apple Help URLs

Table B-1 lists the help-specific URLs supported by Help Viewer. Use these URLs in your help book to link to other help topics and additional help resources. Arguments to help–specific URLs can either be enclosed in single quotes or can use standard URL encoding; for example the book name “SurfWriter Help” would be specified as `SurfWriter%20Help`.

__Table B-1__  Help URLs

| URL | Syntax | Action |
| `help:anchor` | `help:anchor=anchor_name bookID=help_book_name` | Opens Help Viewer to the location in a help book identified by the given anchor. |
| `help://full/path.html` | `help://path/to/page.html` | Opens the specified file in Help Viewer. |
| `help:goto_helpcenter` | `help:goto_helpcenter=developer` | Loads the Help Center in Help Viewer. There are two possible arguments to this URL: `user` and `developer`. These specify the user and developer help centers, respectively. In Mac OS X version 10.2 and later, this URL toggles the position of the Help Center drawer. |
| `help:openbook` | `help:openbook=help_book_name` | Opens the specified help book in Help Viewer. |
| `help:runscript` | `help:runscript='elp_folder_name/subfolder/scriptname string='optional_string_parameter'` | Runs the specified script. The `string` argument is an optional argument that is passed to the script. |
| `help:search` | `help:search='search_string' bookID='help_book_name'` | Initiates a search of a help book using the specified search criteria. Help Viewer then displays the search results. |

[Next](Apple%20Help%20Segments.md)[Previous](Apple%20Help%20Meta%20Tag%20Properties.md)

