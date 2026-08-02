---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.04.html
archived_at: '2026-07-15T07:58:46.242320Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.03.md)

## Troubleshooting WebObjects 4.0 Template Parsing

The WebObjects template parser parses the HTML that is to be included in a response. In WebObjects 4.0, the template parser preserves all of the static HTML that you provide in a component's template. Previously, the parser recognized many HTML tags and performed special processing based on the type of tag. The 4.0 template parser ignores all tags besides __<WEBOBJECT>__ and HTML comment tags.
The new parser has several advantages:

- It solves the problem many have encountered where WebObjects attempts to "fix" your HTML. For example, it previously was difficult to split a container element, such as a form, across two components because WebObjects would insert a closing tag for you.
- It improves your application's performance because it tends to treat larger parts of a file as a single chunk than the previous parser did.
- It allows you to suppress the copying of comments to the outgoing response. This speeds up response generation and shortens download times.

A WebObjects application may unknowingly depend upon the previous behavior of the template parser. For this reason, a compatibility flag is available on WOApplication to revert to the previous behavior.
Usually when 4.0 template parsing produces an error, it is because you have included a WebObjects dynamic form element inside of a static HTML __FORM__ element. Change the __FORM__ element to a WOForm, and your component should operate normally again. An error may also arise if your HTML pages contain __BODY__ or __IMG__ tags with __src__ parameters containing relative pathnames (absolute pathnames aren't a problem). Change the affected tags to WOBody and WOImage, respectively.
If you want, you can go back to the previous parser by implementing this method in your application class (shown in Java and WebScript):

```
public boolean requiresWOF35TemplateParser() {
    return true;
}
- requiresWOF35TemplateParser {
    return YES;
}
```


If you use the WebObjects 4.0 template parser, you might want to suppress the inclusion of HTML comments. Use the following methods, which have been added to WOApplication (as an alternative, you can use the option described in the section [Command-Line Options](NewInWO4.09.md#apple-giytemzy)):

### WOApplication Template Parsing Methods.

|  __WOApplication__ |  |
|  Method |  Description |
|  setIncludeCommentsInResponses: (class or static method) |  Sets whether the application's HTML parser includes comments from a component's HTML template as part of a response. The default is YES or true. Use this method only in the application's initializer or constructor. |
|  includeCommentsInResponses (class or static method) |  Returns YES or true if the HTML parser includes comments in the responses. Returns NO or false if the application doesn't include any comments from a component's HTML template in the response. The default is YES or true. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.05.md)
