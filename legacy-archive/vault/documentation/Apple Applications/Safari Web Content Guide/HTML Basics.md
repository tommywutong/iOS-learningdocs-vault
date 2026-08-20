---
title: Safari Web Content Guide
apple_id: TP40002051
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/IntroductiontoHTML/IntroductiontoHTML.html
archived_at: '2026-07-15T05:19:15.891821Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Web Content Guide](Developing%20Web%20Content%20for%20Safari.md)


[Next](CSS%20Basics.md)[Previous](Getting%20Geographic%20Locations.md)

# HTML Basics

HyperText Markup Language (HTML) is the fundamental mark-up language used to create web content. Your HTML needs to be well structured and valid to work well with Safari on the desktop and Safari on iOS. Read this appendix to learn more about creating conforming HTML content.

See _[Safari HTML Reference](../Safari%20HTML%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanbz)_ for a complete guide to all the HTML elements supported by Safari.

HTML is the standard for content structure on the web. Its original intention of the designers was to provide the structure required for web browsers to parse its content into a meaningful format. This structure could define entire documents, complete with headings, text, lists, data tables, images, and more. As the web flourished, it also began to incorporate style and multimedia aspects as well.

Arguably the most important feature of HTML is the ability to "hyperlink" text. This gives content providers the ability to assign the URI of other content on the web to a block of text, allowing it to be clicked and followed by the user of the content.

The most recent revisions of the HTML standard are returning to the "old days" of separating the structure of web content (HTML) from the presentation of the content (using a technology called Cascading Style Sheets, or CSS). You can learn more about creating effective web content style in the [CSS Basics](CSS%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tanbrfvjvomi) appendix.

This appendix, conversely, covers only the structure of HTML and how to properly format a document for a variety of clients. It does not discuss advanced HTML features or proper webpage layout and design.

There are a few basic structure blocks that make up the core of an HTML document. The blocks are described in the context of the HTML code shown in Listing A-1.

__Listing A-1__  Basic HTML document

```
<!DOCTYPE html>
<html>
    <head>
        <title>HTML Sample Code</title>
    </head>
    <body>
        <div>
            <img src="myWelcomeGraphic.gif" alt="Welcome!">
        </div>
        <h1>Big Heading</h1>
        <p>This is our HTML sample code. It shows many elements:</p>
        <ul>
            <li>The HTML document block.</li>
            <li>The HEAD and title of the page.</li>
            <li>A paragraph.</li>
            <li>An unordered list.</li>
        </ul>
    </body>
</html>
```

__The html document block:__ The `<html>` document block is the entirety of the HTML code for a webpage. In the example, the tags defining this block—`<html>` and `</html>`—are located towards the top and bottom of the document. The document is prefaced with a `DOCTYPE` declaration, which tells browsers which specification to parse your webpage against. If you are following the strict conventions of the HTML5 specification, you should use the declaration shown above. Otherwise it can be left off, but it defaults to a "quirks" mode. Refer to the [HTML5 specification](http://dev.w3.org/html5/spec) for more on document validation types.

__The head block:__ The `<head>` block defines a block of metadata about the webpage. In this case, you can see the webpage has a `<title>` element within it. The title is the text that is displayed at the top of a web browser window. The `<head>` block also can contain a variety of other metadata, such as externally linked CSS style sheets (using the `link` tag) and sets of JavaScript functions. This block should always contain at least the title, and should always be external to the body content.

__The body block:__ This block defines the entire body of the document—it should encompass the visible content of the webpage itself. The body block itself is not designed for inline content. Rather, you should define other block elements (such as paragraphs, divisions, and headers) and embed content within them. The `<body>` block should be used to specify style parameters for the entirety of the content.

_Other block elements:_ There are a number of other fundamental block elements enclosed within the content's `<body>` block. They include:

- _Heading._ Specified in this case by the `<h1>` and `</h1>` tags, this defines the header for a following block of content. The headers can be of six different sizes, ranging from a very large first-level heading (defined with the `<h1>` and `</h1>` tags) down to a small sixth-level heading (defined with the `<h6>` and `</h6>` tags). It should contain only brief text—other content such as large text blocks, images, and movies should be embedded in other appropriate block elements such as paragraphs and divisions.
- _Paragraph._ Specified by the `<p>` and `</p>` tags, this is one of the fundamental block elements for web content. Each individual paragraph should contain the inline text content that defines the readable content of a webpage and should not enclose any other block elements. Generally, paragraph blocks are for text only. An alternative to the paragraph is the division, and that is the most appropriate block element for other media types such as images and movies.
- _Division/Section._ Specified by the `<div>` and `</div>` tags, the division is designed to contain all kinds of content, including text, images, and other multimedia. It also can encompass other block elements such as paragraphs, though enclosing divisions within other divisions is generally not recommended. Generally, division blocks are used to define unified styles for blocks of content. In the example above, the division block contains the heading image for the webpage.
- _List._ HTML supports two basic kinds of lists, the ordered list (specified by the `<ol>` and `</ol>` tags) and the unordered list (specified by the `<ul>` and `</ul>` tags), as in the example above. An ordered list tags each list element (specified by the `<li>` and `</li>` tags) with an incremental number (1, 2, 3, and so on). An unordered list tags each list element with a bullet, though this marker can be changed using CSS styling.

Now you've learned some of the fundamental skeleton elements of HTML structure. Block elements such as paragraphs and divisions are the core of the content—by themselves they are invisible, but they contain inline elements such as text, images, and movies. The next section takes you a little deeper into some features of HTML content.

You've learned about the fundamental elements that define HTML structure, but a webpage is useless without any kind of content in it. Now that you've laid down the foundation for the webpage, you should place some content to create a rich experience for your users. This appendix discusses some basic inline HTML elements; for all the elements supported by Safari and WebKit, refer to _[Safari HTML Reference](../Safari%20HTML%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanbz)_.

The most common web content contains a lot of text and a few images. Think of a travel journal, for example, that has a discussion of the day's events alongside a few photos from the journey. As the Internet has matured, you may have seen more in the way of movies, animations, and other "rich" forms of content introduced to the web. But the most common media is still a combination of text and images.

Displaying text is a simple thing in HTML. Once you've established the surrounding block element—a paragraph, for example, as discussed in the previous section—the text can just be placed inline. An example from the fictional travel journal might be as shown in Listing A-2:

__Listing A-2__  Adding a paragraph

```
<p>
Today, we arrived in Cupertino, California. We visited the Apple campus. It was a bright sunny day and exhibited none of the fog that was so prevalent during our stay in San Francisco.
</p>
```

It's a simple textual entry, but there's not much else to it. A good travel journal also marks the date and time of each entry, so you should add that to the content, as well. Listing A-3 shows the time and date added as a heading.

__Listing A-3__  Adding a heading

```
<h1>Friday, May 20, 2005 - 4:40PM</h1>
<p>
Today, we arrived in Cupertino, California. We visited the Apple campus. It was a bright sunny day and exhibited none of the fog that was so prevalent during our stay in San Francisco.
</p>
```

It's still a simple textual entry, but at least you've provided your reader with a little extra information. But what if your reader has no idea what Apple is? One of the great features of HTML is the ability to "hyperlink" documents—create links to external webpages. Using the `<a>` and `</a>` hyperlink tags, you can link your reader to the Apple website as shown in Listing A-4.

__Listing A-4__  Creating a hyperlink

```
<h1>Friday, May 20, 2005 - 4:40PM</h1>
<p>
Today, we arrived in Cupertino, California. We visited the <a href="http://www.apple.com/" title="Apple web site">Apple</a> campus. It was a bright sunny day and exhibited none of the fog that was so prevalent during our stay in San Francisco.
</p>
```

Notice that the word "Apple" is now surrounded by this hyperlink element. The element describes two particular attributes:

- _The href attribute:_ This links to the URL of the webpage you want to link to. If you specified a relative URL, such as "myPage.html" or "/pages/myPage.html", the link would point to a file within the same folder as your code, or in a separate folder, respectively. In this example, the value is a fully qualified URL, so it simply links to that site (the Apple homepage).
- _The title attribute:_ This is an optional attribute, but one you should get into the habit of using. The `title` attribute provides an alternate description of the link. In Safari, holding the mouse over the hyperlink for a couple of seconds reveals this value as a tooltip. It's a great way to provide information about a link before the user clicks it, letting them decide if they want to leave your webpage or not. Additionally, this information is used by screen readers and other accessibility devices, so by using this attribute, you help extend your content to a larger community.

With this hyperlink in place, the word "Apple" in the travel journal is now displayed as a clickable link. Clicking the word redirects the user to the Apple homepage.

So far the travel journal reads great. But to really capture the attention of your readers, you might want to include an image. An image in HTML is specified by the `<img>` tag. It's important to note that an image is an inline element, so needs to be placed within a block element such as a paragraph. It is also a little different from some other inline elements in that it doesn't require a closing tag. Listing A-5 shows how to add an image to the travel journal entry.

__Listing A-5__  Adding an image

```
<h1>Friday, May 20, 2005 - 4:40PM</h1>
<p>
<img src="cupertino.gif" alt="Picture of Cupertino, CA">
<br>
Today, we arrived in Cupertino, California. We visited the <a href="http://www.apple.com/" title="Apple web site">Apple</a> campus. It was a bright sunny day and exhibited none of the fog that was so prevalent during our stay in San Francisco.
</p>
```

Notice that the image definition looks a lot like the hyperlink definition. The `src` attribute defines the URL to the image (with the same rules for relative versus absolute URLs as in the hyperlink), and the `alt` attribute defines a block of alternate text—this text can also be read by screen readers, or can be shown by some browsers when images are turned off in the browser.

Another small element we added was the `<br>` line break element. Remember that an image is an inline element, just like text. Without a forced line break, the image would display and the text would follow directly after, left to right, one after the other. That's a little awkward for a travel journal, but useful when you have small images (like mathematical equations) that you want integrated into the text. Add the line break to force the next line of text to a new line.

Now you've learned about actual web content—the inline text and media that defines what a user reads and views when they visit your webpage. This section is by no means an exhaustive discussion on the content you can provide to your users. For more information on the content that Safari and WebKit support, refer to _[Safari HTML Reference](../Safari%20HTML%20Reference/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanbz)_.

This section discusses a few more features of HTML that you may want to use in your web content.

One other common block element is the `<table>` block. You can add a `<table>` block to display any kind of tabular data. To the previous example, let's add a table of temperatures that the journal writer experienced on his or her day in Cupertino. For the information to be useful, you'll also want to add something about the time at which the temperature was recorded. Both the time and temperature can be labeled using table headers, specified by the `<th>` and `</th>` tags. Notice that the order of the table headers and table cells (specified by the `<td>` and `</td>` tags) match within their particular row (specified by the `<tr>` and `</tr>` tags) in Listing A-6.

__Listing A-6__  Creating a table

```
<h1>Friday, May 20, 2005 - 4:40PM</h1>
<p>
<img src="cupertino.gif" alt="Picture of Cupertino, CA">
<br>
Today, we arrived in Cupertino, California. We visited the <a href="http://www.apple.com/" title="Apple web site">Apple</a> campus. It was a bright sunny day and exhibited none of the fog that was so prevalent during our stay in San Francisco.
</p>

<table>
    <tr>
        <th>Time</th>
        <th>Temperature</th>
    </tr>
    <tr>
        <td>9:00AM</td>
        <td>65 degrees</td>
    </tr>
    <tr>
        <td>12:00PM</td>
        <td>76 degrees</td>
    </tr>
    <tr>
        <td>3:00PM</td>
        <td>78 degrees</td>
    </tr>
</table>
```

Another useful feature is the ability to integrate JavaScript—an interpreted language processed by web browsers—within HTML. JavaScript can do a variety of tasks, many of which are addressed in _[WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483)_. The JavaScript code can be embedded in external files, within the `<script>` block of the webpage's `<head>` block, or even inline with the elements, using the various JavaScript delegates provided by the browser. For example, if you want to display an alert when the user clicks a button, add the code (or the function call, if the code is defined elsewhere) to the button's `onClick` delegate:

```
<input type="button" value="Click Me!" onClick="alert('This is an alert!')">
```

[Next](CSS%20Basics.md)[Previous](Getting%20Geographic%20Locations.md)

