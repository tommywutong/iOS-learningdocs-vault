---
title: Instantiating Attributed Strings with Markdown Syntax
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/instantiating-attributed-strings-with-markdown-syntax
source_url: 'https://developer.apple.com/documentation/foundation/instantiating-attributed-strings-with-markdown-syntax'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/instantiating-attributed-strings-with-markdown-syntax.json'
content_hash: 'sha256:c2e35ebb30e8475d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Strings and Text](strings-and-text.md) · [AttributedString](attributedstring.md)

# Instantiating Attributed Strings with Markdown Syntax

<sub>API Collection</sub>

Use a Markdown-syntax string to iniitalize an attributed string with standard or custom attributes.

## Overview

You can use familiar Markdown syntax to initialize an attributed string with both its initial text and attributes for things like inline styles and links. In many cases, this produces easier-to-read code than manually setting attributes on ranges of an existing attributed string.

```swift
if let attString = try? AttributedString(
    markdown: "See the *latest* news at [our website](https://example.com)."),
    let websiteRange = attString.range(of: "our website"),
    let link = attString[websiteRange].link {
    print("\(link)") // Prints "https://example.com".
}
```

In this example, `attString` contains five runs, with attributes parsed from the syntax in the `markdown` parameter:

- `“See the “`, with no attributes.
- `“latest”`, with an [InlinePresentationIntentAttribute](attributescopes/foundationattributes/inlinepresentationintentattribute.md) whose value is [NSInlinePresentationIntentEmphasized](inlinepresentationintent/emphasized.md).
- `“ news at “`, with no attributes.
- `“our website”`, with an [LinkAttribute](attributescopes/foundationattributes/linkattribute.md) whose value is a [URL](url.md).
- `“.”`, with no attributes.

You can also use custom attributes defined with the [MarkdownDecodableAttributedStringKey](markdowndecodableattributedstringkey.md) protocol in the Markdown string. To do this, use Apple’s Markdown extension syntax: `^[text](attribute1: value1, attribute2: value2, …)`.

When using attributes beyond those provided by the system, be sure to use initializers that take a `scope` parameter, and provide the scope that defines the custom attributes.

> [!tip] Tip
> The [AttributedString](attributedstring.md) initializers that take a `localized` parameter can also use Markdown syntax. These initializers allow you to use Markdown in your app’s strings files.

## Topics

### Initializing from Markdown Strings

- [init(markdown:options:baseURL:)](<attributedstring/init(markdown_options_baseurl_)-52n3u.md>) — Creates an attributed string from a Markdown-formatted string using the provided options.
- [init(markdown:including:options:baseURL:)](<attributedstring/init(markdown_including_options_baseurl_)-4m51b.md>) — Creates an attributed string from a Markdown-formatted string using the provided options and attribute scope.
- [init(markdown:including:options:baseURL:)](<attributedstring/init(markdown_including_options_baseurl_)-89e48.md>) — Creates an attributed string from a Markdown-formatted string using the provided options and attribute scope that a key path identifies.

### Initializing from Markdown Data

- [init(markdown:options:baseURL:)](<attributedstring/init(markdown_options_baseurl_)-2sg1o.md>) — Creates an attributed string from Markdown-formatted data using the provided options.
- [init(markdown:including:options:baseURL:)](<attributedstring/init(markdown_including_options_baseurl_)-4co46.md>) — Creates an attributed string from Markdown-formatted data using the provided options and attribute scope.
- [init(markdown:including:options:baseURL:)](<attributedstring/init(markdown_including_options_baseurl_)-5nap7.md>) — Creates an attributed string from Markdown-formatted data using the provided options and attribute scope that a key path identifies.

### Initializing with Markdown from URL Contents

- [init(contentsOf:options:baseURL:)](<attributedstring/init(contentsof_options_baseurl_).md>) — Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data, using the provided options.
- [init(contentsOf:including:options:baseURL:)](<attributedstring/init(contentsof_including_options_baseurl_)-1x6fz.md>) — Creates an attributed string from the contents of a specified URL that contains Markdown-formatted data, using the provided options and attribute scope.
- [init(contentsOf:including:options:baseURL:)](<attributedstring/init(contentsof_including_options_baseurl_)-1fcpy.md>) — Creates an attributed string from the contents of a specified Markdown URL, using the provided options and attribute scope that a key path identifies.

### Specifying Markdown Parsing Options

- [MarkdownParsingOptions](attributedstring/markdownparsingoptions.md) — Options that affect the parsing of Markdown content into an attributed string.
