---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/ExternalAccess.html
archived_at: '2026-07-15T05:17:29.779143Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Accessing%20Command%20Line%20Utilities.md)[Previous](Specifying%20Access%20Keys.md)

# Accessing External Resources

Widgets can open applications and web pages outside of their bundle. If your widget provides a subset of information found on the Internet, a link to the full data set that opens in Safari is appropriate. If your widget interfaces with an application, for example, iTunes, it should open it first. Dashboard can do this all for you.

Sometimes you may want your widget to open a webpage when certain information is clicked. For instance, clicking a stock symbol in a stock ticker widget would probably load a webpage in the default browser displaying information relevant to the stock.

To open a webpage, use the `widget.openURL(url)` method. For example, you may use it inside of a function to dynamically assemble a URL using the contents of a variable you set elsewhere in your code:

__Listing 7__  Assembling a URL and passing it to `widget.openURL`

```
<html>
<head>
<script>
    ...
    function clicked(section)
    {
        if (widget)
        {
            widget.openURL('http://www.apple.com/' + section);
        }
    }
    ...
</script>
</head>
<body>
    ...
    <span onclick="clicked('developer/')">Developer</span>
    <span onclick="clicked('store/')">Store</span>
    ...
</body>
</html>
```

In Listing 7, an arbitrary function is called when a user clicks within some text. A portion of a URL is passed to the `clicked` function and then appended onto another string, which is then passed to the `openURL` method. It then opens the user's default browser with the provided URL.

Alternatively, you can embed the method in any `<span>` tag:

```
<span onclick="widget.openURL('http://www.apple.com/')">Apple</span>
```


In addition to being able to open a webpage, your widget can open applications. Calling `widget.openApplication()` dismisses Dashboard and either opens the specified application or, if it was already open, brings it to the forefront.

The parameter passed into this method is the bundle ID for an application. For instance, to open iTunes, you pass in the string `com.apple.iTunes`:

```
widget.openApplication("com.apple.iTunes");
```

Note that there is no facility for passing arguments to an application. For this level of interactivity between a widget and application, you could try one of these options:

- Use the `widget.system()` method, as discussed in [Accessing Command Line Utilities](Accessing%20Command%20Line%20Utilities.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanjqfvjvomi), with the `open` command-line utility
- Implement a widget plug-in, as discussed in [Creating a Widget Plug-in](Creating%20a%20Widget%20Plug-in.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanjrfvjvomi)

[Next](Accessing%20Command%20Line%20Utilities.md)[Previous](Specifying%20Access%20Keys.md)

