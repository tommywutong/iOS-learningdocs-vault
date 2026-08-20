---
title: Safari Web Content Guide
apple_id: TP40002051
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/IntroductiontoCSS/IntroductiontoCSS.html
archived_at: '2026-07-15T05:19:15.882733Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Web Content Guide](Developing%20Web%20Content%20for%20Safari.md)


[Next](Document%20Revision%20History.md)[Previous](HTML%20Basics.md)

# CSS Basics

Cascading Style Sheets (CSS) separates the presentation details from the HTML content, allowing you to create style sheets for different platforms. If you are optimizing your web content for Safari on iOS, you need to use CSS to access some of the iOS web content features. Read this appendix to learn how to add CSS to existing HTML content.

See _[Safari CSS Reference](../Safari%20CSS%20Reference/Introduction%20to%20Safari%20CSS%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjq)_ for a complete guide to all the CSS properties supported by Safari.

CSS is an extension to standard HTML content that allows you to fine-tune the presentation of web content. With CSS you can change a variety of style attributes of the content you are designing, such as the font for a block of text, the background color of a table, or the leading (line spacing) between lines of text.

CSS allows you to cater to different clients and preferences, because you can change the style of a webpage on the fly without ever editing the HTML structure. Instead of embedding style within the HTML structure, such as using the `bgcolor` attribute for the webpage body, you should place CSS style definitions in a separate block outside of it. In fact, your webpages are more maintainable if you separate your HTML and CSS code into different files. This way, you can use one style sheet (which holds your style definitions) across multiple webpages, dramatically simplifying your code.

The various ways you can define style for an HTML element within your webpages are described in the remaining sections of this appendix.

Using inline CSS—where style definitions are written directly into the HTML element definition—is perhaps the easiest way to define style for an element. You can do this using the `style` attribute for the element. For example, start with this paragraph:

```
<p>The quick brown fox jumped over the lazy dog.</p>
```

Without any style definitions, this renders in the default paragraph font and style for the browser rendering it. But let's say you wanted to change the style of the paragraph to display in a boldface. You can do this with the CSS `font-weight` property. To change the style for this one paragraph, add the `font-weight` key and the value for the style you want directly to the paragraph's `style` attribute:

```
<p style="font-weight: bold;">The quick brown fox jumped over the lazy dog.</p>
```

This changes the font style of that paragraph to boldface. There are some downsides to using the style definitions inline with the HTML, though:

- The definition is not reusable. For each paragraph that you want displayed in boldface, you have to type the same style definition—one for each paragraph. If you wanted to change the bold style to an italic style, for example, you would have to change the definition for each and every paragraph, as well.
- The code can get cluttered. Most of the time, you won't have a single style definition. For a particular paragraph, you may want to have it display in boldface, indent it 20 pixels from the left margin, and give it a blue background color with a black border. At minimum, this requires four CSS style definitions _for each paragraph you want to match this style._

One of the big advantages of CSS is the ability to separate the style from the structure, but that advantage is lost with this method. Other methods of using CSS in your content preserve the advantage, as explained in the following sections.

Near the beginning of every HTML document is a `<head>` block, which defines invisible metadata about the content. Within this section you can define a variety of CSS definitions that you can then reuse within the actual body content.

In the previous section there was an example of a paragraph in boldface with a blue background and a black border, all indented 20 pixels from the left margin. The definitions for that style look like this:

```
font-weight: bold;
background-color: blue;
border: 1px solid black;
margin-left: 20px;
```

But how do you embed these definitions within HTML elements without typing them directly into the HTML? First, you need to define them within the style section of the `<head>` block for the webpage. Second, you need an identifier to isolate that particular set of style definitions from any others in the `<style>` block. Using the identifier `notebox`, the style definition looks like this:

```
...
<head>
    <style type="text/css">
        .notebox {
            font-weight: bold;
            background-color: blue;
            border: 1px solid black;
            margin-left: 20px;
         }
    </style>
</head>
...
```

Notice that the definitions are bound by braces, and that the identifier ( `notebox`) is preceded by a period. The latter allows you to use this set of style definitions for _any_ element within your HTML content. If you want to limit its use only to paragraph elements, change the identifier to:

```
p.notebox
```

This tells the browser to use the definitions only if they are defined within a `<p>` paragraph element. If you want to use these styles for _all_ paragraphs, then you don't need the custom identifier. Change the identifier to `p`.

You've learned how to define the custom styles in the `<head>` block of your content. But how do you actually tell the browser which paragraphs should use these styles? Here are two paragraphs of text in HTML:

```
<p>This is some plain boring text.</p>
<p class="notebox">This is a finely styled paragraph!</p>
```

There’s a new attribute in the second paragraph: `class`. This is how you specify the style definition that a particular element should render itself with. The top paragraph in the example above would render as usual, in the default paragraph style for the browser. But with the style class of the second paragraph set to your new `notebox`, it will render with a bold font, a blue background color, a 1-pixel solid black border, all 20 pixels from the left margin. For any paragraph (or any element, since we didn't specify an explicit element it could be assigned to), simply use that class attribute to name the identifier of your style definition.

There is however one disadvantage to this method of embedding CSS in a webpage. Though the definitions are reusable within the webpage—you can now specify as many `notebox` paragraphs as you want—they are _not_ reusable across multiple webpages. If you want the paragraph's text to be rendered in an italic style instead of a bold one, you'd have to change that definition on each webpage where you integrated it. The next section describes the most scalable way to use CSS within your web content.

If you want to use a particular style across multiple webpages, there's only one way to do it: externally linked style sheets. Since each webpage has to know about the style definitions you created, placing all of them into an external file and then linking each webpage to that file seems like a reasonable way to inform them. That way, if you want to change boldface to italic, you only have to change it once—in the external file.

An external style sheet is almost exactly the same as the `<style>` block that you defined in the last section, but it’s not embedded in HTML. All the browser needs are the style definitions themselves. Listing B-1 shows a new file, called `styles.css`, that contains all the style definitions for the webpage.

__Listing B-1__  The styles.css file

```
.bordered {
    font-weight: bold;
    background-color: blue;
    border: 1px solid black;
    margin-left: 20px;
}

.emphasized {
    font-style: italic;
}
```

For good measure, there is another style definition—one that simply sets the font style of the element's text to an italic style. Now you have to somehow let the HTML content know about this external style sheet. You won't have any more embedded style definitions, so you can remove the `<style>` block altogether. In its place—still in the `<head>` block of the webpage—you'll add a `<link>` element that links the external style sheet to the document:

```
<link rel="stylesheet" href="styles.css" type="text/css">
```

This line tells the browser to link to this external style sheet. Note that the URL specified by `href` is relative—for this particular line to link the style sheet correctly, `styles.css` must be in the same folder as the HTML linking to it.

Once you've included this line, you can use the HTML `class` attribute just as in the previous section:

```
<p>This is some plain boring text.</p>
<p class="emphasized">This is some italic text.</p>
<p class="bordered">This is a finely styled paragraph!</p>
```

You've learned how to integrate CSS style into your web content. For information on what kinds of CSS properties and features are supported by Safari and WebKit, refer to _[Safari CSS Reference](../Safari%20CSS%20Reference/Introduction%20to%20Safari%20CSS%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjq)_.

[Next](Document%20Revision%20History.md)[Previous](HTML%20Basics.md)

