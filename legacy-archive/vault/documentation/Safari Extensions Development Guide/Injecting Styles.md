---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/AddingStyles/AddingStyles.html
archived_at: '2026-07-27T06:57:07.716178Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Using%20Your%20Extension%20to%20Block%20Content.md)[Previous](Injecting%20Scripts.md)

# Injecting Styles

You can designate CSS style sheets to be injected into websites. Your style sheets can add to or override styles provided by the website author.

## About Injected Style Sheets

Injected style sheets are treated as user style sheets, as defined by the W3C. This means that first your injected styles are defined, then the author’s styles are added, then any of the author’s properties declared as `!important` are added, then your properties defined as `!important` are added. At each stage, a new definition overrides any previous one.

This means that style properties in your injected style sheets are added to existing page style properties, but do not override them, unless you declare them as `!important`.

For example, to override a website using colored text on a colored background and set it to black text on a white background, you could add these styles:

```
body {
     color:black !important;
     background:white !important;
     }
```

## Adding a Style Sheet

To add an injected style sheet, follow these steps:

1. Create an extension folder—open Extension Builder, click +, choose New Extension, give it a name and location.
2. Drag your style sheet into the extension folder.
3. Click New Style Sheet under Injected Extension Content in Extension Builder, as illustrated in Figure 11-1.

   __Figure 11-1__  Specifying an injected style sheet

   （原归档配图获取待重试：`addingStylesheets.jpg`）
4. Choose your style sheet from the pop-up menu.

You can have more than one injected style sheet.

In order for your style sheets to be injected, you must specify either Some or All website access for your extension. You can have your style sheet apply to a single webpage, all webpages, or only webpages from certain domains. For details, see the description of whitelists and blacklists in [Access and Permissions](Access%20and%20Permissions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqobnknltc).

If you reference images or other external resources in your style sheets, you can use relative URLs to indicate sources within your extension package, relative to the style sheet.

__Important:__ In injected scripts, relative URLs are relative to the webpage the script is injected into. In injected style sheets, relative URLs are relative to the style sheet.

[Next](Using%20Your%20Extension%20to%20Block%20Content.md)[Previous](Injecting%20Scripts.md)
