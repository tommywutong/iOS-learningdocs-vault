---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Intro/Ingredients.html
archived_at: '2026-07-15T07:47:10.865794Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Start.book.md) [!Previous Section](Start.book.md)

# The Ingredients of a WebObjects Application

In its simplest form, a WebObjects application contains these ingredients:

- Dynamic HTML pages (called _components_)
- WebObjects classes that provide an infrastructure for the web application
- An application executable that responds to requests from a web browser

Of these ingredients, you only have to provide the components. Create an application directory under <DocumentRoot>__/WebObjects__ (<DocumentRoot> is your HTTP server's document root), and place the components in that directory. The application directory must have the extension __.woa.__
A default application executable is provided as part of the WebObjects product. The executable uses instances of the WebObjects classes to receive requests from a web browser and responds to them using the components that you provide.
More complex WebObjects applications may also contain:

- An optional application script that creates and manages application-wide resources
- An optional session script that creates and manages session-wide resources
- Optional compiled code that implements custom data and logic (WebObjects Pro and Enterprise only)

For information on using application or session scripts , see "[The Role of Scripts in a WebObjects Application](../WebScript/RoleOfScripts.md)" in the chapter "Using WebScript." For information on including compiled code, see "Creating a Compiled WebObjects Application" in _Getting Started With WebObjects Builder_.

[!Table of Contents](Start.book.md) [!Next Section](Components.md)
