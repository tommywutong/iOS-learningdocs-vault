---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/VarScopeSummary.html
archived_at: '2026-07-15T07:48:06.414133Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](VariablesAndScope.md)

# Variables and Scope: a Summary

The following table summarizes the different types of variables in WebScript:

| Variable Type | Where It's Declared | Where It's Visible | How Long It Lives |
| --- | --- | --- | --- |
| Local | Inside a method in either an application or a component script | Only inside the method in which it's declared | For the duration of the method |
| Component | Outside a method in a component script | Inside the script in which it's declared | For the duration of a component, which is determined by the application's page-cache size |
| Session | Outside a method in a session script | Component scripts can access session variables by sending accessor messages to the WOSession object. Every session has its own version of a session variable. | For the duration of the session |
| Application | Outside a method in an application script | In the application script. Component scripts can access application variables by sending accessor messages to the WOApplication object. Every session sees application variables with the same value. | For the duration of the application |

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](AccessingAndSharingVars.md)
