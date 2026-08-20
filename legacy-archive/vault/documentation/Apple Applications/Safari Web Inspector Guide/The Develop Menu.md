---
title: Safari Web Inspector Guide
apple_id: TP40007874
resource_type: Guide
platform: iAd System JS|Safari (Mobile)|Safari|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2018-02-07'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Safari_Developer_Guide/TheDevelopMenu/TheDevelopMenu.html
archived_at: '2026-07-15T05:18:48.893578Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Web Inspector Guide](About%20Safari%20Web%20Inspector.md)


[Next](Keyboard%20Shortcuts.md)[Previous](The%20Console.md)

# The Develop Menu

The Develop menu contains a set of tools to assist you in prototyping, debugging, and optimizing your website:

- Open Page With—Open the current webpage in another web browser. Any app that registers as a viewer for HTTP URLs appear here.
- User Agent—Browsers send a user agent string that identifies the browser type and version to the server. The same string is sent in response to a JavaScript request for the user agent string. Use this menu item to modify the user agent string Safari sends, to simulate visiting your site using a different browser or device type. See [Changing the User Agent String](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnznknltk).
- Show Web Inspector—Open Web Inspector.
- Show Error Console—Open the console in Web Inspector. See [The Console](The%20Console.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnrnknltc).
- Show Page Source—Open the Source Code in Web Inspector to see the HTML of the current page. See [Source versus DOM](Resources%20and%20the%20DOM.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqmznknltk).
- Show Page Resources—Open the Resources navigation sidebar in Web Inspector to view all images, scripts, and style sheets attached to the current page. See [Resources and the DOM](Resources%20and%20the%20DOM.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqmznknltc).
- Show Snippet Editor—Open the Snippet Editor window to interactively prototype HTML, CSS, or JavaScript snippets. See [Snippet Editor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnznknltg).
- Show Extension Builder—Open Extension Builder to install, modify, create, or uninstall a Safari extension. See _[Safari Extensions Development Guide](https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009977)_.
- Start Profiling JavaScript—Turn on the JavaScript profiler to see how many times each function is called, how long it takes, and so on. See [JavaScript and Events Recording](Timelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnbnknlto).
- Start Timeline Recording—Record detailed information about the status of incoming HTTP requests, JavaScript events, and layout rendering. See [Recording Timelines](Timelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzufvbuqnbnknlte).
- Empty Caches—Delete all caches stored by the browser. Select this if you’re suspicious that your webpage is using stale cached content.
- Disable Caches—Turn off caching to see how a website loads the first time. Select this if you’re suspicious that your webpage is using stale cached content.
- Disable Images—Turn off image display and view websites as text only.
- Disable Styles—Turn off CSS style properties to view the page purely as HTML and JavaScript.
- Disable JavaScript—View websites with the JavaScript interpreter disabled.
- Disable Site-specific Hacks—Use this to disable the modifications to Safari and test your site for correct operation (if Apple engineers have modified Safari specifically to work around a problem with your website).
- Disable Local File Restrictions—Disable security checks that may prohibit local development.
- Enable WebGL—Turn on the ability to view OpenGL content in Safari.
- Allow JavaScript in the Address Bar—Allow JavaScript to be executed on the page by typing `javascript:` followed by a valid JavaScript expression in the Address bar.

Every browser has a user agent string that identifies its type and version number. The browser sends this string to the server. Your website can also use JavaScript to read the user agent string to determine which version of a browser a user is running. You can choose what Safari reports as its user agent from the User Agent submenu.

This can be useful to quickly test your code to see if it is reacting to various user agents as you expect, without having to actually load the page in multiple versions of multiple browsers. The User Agent submenu is shown in Figure A-1.

__Figure A-1__  The type and version of various browsers in the User Agent submenu

!

You can choose the common versions of most popular browsers from the submenu. Note that the list includes the versions of Safari found on iPhone, iPad, and iPod touch.

The Other... menu item opens a sheet showing the default user agent string, which you can edit to any string you like.

Snippet Editor provides an interactive sandbox for previewing HTML and CSS, as shown in Figure A-2.

__Figure A-2__  Snippet Editor can help you isolate problems with your markup

!

[Next](Keyboard%20Shortcuts.md)[Previous](The%20Console.md)

