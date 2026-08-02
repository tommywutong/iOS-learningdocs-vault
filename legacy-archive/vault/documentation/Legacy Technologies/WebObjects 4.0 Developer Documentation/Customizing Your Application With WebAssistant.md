---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb12.html
archived_at: '2026-07-18T01:24:23.327067Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DirectToWeb11.md)

# Customizing Your Application With WebAssistant

The WebAssistant allows you to customize each page of your application. You can specify:

- Which entities of the model the application displays and, of these, which are read-only
- Global attributes of pages, such as style, color, and border thickness
- Which properties are displayed, and in what order

By default, an entity's properties are listed in alphabetical order. Often, you'll want to change the order, as well as hiding some properties.

- How number and date strings should be represented
- How relationships should be represented

To activate the WebAssistant, click Customize in the Direct to Web header. A Java applet window appears showing the WebAssistant.
When you have activated the WebAssistant in your browser, a frame appears at the bottom of each page in your application in the browser (assuming it supports Java applets), containing a "Show WebAssistant" button and a status field. To bring the WebAssistant to the front, click the Show WebAssistant button (rather than clicking Customize again).

### Running WebAssistant With appletviewer

If you browser is incapable of running applets (such as WebAssistant), or if you want to run WebAssistant in a different machine from your browser, you can launch WebAssistant using the Java program __appletviewer__. To do this:

- Launch your application with the command-line option D2WLiveAssistantEnabled set to YES.
- In the console output look for a line similar to the following:

```
Jul 23 10:29:48 D2WTest[527] Server-side Live Assistant launch line:
appletviewer http://localhost:8888/cgi-
bin/WebObjects/D2WTest.woa/wa/D2WActions/openLiveAssistant
```

- Open a shell such as provided by the Terminal application on Mac OS X Server systems or the Bourne Shell on Yellow Box for Windows systems.
- Copy the string from "appletviewer" to "openLiveAssistant" to the shell and press Return (or Enter).

If the port number is -1, look in the console output for the actual port number of the application and substitute that.

When you complete this procedure, WebAssistant launches and is connected to your application. If you stop and restart the Direct to Web application, the WebAssistant will re-connect to it on the same port.
A standalone WebAssistant has exactly the same functionality as one launched inside your browser. However, if the browser you are using is not Java-enabled, your pages are not automatically refreshed after you click Update. You must either click your browser's "reload" or "refresh" button or (when you are picking a new type of page, such as a MasterDetails page instead of a ListPage), you will have to re-navigate to the same page.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DirectToWeb13.md)
