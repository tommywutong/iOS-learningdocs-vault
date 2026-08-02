---
title: Safari HTML Reference
apple_id: TP40002049
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: WebKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariHTMLRef/Articles/HTMLTags.html
archived_at: '2026-07-15T05:19:05.570210Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML Reference](Introduction.md)


[Next](Supported%20Attributes.md)[Previous](Explanation%20of%20Terms.md)

# Supported HTML

Safari and WebKit implement a large subset of the HTML5 Specification defined by the World Wide Web Consortium (W3C). This reference defines every symbol in the specification that Safari implements. If a element is not listed here, it is not supported by Safari and WebKit.

Specifies a hyperlink or a page anchor.

____Syntax____: |  |
```
<a href="URL"> ... </a>
```

____Discussion____: When the `href` attribute is used with the `a` element, the text or image enclosed by the element becomes a hyperlink, linked to the URL specified by `URL`. When the `name` attribute is used, the element becomes an anchor that can be linked to by a hyperlink.

Specifies an abbreviated form of a string. Use `abbr` instead of `acronym`.

____Syntax____: |  |
```
<abbr title="fullstring"> abbrev </abbr>
```

____Discussion____: In Safari, the string specified by `abbr` is displayed onscreen while the content of `fullstring` is revealed in help element form by holding the mouse over the abbreviated value. This element is also useful for applications that read the underlying HTML code of a page, such as screen readers. Use `abbr` instead of `acronym`.

Obsolete. Specifies the acronym form of a string. Use `abbr` instead.

____Discussion____: The `acronym` element behavior was identical to the behavior of the `abbr` element.

____Availability____: The `acronym` element has been declared obsolete in the HTML5 specification.

Specifies a street address.

____Syntax____: |  |
```
<address> streetaddress </address>
```

____Discussion____: The `address` element specifies a street address. The address enclosed within the element is italicized. Line breaks (such as ones between a street address and a city/state/zip) are not automatically inserted.

Obsolete. Embeds a Java applet within a page. Use `embed` or `object` instead.

____Discussion____: The applet is displayed at the location of the element in the page. The location of the applet is given by the URL specified by an `archive` parameter.

____Availability____: The `applet` element has been declared obsolete in the HTML5 specification.

Specifies a specific area within an image map.

____Syntax____: |  |
```
<area shape="shapetype" coords="coords" href="URL">
```

____Discussion____: The `area` element defines discrete areas within an image map (defined by an enclosing `map` element). The area defined by this element acts as a hyperlink, linked to the URL specified by `URL`, bounding shape specified by `shape`, and coordinates specified by `coords`.

Specifies an independent section of a page.

____Discussion____: Use `article` instead of `div` to contain a forum post, newspaper article, or blog entry. An article may be nested inside another `article` element.

Specifies a section of a page that is tangentially related to the surrounding content.

____Discussion____: The `aside` element can indicate parenthetical content like pull quotes or sidebars.

Embeds audio into a webpage.

____Syntax____: |  |
```swift
<audio src="url"
    autoplay="autoplay" <!-- Boolean attribute. Omit to prevent autoplay. -->
    start="00:00:00.00"
    loopstart="00:00:00.07" <!-- 7 seconds -->
    loopend="00:00:00.19"
    end="00:00:00.27"
    playcount="4" <!-- play 4x -->
    controls="true" >
```

____Discussion____: The `audio` element might contain fallback content for browsers that do not support this element. Any content enclosed within the `audio` element is ignored by browsers that support the `audio` element (but it must be valid HTML).

The `audio` element supports inclusion of `source` elements to provide multiple versions of an audio clip encoded with different codecs, at different bit rates, and so on. These `source` elements must be the first elements inside the `audio` element before any fallback content. See `source` for more information.

Displays text in a bold style.

____Syntax____: |  |
```
<b> content </b>
```

____Discussion____: The text specified by `content` is displayed in the bold style, but otherwise matches the style of the enclosing element. Consider using `em` to add emphasis and `strong` to indicate importance before choosing `b`. Styles should be more finely tuned using CSS instead of using HTML style elements.

Defines the base URL for all linked objects on a page.

____Syntax____: |  |
```
<base href="URL">
```

____Discussion____: The URL specified by `href` acts as the base URL for any relatively linked object—such as an image, hyperlink, or Java applet—on the page. If a URL is specified absolutely (with a fully qualified URL), it is not affected by this element. The `base` element must be placed in the `head` section of a page.

Obsolete. Specifies the base font for a page. Use CSS styling instead.

____Discussion____: The font is used as the default font for the page unless otherwise specified. The font is specified by `face`, its size is specified by `size`, and its color is specified by `color`. These attributes and their various options are defined in `[Supported Attributes](Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danjyfvjvomi)`. Use CSS styling to set this property for the enclosing elements unless you have a specific reason to use `basefont`.

____Availability____: The `basefont` element has been declared obsolete in the HTML5 specification.

Specifies text that may be displayed in a unique direction.

____Syntax____: |  |
```
<p> English content and <bdi> Arabic content </bdi> </p>
```

____Discussion____: Use `bdi` when the directional display of the text is unknown. Unlike `bdo` elements, `bdi` elements are not automatically displayed in a unique direction. See [http://www.w3.org/TR/CSS2/visuren.html#direction](http://www.w3.org/TR/CSS2/visuren.html#direction) for more information on directional text.

Displays text in a different direction.

____Syntax____: |  |
```
<bdo dir="dir"> content </bdo>
```

____Discussion____: The text specified by `content` is displayed left to right if `dir` is set to `ltr`; it is displayed right-to-left if it is set to `rtl`. See [http://www.w3.org/TR/CSS2/visuren.html#direction](http://www.w3.org/TR/CSS2/visuren.html#direction) for more information on directional text.

Obsolete. Displays text in a large size. Use CSS styling instead.

____Discussion____: The text specified by `content` is displayed in a larger size but otherwise matches the style of the enclosing element. Styles should be more finely tuned using CSS instead of using HTML style elements.

____Availability____: The `big` element has been declared obsolete in the HTML5 specification.

Displays text in an indented quotation style.

____Syntax____: |  |
```
<blockquote> content </blockquote>
```

____Discussion____: The text specified by `content` is indented (on both sides of the text block), but otherwise matches the style of the enclosing element. Styles should be more finely tuned using CSS instead of using HTML style elements.

Defines the entirety of the document body.

____Syntax____: |  |
```
<body> content </body>
```

____Discussion____: The content specified by `content` comprises most of the content of the page.

Represents a single line break.

____Syntax____: |  |
```
<br>
```

____Discussion____: Layout should be more finely tuned using CSS instead of using HTML style elements.

Defines an interactive button on a page.

____Syntax____: |  |
```
<button> content </button>
```

____Discussion____: The text specified by `content` is displayed within the frame of the button. This differs from the `button` input type in that you can specify content within the `button` element.

Specifies an advanced drawing region.

____Syntax____: |  |
```
<canvas id="identifer" height="value" width="value">
```

____Discussion____: The `canvas` element specifies the location of an advanced drawing region. The `canvas` element supports the same attributes as the `img` element with the exception of the `src` attribute, which is ignored for the `canvas` element. You can specify any of the other attributes you would normally specify for an image. The identifier specified by `id` is required for Dashboard widgets, as are the height and width specified by `height` and `width`, respectively.

Read _[Safari HTML5 Canvas Guide](../../Audio%20Video/Safari%20HTML5%20Canvas%20Guide/About%20Canvas.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbs)_ for more information.

Defines a caption for an HTML table.

____Syntax____: |  |
```
<caption> content </caption>
```

____Discussion____: The text specified by `content` is displayed as a caption for the table in which the caption is enclosed.

Deprecated. Defines a region of content to be centered. Use CSS styling instead.

____Discussion____: The content wrapped by the `center` element is centered within its enclosing element. Styles should be more finely tuned using CSS instead of using HTML style elements.

____Availability____: The `center` element has been declared obsolete in the HTML5 specification.

Specifies a citation.

____Syntax____: |  |
```
<cite> content </cite>
```

____Discussion____: The `cite` element specifies a citation. The text enclosed within the element is italicized.

Specifies text as computer code.

____Syntax____: |  |
```
<code> content </code>
```

____Discussion____: The `code` element specifies a block of code. The text enclosed within the element uses a "teletype" monospaced character font.

Specifies attributes of columns in a table.

____Syntax____: |  |
```
<col properties >
```

____Discussion____: The `col` element allows you specify attributes for a given table column, with those attributes specified by `properties`. A series of `col` elements must be placed in order of the actual table columns. These elements must be placed within a table or a `colgroup`.

Specifies attributes for multiple columns in a table.

____Syntax____: |  |
```
<colgroup properties ></colgroup>
```

____Discussion____: The `colgroup` element specifies attributes for multiple table columns, with those attributes specified by `properties`. For example, to set center column alignment for three different columns, you would use `<colgroup span="3">`. These elements must be placed within a table.

Obsolete. Specifies a command the user can invoke. Use `menuitem` instead.

____Discussion____: The `command` element has been declared obsolete in the HTML5 specification.

Contains a set of `option` elements for a control.

____Syntax____: |  |
```
<input name="state" list="states">
    <datalist id="states">
        <option>Alabama</option>
        <option>Alaska</option>
        …
        <option>Wyoming</option>
    </datalist>
```


Specifies a definition for a term.

____Syntax____: |  |
```
<dd> content </dd>
```

____Discussion____: The `dd` element specifies a definition for a term within an HTML definition list. The text enclosed within the element is indented under the term specified by the enclosing `dt` block.

Specifies a block of deleted text.

____Syntax____: |  |
```
<del> content </del>
```

____Discussion____: The `del` element specifies a block of deleted text, which is marked with a horizontal line through the center.

Specifies a control for additional information, typically displaying a disclosure triangle.

____Syntax____: |  |
```
<details>
     <summary> Summary info </summary>
     <p> Detailed information </p>
</details>
```

____Discussion____: Nested content is revealed on user interaction. The `summary` element should be included in a `details` element.

____Availability____: The `details` element was introduced in the HTML5 specification.

Specifies a definition.

____Syntax____: |  |
```
<dfn> content </dfn>
```

____Discussion____: The `dfn` element specifies a definition of any sort.

Obsolete. Specifies a directory list. Use CSS styling or list elements as appropriate.

____Discussion____: The `dir` element specifies a directory list, each element of which is specified by an `li` element. List styles should be more finely tuned using CSS instead of using HTML style elements, and the structure should be defined instead with the `ul` and `ol` elements.

____Availability____: The `dir` element has been declared obsolete in the HTML5 specification.

Specifies a styleless section in a document.

____Syntax____: |  |
```
<div> content </div>
```

____Discussion____: The `div` element specifies a section in a document as a block element. Multiple divs stack vertically on the page. Use CSS styles to tune the style properties of this element.

Specifies a definition list.

____Syntax____: |  |
```
<dl> content </dl>
```

____Discussion____: The `dl` element specifies a definition list. Within the bounds of this block, terms to be defined should be marked using the `dt` element, and their definitions should be marked using the `dd` element.

Specifies a definition term.

____Syntax____: |  |
```
<dt> content </dt>
```

____Discussion____: The `dt` element specifies a definition term. It should be used to mark an actual term within the bounds of a definition list (`dl`). Definitions should follow each term, and be marked using the `dd` element.

Specifies emphasized text.

____Syntax____: |  |
```
<em> content </em>
```

____Discussion____: The `em` element specifies a block of emphasized text. Use CSS to finely tune styles instead of using HTML style elements.

Deprecated. Embeds an object within a page. Use the `object` element to embed objects.

____Discussion____: The object, if visible, is displayed at the location of the element in the page, with a height specified by `height` and a width specified by `width`. The location of the object is given by the URL specified by `src`, or `code` if the applet is in a standard Java class file.

____Availability____: The `embed` element has been deprecated in the HTML 4.01 standard.

Specifies a set of fields.

____Syntax____: |  |
```
<fieldset>
    caption input
    caption input
</fieldset>
```

____Discussion____: The `fieldset` element encloses a set of input fields, and draws a box around them. The fields themselves are made with input elements specified by `input` and the names of the fields are plaintext specified by `caption`.

Specifies a caption for a `figure` element.

The content specified by `figure` may be removed without affecting the page flow.

____Syntax____: |  |
```
<figure>
    <img src="image.png" alt="Description of image">
    <figcaption>Figure 1. An HTML element.</figcaption>
</figure>
```

____Discussion____: Typically includes an image or video; may include a caption (`figcaption`).

Obsolete. Defines a font style for the content the element encloses. Use CSS styling instead.

____Discussion____: The content specified by `content` is altered based on a variety of properties, such as `face`, `size`, and `color`. Styles should be more finely tuned using CSS instead of using HTML style elements.

____Availability____: The `font` element has been declared obsolete in the HTML5 specification.

Specifies content for the section footer.

____Availability____: The `footer` element was introduced in the HTML5 specification.

Specifies an HTML form.

____Discussion____: The `form` element specifies a form on a page. Each individual form (with its variety of inputs such as checkboxes, text fields, and password fields) should be enclosed in its own form element. If using the form for some kind of submission, the form's submit button should also be enclosed within this element.

Form elements are described in [Supported Attributes](Supported%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danjyfvjvomi).

Obsolete. Displays a URL in an inline frame. Use `iframe` instead.

____Discussion____: The `frame` element specifies a directory list, each element of which is specified by an `li` element. List styles should be more finely tuned using CSS instead of using HTML style elements, and the structure should be defined instead with the `ul` and `ol` elements.

____Availability____: The `frame` element has been declared obsolete in the HTML5 specification.

Obsolete. Specifies a frameset. Use `iframe` instead.

____Discussion____: The `frameset` element specifies the overall frameset for a number of frames (each specified with the `frame` element. The URL for the frame is specified by `src`. The size of each column should be specified by the `cols` and `rows` properties.

____Availability____: The `frameset` element has been declared obsolete in the HTML5 specification.

Specifies various headers.

____Syntax____: |  |
```
<h#> content </h#>
```

____Discussion____: Heading elements specify a block of header text, with `h1` representing the largest font size and `h6` representing the smallest. Styles should be more finely tuned using CSS instead of using HTML style elements.

Specifies metainformation about the HTML document.

____Syntax____: |  |
```
<head> content </head>
```

____Discussion____: The `head` element can contain a number of informational elements, such as `title` for the page title or `style` for a CSS definition block.

Specifies .

____Syntax____: |  |
```
<header> content </header>
```

____Discussion____: .

Specifies .

____Syntax____: |  |
```
<hgroup> content </hgroup>
```

____Discussion____: .

Specifies a horizontal line.

____Discussion____: The `hr` element specifies a horizontal line. Styles should be more finely tuned using CSS instead of using HTML style elements.

Specifies the HTML document.

____Discussion____: The `html` element specifies an HTML document, and should encompass all the content of the page.

Displays text in an italic style.

____Syntax____: |  |
```
<i> content </i>
```

____Discussion____: The text specified by `content` is displayed in the italic style, but otherwise matches the style of the enclosing element. Consider using the `em`, `strong`, `mark`, `cite`, and `dfn` elements before choosing `i`. Styles should be more finely tuned using CSS instead of using HTML style elements.

Displays a URL in an inline frame.

____Syntax____: |  |
```
<iframe src="URL"></iframe>
```

____Discussion____: The URL specified by `src` loads into an inline frame placed wherever the `iframe` element is entered.

Displays an inline image.

____Syntax____: |  |
```
<img src="img.jpg" srcset="img_HD.jpg 2x, img_sm.jpg 100w, img_smHD.jpg 100w 2x">
```

____Discussion____: The image file specified by `src` or `srcset` is displayed inline in the enclosing element. Descriptors in `srcset` refer to maximum pixel width (`w`), height (`h`), or density (`x`).

Displays an input for an HTML form.

____Syntax____: |  |
```
<input type="type">
```

____Discussion____: The `input` element specifies an input mechanism in an HTML form. The available types of input are listed in `[Supported Input Values](InputTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danjvfvjvomi)`.

Specifies a block of inserted text.

____Syntax____: |  |
```
<ins> content </ins>
```

____Discussion____: The `ins` element specifies a block of inserted text, which is marked with an underline.

Specifies text as keyboard text.

____Syntax____: |  |
```
<kbd> content </kbd>
```

____Discussion____: The `kbd` element specifies a block of keyboard text. The text enclosed within the element uses a "teletype" monospaced character font.

Provides public key generation for forms.

____Syntax____: |  |
```
<keygen name="name" challenge="challenge_value">
```

____Discussion____: The `keygen` element places a form element on the page, which generates a 512, 1024, or 2048-bit public key as its value. The challenge specified by `challenge` and the public key are DER encoded and digitally signed with a private key (stored in a local database). The result is then encoded in Base64 and is returned as the value of this field.

Specifies a label for input controls.

____Syntax____: |  |
```
<label for="id"> content </label>
```

____Discussion____: The `label` element specifies a label for the input control whose name is specified by `for`. The text specified by `content` makes up the body of the label.

Specifies individual layers on a webpage. The `layer` element is not well-supported and should be replaced with `iframe` frames using CSS styling techniques in HTML 4.01 Transitional documents. In HTML 4.01 Strict documents, `layer` should be replaced with `object` or `div`.

____Syntax____: |  |
```
<layer> content </layer>
```

____Discussion____: The `layer` element specifies an independent layer of content on a webpage.

Specifies the caption for a fieldset.

____Syntax____: |  |
```
<legend> content </legend>
```

____Discussion____: The `legend` element specifies the label for a fieldset (specified by the `fieldset` element). The caption specified by `content` is merged with the box surrounding the fieldset.

Specifies a list element.

____Syntax____: |  |
```
<li> content </li>
```

____Discussion____: Within a list block (specified by `ul` for an unordered list, or `ol` for an ordered list), `li` specifies single list element, whose content is specified by `content`. List styles should be more finely tuned using CSS instead of using HTML style elements.

Specifies a connection to an external file.

____Syntax____: |  |
```
<link href="URL">
```

____Discussion____: The `link` element specifies an external file that is related to the HTML document it is enclosed in. For example, you should use `link` in the head of an HTML document to specify an external CSS stylesheet.

Obsolete. Indicates a block of preformatted text. Use `pre` and `code` instead.

____Availability____: The `listing` element has been declared obsolete in the HTML5 specification.

Specifies the main content of the `body` element.

____Discussion____: Only one `main` element is included in a `body` element. The main content should not be nested in other block elements.

Specifies a browser-processed image map.

____Syntax____: |  |
```
<map name="id" id="id">
```

____Discussion____: The `map` element encloses the `area` elements that define the regions of an image map. The identifier specified by `id` and the name specified by `name` should be used by an `img` element’s `usemap` property.

Specifies a highlighted element.

____Discussion____: The `mark` element can be used to highlight search results.

Obsolete. Specifies a horizontally scrolling block of content. Use JavaScript instead.

____Discussion____: The `marquee` element specifies a block of content that scrolls horizontally.

____Availability____: The `marquee` element has been declared obsolete in the HTML5 specification.

Specifies a menu list.

____Discussion____: The `menu` element specifies a menu list. Within the bounds of this block, terms to be defined should be marked using the `dt` element, and their definitions should be marked using the `dd` element. The `menu` element was deprecated in the HTML 4.01 standard but reintroduced in HTML5.

Specifies metainformation about an HTML page.

____Syntax____: |  |
```
<meta name="title" content="content">
```

____Discussion____: The `meta` element specifies a list of metainformation about a page, such as keywords for a search engine to index. The title specified by `name` defines what metainformation you are displaying. The text specified by `content` is the actual metainformation.

For information on Apple-specific meta tag keys, see `[Supported Meta Tags](MetaTags.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojtfvjvomi)`.

Displays a gray horizontal bar with an area of color inside, representing a scalar or fractional value. Similar to the `progress` element.

____Syntax____: |  |
```
<p> Player 1: 16 out of 20 honor <meter min="0" max="20" low="0" high="20" value="16"> 16 out of 20 </meter> </p>
<p> Player 2: 20% of recruitable heroes <meter value="0.20"> 20% of recruitable heroes </meter> </p>
```

____Discussion____: Use `progress` to illustrate task completion. Use `meter` to show a value in a range.

____Availability____: The `meter` element was introduced in the HTML5 specification.

Specifies a section with navigation links.

____Syntax____: |  |
```
<nav>
    <ul>
        <li><a href="#">Link1</a></li>
        <li><a href="#">Link2</a></li>
        <li><a href="#">Link3</a></li>
    </ul>
</nav
```

____Discussion____: You can create multiple `nav` elements in one document. The `nav` element was introduced in the HTML5 specification.

Obsolete. Specifies a region of content with no embedded line breaks. Use CSS styling instead.

____Discussion____: The content displays with no line breaks. Use the `nobr` element for text blocks that must remain on one line.

____Availability____: The `nobr` element has been declared obsolete in the HTML5 specification.

Obsolete. Specifies content to display when embedded objects are not supported. Use `object` if necessary.

____Discussion____: The `noembed` element specifies a block of content that displays in browsers that do not support embedded objects.

____Availability____: The `noembed` element has been declared obsolete in the HTML5 specification.

Obsolete. Specifies content that displays in browsers that do not support frames. There is no replacement element.

____Discussion____: The `noframes` element specifies a block of content that displays in browsers that do not support frames or have them deactivated. Because frames are no longer supported the `noframe` element is not needed.

____Availability____: The `noframes` element has been declared obsolete in the HTML5 specification.

Specifies content that displays in browsers that do not support layers.

____Syntax____: |  |
```
<nolayer> content </nolayer>
```

____Discussion____: The `nolayer` element specifies a block of content that displays in browsers that do not support layers.

Specifies content to display in browsers that do not run scripts.

____Syntax____: |  |
```
<noscript> content </noscript>
```

____Discussion____: The `noscript` element specifies a block of content that displays in browsers that do not support the execution of scripts or have them deactivated.

Embeds an object within a page.

____Syntax____: |  |
```
<object height="value" width="value" archive="URL" data="URL"> content </object>
<object height="value" width="value" data="URL" codebase="URL"> content </object>
```

____Discussion____: The object is displayed at the location of the element in the page, with a height specified by `height` and a width specified by `width`.

The location of the object is given by the URL specified by `archive` for a Java archive, `data` for some arbitrary embedded data (an image, for example), or `codebase` for object code of any other type.

Specifies an ordered list.

____Syntax____: |  |
```
<ol> content </ol>
```

____Discussion____: The `ol` element specifies an ordered, numbered list. Within the bounds of this block, list items should be defined using the `li` element.

Specifies a group of options.

____Syntax____: |  |
```
<optgroup label="label"> options </optgroup>
```

____Discussion____: Within a `select` input type, the `optgroup` element specifies a subgroup of options. Within the bounds of this block, individual options are specified using the `option` element. The title of the subgroup is specified by `label`, and in Safari is displayed as bold gray text, with the subgroup’s associated options indented under it.

Specifies a list option.

____Syntax____: |  |
```
<option value="value"> title </option>
```

____Discussion____: Within a `select` input type, the `option` element specifies a single selectable option. The form value of the option is specified by `value`, and its visible name is specified by `title`. These elements can be placed directly within a `select` input type or within an `optgroup` within a `select` element.

Specifies the result of a calculation.

____Syntax____: |  |
```
<output name="result"> content </output>
```

____Discussion____: Use a script to add the result to the text specified by `content`.

____Availability____: The `output` element was introduced in the HTML5 specification.

Displays a paragraph.

____Syntax____: |  |
```
<p> content </p>
```

____Discussion____: The `p` element indicates a paragraph in the document.

Represents a parameter for an `object` declaration.

____Syntax____: |  |
```
<param name="name" value="value">
```

____Discussion____: The `param` element represents a specific parameter for an embedded `object` element. You can place any number of these, but they must be enclosed within the `object` block. The parameter’s name/key is specified by `name` and its value is specified by `value`.

Obsolete. Represents a MIME type. Use `"text/plain"` instead.

____Discussion____: MIME types indicate the type of media to be displayed.

____Availability____: The `plaintext` element has been declared obsolete in the HTML5 specification.

Represents a block of preformatted text.

____Syntax____: |  |
```
<pre> content </pre>
```

____Discussion____: The `pre` element preserves the formatting of the block of text specified by `content`, specifically line breaks and multiple spaces. Normal text operation in Safari displays no difference between a single space and multiple consecutive spaces. In Safari, text enclosed in this element is also rendered in a monospace "teletype" font.

Displays a representation of task completion. Similar to the `meter` element.

____Syntax____: |  |
```
<progress value="100" max="450"> 45% </progress>
```

____Discussion____: Use `progress` to illustrate task completion. Use `meter` to show a value in a range.

____Availability____: The `progress` element was introduced in the HTML5 specification.

Displays an inline quotation.

____Syntax____: |  |
```
<q> content </q>
```

____Discussion____: The text specified by `content` is displayed in quotes, but otherwise matches the style of the enclosing element. Styles should be more finely tuned using CSS instead of using HTML style elements.

Specifies parenthesis to display if the `ruby` element is not supported.

____Syntax____: |  |
```
<ruby>
     漢 <rp> ( </rp> <rt> Kan </rt> <rp> ) </rp>
</ruby>
```

____Discussion____:

____Availability____: The `rp` element was introduced in the HTML5 specification.

Specifies a ruby annotation showing pronunciation of East Asian characters.

____Syntax____: |  |
```
<ruby>
     漢 <rp> ( </rp> <rt> Kan </rt> <rp> ) </rp>
</ruby>
```

____Availability____: Th `ruby` element was introduced in the HTML5 specification.

Specifies the pronunciation of East Asian characters.

____Syntax____: |  |
```
<ruby>
     漢 <rp> ( </rp> <rt> Kan </rt> <rp> ) </rp>
</ruby>
```

____Availability____: The `rt` element was introduced in the HTML5 specification.

Deprecated. Defines a block of text in strikethrough style. Use `del` to indicate document edits.

____Discussion____: The content inside the `s` element is rendered with a horizontal line through the center. The `del` element is more appropriate to show text that was removed. Styles should be more finely tuned using CSS instead of using HTML style elements when possible.

____Availability____: The `s` element has been deprecated in the HTML 4.01 standard.

Specifies text as sample code.

____Syntax____: |  |
```
<samp> content </samp>
```

____Discussion____: The `samp` element specifies a block of code. The text enclosed within the element uses a "teletype" monospaced character font.

Embeds and executes script code.

____Syntax____: |  |
```
<script type="mimetype"> code </script>
```

____Discussion____: The `script` element specifies a block of script code, such as JavaScript. The code specified by `code` is invisible onscreen, but is visible in the page source. Code embedded within `script` elements (unless defined inside functions) is executed immediately on page load. The MIME type of the script should be specified by `type`.

Specifies a generic section of a document when `article` is not appropriate.

____Syntax____: |  |
```
<section>
     <h1> Heading </h1>
     <p> content </p>
</section>
```

____Discussion____: The content in a `section` should be related. If content is unrelated use a `div` element for grouping.

____Availability____: The `section` element was introduced in the HTML5 specification.

Specifies a selection input type.

____Syntax____: |  |
```
<select> options </select>
```

____Discussion____: The `select` element specifies a selection menu. This block must contain a set of `option` elements or `optgroup` elements containing options. In Safari, if the `size` property is explicitly set for this element, the input box resembles a Mac OS X combo box, otherwise it resembles a pop-up menu.

Displays text in a small size.

____Syntax____: |  |
```
<small> content </small>
```

____Discussion____: The text specified by `content` is displayed in a smaller size, but otherwise matches the style of the enclosing element. Styles should be more finely tuned using CSS instead of using HTML style elements.

Provides a resource URI for a multimedia element such as `audio` or `video`.

____Syntax____: |  |
```
<video poster="bananas.png" ... >
    <source
        src="bananas.mp4"
        type="video/mp4; codecs=&quot;avc1.42E01E, mp4a.40.2&quot;"
        media="screen"
        pixelration="1.78"  <!-- 16:9 -->
    >
    </source>
    <source ...></source>
    <source ...></source>

    <!-- Fallback content for browsers that do not support the video element goes here. -->

</video>
```

____Discussion____: Specify type and codec information appropriately. Browsers use this information to choose the media that is most appropriate according to available codecs, and screen resolution.

____Availability____: Available in Safari 3.1 and later.

Specifies an inline styleless section in a document.

____Syntax____: |  |
```
<span> content </span>
```

____Discussion____: The `span` element specifies a section in a document. Multiple consecutive spans are placed horizontally on the page by default. Use CSS styles to tune the style properties of this element.

Obsolete. Defines a block of text in strikethrough style. Use the `del` instead.

____Discussion____: The content specified by `content` is rendered with a horizontal line through the center. The `del` element is more appropriate for this function. Styles should be more finely tuned using CSS instead of using HTML style elements.

____Availability____: The `strike` element has been declared obsolete in the HTML5 specification.

Specifies important text.

____Syntax____: |  |
```
<strong> content </strong>
```

____Discussion____: The `strong` element specifies a block of text with "strong" importance. Styles should be more finely tuned using CSS instead of using HTML style elements.

Defines an inline stylesheet.

____Syntax____: |  |
```
<style type="mimetype"> css_declarations </style>
```

____Discussion____: The `style` element specifies a CSS stylesheet within the page. All CSS declarations should be placed within this block. This element should be placed in the `head` section of a page. If you are linking to an external stylesheet, use the `link` element instead.

Specifies text as subscript.

____Syntax____: |  |
```
<sub> content </sub>
```

____Discussion____: The text specified by `content` is displayed in a smaller size and is subscripted, but otherwise matches the style of the enclosing element. Styles should be more finely tuned using CSS instead of using HTML style elements.

Specifies a summary for a `details` element.

____Syntax____: |  |
```
<details>
     <summary> Summary info </summary>
     <p> Detailed information </p>
</details>
```

____Discussion____: When a `details` element `summary` is absent the heading "details" is used by default.

____Availability____: The `summary` element was introduced in the HTML5 specification.

Specifies text as superscript.

____Syntax____: |  |
```
<sup> content </sup>
```

____Discussion____: The text specified by `content` is displayed in a smaller size and is superscripted, but otherwise matches the style of the enclosing element. Styles should be more finely tuned using CSS instead of using HTML style elements.

Defines a data table.

____Syntax____: |  |
```
<table> content </table>
```

____Discussion____: The `table` element defines a table structure for a page. The HTML specified by `content` should contain the other structural elements such as table rows (`tr`) and table cells (`td`).

Defines a table’s body.

____Syntax____: |  |
```
<tbody> content </tbody>
```

____Discussion____: The `tbody` element defines the body for a table. This element is only a structural definition and by default does not render anything unique, so the HTML specified by `content` should contain the other structural elements such as table rows (`tr`) and table cells (`td`).

Defines a table cell.

____Syntax____: |  |
```
<td> content </td>
```

____Discussion____: The `td` element defines a cell within a table. Cells are usually enclosed by table row (`tr`) definitions. Consecutive table cells are placed horizontally onscreen.

Specifies a text area input type.

____Syntax____: |  |
```
<textarea rows="value" cols="value"> content </textarea>
```

____Discussion____: The `textarea` element specifies a scrollable, multiline text input block. You can specify its size onscreen by specifying values for `rows` and `cols`.

Safari on iOS extends the `textarea` element with two additional properties, `autocorrect` and `autocapitalize`, described in `[Supported HTML](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi3delktk4za)`.

Defines a table’s footer.

____Syntax____: |  |
```
<tfoot> content </tfoot>
```

____Discussion____: The `tfoot` element defines a footer for a table. This element is only a structural definition and by default does not render anything unique, so the HTML specified by `content` should contain the other structural elements such as table rows (`tr`) and table cells (`td`).

The `meter` element was introduced in the HTML5 specification.

Defines header text for a table column.

____Syntax____: |  |
```
<th> content </th>
```

____Discussion____: Table headers should be placed in their own table row, usually the first row in a table definition, and should correspond in number to table cell definitions in later rows. In Safari, the text specified by `content` is displayed in a bold face.

Defines a table’s header.

____Syntax____: |  |
```
<thead> content </thead>
```

____Discussion____: The `thead` element defines a header for a table. This element is only a structural definition and by default does not render anything unique, so the HTML specified by `content` should contain the other structural elements such as table rows (`tr`) and table cells (`td`).

Defines the visible window title for the page.

____Syntax____: |  |
```
<title> content </title>
```

____Discussion____: The text specified by `content` is displayed at the top of a browser window, but remains invisible in embedded WebKit web views unless requested programatically. The `title` element must be placed in the `head` section of a page.

Defines a table row.

____Syntax____: |  |
```
<tr> content </tr>
```

____Discussion____: The `tr` element defines a row within a table. Table cells are usually enclosed by these rows. Consecutive table rows are placed vertically onscreen.

Specifies a text component of the parent `audio` or `video` element.

____Syntax____: |  |
```
<video src="mysource.mp4">
     <track kind="captions" src="myCaptions.srt">
     <track kind="description" src="myDescription.srt">
</video>
```

____Discussion____: The track element can indicate `subtitles`, `captions`, `description`, `chapters` or `metadata` through the `kind` attribute. See _[Safari HTML5 Audio and Video Guide](../../Audio%20Video/Safari%20HTML5%20Audio%20and%20Video%20Guide/About%20HTML5%20Audio%20and%20Video.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmrt)_ for more information.

____Availability____: The `track` element was introduced in the HTML5 specification.

Obsolete. Displays text in a "teletype" style. Use CSS styling instead.

____Discussion____: The text is displayed in a monospaced "teletype" style, but otherwise matches the style of the enclosing element. Styles should be more finely tuned using CSS instead of using HTML style elements. Semantic HTML alternatives to `tt` include: `kdb` for keyboard input, `var` for variables, `code` for computer code, and `samp` for computer output.

____Availability____: The `tt` element has been declared obsolete in the HTML5 specification.

Deprecated. Defines a block of underlined text. Use CSS styling instead.

____Discussion____: The content is underlined. The `ins` element is more appropriate for this function. Styles should be more finely tuned using CSS instead of using HTML style elements. Additionally, underlined text should not be used as it might be confused with actual hyperlinks.

____Availability____: The `u` element has been deprecated in the HTML 4.01 standard.

Specifies an unordered list.

____Syntax____: |  |
```
<ul> content </ul>
```

____Discussion____: The `ul` element specifies an unordered, bulleted list. Within the bounds of this block, list items should be defined using the `li` element.

Specifies a variable.

____Syntax____: |  |
```
<var> content </var>
```

____Discussion____: The `var` element specifies a variable. The text enclosed within the element is italicized.

Embeds video into a webpage.

____Syntax____: |  |
```swift
<video src="url"
    poster="freezeframe.png"
    autoplay="autoplay" <!-- Boolean attribute. Omit to prevent autoplay. -->
    start="00:00:00.00"
    loopstart="00:00:00.07" <!-- 7 seconds -->
    loopend="00:00:00.19"
    end="00:00:00.27"
    playcount="4" <!-- play 4x -->
    controls="true"
    width="640"
    height="480"
>
```

____Discussion____: The `video` element might contain fallback content for browsers that do not support this element. Any content enclosed within the `video` element is ignored by browsers that support the `video` element (but it must be valid HTML).

The `video` element supports inclusion of `source` elements to provide multiple versions of a video clip encoded with different codecs, at different bit rates, and so on. These `source` elements must be the first elements inside the `video` element before any fallback content. See `source` for more information.

Specifies a block in which line breaks are permitted.

____Syntax____: |  |
```
<wbr> content </wbr>
```

____Discussion____: Within a `nobr` block (in which line breaks are enabled), any content specified by `content` is permitted to use line breaks. The line breaks themselves must still be requested using the `br` element.

Obsolete. Represents a block of literal text. Use `pre` and `code` instead.

____Discussion____: The `xmp` element preserves the formatting of the block of text, specifically line breaks, multiple spaces, and the greater-than and less-than symbols that accompany HTML elements. This block is also prefaced with a `newline` element. In Safari, text enclosed in this element is also rendered in a monospace "teletype" font.

____Availability____: The `xmp` element has been declared obsolete in the HTML5 specification.

[Next](Supported%20Attributes.md)[Previous](Explanation%20of%20Terms.md)

