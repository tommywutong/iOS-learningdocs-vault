---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/BlockingContent/blockingcontent.html
archived_at: '2026-07-27T06:57:07.723666Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](The%20Windows%20and%20Tabs%20API.md)[Previous](Injecting%20Styles.md)

# Using Your Extension to Block Content

Your browser extension can use content-blocking rules to hide elements, block loads, and strip cookies from requests. Your extension provides the content-blocking rules in a structured format and WebKit compiles those rules into bytecode that it can process efficiently at runtime. As a result, Safari's page request will not include blocked content, such as third-party scripts. By avoiding unnecessary or unwanted downloads, Safari uses less memory and has better performance.

Earlier OS X content-blocking methodology used the `onbeforeload` event and [canLoad](https://developer.apple.com/documentation/safariextensions/safaricontentbrowsertabproxy/1635506-canload) message. Both those elements have been deprecated. If you provide a content-blocking rules file for your extension you can not access the `onbeforeload` event and [canLoad](https://developer.apple.com/documentation/safariextensions/safaricontentbrowsertabproxy/1635506-canload) message.

For more information on the Safari Content Blocking model, watch the WWDC 2015 session [Safari Extensibility: Content Blocking and Shared Links](https://developer.apple.com/videos/wwdc/2015/?id=511). For information on how to format content-blocking rules, see _[Safari Content-Blocking Rules Reference](https://developer.apple.com/library/archive/documentation/Extensions/Conceptual/ContentBlockingRules/Introduction/Introduction.html#//apple_ref/doc/uid/TP40016265)_.

## Creating Content-Blocking Rules

Begin creating your content-blocking rules by examining the webpage resources with Safari Web Inspector. After identifying the elements you want to block, create content-blocking rules that match only those target elements and choose the actions to perform.

In Figure 12-1 the `div` element with the `id` "icon" has been selected in Web Inspector.

__Figure 12-1__  Selecting a page element

（原归档配图获取待重试：`withIcon_2x.png`）

Figure 12-2 shows content blocking in action. The single rule in [Listing 12-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmrufvjvomy) set the CSS for the "icon" element to `display: none`. Notice that the "icon" element is still in the HTML, but the element is not displayed.

__Figure 12-2__  After hiding an element

（原归档配图获取待重试：`withoutIcon_2x.png`）

A set of content-blocking rules is represented as an array of rule dictionaries. Each rule dictionary contains a trigger and an action dictionary. The triggers tell Safari what circumstance activates the rule's action. The action tells Safari what to do with the selected web content, whether to block or not display the content or ignore previously listed rules. Listing 12-1 is a set of content-blocking rules containing one rule dictionary. The format for content-blocking rules is described in _[Safari Content-Blocking Rules Reference](https://developer.apple.com/library/archive/documentation/Extensions/Conceptual/ContentBlockingRules/Introduction/Introduction.html#//apple_ref/doc/uid/TP40016265)_.

__Listing 12-1__  Hiding an element

```
[{
    "trigger": {
        "url-filter": "webkit.org"
    },
    "action": {
        "selector": "#icon",
        "type": "css-display-none"
    }
}]
```

## Adding Content-Blocking Rules to Your Extension

Now that you've created your content-blocking rules, you can compile them in a Safari extension. In Extension Builder click your extension’s icon to bring up the main interface, shown in Figure 12-3. Select the dropdown box "Content Blocker File" and choose your rules file.

__Figure 12-3__  Extension Builder's main interface

（原归档配图获取待重试：`ExtensionBuilder_AdBlocker_2x.png`）

## Dynamically Changing Content-Blocking Rules

You can provide your users customization options such as letting them choose what content to block and ignoring a block list when they are on a certain page. Save user input as a JSON string or a JSON object and call the JavaScript API method `contentBlockingRules` in your extensions's Global Page to dynamically configure your content-blocking rules. Listing 12-2 shows this method loading rules from an object named `contentBlockingRules`. Use the `setContentBlocker` method to clear the extension's previous settings by passing `null` or `undefined`.

__Listing 12-2__  Dynamically configuring content-blocking rules

```
var contentBlockingRules = [{
    "action": {
        "type": "block"
    },
    "trigger": {
        "url-filter": "webkit.org/images/icon-gold.png"
    }
}];
safari.extension.setContentBlocker(contentBlockingRules);
```

[Next](The%20Windows%20and%20Tabs%20API.md)[Previous](Injecting%20Styles.md)
