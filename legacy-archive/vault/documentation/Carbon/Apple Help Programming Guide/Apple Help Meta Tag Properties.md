---
title: Apple Help Programming Guide
apple_id: TP30000903
resource_type: Guide
platform: macOS
topic: User Experience
technology: Carbon
published: '2013-01-28'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProvidingUserAssitAppleHelp/appendix_a/appendixa.html
archived_at: '2026-07-15T05:24:23.245902Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple Help Programming Guide](Introduction%20to%20Apple%20Help%20Programming%20Guide.md)


[Next](Apple%20Help%20URLs.md)[Previous](Opening%20Your%20Help%20Book%20in%20Help%20Viewer.md)

# Apple Help Meta Tag Properties

Table A-1 lists the properties defined by Apple Help for use with the `meta` element. The Apple Help meta tag properties control how your help book is identified and displayed by Help Viewer.

All XML pages should start with this above the `<head>` tag:

`<?xml version="1.0" encoding="utf-8"?>`

`<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-
transitional.dtd">`

`<html xmlns="http://www.w3.org/1999/xhtml">`

The title page should include the following tags under the `<head>` tag:

`<meta name="robots" content="anchors" />`

`<link href="sty/access.css" rel="stylesheet" media="all" />`

__Table A-1__  Apple Help meta tags

| Property name | Specifies | Example |
| `KEYWORDS` | Additional search terms for an HTML help page. See [Setting Keywords](Authoring%20Apple%20Help.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbtfvbuqmrqgywugskijjdeqr2b). | `<meta name="KEYWORDS"`  `content="discard, dispose, delete,`  `clear, erase">` |
| `ROBOTS` | Controls how a file is indexed. See [Specifying What Is Indexed](Authoring%20Apple%20Help.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbtfvbuqmrqgywugskiineugr2j). | `<meta name="ROBOTS"`  `content="NOINDEX">` |

[Next](Apple%20Help%20URLs.md)[Previous](Opening%20Your%20Help%20Book%20in%20Help%20Viewer.md)

